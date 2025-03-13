from tkinter import *
from time import strftime
from PIL import Image, ImageTk
from tkinter import messagebox
from playsound import playsound
import threading
import random
import time

window = Tk()
window.geometry("310x600")
window.title("bleckbery")
window.config(background="black")


def times():
    string = strftime("%H:%M")
    Tiden_Mobil.config(text=string)
    Tiden_Mobil.after(1000, times)
    

    
Talet = random.randint(1,100)

class GissaTalet(Toplevel):
    def __init__(self, window = None,):
        super().__init__(master= window)       
        self.geometry("310x600")
        self.title("Gissa talet!")
        self.config(background="Black")

        Gissa_Text = Label(self, text="Gissa på ett tal (1-100):", bg="Orange")
        Gissa_Text.place(x=30, y=110)
        Skriv_tal = Entry(self, bg="White")
        Skriv_tal.place(x=200,y=110, width=60)
        

        Välkommen = Label(self, font="Arial", text= "Välkommen till Gissa talet!", bg="Orange")
        Välkommen.place(x=30, y=40)

        def högre_lägre():
            try:
                CoolaTal = int(Skriv_tal.get())
            except:
                Ingen_Siffra = Label(self,bg="Orange", text= "Skriv en siffra mellan 1-100")
                Ingen_Siffra.place(x=30, y=200)
            if CoolaTal < Talet:
                Högre_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Fel.")
                Högre_Tal.place(x=30, y=200)
                Högre_Tal_Sa = Label(self,bg="Orange", text= "Talet är Högre")
                Högre_Tal_Sa.place(x=30, y=220)
            elif CoolaTal > 100:
                Fel_Inmattning = Label(self,bg="Orange", text="Skriv en siffra mellan 1-100")
                Fel_Inmattning.place(x=30, y=200)
            elif CoolaTal > Talet:
                Lägre_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Fel.")
                Lägre_Tal_Sa = Label(self,bg="Orange", text= "Talet är Lägre")
                Lägre_Tal_Sa.place(x=30, y=220)
                Lägre_Tal.place(x=30, y=200)
            elif CoolaTal == Talet:
                Korrekt_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Korrekt!")
                Korrekt_Tal.place(x=30, y=200)
                Korrekt_Tal_Sa = Label(self,bg="Orange", text= "Talet är varken högre eller lägre!")
                Korrekt_Tal_Sa.place(x=30, y=220)
        Gissa_Knapp = Button(self,text="Gissa!",command=högre_lägre, bg="White")
        Gissa_Knapp.place(x=200,y=135, width=60,)

expression = ""
class Välj(Toplevel):
    def __init__(gui, window = None,):
        super().__init__(master= window)   
        gui.geometry("400x200")
        gui.title("Inloggning")

        label = Label(gui, text="Skriv ditt Namn:")
        label.place(x=0, y=0)
        Meddelande1 = Entry(gui, width=10)
        Meddelande1.place(x=100, y=0)

        label = Label(gui, text="Skriv din Adress:")
        label.place(x=0, y=25)
        Meddelande2 = Entry(gui, width=10)
        Meddelande2.place(x=100, y=25)

        label = Label(gui, text="Skriv ditt personnummer:")
        label.place(x=0, y=50)
        Meddelande3 = Entry(gui, width=10)
        Meddelande3.place(x=140, y=50)

        val = StringVar(gui)
        option_list = ["Iphone", "Samsung", "Xperia", "Övrigt"]
        val.set("Välj Din Mobil")
        dropdown = OptionMenu(gui, val, *option_list)
        dropdown.place(x=250,y=0)

        def knapp_trycksak():
            if len(Meddelande1.get()) == 0:
                messagebox.showerror("Error","Du måste skriva ett namn!!")
            elif len(Meddelande2.get()) == 0:
                messagebox.showerror("Error","Du måste skriva en giltlig adress")
            elif len(Meddelande3.get()) != 12:
                messagebox.showerror("Error","Skriv ditt personnummer med 12 siffror")
            else:
                messagebox.askquestion(title="Dina Val", message= "Ditt Namn: " + Meddelande1.get() + ", Din Adress:  " + Meddelande2.get() + ", Ditt Personnummer: " + Meddelande3.get() + ", Din Telefon: " + val.get())
    
        knapp = Button(gui, text="Bekräfta", command=knapp_trycksak)
        knapp.place(x=10,y=100)
