import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
import TickerGUI

class SentimentGUI(ttk.Frame):
    def __init__(self, container, ticker, prediction):
        container.geometry("400x400")
        super().__init__(container)
        self.container = container
        self.ticker = ticker
        self.pack()
        if(prediction == 1):
            self.prediction = True
        else:
            self.prediction = False

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
        self.headlineTxt = tk.Listbox(self.boxFrame, width = 60, height = 6)
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
        file = open("headlineData.csv","r")
        headlines = file.readlines()
        headlines = headlines[1].split(",")
        file.close()
        for headline in headlines[2:]:
            self.headlineTxt.insert(tk.END, headline)

        self.headlineTxt.config(state="disabled")

        #source label
        self.srclabel = ttk.Label(self.headlineFrame,text="Source: https://finviz.com/quote.ashx?t="+self.ticker)
        self.srclabel.pack(side="bottom")

        #direction frame
        self.directionFrame = ttk.Frame(self)
        self.directionFrame.pack()

        #up/down stock
        if self.prediction:
            self.imgfile = "goodStock.jpg"
            self.labeltxt = "We predict this stock with rise! Buy! Buy! Buy!"
        else:
            self.imgfile = "badStock.jpg"
            self.labeltxt = "We predict this stock with fall! Sell Sell Sell!"


        #direction label
        self.directionLabel = ttk.Label(self.directionFrame,text=self.labeltxt)
        self.directionLabel.pack(side="top")

        #direction image
        self.img = Image.open(self.imgfile)
        self.img = self.img.resize((100,75),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.imglbl = Label(self.directionFrame,image=self.img)
        self.imglbl.pack()

        #disclaimer labels
        self.disclaimertxt = "This prediction is 58% accurate\nThis is not financial advice\nAny investments are made at your own risks.\n71.2% of retail investor accounts lose money"
        self.disclaimerLabel = ttk.Label(self.directionFrame,text=self.disclaimertxt)
        self.disclaimerLabel.config(font=("Courier", 6))
        self.disclaimerLabel.pack(side="bottom")


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
            if line == self.ticker+"\n":
                found = True

        # if it is then add a button to remove it
        if found:
            self.removeButton = ttk.Button(self.footerFrame,text="Remove from Watchlist",command = self.Remove)
            self.removeButton.pack()
        # otherwise add a button to add it to the watchlist
        else:
            self.addButton = ttk.Button(self.footerFrame,text="Add to Watchlist",command = self.Add)
            self.addButton.pack()


    def Back(self):
        self.destroy()
        TickerGUI.TickerGUI(self.container)

    def Remove(self):
        index = self.lines.index(self.ticker+"\n")
        self.lines.pop(index)
        file = open("watchList.txt","w+")
        for line in self.lines:
            file.write(line)
        file.close()
        removeLabel = tk.Label(self.footerFrame,text="Removed!")
        removeLabel.pack(side = "bottom")


    def Add(self):
        file = open("watchList.txt","a")
        file.write(self.ticker+"\n")
        file.close()
        addLabel = tk.Label(self.footerFrame,text="Added!")
        addLabel.pack(side="bottom")