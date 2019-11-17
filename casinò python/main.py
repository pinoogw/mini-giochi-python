import random
import requests
import os
import socket
import hashlib
import time
import datetime
import uuid
import platform
import subprocess


tempo = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
patrimonio = 3000000



def menu(): #menu
    print("sono le " + tempo)
    print("1-per chiudere")
    print("2-roulette")
    print("3-blackjack")
    print("4-indovina la carta")
    print("5-fondi")
    print("6-altri comandi")

def scegli(): #scelta menu
    modalita = int(input("scegli la modalità di gioco "))
    while modalita not in [1,2,3,4,5,6]:
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
   


ip = requests.get("https://api.myip.com")
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
    print(z)
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
    else:
        rimanenti = soldi - giocata
        ric = open('fondi-giocatore.txt','w')
        ric.write(str(rimanenti))
        sa.close()
        memoria = open("memoria.txt",'w')
        memoria.write(str(giocata))
        memoria.close()

def vincita():
    print("complimenti hai vinto ")
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

def perdita():
    print("complimenti hai perso ")
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
    
    

def indovinalacarta():#indovina la carta
    giocata()
    print("scegli una carta da 1-13")
    #scelta = input()
    vincente = random.randint(1,2)
    print(vincente)
    scelta = int(input())
    if scelta == vincente:
        print("hai vinto")
        vincita()
    else:
        perdita()
        print("hai perso")

def blackjack():
    print("benvenuto nel blackjack")
    x=int(input("premi 1 per giocare a modalita facile, 2 per modalita difficile"))
    if x == 1:
        #giocata()
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("mescolando")
            time.sleep(4)
            giocatore =  random.randint(1,13)
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
                    continuare = False
                    if banco > giocatore or giocatore > 21:
                        #perdita()
                        print("perso")
                    else:
                        #vincita()
                        print("vinto")
    else:
        print("modalita difficile attivata ")
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("mescolando")
            time.sleep(4)
            giocatore =  random.randint(1,13)
            print(giocatore)
            continuare = str(input("continuare "))
            while continuare == "si":
                if giocatore > 21:
                    print("hai superato 21 ")
                    break
                giocatore = giocatore +  random.randint(1,13)
                continuare = str(input("continuare "))
                if continuare != "si":
                    continuare = False
                    if banco > giocatore or giocatore > 21:
                        #perdita()
                        print("perso")
                    else:
                        #vincita()
                        print("vinto")

def roulette():
    colore = str(input("scelga un colore (Rosso o nero)"))
    numero = int(input("scelga un numero"))
    if colore == "rosso":
        colore = 1
    else:
        colore = 2
    coloreWin =   random.randint(1,2)
    numeroWin =  random.randint(1,90)
    if colore == coloreWin and numero == numeroWin:
        #vincita()
        print("hai vinto")
    else:
        #perdita()
        print("perso")
        
def chiudere():
    exit()         


    
def main():
    if os.path.isfile("newusers.txt") is False:
        newusers()
    else:
        pass
    giocatore()
    ban()
    autoban()
    menu()
    scegli()
   
main()

    
