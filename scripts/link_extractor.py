#!/usr/bin/env python3
"""
统一链接提取器 (Universal Link Extractor)
功能：自动识别链接类型（Weibo/Twitter/X），并调用相应的提取器获取内容。
"""

import sys
import argparse
import re
from typing import Optional
from urllib.parse import urlparse

# 尝试导入同目录下的提取器
try:
    from weibo_extractor import WeiboExtractor
    from twitter_extractor import TwitterExtractor
except ImportError:
    # 如果作为模块运行可能需要调整路径
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from weibo_extractor import WeiboExtractor
    from twitter_extractor import TwitterExtractor

class LinkExtractor:
    def __init__(self, proxy: Optional[str] = None):
        self.weibo_extractor = WeiboExtractor()
        self.twitter_extractor = TwitterExtractor(proxy=proxy)
        
    def extract(self, url: str) -> str:
        """根据 URL 自动分发到对应的提取器"""
        domain = urlparse(url).netloc
        
        if any(x in domain for x in ['weibo.com', 'weibo.cn']):
            return self._extract_weibo(url)
        elif any(x in domain for x in ['twitter.com', 'x.com']):
            return self._extract_twitter(url)
        else:
            return f"❌ 不支持的链接域名: {domain}\n目前仅支持: weibo.com, weibo.cn, twitter.com, x.com"

    def _extract_weibo(self, url: str) -> str:
        print(f"🔍 检测到微博链接: {url}")
        post = self.weibo_extractor.extract(url)
        if post:
            # 默认使用 Markdown 格式
            return post.format_output('markdown')
        return "❌ 微博提取失败"

    def _extract_twitter(self, url: str) -> str:
        print(f"🔍 检测到 Twitter/X 链接: {url}")
        data = self.twitter_extractor.extract(url)
        if data:
            return self.twitter_extractor.format_output(data)
        return "❌ Twitter 提取失败 (请检查网络或代理)"

def main():
    parser = argparse.ArgumentParser(
        description='统一链接提取器 - 自动识别 Weibo/Twitter 链接并提取内容',
        epilog='示例: python link_extractor.py https://x.com/user/status/123'
    )
    parser.add_argument('urls', nargs='+', help='一个或多个链接')
    parser.add_argument('-p', '--proxy', help='指定代理 (仅对 Twitter 有效，Weibo 直连)')
    
    args = parser.parse_args()
    
    extractor = LinkExtractor(proxy=args.proxy)
    
    for i, url in enumerate(args.urls):
        if i > 0:
            print("\n" + "-"*50 + "\n")
        print(extractor.extract(url))

if __name__ == '__main__':
    main()
