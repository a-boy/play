import scrapy
# Scrapy (/ˈskreɪpaɪ/)
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']
    # custom_settings = {
    #         "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7"
    #     }

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

 # $ scrapy runspider myspider.py