poäng = 0
fart = 10

x = 150
y = 300
game_over = False

class Flappy(Toplevel):
    def __init__(flappy, window = None,):
        super().__init__(master= window)   

        flappy.geometry('1000x600')
        flappy.title('Flappy bird')


        bild_fågel = Image.open('Slutprojekt/Bilder/fagel.png')
        bild_fågel = ImageTk.PhotoImage(bild_fågel)

        bild_rör_nere = Image.open('Slutprojekt/Bilder/ror.png')
        bild_rör_uppe = bild_rör_nere.rotate(180)

        bild_rör_nere = ImageTk.PhotoImage(bild_rör_nere)
        bild_rör_uppe = ImageTk.PhotoImage(bild_rör_uppe)

        bild_starta_om = Image.open('Slutprojekt/Bilder/starta_om.png')
        bild_starta_om = ImageTk.PhotoImage(bild_starta_om)


        canvasflappy = Canvas(flappy, highlightthickness=0, bg= '#00bfff')
        canvasflappy.place(relheight= 1, relwidth= 1)

        text_poäng = canvasflappy.create_text(50,50, text= '0', fill = 'white', font =('D3 Egoistism outline',30))

        fågel = canvasflappy.create_image(x,y, anchor= 'nw', image = bild_fågel)
        rör_uppe = canvasflappy.create_image(1200, -550, anchor= 'nw', image = bild_rör_uppe)
        rör_nere = canvasflappy.create_image(1200, 550, anchor= 'nw', image = bild_rör_nere)

        def rör_fågel_knapp(event):
            global x,y
            if not game_over:
                y -=30
                canvasflappy.coords(fågel ,x,y)

        flappy.bind( "<space>", rör_fågel_knapp)

        def flytta_fågel():
            global x, y
            y += 5
            canvasflappy.coords(fågel, x, y)
            if y < 0 or y > canvasflappy.winfo_height():
                spel_över()
            
            if not game_over:
                flappy.after(50, flytta_fågel)

        def flytta_rör():
            global poäng,game_over,fart
            canvasflappy.move(rör_uppe, -fart, 0)
            canvasflappy.move(rör_nere, -fart, 0)
            if canvasflappy.coords(rör_nere)[0] < -100:
                h = flappy.winfo_height()
                num = random.choice([i for i in range(160,h,160)])
                canvasflappy.coords(rör_nere, flappy.winfo_width(), num + 160)
                canvasflappy.coords(rör_uppe, flappy.winfo_width(), num - 900)

            if 145 < canvasflappy.coords(rör_nere)[0] <155:
                poäng += 1
                fart += 1
                canvasflappy.itemconfigure(text_poäng, text= str(poäng))

            if canvasflappy.coords(rör_nere):
                if (canvasflappy.bbox(fågel)[0] < canvasflappy.bbox(rör_nere)[2] and 
            canvasflappy.bbox(fågel)[2] > canvasflappy.bbox(rör_nere)[0] and 
            (canvasflappy.bbox(fågel)[1] < canvasflappy.bbox(rör_uppe)[3] or 
            canvasflappy.bbox(fågel)[3] > canvasflappy.bbox(rör_nere)[1])):
                        spel_över()
            if not game_over:
                flappy.after(50, flytta_rör)



        def starta_om_spel():
            global x,y,poäng,fart,game_over
            x = 150
            y = 300
            poäng = 0
            fart = 10
            game_over = False
            canvasflappy.coords(fågel, x,y)
            canvasflappy.coords(rör_uppe, 1200, -550)
            canvasflappy.coords(rör_nere, 1200, 550)
            canvasflappy.itemconfigure(text_poäng, text="0")
            text_game_over.place_forget()
            starta_om_knapp.place_forget()
            flytta_fågel()
            flytta_rör()



        def spel_över():
            global game_over
            game_over = True
            text_game_over.place(relx= 0.5, rely=0.4, anchor='center')
            starta_om_knapp.place(relx=0.5, rely= 0.7, anchor= 'center')


        text_game_over = Label(flappy, text= 'Du suger! spela igen?', font=('D3 Egoistism outline',30),fg='White', bg='#00bfff')
        starta_om_knapp = Button(flappy, border=0, image= bild_starta_om, activebackground='#00bfff', bg= '#00bfff', command= starta_om_spel)


        flappy.after(50, flytta_fågel)
        flappy.after(50, flytta_rör)

        flappy.mainloop()


