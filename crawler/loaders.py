from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Identity
from w3lib.html import remove_tags


class CoinpanLoader(ItemLoader):
    default_output_processor = TakeFirst()
    
    content_in = MapCompose(remove_tags)
    
    comment_out = Identity()
