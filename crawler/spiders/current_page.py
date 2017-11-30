from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.loaders import CoinGalleryLoader, CoinpanLoader
from crawler.items import CrawlerItem
import datetime


def community_pages():
    page_list = list()
    for no in range(1, 4):
        page_list.append('https://coinpan.com/index.php?mid=free&page={}'.format(no))
        page_list.append('http://gall.dcinside.com/board/lists/?id=bitcoins&page={}'.format(no))
    
    return page_list


class CurrentPageSpider(CrawlSpider):
    name = 'current_page'
    allowed_domains = ['gall.dcinside.com', 'coinpan.com']
    start_urls = community_pages()
    custom_settings = {
        'FEED_URI': 'storage/current_page.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_FIELDS': [
            'community', 'page_no', 'title', 'uploaded_at',
            'view_count', 'comment_count', 'good_count', 'bad_count',
            'content', 'created_at',
        ]
    }
    
    rules = (
        Rule(LinkExtractor(allow=('view/\?id=bitcoins&no=\d+&',)), callback='parse_coingallery_item'),
        Rule(LinkExtractor(allow=('document_srl=\d+',)), callback='parse_coinpan_item'),
    )
    
    def parse_coingallery_item(self, response):
        l = CoinGalleryLoader(item=CrawlerItem(), response=response)
        l.add_value('community', 'coingallery')
        l.add_value('page_no', response.url, re='no=(\d+)')
        l.add_xpath('title', '//dl[@class="wt_subject"]//dd/text()')
        l.add_xpath('content', '//div[@class="con_substance"]//table')
        l.add_xpath('comment_count', '//span[@id="re_count"]/text()')
        l.add_xpath('uploaded_at', '//div[@class="w_top_right"]//b/text()')
        l.add_xpath('view_count', '//dd[@class="dd_num"]/text()')
        l.add_xpath('good_count', '//span[@id="recommend_view_up"]/text()')
        l.add_xpath('bad_count', '//span[@id="recommend_view_down"]//span/text()')
        l.add_value('created_at', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        return l.load_item()
    
    def parse_coinpan_item(self, response):
        l = CoinpanLoader(item=CrawlerItem(), response=response)
        l.add_value('community', 'coinpan')
        l.add_xpath('page_no', '//p[@class="perlink"]//@href', re='coinpan.com/(\d+)')
        l.add_xpath('title', '//div[@class="read_header"]//a/text()')
        l.add_xpath('content', '//div[@class="read_body"]//div[contains(@class, "xe_content")]')
        l.add_value('created_at', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        header = l.nested_xpath('//ul[@class="wt_box gray_color"]//li')
        header.add_xpath('uploaded_at', '//span', re='\d{4}\.\d{2}\.\d{2}\W+\d{2}:\d{2}')
        header.add_xpath('comment_count', 'a[@href="#comment"]//b/text()')
        header.add_xpath('good_count', '//a[contains(text(), "추천")]//b/text()')
        header.add_xpath('bad_count', '//a[contains(text(), "비추천")]//b/text()')
        header.add_xpath('view_count', '//a[contains(text(), "조회")]//b/text()')
        
        return l.load_item()
