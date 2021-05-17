import tkinter as tk
from TickerGUI import TickerGUI
from SentimentGUI import SentimentGUI


class RootGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sentimental Stocks")
        self.resizable(False,False)

        TickerGUI(self)

if __name__ == "__main__":
    gui = RootGUI()
    gui.mainloop()