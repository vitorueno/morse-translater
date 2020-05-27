import tkinter as tk
from .gui import App
from .constants import WIDGET_TEXT, FONT, INPT_W


if __name__ == "__main__":
    root = tk.Tk(className=' Morse Translater')
    root.geometry('500x250')
    root.maxsize(500,250)
    App(root)
    root.mainloop()
    