"""
Scrapy settings for crawler project

For simplicity, this file contains only settings considered important or
commonly used. You can find more settings consulting the documentation:

http://doc.scrapy.org/en/latest/topics/settings.html
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
"""
import datetime

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure concurrent requests performed by Scrapy
DOWNLOAD_DELAY = 0.05
CONCURRENT_REQUESTS = 24
CONCURRENT_REQUESTS_PER_DOMAIN = 12
CONCURRENT_REQUESTS_PER_IP = 12

# Configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 3

# Configure cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'kr',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'crawler.middlewares.CrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
ITEM_PIPELINES = {
    'crawler.pipelines.DuplicatesPipeline': 300,
    'crawler.pipelines.ValidatesPipeline': 301,
}

# Configure HTTP caching
HTTPCACHE_ENABLED = False
HTTPCACHE_GZIP = True
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Configure log
LOG_FORMATTER = 'crawler.middlewares.PoliteLogFormatter'
LOG_LEVEL = 'INFO'
LOG_FILE = '.scrapy/logs/%s.log' % datetime.datetime.now().strftime('%Y-%m-%d')

# Configure feed
FEED_URI = 'crawler/feeds/%s.csv' % datetime.datetime.now().strftime('%Y-%m-%d')
FEED_EXPORT_ENCODING = 'utf8'
FEED_FORMAT = 'csv'
