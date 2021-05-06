import tkinter as tk
from tkinter import ttk
from SentimentGUI import SentimentGUI
import scrapy
from scrapy.crawler import CrawlerProcess
from scraper import HeadlineSpider
import os

class TickerGUI(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.container = container
        self.pack()
        self.entryFrame = ttk.Frame(self)
        self.entryFrame.pack()

        # entry title
        self.entryLabel = ttk.Label(self.entryFrame, text="Enter company stock Ticker")
        self.entryLabel.pack()

        # ticker entry box
        self.tickerEntry = ttk.Entry(self.entryFrame)
        self.tickerEntry.pack()

        # submit button
        self.entrySubmitButton = ttk.Button(self.entryFrame,text="Submit",
                                            command = lambda : self.submit(self.tickerEntry.get()))
        self.entrySubmitButton.pack()

        self.watchlistFrame = ttk.Frame(self)
        self.watchlistFrame.pack()

        # watchlist title
        self.watchLabel = ttk.Label(self.watchlistFrame,text="Watchlist")
        self.watchLabel.pack()

        #watchlist menu
        file = open("Watchlist.txt","r")
        self.data = file.readlines()
        file.close()

        self.watchlistMenu = tk.Listbox(self.watchlistFrame, height = 7)
        self.watchlistMenu.pack(side = "left",fill="both")

        self.watchlistMenu.bind('<<ListboxSelect>>',self.clickEvent)

        scrollbar = ttk.Scrollbar(self.watchlistFrame)
        scrollbar.pack(side = "right",fill="both")
        self.watchlistMenu.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command = self.watchlistMenu.yview)

        for i in range(0,len(self.data)):
            self.watchlistMenu.insert(i,self.data[i])

    def clickEvent(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.tickerEntry.delete(0,len(self.tickerEntry.get()))
            self.tickerEntry.insert(0,data)

    def submit(self,ticker):
        # Do Scraping ///
        os.system('cmd /c scrapy runspider scraper.py -a ticker='+ticker)
        #load display page ///
        self.destroy()
        SentimentGUI(self.container,ticker)

    def validateTicker(self,ticker):
        pass
    # Do Validation ///

