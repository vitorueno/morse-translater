import tkinter as tk
from .constants import WIDGET_TEXT, FONT, INPT_W
from .decrypt import decrypt
from .encrypt import encrypt


class App(tk.Frame):
    def __init__(self, master=None, lang='ENGLISH'):
        super().__init__(master)
        self.master = master
        self.mode = 'text'
        self.output_txt = ''
        self.text = WIDGET_TEXT[lang]
        self.lang = lang
        self.create_containers()
        self.create_widgets()

    def set_mode_label_text(self):
        if self.lang == 'ENGLISH':
            text = 'Mode: Text to Morse' if self.mode == 'text' else 'Mode: Morse to Text'
        else:
            text = 'Modo: Texto para Morse' if self.mode == 'text' else 'Modo: Morse para Texto'
        return text

    def create_containers(self):
        self.container_1 = tk.Frame(self.master, pady='18')
        self.container_1.pack()

        self.container_2 = tk.Frame(self.master)
        self.container_2.pack()

        self.container_3 = tk.Frame(self.master)
        self.container_3.pack()

        self.container_4 = tk.Frame(self.master, pady='20')
        self.container_4.pack()
        
        self.container_5 = tk.Frame(self.container_4, padx='10')
        self.container_5.pack(side='left')

    def create_widgets(self):
        self.main_title = tk.Label(
            self.container_1, text=self.text['main_title'], font=('Arial', '17'))
        self.main_title.pack()

        self.mode_label = tk.Label(
            self.container_1, text=self.set_mode_label_text(), font=FONT)
        self.mode_label.pack()

        self.title_input = tk.Label(
            self.container_2, text=self.text['title_input'], font=FONT)
        self.title_input.pack()

        self.title_output = tk.Label(
            self.container_3, text=self.text['title_output'], font=FONT)
        self.title_output.pack()

        self.input = tk.Entry(
            self.container_2, width=INPT_W)
        self.input.pack()

        self.output_label = tk.Entry(
            self.container_3, text=self.output_txt, width=INPT_W, bg='white')
        self.output_label.pack()

        self.translate_button = tk.Button(
            self.container_4, text=self.text['translate_btn'], font=FONT,
            command=self.translate)
        self.translate_button.pack()

        self.change_btn = tk.Button(
            self.container_5, text=self.text['change_btn'], font=FONT,
            command=self.change_mode)
        self.change_btn.pack()

    def translate(self):
        if self.mode == 'text':
            try:
                self.clear_output()
                self.output_label.insert(0, encrypt(self.input.get()))
            except:
                self.clear_output()
                self.output_label.insert(0, self.text['ERROR'])

        elif self.mode == 'morse':
            try:
                self.clear_output()
                self.output_label.insert(0, decrypt(self.input.get()).lower())
            except:
                self.clear_output()
                self.output_label.insert(0, self.text['ERROR'])

    def change_mode(self):
        self.mode = 'morse' if self.mode == 'text' else 'text'
        self.clear_input()
        self.clear_output()
        self.mode_label['text'] = self.set_mode_label_text()

    def clear_output(self):
        self.output_label.delete(0, len(self.output_label.get()))

    def clear_input(self):
        self.input.delete(0, len(self.input.get()))


if __name__ == "__main__":
    root = tk.Tk(className=' Morse Translater')
    root.geometry('500x250')
    App(root)
    root.mainloop()
