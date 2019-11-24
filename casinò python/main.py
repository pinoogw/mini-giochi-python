import random
import os
import socket
import hashlib
import time
import datetime
import uuid
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox


tempo = str(datetime.datetime.now().strftime("%H:%M:%S: %Y-%m-%d"))




def menu(): #menu
    print("sono le " + tempo)
    print("1-per chiudere")
    print("2-roulette")
    print("3-blackjack")
    print("4-indovina la carta")
    print("5-fondi")
    print("6-slot")
    print("7-dadi")

def scegli(): #scelta menu
    try:
        modalita = int(input("scegli la modalità di gioco "))
        while modalita not in [1,2,3,4,5,6,7]:
            print("modalità di gioco non disponibile ")
            modalita = int(input("scegli la modalità di gioco "))
        if modalita == 1:
            chiudere()
        if modalita == 2:
            roulette()
        if modalita == 3:
            blackjack()
        if modalita == 4:
            indovinalacarta()
        if modalita == 5:
            ricarica()
        if modalita == 6:
            slot()
        if modalita == 7:
            dadi()
    except ValueError:
        print("errore inserire solo numeri")
   


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
F = socket.gethostname()



def ban(): #ban
    F = socket.gethostname()
    with open('ban.txt','r')  as f:
        for line in f:
            if line == F:
                print("sei stato bannato")
                exit()
                banned = open('ban.txt', 'r')
                banned.close()
                break


def lista(): #comandi extra
    print("soldi")


def giocatore():
    with open('giocatore.txt') as file:
        f = open('giocatore.txt','r')
        giocatori = f.readline()
    print("benvenuto")
    print(giocatori)
    

def comandi():
    comando = input("inserire comando")
    if comando == "soldi":
        soldi = open('fondi-giocatore.txt','r')
        soldi = soldi.readlines()
        print(soldi)





def bancav():
    patrimonioo = open('banca.txt','r')
    patrimonio = patrimonioo.readline()
    print(patrimonio)
    patrimonio = int(patrimonio)
    if patrimonio == 0:
        print("banca vuota riavvio necessario")
        patrimonio = int(patrimonio + 30000000)
        soldi = open('banca.txt','w')
        soldi.write(str(patrimonio))
        soldi.close()
    else:
        patrimonio = patrimonio - 300
        asilo = open('banca.txt','w')
        asilo.write(str(patrimonio))
        patrimonioo.close()
        


def newusers(): #nuovo utente
    f = open("newusers.txt","w+")
    subprocess.check_call(["attrib","+H","newusers.txt"])
    login = input("inserire il nome utente")
    log = open("giocatore.txt", 'a')
    log.write(login + '-' + F)
    log.close()

def autoban(): #ban automatico
    z = os.stat("giocatore.txt").st_size
    if z == 0 and os.path.isfile('newusers.txt') is True:
        f = open('ban.txt','a')
        f.write(hostname)
        f.close()
        exit()

def ricarica(): #aggiungi soldi al conto utente
    sa = open('fondi-giocatore.txt','r')
    soldi = sa.readline()
    print(soldi)
    ricarica=int(input("ti quanto vuoi ricaricare "))
    soldi = int(soldi)
    totale = soldi + ricarica
    ricarico = open('fondi-giocatore.txt','w')
    ricarico.write(str(totale))
    sa.close()

def giocata():
    sa = open('fondi-giocatore.txt','r')
    soldi = sa.readline()
    print(soldi)
    giocata = int(input("quanto vuoi giocare "))
    soldi = int(soldi)
    if giocata > soldi:
        print("stai giocando troppo ")
        root = tk.Tk()
        root.withdraw()
        MsgBox = tk.messagebox.askquestion ('elevato','hai giocato un numero troppo elevato',icon = 'error')
        root.destroy()
        exit()
    else:
        rimanenti = soldi - giocata
        ric = open('fondi-giocatore.txt','w')
        ric.write(str(rimanenti))
        sa.close()
        memoria = open("memoria.txt",'w')
        memoria.write(str(giocata))
        memoria.close()

def vincita():
    root = tk.Tk()
    root.withdraw()
    MsgBox = tk.messagebox.askquestion ('Vittoria','hai vinto',icon = 'info')
    root.destroy()
    vincita = open('fondi-giocatore.txt','r')
    soldi = vincita.readline()
    soldi = int(soldi)
    bancav()
    pino = open("memoria.txt.",'r')
    giocata = pino.readline()
    giocata = int(giocata)
    vincitaa = soldi + giocata + 300
    of = open('fondi-giocatore.txt','w')
    of.write(str(vincitaa))
    vincita.close()
    log = open("transizioni.txt",'a')
    log.write(str('\n' + tempo + "si è verificata una perdita della banca di " + vincitaa))
    log.close()