def play_audio_image():
    audio_thread = threading.Thread(target=play_audio_lebon)
    audio_thread.start()
    show_image()

def play_audio_lebon():
    try:
        playsound("Slutprojekt/Ljud/SunshineLjud.mp3")  # Uppdatera med sökvägen till ditt ljudfil
    except Exception as e:
        print("Error playing audio:", e)

def show_image():
    image_window = Toplevel()
    image_window.title("lebon")
    image_window.geometry("600x900")

    Lebonbild = Image.open("Sunshine.jpg")  # Uppdatera med sökvägen till din bildfil
    photo = ImageTk.PhotoImage()

    image_label = Label(image_window, image=photo)
    image_label.image = photo
    image_label.pack()

def knapp_bon_click():
    play_audio_image()

Telefon_färg = Canvas(window, width=275,height=530,bg="pink")
Telefon_färg.place(x=15,y=15)

Telefon_färg_Ladda = Canvas(window, width=250,height=450,bg="Lightblue")
Telefon_färg_Ladda.place(x=25,y=50)

Kamera = Canvas(window, width=10, height=10, bg="Black")
Kamera.pack(anchor="center",pady=32)

Sättpå_Knapp = Canvas(window, width=25, height=25, bg="Black")
Sättpå_Knapp.place(x=140,y=515)

KnappBon = Button(window, height=1,width=1,command=knapp_bon_click,bg="Black")
KnappBon.place(x=145,y=20)
Black_Bar_Topp = Label(window,bg="black",width=35,height=1)
Black_Bar_Topp.place(x=25,y=50)
Black_Bar_Höger = Label(window,bg="black",width=1,height=30)
Black_Bar_Höger.place(x=270,y=50)
Black_Bar_Vänster = Label(window,bg="black",width=1,height=30)
Black_Bar_Vänster.place(x=25,y=50)
Black_Bar_Botten = Label(window,bg="black",width=36,height=1)
Black_Bar_Botten.place(x=25,y=490)
    
Laddning = 0
for i in range(Laddning,101):
        LaddningVisa = Label(window,text=("Loading",i,"%"),font="Arial 15 bold",fg="White",bg="Lightblue")
        LaddningVisa.place(x=92,y=250)
        time.sleep(0.01)
        Laddning = i+1
        LaddningVisa.update()
        LaddningVisa.place_forget()
playsound("Slutprojekt/Ljud/Load.mp3")      
Klart = Label(window,text="Klart",font="Arial 15 bold",fg="White",bg="Lightblue")   
def klart():
    Klart.place(x=192,y=250)
    window.after(1000,förstöra)

def förstöra():
    Klart.place_forget()
klart()


Bakgrundsbild = Image.open("Slutprojekt/Bilder/wolf.png")
PhotoWolf = ImageTk.PhotoImage(Bakgrundsbild)
Wolf = Label(window, image=PhotoWolf, width=250,height=450)
Wolf.place(x=25,y=50)
Black_Bar_Topp = Label(window,bg="black",width=35,height=1)
Black_Bar_Topp.place(x=25,y=50)
Black_Bar_Höger = Label(window,bg="black",width=1,height=30)
Black_Bar_Höger.place(x=270,y=50)
Black_Bar_Vänster = Label(window,bg="black",width=1,height=30)
Black_Bar_Vänster.place(x=25,y=50)
Black_Bar_Botten = Label(window,bg="black",width=36,height=1)
Black_Bar_Botten.place(x=25,y=490)

Click_Gissa = PhotoImage(file="Slutprojekt/Bilder/Guess.png")
Bild_Gissa= Label(image=Click_Gissa)
KnappGissa = Button(window, height=40,width=40,text="Gissa",image=Click_Gissa)
KnappGissa.bind("<Button>", lambda e: GissaTalet(window))
KnappGissa.place(x=205,y=350)

