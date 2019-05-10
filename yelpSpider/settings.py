# -*- coding: utf-8 -*-

# Scrapy settings for yelpSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# BOT_NAME = 'yelpSpider'

# 数据保存路径
# DATA_PATH_PREFIX = "D:/yelp/data"

SPIDER_MODULES = ['yelpSpider.spiders']
NEWSPIDER_MODULE = 'yelpSpider.spiders'

# MYSQL_HOST = "184.181.11.233"
# MYSQL_PORT = 3306
# MYSQL_USER = "ebuyhouse"
# MYSQL_PASSWD = "ebuyhouse135"
# MYSQL_DB = "crawl_data"


# 默认情况下,RFPDupeFilter只记录第一个重复请求。将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
# DUPEFILTER_DEBUG = True
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
REDIS_HOST = '192.168.139.101'
REDIS_PORT = 6379

LOG_LEVEL = 'DEBUG'
# 关掉重定向, 不会重定向到新的地址
# REDIRECT_ENABLED = False
# 返回301, 302时, 按正常返回对待, 可以正常写入cookie
# HTTPERROR_ALLOWED_CODES = [301, 302]

# PHANTOMJS_PATH = 'D:\\devtools\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 40
# CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept-Encoding': 'gzip',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'realtorSpider.middlewares.RealtorspiderSpiderMiddleware': 543,
#}

# 下载中间件配置User-Agent池
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# USER_PASS = "wh429004:ylsvtvu1"
# 代理
"""



"""
PROXIES = [
    {'ip_port': '121.239.88.183:22573', 'user_pass': 'wh429004:ylsvtvu1'},
    {'ip_port': '114.220.71.205:16522', 'user_pass': 'wh429004:ylsvtvu1'},
    # {'ip_port': '39.106.94.239:27140', 'user_pass': 'wh429004:ylsvtvu1'},
    # {'ip_port': '125.106.217.119:18477', 'user_pass': 'wh429004:ylsvtvu1'},
    # {'ip_port': '183.148.135.157:15300', 'user_pass': 'wh429004:ylsvtvu1'},
    # {'ip_port': '209.141.32.12:80', 'user_pass': ''},
    # {'ip_port': '98.143.145.29:62354', 'user_pass': ''},
    # {'ip_port': '138.68.59.157:1210', 'user_pass': ''},
    # {'ip_port': '159.65.184.162:9050', 'user_pass': ''},
    # {'ip_port': '108.170.109.186:38355', 'user_pass': ''},
    # {'ip_port': '35.228.111.162:3128', 'user_pass': ''},
    # {'ip_port': ' 208.97.31.229:53124', 'user_pass': ''},
    # {'ip_port': '96.44.183.149:55225', 'user_pass': ''},
    # {'ip_port': '162.144.126.204:8133', 'user_pass': ''},
    # {'ip_port': '174.76.35.15:1080', 'user_pass': ''},
    # {'ip_port': '67.229.103.114:3128', 'user_pass': ''},
    # {'ip_port': '132.145.201.21:3128', 'user_pass': ''},
    # {'ip_port': '34.214.115.0:443', 'user_pass': ''},
    # {'ip_port': '104.248.66.100:3128', 'user_pass': ''},
    # {'ip_port': '40.114.109.214:3128', 'user_pass': ''},
    # {'ip_port': '134.209.49.222:3128', 'user_pass': ''},
    # {'ip_port': '67.205.151.211:3128', 'user_pass': ''},
    # {'ip_port': '68.183.111.90:80', 'user_pass': ''},
    # {'ip_port': '157.230.140.12:80', 'user_pass': ''},
    # {'ip_port': '47.254.21.23:80', 'user_pass': ''},
    # {'ip_port': '96.87.188.193:61748', 'user_pass': ''},
    # {'ip_port': '162.211.126.220:443', 'user_pass': ''},
    # {'ip_port': '52.9.244.23:3128', 'user_pass': ''},
    # {'ip_port': '45.55.9.218:1080', 'user_pass': ''},
]
# PROXIES = [
#     {'ip_port': '97.72.175.238:87', 'user_pass': ''},
#     {'ip_port': '108.46.171.184:43780', 'user_pass': ''},
#     {'ip_port': '192.169.190.207:10976', 'user_pass': ''},
#     {'ip_port': '198.199.120.102:1080', 'user_pass': ''},
#     {'ip_port': '162.243.25.182:33379', 'user_pass': ''},
#     {'ip_port': '209.141.32.12:80', 'user_pass': ''},
#     {'ip_port': '98.143.145.29:62354', 'user_pass': ''},
#     {'ip_port': '138.68.59.157:1210', 'user_pass': ''},
#     {'ip_port': '159.65.184.162:9050', 'user_pass': ''},
#     {'ip_port': '108.170.109.186:38355', 'user_pass': ''},
#     {'ip_port': '35.228.111.162:3128', 'user_pass': ''},
#     {'ip_port': ' 208.97.31.229:53124', 'user_pass': ''},
#     {'ip_port': '96.44.183.149:55225', 'user_pass': ''},
#     {'ip_port': '162.144.126.204:8133', 'user_pass': ''},
#     {'ip_port': '174.76.35.15:1080', 'user_pass': ''},
#     {'ip_port': '67.229.103.114:3128', 'user_pass': ''},
#     {'ip_port': '132.145.201.21:3128', 'user_pass': ''},
#     {'ip_port': '34.214.115.0:443', 'user_pass': ''},
#     {'ip_port': '104.248.66.100:3128', 'user_pass': ''},
#     {'ip_port': '40.114.109.214:3128', 'user_pass': ''},
#     {'ip_port': '134.209.49.222:3128', 'user_pass': ''},
#     {'ip_port': '67.205.151.211:3128', 'user_pass': ''},
#     {'ip_port': '68.183.111.90:80', 'user_pass': ''},
#     {'ip_port': '157.230.140.12:80', 'user_pass': ''},
#     {'ip_port': '47.254.21.23:80', 'user_pass': ''},
#     {'ip_port': '96.87.188.193:61748', 'user_pass': ''},
#     {'ip_port': '162.211.126.220:443', 'user_pass': ''},
#     {'ip_port': '52.9.244.23:3128', 'user_pass': ''},
#     {'ip_port': '45.55.9.218:1080', 'user_pass': ''},
# ]
# 代理服务器
# proxyServer = "http://http-dyn.abuyun.com:9020"
# PROXY_SERVER = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H012345678901zyx"
# proxyPass = "0123456789012xyz"
# PROXY_USER= "H012345678901zyx"
# PROXY_PASS= "0123456789012xyz"

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'yelpSpider.middlewares.RandomProxy': 543,
    'yelpSpider.middlewares.RandomUserAgent': 542,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'yelpSpider.pipelines.YelpspiderPipeline': 300,
# }

ITEM_PIPELINES = {
   'yelpSpider.pipelines.YelpspiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# 如果要保证纵向爬取的时候，数据漏爬，可以打开此配置
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
