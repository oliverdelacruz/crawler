from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import AmazonItem

class AmazonSpider(CrawlSpider):
    name = "amazon_spider"
    allowed_domains = [
        'amazon.com',
        'amazon.uk',
        'amazon.de',
        'amazon.fr',
        'amazon.es',
        'amazon.it'
        ]
    start_urls = [
        # 'https://www.amazon.com/dp/B0046UR4F4',
        'https://www.amazon.co.uk',
        # 'https://www.amazon.de/',
        # 'https://www.amazon.fr/',
        # 'https://www.amazon.es/',
        # 'https://www.amazon.it/'
    ]

    rules = (
        Rule(LinkExtractor(),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print("------------------------------")
        print('Processing..' + response.url)

    # def parse(self, response):
    #     items = AmazonItem()
    #     title = response.xpath('//h1[@id="title"]/span/text()').extract()
    #     sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
    #     category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
    #     availability = response.xpath('//div[@id="availability"]//text()').extract()
    #     items['product_name'] = ''.join(title).strip()
    #     items['product_sale_price'] = ''.join(sale_price).strip()
    #     items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
    #     items['product_availability'] = ''.join(availability).strip()
    #     yield items

    # def parse(self, response):
    #     response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('span small::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
    #
    #     next_page = response.css('li.next a::attr(href)').get()
    #     if next_page is not None:
    #         yield response.follow(next_page, callback=self.parse)

        # def parse_item(self, response):
        #     item = scrapy.Item()
        #     item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        #     item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        #     item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        #     return item