from scrapy.exceptions import DropItem


class ValidatesPipeline(object):
    def process_item(self, item, spider):
        if not item.get('title', None):
            raise DropItem("Invalid item found: %s" % item['page_no'])
        else:
            return item


class DuplicatesPipeline(object):
    __slots__ = ['seen']
    
    def __init__(self):
        self.seen = set()
    
    def process_item(self, item, spider):
        if item['page_no'] in self.seen:
            raise DropItem("Duplicate item found: %s" % item['page_no'])
        else:
            self.seen.add(item['page_no'])
            return item
