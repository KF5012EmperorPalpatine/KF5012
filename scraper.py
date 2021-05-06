import scrapy
from scrapy.spiders import CrawlSpider, Rule



class HeadlineSpider(scrapy.Spider):
    name = "Headline_spider"
    def __init__(self,ticker,*a,**kw):
        super(HeadlineSpider,self).__init__(*a,**kw)
        self.url = "https://finviz.com/quote.ashx?t="+ticker

    def start_requests(self):
        yield scrapy.Request(url= self.url,callback=self.parse)

    def parse(self, response):
        SET_SELECTOR = '.news-link-left'
        file = open("headlineData.txt", "w+")
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            file.write(brickset.css(NAME_SELECTOR).extract_first() + "\n")
        file.close()


