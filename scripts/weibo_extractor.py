#!/usr/bin/env python3
"""
微博链接提取器
功能：从微博链接中提取帖子内容并格式化输出
支持：weibo.com、m.weibo.cn 等链接
"""

import re
import json
import argparse
from typing import List, Dict, Optional
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup


class WeiboPost:
    """微博帖子数据模型"""
    
    def __init__(self, data: Dict):
        self.url = data.get('url', '')
        self.text = data.get('text', '')
        self.author = data.get('author', '')
        self.created_at = data.get('created_at', '')
        self.reposts_count = data.get('reposts_count', 0)
        self.comments_count = data.get('comments_count', 0)
        self.attitudes_count = data.get('attitudes_count', 0)
        self.pics = data.get('pics', [])
        self.topics = data.get('topics', [])
        self.links = data.get('links', [])
    
    def format_output(self, format_type: str = 'markdown') -> str:
        """格式化输出"""
        if format_type == 'markdown':
            return self._format_markdown()
        elif format_type == 'json':
            return self._format_json()
        else:
            return self._format_plain()
    
    def _format_markdown(self) -> str:
        """Markdown 格式输出"""
        output = []
        output.append(f"## {self.author} 的微博")
        output.append(f"**发布时间**: {self.created_at}")
        output.append(f"**原文链接**: {self.url}")
        output.append("")
        output.append("### 内容")
        output.append(self.text)
        output.append("")
        
        if self.topics:
            output.append(f"**话题**: {', '.join(self.topics)}")
            output.append("")
        
        if self.links:
            output.append("### 引用链接")
            for link in self.links:
                output.append(f"- {link}")
            output.append("")
        
        if self.pics:
            output.append(f"**图片**: {len(self.pics)} 张")
            output.append("")
        
        output.append("### 互动数据")
        output.append(f"- 转发: {self.reposts_count}")
        output.append(f"- 评论: {self.comments_count}")
        output.append(f"- 点赞: {self.attitudes_count}")
        output.append("")
        output.append("---")
        
        return "\n".join(output)
    
    def _format_json(self) -> str:
        """JSON 格式输出"""
        data = {
            'url': self.url,
            'author': self.author,
            'text': self.text,
            'created_at': self.created_at,
            'topics': self.topics,
            'links': self.links,
            'pics': self.pics,
            'metrics': {
                'reposts': self.reposts_count,
                'comments': self.comments_count,
                'likes': self.attitudes_count
            }
        }
        return json.dumps(data, ensure_ascii=False, indent=2)
    
    def _format_plain(self) -> str:
        """纯文本格式输出"""
        output = []
        output.append(f"作者: {self.author}")
        output.append(f"时间: {self.created_at}")
        output.append(f"链接: {self.url}")
        output.append("-" * 50)
        output.append(self.text)
        if self.topics:
            output.append(f"\n话题: {', '.join(self.topics)}")
        if self.links:
            output.append(f"\n外链: {', '.join(self.links)}")
        output.append(f"\n转发:{self.reposts_count} | 评论:{self.comments_count} | 点赞:{self.attitudes_count}")
        output.append("=" * 50)
        return "\n".join(output)


