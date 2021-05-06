import tkinter as tk
from tkinter import ttk
import TickerGUI

class SentimentGUI(ttk.Frame):
    def __init__(self,container,ticker):
        super().__init__(container)
        self.container = container
        self.ticker = ticker
        self.pack()

        ## Headline Frame
        self.headlineFrame = ttk.Frame(self)
        self.headlineFrame.pack()

        #Ticker label
        self.tickerLabel = ttk.Label(self.headlineFrame,text=ticker)
        self.tickerLabel.config(font=("Courier", 30))
        self.tickerLabel.pack()


        # frame for listbox + scrollbar formatting
        self.boxFrame = ttk.Frame(self.headlineFrame)
        self.boxFrame.pack()

        #Headline text box + scroll bar
        self.headlineTxt = tk.Listbox(self.boxFrame, width = 60, height = 3)
        self.headlineTxt.pack(side = "left",fill="both")

        yscrollbar = tk.Scrollbar(self.boxFrame)
        yscrollbar.pack(side="right",fill="both")
        xscrollbar = tk.Scrollbar(self.headlineFrame,orient="horizontal")
        xscrollbar.pack(fill="both")

        self.headlineTxt.config(yscrollcommand = yscrollbar.set)
        self.headlineTxt.config(xscrollcommand = xscrollbar.set)
        yscrollbar.config(command = self.headlineTxt.yview)
        xscrollbar.config(command = self.headlineTxt.xview)

        #inserting data
        file = open("headlineData.txt","r")
        headlines = file.readlines()
        file.close()
        for line in headlines:
            self.headlineTxt.insert(tk.END, line)

        self.headlineTxt.config(state="disabled")

        #source label
        self.srclabel = ttk.Label(self.headlineFrame,text="Source: https://finviz.com/quote.ashx?t="+self.ticker)
        self.srclabel.pack(side="bottom")

        #footerframe
        self.footerFrame = ttk.Frame(self)
        self.footerFrame.pack()

        # back button
        self.backButton = ttk.Button(self.footerFrame,text="Back",command = self.Back )
        self.backButton.pack(side="left")

        # checking if ticker is in watchlist
        file = open("watchList.txt","r")
        self.lines = file.readlines()
        file.close()
        found = False
        for line in self.lines:
            if line == self.ticker:
                found = True

        # if it is then add a button to remove it
        if found:
            self.removeButton = ttk.Button(self.footerFrame,text="Remove from Watchlist",command = self.Remove)
            self.removeButton.pack()
        ## otherwise add a button to add it to the watchlist
        else:
            self.addButton = ttk.Button(self.footerFrame,text="Add to Watchlist",command = self.Add)
            self.addButton.pack()



    def getSentiment(self):
        pass

    def Back(self):
        self.destroy()
        TickerGUI.TickerGUI(self.container)

    def Remove(self):
        index = self.lines.index(self.ticker)
        self.lines.pop(index)
        file = open("watchList.txt","w+")
        for line in self.lines:
            file.write(line)
        removeLabel = tk.Label(self.footerFrame,text="Removed!")
        removeLabel.pack(side = "bottom")


    def Add(self):
        file = open("watchList.txt","a")
        file.write(self.ticker+"\n")
        file.close()
        addLabel = tk.Label(self.footerFrame,text="Added!")
        addLabel.pack(side="bottom")