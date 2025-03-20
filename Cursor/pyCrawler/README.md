# Hacker News 爬虫

这是一个简单的 Python 爬虫程序，用于爬取 Hacker News 网站的内容。

## 功能特点

- 爬取 Hacker News 首页的热门故事
- 支持多页爬取
- 获取故事的标题、链接、分数和作者信息
- 包含请求延迟，避免对目标网站造成压力

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

直接运行 Python 脚本：

```bash
python hacker_news_crawler.py
```

## 输出示例

程序会输出以下信息：
- 故事标题
- 故事链接
- 故事分数
- 作者信息

## 注意事项

- 请遵守网站的爬虫规则
- 建议适当调整爬取间隔时间
- 默认爬取前 3 页内容，可以通过修改代码中的 `pages` 参数来调整 