def perdita():
    root = tk.Tk()
    root.withdraw()
    MsgBox = tk.messagebox.askquestion ('Perdita','hai perso',icon = 'info')
    root.destroy()
    vincita = open('fondi-giocatore.txt','r')
    soldi = vincita.readline()
    soldi = int(soldi)
    pino = open("memoria.txt.",'r')
    giocata = pino.readline()
    giocata = int(giocata)
    vincitaa = soldi + 0
    of = open('fondi-giocatore.txt','w')
    of.write(str(vincitaa))
    vincita.close()
    log = open("transizioni.txt",'a')
    log.write('\n' + tempo + "si è verificata una vittoria della banca ")
    log.close()
    
    

def indovinalacarta():#indovina la carta
    giocata()
    print("scegli una carta da 1-13")
    #scelta = input()
    vincente = random.randint(1,13)
    scelta = int(input())
    if scelta == vincente:
        print("hai vinto")
        vincita()
    else:
        perdita()
        print("hai perso")
 def slot():
    giocata()
    print("generando")
    time.sleep(5)
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    e=random.randint(0,9)
    f=random.randint(0,9)

    print("-----------------")
    print("|",x,"|",y,"|",z,"|")
    print("|",a,"|",b,"|",c,"|")
    print("|",d,"|",e,"|",f,"|")
    print("-----------------")
    
    if x==y and y==z and z==a and a==b and b==c and c==d and d==e and e==f:
        print("hai fatto jackpot")
        vincita()
    elif x==y and y==z:
        vincita()
    elif a==b and b==c:
        vincita()
    elif d==e and e==f:
        vincita()
    elif x==b and b==f:
        vincita()
    elif z==b and b==d:
        vincita()
    elif x==a and x==d:
        vincita()
    elif y==b and b==e:
        vincita()
    elif z==c and c==f:
        vincita()
    else:
        perdita()
def blackjack():
    giocata()
    print("benvenuto nel blackjack")
    x=int(input("premi 1 per giocare a modalita facile, 2 per modalita difficile "))
    if x == 1:
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("mescolando")
            time.sleep(2)
            giocatore =  random.randint(0,13)
            print(giocatore)
            continuare = str(input("continuare "))
            while continuare == "si":
                if giocatore > 21:
                    print("hai superato 21 ")
                    break
                giocatore = giocatore +  random.randint(1,13)
                print(giocatore)
                continuare = str(input("continuare "))
            if continuare != "si":
                if banco > giocatore or giocatore > 21:
                    perdita()
                else:
                    vincita()

    else:
        print("modalita difficile attivata ")
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("mescolando")
            time.sleep(2)
            giocatore =  random.randint(1,13)
            print(giocatore)
            continuare = str(input("continuare "))
            while continuare == "si":
                giocatore = giocatore +  random.randint(1,13)
                if giocatore > 21:
                    print("hai superato 21 ")
                    break
                continuare = str(input("continuare "))
            if continuare != "si":
                continuare = False
                if banco > giocatore or giocatore > 21:
                    perdita()
                else:
                    vincita()

def roulette():
    giocata()
    colore = str(input("scelga un colore (Rosso o nero) "))
    numero = int(input("scelga un numero "))
    if colore == "rosso":
        colore = 1
    else:
        colore = 2
    coloreWin =   random.randint(1,2)
    numeroWin =  random.randint(1,90)
    if colore == coloreWin and numero == numeroWin:
        vincita()
    else:
        perdita()
 
def dadi():
    giocata()
    print("benvenuto nel gioco dei dadi")
    x=random.randint(1,10)
    vita=3
    print("il tuo compito è cercare di indovinare quanto uscira nel lancio di " + str(x) + " lanci")
    dado = 0
    while x>0:
        dadop=random.randint(1,6)
        dado = dado + dadop
        x=x-1
    print("-----------------")
    print(dado)
    while vita>0:
        giocatore=int(input("scegli il tuo numero "))
        if giocatore == dado:
            vincita()
            break
        else:
            if giocatore>dado:
                print("troppo alto")
            else:
                print("troppo basso")
        vita=vita-1
        if vita == 0:
            perdita()
def chiudere():
    exit()         


    
def main():
    try:
        if os.path.isfile("newusers.txt") is False:
            newusers()
        else:
            pass
        giocatore()
        ban()
        autoban()
        menu()
        scegli()
    except:
        root = tk.Tk()
        root.withdraw()
        MsgBox = tk.messagebox.askquestion ('Exit Application','è stato rilevato un errore vuoi loggarlo',icon = 'error')
    if MsgBox == 'yes':
        tk.messagebox.showinfo('Exit','puoi trovare il log a nel file errore.txt' )
        root.destroy()
        log = open("errore.txt",'a')
        log.write('\n' + tempo + "si è verificato un errore ")
        log.close()
    else:
        tk.messagebox.showinfo('Exit','Grazie lo stesso')
   
main()

    
