
from tkinter import *
from tkinter import ttk
import os


def click ():      
    
    hostname = entry.get()
    response = os.system("ping -c 1 " + hostname)
    
    
    if response == 0:
        label["text"] = "online"
    else:
        label["text"] = "offline"
    #window.destroy()


search_ip = "test"

root = Tk()
root.title("track ip")
root.geometry("250x200") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="search ip", command=click)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
  
root.mainloop()