Click_Uppg = PhotoImage(file="Slutprojekt/Bilder/Task.png")
Bild_Uppg= Label(image=Click_Uppg)
KnappVälj = Button(window, height=40,width=40,image=Click_Uppg)
KnappVälj.bind("<Button>", lambda e: Välj(window))
KnappVälj.place(x=130,y=350)

Click_Flappy = PhotoImage(file="Slutprojekt/Bilder/Flappybird.png")
Bild_Flappy= Label(image=Click_Flappy)
KnappFlappy = Button(window, height=40,width=40,image=Click_Flappy)
KnappFlappy.bind("<Button>", lambda e: Flappy(window))
KnappFlappy.place(x=55, y=350)

Click_Settings = PhotoImage(file="Slutprojekt/Bilder/Settings.png")
Bild_Settings = Label(image=Click_Settings)
KnappSettings = Button(window, height=40,width=40,image=Click_Settings)
KnappSettings.bind("<Button>", lambda e: Välj(window))
KnappSettings.place(x=55, y=425)

BildpåDully = Image.open("Slutprojekt/Bilder/dully.png")
Photopådully = ImageTk.PhotoImage(BildpåDully)
Dully = Label(window, image=Photopådully, width=250,height=450)

BildpåDavid = Image.open("Slutprojekt/Bilder/David.png")
PhotopåDavid = ImageTk.PhotoImage(BildpåDavid)
David = Label(window, image=PhotopåDavid, width=250,height=450)

BildpåBeast = Image.open("Slutprojekt/Bilder/Mrbeast.png")
PhotopåBeast = ImageTk.PhotoImage(BildpåBeast)
MrBeast = Label(window, image=PhotopåBeast, width=250,height=450)

BildpåViktor = Image.open("Slutprojekt/Bilder/Viktor.png")
PhotopåViktor = ImageTk.PhotoImage(BildpåViktor)
Viktor = Label(window, image=PhotopåViktor, width=250,height=450)

BildpåTony = Image.open("Slutprojekt/Bilder/Tony.png")
PhotopåTony = ImageTk.PhotoImage(BildpåTony)
Tony = Label(window, image=PhotopåTony, width=250,height=450)

BildpåStefan = Image.open("Slutprojekt/Bilder/Stefan.png")
PhotopåStefan = ImageTk.PhotoImage(BildpåStefan)
Stefan = Label(window, image=PhotopåStefan, width=250,height=450)

BildpåJiro = Image.open("Slutprojekt/Bilder/Jiro.png")
PhotopåJiro = ImageTk.PhotoImage(BildpåJiro)
Jiro = Label(window, image=PhotopåJiro, width=250,height=450)

BildpåSebbe = Image.open("Slutprojekt/Bilder/Sebbe.png")
PhotopåSebbe = ImageTk.PhotoImage(BildpåSebbe)
Sebbe = Label(window, image=PhotopåSebbe, width=250,height=450)


Meddelande1 = Canvas(window, height=40, width=200, bg="White")
Meddelande1_label = Label(window, text="Meddelande", font="Arial 7", bg="white")


def dully():
    Dully.place(x=25,y=50)
    
def david():
    David.place(x=25,y=50)
    
def Mrbeast():
    MrBeast.place(x=25,y=50)
    
def viktor():
    Viktor.place(x=25,y=50)

def tony():
    Tony.place(x=25,y=50)
    
def stefan():
    Stefan.place(x=25,y=50)
    
def jiro():
    Jiro.place(x=25,y=50)

def sebbe():
    Sebbe.place(x=25,y=50)
    

OlikaRinger = [dully, david, Mrbeast, viktor, tony, stefan, jiro, sebbe]


def meddelandeolja():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_Viktor.pack(anchor=CENTER,pady=20)

def meddelandemamma():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddedlande_mamma.pack(anchor=CENTER, pady=20)

def meddelandemelissa():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_Melissa.pack(anchor=CENTER, pady=20)

def meddelandelennon():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_Lennon.pack(anchor=CENTER, pady=20)

def meddelandejiro():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_jiro.pack(anchor=CENTER, pady=20)

def meddelandemirre():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_mirre.pack(anchor=CENTER, pady=20)

def meddelandebui():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_bui.pack(anchor=CENTER, pady=20)  

def meddelandealexander():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_alexander.pack(anchor=CENTER, pady=20)   

