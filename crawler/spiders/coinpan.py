import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
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
        data = CrawlerItem()
        pattern = 'free/(\d+)' if response.url.count('/free/') else 'document_srl=(\d+)'
        data['page_no'] = re.search(pattern, response.url).group(1)
        data['title'] = response.xpath("//div[@class='read_header']//a/text()").extract_first()
        content = response.xpath('//div[@class="read_body"]//div[contains(@class, "xe_content")]').extract_first()
        data['content'] = re.sub('<[A-Za-z\/][^>]*>', '', content)
        
        data_set = response.xpath('//ul[@class="wt_box gray_color"]//li')
        data['uploaded_at'] = data_set.re_first('\d{4}\.\d{2}\.\d{2}\W+\d{2}:\d{2}')
        data['comment_count'] = data_set.xpath('a[@href="#comment"]//b/text()').extract_first()
        for tag in data_set:
            if tag.re("\W추천"):
                data['good_count'] = tag.css('b::text').extract_first()
            elif tag.re("\W비추천"):
                data['bad_count'] = tag.css('b::text').extract_first()
            elif tag.re("\W조회"):
                data['view_count'] = tag.css('b::text').extract_first()
        
        return data
