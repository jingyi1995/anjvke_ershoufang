# -*- coding: utf-8 -*-
import random
# Scrapy settings for ershoufang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ershoufang'
# BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['ershoufang.spiders']
NEWSPIDER_MODULE = 'ershoufang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# COOKIE = 'lianjia_uuid=78afb6cb-e84a-46b9-8b9c-fc8b35fe8a2b; UM_distinctid=15b2d75853f310-0870b0fb315b3f-1c3e6b52-13c680-15b2d7585404e6; all-lj=138f1e66bf8c368d8c8b328e9ff033b4; cityCode=su; ubt_load_interval_b=1491655701528; gr_user_id=52f0509f-90f6-4da0-8d69-059ecb000033; ubta=1641808036.2328422.1491655702031.1491655702031.1491655702031.1; ubtc=1641808036.2328422.1491655702036.2F24693F4EA1E476984304F8DE575445; ubtd=1; select_city=110000; _smt_uid=58e0a12b.28dcf00a; lianjia_ssid=57e186f1-94d5-48c1-aa57-534ada92a3ed'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
RETRY_ENABLED = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 设置延迟时间，注意安居客网站有反爬虫机制，不能设置过快，过快会封ip
num=[55,60,50,48]
DOWNLOAD_DELAY = random.choice(num)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 2
CONCURRENT_REQUESTS_PER_IP = 2

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ershoufang.middlewares.ErshoufangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ershoufang.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'ershoufang.pipelines.ErshoufangPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ershoufang.middlewares.RotateUserAgentMiddleware': 400 ,
    # 'ershoufang.middlewares.ABYProxyMiddleware': 1 # 如果用了代理这里要取消注释
}


