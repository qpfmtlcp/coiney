from scrapy.exceptions import DropItem


class ValidatesPipeline(object):
    def process_item(self, item, spider):
        if not item.get('title', None):
            raise DropItem("Invalid item found: %s" % item['page_no'])
        else:
            return item


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
