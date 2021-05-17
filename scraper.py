import scrapy
from scrapy.spiders import CrawlSpider, Rule



class HeadlineSpider(scrapy.Spider):
    name = "Headline_spider"
    def __init__(self,ticker,*a,**kw):
        super(HeadlineSpider,self).__init__(*a,**kw)
        self.url = "https://finviz.com/quote.ashx?t="+ticker

    def start_requests(self):
        yield scrapy.Request(url= self.url,callback=self.parse, errback = self.errorParse)

    def parse(self, response):
        SET_SELECTOR = '.news-link-left'
        file = open("headlineData.csv", "w+")
        headlines = []
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            headlines.append(brickset.css(NAME_SELECTOR).extract_first())
        file.write("empty1,empty2")
        for headerNum in range(1,len(headlines)):
            file.write(",headline"+str(headerNum))
        file.write("\nspacer2,spacer2")
        for headline in headlines:
            file.write(","+headline)
        file.close()

    def errorParse(self):
        file = open("headlineData.csv","w+")
        file.write("INVALID")
        file.close()
