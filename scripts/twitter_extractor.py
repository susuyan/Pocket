#!/usr/bin/env python3
"""
X/Twitter 内容提取器 (Robust Version)
功能：从 X/Twitter 链接中提取帖子内容（仅内容）
特性：
1. 优先使用 Guest Token 直接访问官方 API (最稳定)
2. 自动轮询多个 Nitter 实例作为备选
3. 自动检测系统代理
4. 输出简洁，仅包含内容
"""

import re
import json
import argparse
import os
import sys
import time
from typing import List, Dict, Optional
from datetime import datetime
import requests
from bs4 import BeautifulSoup

class TwitterExtractor:
    # Twitter Web Client Bearer Token (固定值)
    GUEST_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

    # Nitter 实例列表 (按稳定性排序)
    NITTER_INSTANCES = [
        "https://nitter.privacydev.net",
        "https://nitter.poast.org",
        "https://nitter.lucabased.xyz",
        "https://nitter.net",
        "https://nitter.cz",
        "https://nitter.projectsegfau.lt",
        "https://nitter.eu.projectsegfau.lt",
        "https://nitter.moomoo.me",
        "https://nitter.soopy.moe",
        "https://xcancel.com",
    ]
    
    def __init__(self, proxy: Optional[str] = None):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        # 代理设置
        self.proxies = None
        
        # 1. 优先使用用户传入的代理
        if proxy:
            self.proxies = {'http': proxy, 'https': proxy}
            print(f"🔌 使用指定代理: {proxy}")
        # 2. 其次尝试自动检测系统代理
        else:
            sys_proxy = self._detect_system_proxy()
            if sys_proxy:
                self.proxies = {'http': sys_proxy, 'https': sys_proxy}
                print(f"🔌 自动检测到系统代理: {sys_proxy}")
        
        if self.proxies:
            self.session.proxies = self.proxies

    def _detect_system_proxy(self) -> Optional[str]:
        """检测系统环境变量中的代理设置"""
        # 常见的代理环境变量
        keys = ['ALL_PROXY', 'all_proxy', 'HTTPS_PROXY', 'https_proxy', 'HTTP_PROXY', 'http_proxy']
        for key in keys:
            val = os.environ.get(key)
            if val:
                # 确保有协议前缀
                if not val.startswith('http'):
                    return f"http://{val}"
                return val
        return None

    def extract(self, url: str) -> Optional[Dict]:
        """提取推文内容"""
        # 提取 tweet ID
        match = re.search(r'(?:twitter|x)\.com/([^/]+)/status/(\d+)', url)
        if not match:
            # 尝试处理短链接或不规范链接
            match = re.search(r'/status/(\d+)', url)
            
        if not match:
            print(f"❌ 无法识别的 Twitter 链接: {url}")
            return None
            
        tweet_id = match.group(2) if len(match.groups()) > 1 else match.group(1)
        
        # 1. 尝试 Guest Token (API)
        # print("⏳ 尝试直接连接 X API (Guest Mode)...")
        guest_data = self._extract_via_guest_token(tweet_id)
        if guest_data:
            return guest_data

        # 2. 尝试 Nitter 实例
        # print("⚠️ X API 连接失败，尝试 Nitter 代理...")
        for instance in self.NITTER_INSTANCES:
            try:
                # 需要 username，如果正则没取到，随便填一个，Nitter 通常能重定向或兼容
                username = "user"
                nitter_url = f"{instance}/{username}/status/{tweet_id}"
                
                # 缩短超时时间，快速失败
                response = self.session.get(nitter_url, timeout=5)
                
                if response.status_code == 200:
                    post_data = self._parse_nitter_page(response.text, url, instance)
                    if post_data:
                        return post_data
            except Exception:
                continue

        # 3. Syndication API (保底)
        try:
            syndication_url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&lang=en"
            response = self.session.get(syndication_url, timeout=5)
            if response.status_code == 200:
                return self._parse_syndication_response(response.json(), url)
        except Exception:
            pass

        return None

    def _get_guest_token(self) -> Optional[str]:
        headers = {
            "authorization": f"Bearer {self.GUEST_BEARER_TOKEN}",
            "user-agent": self.headers['User-Agent']
        }
        try:
            response = requests.post(
                "https://api.twitter.com/1.1/guest/activate.json", 
                headers=headers, 
                proxies=self.proxies,
                timeout=5
            )
            if response.status_code == 200:
                return response.json()["guest_token"]
        except Exception:
            pass
        return None

    def _extract_via_guest_token(self, tweet_id: str) -> Optional[Dict]:
        guest_token = self._get_guest_token()
        if not guest_token:
            return None
            
        url = "https://twitter.com/i/api/graphql/s-CskcDsK2j0Nq5X6yV6lA/TweetResultByRestId"
        headers = {
            "authorization": f"Bearer {self.GUEST_BEARER_TOKEN}",
            "x-guest-token": guest_token,
            "content-type": "application/json",
            "user-agent": self.headers['User-Agent']
        }
        
        variables = {
            "tweetId": tweet_id,
            "withCommunity": False,
            "includePromotedContent": False,
            "withVoice": False
        }
        
        # 简化的 features
        features = {
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
        }
        
        params = {
            "variables": json.dumps(variables),
            "features": json.dumps(features)
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, proxies=self.proxies, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return self._parse_guest_api_data(data, tweet_id)
        except Exception:
            pass
        return None

    def _parse_guest_api_data(self, data: Dict, tweet_id: str) -> Optional[Dict]:
        try:
            result = data['data']['tweetResult']['result']
            legacy = result['legacy']
            core = result['core']['user_results']['result']
            
            # 文本
            text = legacy.get('full_text', '')
            
            # 作者
            author = {
                'name': core['legacy']['name'],
                'username': core['legacy']['screen_name']
            }
            
            # 媒体
            media = []
            if 'extended_entities' in legacy and 'media' in legacy['extended_entities']:
                for m in legacy['extended_entities']['media']:
                    media.append({
                        'type': m.get('type', 'photo'),
                        'url': m.get('media_url_https', '')
                    })
            
            return {
                'text': text,
                'author': author,
                'media': media,
                'quoted_tweet': None # 暂不处理嵌套引用，保持简单
            }
        except Exception:
            return None

    def _parse_nitter_page(self, html: str, original_url: str, instance_url: str) -> Optional[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        tweet_container = soup.find('div', class_='main-tweet')
        if not tweet_container:
            return None
            
        content_div = tweet_container.find('div', class_='tweet-content')
        text = content_div.get_text(separator='\n').strip() if content_div else ""
        
        author_name = tweet_container.find('a', class_='fullname')
        author_user = tweet_container.find('a', class_='username')
        
        author = {
            'name': author_name.get_text().strip() if author_name else "",
            'username': author_user.get_text().strip().replace('@', '') if author_user else ""
        }
        
        media = []
        attachments = tweet_container.find('div', class_='attachments')
        if attachments:
            for img in attachments.find_all('img'):
                src = img.get('src', '')
                if src:
                    if src.startswith('/'): src = instance_url + src
                    media.append({'type': 'photo', 'url': src})
                    
        return {'text': text, 'author': author, 'media': media}

    def _parse_syndication_response(self, data: Dict, url: str) -> Dict:
        text = data.get('text', '')
        author = {
            'name': data.get('user', {}).get('name', ''),
            'username': data.get('user', {}).get('screen_name', '')
        }
        media = []
        for m in (data.get('entities', {}).get('media', []) or []):
            media.append({'type': m.get('type', ''), 'url': m.get('media_url_https', '')})
            
        return {'text': text, 'author': author, 'media': media}

    def format_output(self, data: Dict) -> str:
        """只输出内容，不含元数据"""
        output = []
        
        # 1. 头部：作者信息 (还是保留一下比较好，知道是谁说的)
        # output.append(f"**{data['author']['name']}** (@{data['author']['username']}):")
        # output.append("")
        
        # 2. 正文
        output.append(data['text'])
        
        # 3. 媒体
        if data['media']:
            output.append("")
            for m in data['media']:
                if m['type'] == 'photo':
                    output.append(f"![image]({m['url']})")
                else:
                    output.append(f"[Media: {m['url']}]")
                    
        return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description='X/Twitter 内容提取器')
    parser.add_argument('urls', nargs='+', help='X/Twitter 链接')
    parser.add_argument('-p', '--proxy', help='代理地址')
    args = parser.parse_args()
    
    extractor = TwitterExtractor(proxy=args.proxy)
    
    for url in args.urls:
        data = extractor.extract(url)
        if data:
            print(extractor.format_output(data))
        else:
            print(f"❌ 提取失败: {url} (请检查网络或代理设置)")

if __name__ == '__main__':
    main()
