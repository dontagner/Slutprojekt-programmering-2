from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


window = Tk()
window.geometry("900x600")
window.title("Promilleräknare")
window.config(background="lightblue")

Bakgrundsbild = Image.open("C:\Users\elttag1\OneDrive - Karlskoga Kommun\Skola\Slutprojekt-programmering-2\Bilder\middag.png")
PhotoMiddag = ImageTk.PhotoImage(Bakgrundsbild)
Middag = Label(window, image=PhotoMiddag, width=250,height=450)
Middag.place(x=25,y=50)

window.mainloop()