def meddelandedavid():
    Meddelande1.place(x=50, y=80)
    Meddelande1_label.place(x=50, y=80)
    Meddelande_david.pack(anchor=CENTER, pady=20)  

Meddelande_Viktor = Label(window, text="Viktor: Glöm inte oljan", bg="white", font="Arial 9 bold")
Meddedlande_mamma = Label(window, text="Mamma: Spola efter dig!!", bg="white", font="Arial 9 bold")
Meddelande_Melissa = Label(window, text="Melissa: Röker du igen!?", bg="white", font="Arial 9 bold")
Meddelande_Lennon = Label(window, text="Lennon: 05:12 rolig fågel", bg="white", font="Arial 9 bold")
Meddelande_jiro = Label(window, text="Jiro: 1 Dollar!", bg="white", font="Arial 9 bold")
Meddelande_mirre = Label(window, text="Mio: Eurotruck?", bg="white", font="Arial 9 bold")
Meddelande_bui = Label(window, text="Tony B: VIETNAM!", bg="white", font="Arial 9 bold")
Meddelande_alexander = Label(window, text="Alexander: När är Gähda?", bg="white", font="Arial 9 bold")
Meddelande_david = Label(window, text="David: BOWLING", bg="white", font="Arial 9 bold")


ListMeddelande = [meddelandeolja, meddelandemamma, meddelandemelissa, meddelandelennon, meddelandejiro, meddelandemirre, meddelandebui, meddelandealexander, meddelandedavid]  # Lagra funktionerna utan att anropa dem


def show_random_message():
    # Slumpmässigt beslut om meddelandet ska visas och ljudet ska spelas
    if random.random() < 0.8:
            if random.random() < 0.4:
                random_message_func = random.choice(ListMeddelande)
                random_message_func()
                thread_audio = threading.Thread(target=play_audio)
                thread_audio.start()
                window.after(5000, remove_message)
                window.after(15000, show_random_message)
            else:
                random_message_func = random.choice(OlikaRinger)
                random_message_func() 
                thread_audio = threading.Thread(target=play_audioRing)
                thread_audio.start() 
                window.after(17500, remove_message)
                window.after(27500, show_random_message)

Black_Bar_Topp = Label(window,bg="black",width=35,height=1)
Black_Bar_Topp.place(x=25,y=50)
Black_Bar_Höger = Label(window,bg="black",width=1,height=30)
Black_Bar_Höger.place(x=270,y=50)
Black_Bar_Vänster = Label(window,bg="black",width=1,height=30)
Black_Bar_Vänster.place(x=25,y=50)
Black_Bar_Botten = Label(window,bg="black",width=36,height=1)
Black_Bar_Botten.place(x=25,y=490)



def play_audio():
    try:
        playsound("Slutprojekt/Ljud/Message.mp3")  # Uppdatera med sökvägen till ditt ljudfil
    except Exception as e:
        print("Error playing audio:", e)
        
def play_audioRing():
    try:
        playsound("Slutprojekt/Ljud/Ring.mp3")  # Uppdatera med sökvägen till ditt ljudfil
    except Exception as e:
        print("Error playing audio:", e)
        
Tiden_Mobil = Label(window,bg="Black",fg="White",font=("Arial 9 bold"))
Tiden_Mobil.place(x=136,y=50)
Fredag = Label(window,text="Fre",bg="Black",fg="White",font=("Arial 9 bold"))
Fredag.place(x=70,y=50)
Batteri = Label(window,text="57%",bg="Black",fg="White",font=("Arial 9 bold"))
Batteri.place(x=220,y=50)       

def remove_message():
    Meddelande1.place_forget()
    Meddelande1_label.place_forget()
    Meddelande_Viktor.pack_forget()
    Meddedlande_mamma.pack_forget()
    Meddelande_Melissa.pack_forget()
    Meddelande_Lennon.pack_forget()
    Meddelande_jiro.pack_forget()
    Meddelande_mirre.pack_forget()
    Meddelande_bui.pack_forget()
    Meddelande_alexander.pack_forget()
    Meddelande_david.pack_forget()
    Dully.place_forget()
    David.place_forget()
    MrBeast.place_forget()
    Viktor.place_forget()
    Tony.place_forget()
    Stefan.place_forget()
    Jiro.place_forget()
    Sebbe.place_forget()


show_random_message()
times()
window.mainloop()