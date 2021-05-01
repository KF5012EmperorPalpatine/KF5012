import tkinter as tk
from scrapy.crawler import CrawlerRunner
import scraper
from twisted.internet import reactor

# Functions ----------------------------
def submitTicker():
    ticker = tickerEntry.get()
    if len(ticker) > 5:
        errorLabel.grid(column= 0,row = 150)
        return
    reactor.callFromThread(startCrawl,ticker)

def startCrawl(ticker):
    CrawlerRunner.crawl(scraper.HeadlineSpider, ticker=ticker)
    CrawlerRunner.run()

#create tkinter object and base window
root = tk.Tk(className = "Sentimental Stocks")
root.geometry("500x350")


#header
title = tk.Label(root,text="Sentimental Stocks")
title.config(font=("Courier",30))
title.grid(columnspan = 6, row=50)

#ticker entry frame --------------------------
tickerFrame = tk.Frame(root, width = 250, height = 200, highlightbackground = "#000fff",highlightthickness = 1)
tickerFrame.grid(column = 0, columnspan=3, row=250, rowspan=200)
tickerFrame.grid_propagate(False)

# entry title
entryLabel = tk.Label(tickerFrame,text="Enter company stock Ticker")
entryLabel.grid(column= 0, row=50)

#ticker entry box
tickerEntry = tk.Entry(tickerFrame)
tickerEntry.grid(column = 0, row = 100)

#error label
errorLabel = tk.Label(tickerFrame,text="Invalid Ticker")
# error is only passed into grid when error occurs

#Sentiment Frame ---------------------------------------------
sentimentFrame = tk.Frame(root, width=250,height=200, highlightbackground="#000000",highlightthickness = 1)
sentimentFrame.grid(column=3, columnspan=3, row=250, rowspan=200)
sentimentFrame.grid_propagate(False)

#footerFrame --------------------------------------
footerFrame = tk.Frame(root, width=500, height=100, highlightbackground ='#fff000',highlightthickness = 1)
footerFrame.grid(column=0, columnspan = 6, row=500, rowspan = 100)
footerFrame.grid_propagate(False)

#submit button
submitButton = tk.Button(footerFrame, command = submitTicker, text = "submit")
submitButton.grid(column=250, row=40)

root.mainloop()


