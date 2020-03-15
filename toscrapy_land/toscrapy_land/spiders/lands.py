# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import LandItem

class LandsSpider(scrapy.Spider):
    name = 'lands'
    allowed_domains = ['www.gumtree.com.au']
    start_urls = ['https://www.gumtree.com.au/s-land-for-sale/melbourne/page-1/c20031l3001317']
    
    def start_requests(self):
        for i in range(1,2):
            yield Request('https://www.gumtree.com.au/s-land-for-sale/melbourne/page-%s/c20031l3001317' % i)

    def parse(self, response):
        land = LandItem()
        #for sel in response.xpath('//div[@class="user-ad-row__details"]'):
            #land['title'] = sel.xpath('./div[@class="user-ad-row__info"]/p[@class="user-ad-row__title"]/text()').extract_first()
            #land['price'] = sel.xpath('./div[@class="user-ad-row__info"]/div/span[1]/text()').extract_first()
            #land['negotiable'] = sel.xpath('./div[@class="user-ad-row__info"]/div/span[2]/text()').extract_first()
            #land['age'] = sel.xpath('./div[@class="user-ad-row__extra-info"]/p[@class="user-ad-row__age"]/text()').extract_first()
            #land['region'] = sel.xpath('./div[@class="user-ad-row__extra-info"]/div[@class="user-ad-row__location"]//text()').extract_first()
            #land['location'] = sel.xpath('./div[@class="user-ad-row__extra-info"]/div[@class="user-ad-row__location"]//text()').extract()[1]
        for sel in response.xpath('//div[@class="panel-body panel-body--flat-panel-shadow user-ad-collection__list-wrapper"]/a'):
            land['id'] = sel.xpath('./@id').extract_first()
            land['title'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__info"]/p[@class="user-ad-row__title"]/text()').extract_first()
            land['price'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__info"]/div/span[1]/text()').extract_first()
            land['negotiable'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__info"]/div/span[2]/text()').extract_first()
            land['age'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__extra-info"]/p[@class="user-ad-row__age"]/text()').extract_first()
            land['region'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__extra-info"]/div[@class="user-ad-row__location"]//text()').extract_first()
            land['location'] = sel.xpath('./div[@class="user-ad-row__details"]/div[@class="user-ad-row__extra-info"]/div[@class="user-ad-row__location"]//text()').extract()[1]
            yield land
