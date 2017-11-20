from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.loaders import CoinpanLoader
from crawler.items import CrawlerItem


class CoinpanSpider(CrawlSpider):
    name = 'coinpan'
    allowed_domains = ['coinpan.com']
    start_urls = ['http://www.coinpan.com/index.php?mid=free&page=1']
    
    rules = (
        Rule(LinkExtractor(allow=('/free$', 'index.php\?mid=free&page=\d+$'))),
        Rule(LinkExtractor(allow=('/free/\d+$', 'document_srl=\d+$',)), callback='parse_item'),
    )
    
    def parse_item(self, response):
        l = CoinpanLoader(item=CrawlerItem(), response=response)
        l.add_xpath('page_no', '//p[@class="perlink"]//@href', re='coinpan.com/(\d+)')
        l.add_xpath('title', '//div[@class="read_header"]//a/text()')
        l.add_xpath('content', '//div[@class="read_body"]//div[contains(@class, "xe_content")]')
        
        header = l.nested_xpath('//ul[@class="wt_box gray_color"]//li')
        header.add_xpath('uploaded_at', '//span', re='\d{4}\.\d{2}\.\d{2}\W+\d{2}:\d{2}')
        header.add_xpath('comment_count', 'a[@href="#comment"]//b/text()')
        header.add_xpath('good_count', '//a[contains(text(), "추천")]//b/text()')
        header.add_xpath('bad_count', '//a[contains(text(), "비추천")]//b/text()')
        header.add_xpath('view_count', '//a[contains(text(), "조회")]//b/text()')
        
        return l.load_item()
