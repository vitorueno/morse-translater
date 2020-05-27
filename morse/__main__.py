import tkinter as tk
from .gui import App
from .constants import WIDGET_TEXT, FONT, INPT_W


if __name__ == "__main__":
    root = tk.Tk(className=' Morse Code Translater')
    root.geometry('500x278')
    root.maxsize(500,278)
    App(root)
    root.mainloop()
    