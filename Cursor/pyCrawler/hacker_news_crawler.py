import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class HackerNewsCrawler:
    def __init__(self):
        self.base_url = "https://news.ycombinator.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_page(self, page=1):
        """获取指定页面的内容"""
        url = f"{self.base_url}/news?p={page}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"获取页面时出错: {e}")
            return None

    def parse_stories(self, html):
        """解析故事列表"""
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        #links = soup.find_all('a')
        # print("所有的链接")
        # for link in links:
        #     print(link.name,link['href'],link.get_text())
        stories = []
        
        # 查找所有故事条目
        for link in soup.select('span.titleline>a'):
            # 获取标题和链接    
            title = link.get_text()
            #print(title)
            url = link.get('href')
            if url and not url.startswith('http'):
                url = f"{self.base_url}/{url}"
                
            # 获取分数和作者信息
            subtext = link.parent.parent.parent.next_sibling
            if not subtext:
                continue
                
            score = subtext.find('span', class_='score')
            score = score.get_text().split()[0] if score else '0'
            
            author = subtext.find('a', class_='hnuser')
            author = author.get_text() if author else 'unknown'

            stories.append({
                'title': title,
                'url': url,
                'score': score,
                'author': author
            })
          
        return stories

    def crawl(self, pages=5):
        """爬取多页内容"""
        all_stories = []
        for page in range(1, pages + 1):
            print(f"正在爬取第 {page} 页...")
            html = self.get_page(page)
            stories = self.parse_stories(html)
            all_stories.extend(stories)
            time.sleep(1)  # 添加延迟，避免请求过于频繁
        return all_stories

def main():
    crawler = HackerNewsCrawler()
    stories = crawler.crawl(pages=5)
    
    # 打印结果
    print("\n=== Hacker News 热门故事 ===")
    print(f"爬取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"共获取 {len(stories)} 个故事\n")
    
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story['title']}")
        print(f"   链接: {story['url']}")
        print(f"   分数: {story['score']}")
        print(f"   作者: {story['author']}")
        print()

if __name__ == "__main__":
    main() 