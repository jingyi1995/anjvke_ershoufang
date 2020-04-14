# -*- coding: utf-8 -*-
import scrapy
#from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from scrapy.selector import Selector
import re
import demjson
import time
import string
import requests
from ershoufang.items import ErshoufangItem


class ershoufangSpider(scrapy.Spider):
    name = "ershoufang"
    allowed_domains = ['anjuke.com']
    # 生成起始网址
    start_urls = []
    for i in range(1,51):
        start_urls.append('https://cc.anjuke.com/sale/nanguan/p%d/#filtersort'%i)
        # 后面的起始网址网址，cc代表城市，nanguan是这个城市的一个区

    # 采集每个房屋网址链接
    def parse(self,response):
        # item = ErshoufangItem()
        selector = Selector(response)
        #url = Selector(respone)
        urls =selector.xpath(".//ul[@class='houselist-mod houselist-mod-new']/li")
        for url in urls:
            detail_url = url.xpath(".//div[@class='house-title']/a/@href").extract()[0]
            # item["url"] = detail_url
            yield scrapy.Request(detail_url,callback = self.parse_item)
            # yield item

    # 采集每个链接里面的房屋信息
    def parse_item(self,response):
        item = ErshoufangItem()

        houses = response.xpath(".//div[@class='wrapper-lf']")
        # for house in houses:
        # houseLoc 房屋位置，houseInfo 房屋具体信息（几室几厅等），Community 社区信息（绿化率等）
        # propertyCosts 物业费，totalPrice 房屋总价格
        if houses:
            item['houseLoc'] = houses.xpath(".//p[@class='loc-text']/a/text()").extract(),
            # item['houseEncode'] = house.xpath(".//h4/span[@class='house-encode']/text()").extract()
            item['houseInfo'] = houses.xpath(".//div[@class='houseInfo-content']/text()").extract()
            item['Community'] = houses.xpath(".//div[@class='commap-info-intro']/p/text()").extract()
            item['propertyCosts'] = houses.xpath(".//div[@class='commap-info-intro no-border-rg']/p/text()").extract()
            item['totalPrice'] = houses.xpath(".//span[@class='light info-tag']/em/text()").extract()

        # 采集房屋历史单价
        house_comid = response.xpath('/html').re(r'comid=.*?&')
        if house_comid:
            comid = house_comid[0].split('=')[-1][:-1]
            house_price_url = 'https://cc.anjuke.com/v3/ajax/prop/pricetrend/?commid=' + comid
            # 这里cc对应的是城市，记得要与起始网址的城市保持一致

            headers = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                    "x-requested-with": 'XMLHttpRequest'
                }
            response = requests.get(house_price_url, headers=headers)
            item['houseHistoryPrice'] = response.json().get('community')

            yield item




