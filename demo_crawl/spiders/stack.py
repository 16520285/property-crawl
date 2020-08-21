from scrapy import Spider, Request

from demo_crawl.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["batdongsan.com.vn"]
    start_urls = [
        "https://batdongsan.com.vn/nha-dat-ban",
    ]
    BASE_URL = 'https://batdongsan.com.vn'

    def parse(self, response):
        detail_urls = response.xpath('//a[@class="vipZero product-link"]/@href').extract()
    
        for url in detail_urls:
            yield Request(self.BASE_URL + url, callback=self.parse_detail)

    def parse_detail(self, response):
        # for detail in response.xpath('//div[@class="description"]'):
        item = StackItem()
        item['title'] = response.xpath('//h1[@class="tile-product"]/text()').extract()
        print ('duyyy')
        print (item)
        item['PN'] = response.xpath('//ul[@class="short-detail-2 clearfix pad-16"]/li[3]/span[@class="sp2"]/text()').extract() or response.xpath('//ul[@class="short-detail-2 clearfix pad-16"]/li[2]/span[@class="sp2"]/text()').extract()
        pn = item['PN'][0]
        item['PN'] = pn[0:1]
        yield item
