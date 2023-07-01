import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyshorteners

urlshortner = tk.Tk()
urlshortner.title("URL SHORTNER")
urlshortner.minsize(400,200)
urlshortner.maxsize(400,200)

def shorten_url():
    try:
        value = str(LONG_URL_GET.get())
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(value)
        print(short_url)
        msg = Tk()
        msg.withdraw()
        messagebox.showinfo("İMFORMATİON","YOUR SHORT LİNK:\n"+str(short_url))

    except Exception as e:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("ERROR!","SOMETHİNG'S WRONG!\nPLEASE TRY AGAİN")


LONG_URL_GET_İNFO = tk.Label(urlshortner,text = "ENTER THE\nLİNK:",fg ="green",bg = "white",font = "Arial 15")
LONG_URL_GET_İNFO.place(width = 120,height = 100,x = 0,y = 0) 

LONG_URL_GET = tk.Entry(urlshortner,fg = "blue",bg = "white",font = "Arial 20")
LONG_URL_GET.place(width = 280,height = 100,x = 120,y = 0)

MAKE_SHORT_URL = tk.Button(urlshortner,text = "MAKE SHORT URL",fg = "lime",bg = "black",activeforeground = "black",activebackground = "lime",font = "Arial 20",command = shorten_url)
MAKE_SHORT_URL.place(width = 400,height = 100,x = 0,y = 100)

urlshortner.mainloop()
