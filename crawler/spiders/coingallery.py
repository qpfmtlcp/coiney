from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.loaders import CoinGalleryLoader
from crawler.items import CrawlerItem


class CoinGallerySpider(CrawlSpider):
    name = 'coingallery'
    allowed_domains = ['gall.dcinside.com']
    start_urls = ['http://gall.dcinside.com/board/lists/?id=bitcoins']
    
    rules = (
        Rule(LinkExtractor(allow=('/view/\?id=bitcoins&no=\d+', )), callback='parse_item'),
        Rule(LinkExtractor(allow=('/lists/\?id=bitcoins&page=\d+$', ))),
    )
    
    def parse_item(self, response):
        l = CoinGalleryLoader(item=CrawlerItem(), response=response)
        l.add_value('community', self.name)
        l.add_value('page_no', response.url, re='no=(\d+)')
        l.add_xpath('title', '//dl[@class="wt_subject"]//dd/text()')
        l.add_xpath('content', '//div[@class="con_substance"]//table')
        l.add_xpath('comment_count', '//span[@id="re_count"]/text()')
        l.add_xpath('uploaded_at', '//div[@class="w_top_right"]//b/text()')
        l.add_xpath('view_count', '//dd[@class="dd_num"]/text()')
        l.add_xpath('good_count', '//span[@id="recommend_view_up"]/text()')
        l.add_xpath('bad_count', '//span[@id="recommend_view_down"]//span/text()')
        
        return l.load_item()