class WeiboExtractor:
    """微博内容提取器"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) '
                         'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'SUB=_2AkMSbR7af8NxqwJRmP0SzGvhZY11yQ_EieKkjJ2ZJRMxHRl-yT83qkEctRB6PfaHqS4h4R4q4r4q4r4q4r4q4r4q; M_WEIBOCN_PARAMS=oid%3D4999999999999999%26luicode%3D20000174%26uicode%3D20000174;',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def extract(self, url: str) -> Optional[WeiboPost]:
        """提取微博内容"""
        try:
            # 识别链接类型并规范化
            normalized_url = self._normalize_url(url)
            if not normalized_url:
                print(f"❌ 无法识别的微博链接: {url}")
                return None
            
            print(f"🔍 正在提取: {normalized_url}")
            
            # 获取网页内容
            response = self.session.get(normalized_url, timeout=10)
            response.raise_for_status()
            
            # 解析内容
            post_data = self._parse_mobile_page(response.text, normalized_url)
            
            if post_data:
                print(f"✅ 成功提取: {post_data.get('author', '未知')}")
                return WeiboPost(post_data)
            else:
                print(f"⚠️ 未能提取到内容")
                return None
                
        except requests.RequestException as e:
            print(f"❌ 网络请求失败: {e}")
            return None
        except Exception as e:
            print(f"❌ 提取失败: {e}")
            return None
    
    def _normalize_url(self, url: str) -> Optional[str]:
        """规范化微博链接"""
        # 提取微博 ID
        patterns = [
            r'weibo\.com/\d+/(\w+)',           # weibo.com/uid/mid
            r'm\.weibo\.cn/status/(\d+)',      # m.weibo.cn/status/mid
            r'm\.weibo\.cn/\d+/(\w+)',         # m.weibo.cn/uid/mid
            r'weibo\.cn/\w+/(\w+)',            # weibo.cn/username/mid
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                mid = match.group(1)
                # 转换为移动版链接（更容易解析）
                return f"https://m.weibo.cn/status/{mid}"
        
        return None
    
    def _parse_mobile_page(self, html: str, url: str) -> Optional[Dict]:
        """解析移动版网页"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # 尝试从页面中提取 JSON 数据
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and 'var $render_data' in script.string:
                # 提取 JSON 数据
                json_match = re.search(r'\$render_data = (\[.*?\])\[0\]', script.string, re.DOTALL)
                if json_match:
                    try:
                        data = json.loads(json_match.group(1))[0]
                        return self._parse_json_data(data, url)
                    except:
                        pass
        
        # 如果 JSON 提取失败，尝试 HTML 解析
        return self._parse_html_fallback(soup, url)
    
    def _parse_json_data(self, data: Dict, url: str) -> Dict:
        """从 JSON 数据中提取信息"""
        status = data.get('status', {})
        user = status.get('user', {})
        
        # 提取文本内容
        text = status.get('text', '')
        # 清理 HTML 标签
        text = re.sub(r'<br\s*/?>', '\n', text)
        text = BeautifulSoup(text, 'html.parser').get_text()
        
        # 提取话题
        topics = re.findall(r'#([^#]+)#', text)
        
        # 提取链接
        links = []
        url_struct = status.get('url_struct', [])
        for url_info in url_struct:
            if 'long_url' in url_info:
                links.append(url_info['long_url'])
        
        # 提取图片
        pics = []
        if 'pics' in status:
            pics = [pic.get('large', {}).get('url', '') for pic in status['pics']]
        
        return {
            'url': url,
            'text': text.strip(),
            'author': user.get('screen_name', '未知'),
            'created_at': status.get('created_at', ''),
            'reposts_count': status.get('reposts_count', 0),
            'comments_count': status.get('comments_count', 0),
            'attitudes_count': status.get('attitudes_count', 0),
            'pics': pics,
            'topics': topics,
            'links': links
        }
    
    def _parse_html_fallback(self, soup: BeautifulSoup, url: str) -> Optional[Dict]:
        """HTML 解析备用方案"""
        # 这是一个简化的备用解析方案
        # 实际使用中可能需要根据微博页面结构调整
        
        text_elem = soup.find('div', class_='weibo-text')
        author_elem = soup.find('div', class_='m-text-cut')
        
        if not text_elem:
            return None
        
        text = text_elem.get_text().strip()
        author = author_elem.get_text().strip() if author_elem else '未知'
        
        return {
            'url': url,
            'text': text,
            'author': author,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'reposts_count': 0,
            'comments_count': 0,
            'attitudes_count': 0,
            'pics': [],
            'topics': re.findall(r'#([^#]+)#', text),
            'links': []
        }


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='微博链接提取器 - 从微博链接中提取帖子内容',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 提取单个链接
  python weibo_extractor.py https://weibo.com/1234567890/AbCdEfG

  # 提取多个链接
  python weibo_extractor.py url1 url2 url3

  # 指定输出格式
  python weibo_extractor.py --format json url1

  # 保存到文件
  python weibo_extractor.py --output result.md url1
        """
    )
    
    parser.add_argument(
        'urls',
        nargs='+',
        help='一个或多个微博链接'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'json', 'plain'],
        default='markdown',
        help='输出格式 (默认: markdown)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='输出到文件（不指定则输出到控制台）'
    )
    
    args = parser.parse_args()
    
    # 创建提取器
    extractor = WeiboExtractor()
    
    # 提取所有链接
    posts = []
    for url in args.urls:
        post = extractor.extract(url)
        if post:
            posts.append(post)
    
    if not posts:
        print("\n⚠️ 没有成功提取到任何内容")
        return
    
    # 格式化输出
    output_lines = []
    if args.format == 'json':
        # JSON 格式输出所有帖子
        all_data = [json.loads(post.format_output('json')) for post in posts]
        output_content = json.dumps(all_data, ensure_ascii=False, indent=2)
    else:
        # Markdown 或 Plain 格式
        header = f"# 微博提取结果\n\n提取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n提取数量: {len(posts)} 条\n\n"
        output_lines.append(header)
        
        for i, post in enumerate(posts, 1):
            output_lines.append(post.format_output(args.format))
            if i < len(posts):
                output_lines.append("\n")
        
        output_content = "".join(output_lines)
    
    # 输出结果
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_content)
            print(f"\n✅ 结果已保存到: {args.output}")
        except Exception as e:
            print(f"\n❌ 保存文件失败: {e}")
    else:
        print("\n" + "="*60)
        print(output_content)
        print("="*60)


if __name__ == '__main__':
    main()
