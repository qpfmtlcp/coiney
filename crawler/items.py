import scrapy


class CrawlerItem(scrapy.Item):
    page_no = scrapy.Field()
    title = scrapy.Field()
    author_level = scrapy.Field()
    content = scrapy.Field()
    uploaded_at = scrapy.Field()
    view_count = scrapy.Field()
    comment_count = scrapy.Field()
    good_count = scrapy.Field()
    bad_count = scrapy.Field()
    

