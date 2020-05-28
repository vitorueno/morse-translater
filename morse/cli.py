import typer
import tkinter as tk
from .encrypt import encrypt
from .decrypt import decrypt
from .gui import App


app = typer.Typer()


@app.command()
def run():
    root = tk.Tk(className=' Morse Code Translater')
    root.geometry('500x278')
    root.maxsize(500, 278)
    App(root)
    root.mainloop()


@app.command()
def code(message: str):
    try:
        typer.echo(encrypt(message))
    except:
        typer.echo('ERROR: TRY ANOTHER VALUE')


@app.command()
def decode(message: str):
    try:
        typer.echo(decrypt(message).lower())
    except:
        typer.echo('ERROR: TRY ANOTHER VALUE')


if __name__ == "__main__":
    app()
