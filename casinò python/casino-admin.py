import random
#import requests
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


#ip = requests.get("https://api.myip.com")
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
F = socket.gethostname()
tempo = str(datetime.datetime.now().strftime("%H:%M:%S: %Y-%m-%d"))

def logadmin(): #logadmin
    nome = str(input("inserire nome utente "))
    with open('admin.txt') as f:
        for line in f:
            line = line.strip()
            print(f'{hashlib.sha256(nome.encode()).hexdigest()} --> {nome}')
            if hashlib.sha256(nome.encode()).hexdigest() == line:
                print('nome utente corretto')
                password = str(input("password "))
                with open('admin.txt') as f:
                    for line in f:
                        line = line.strip()
                        print(f'{hashlib.sha256(password.encode()).hexdigest()} --> {password}')
                        if hashlib.sha256(password.encode()).hexdigest() == line:
                            print("accesso autorizzato")
                            admin()
                        else:
                            print("nome utente non corretto ")
                        with open('accesso.txt') as file:
                            testate = open('accesso.txt', 'a')
                            testate.write("attenzione rilevato con password errato alle " + tempo + '\n' + "Dati " + '\n'  + hostname + IPAddr + platform.platform())
                            testate.close()
            else:
                print("nome utente non corretto ")
                tempo = str(datetime.datetime.now())
            with open('accesso.txt') as file:
                testate = open('accesso.txt', 'a')
                testate.write('\n' + "attenzione rilevato con nome errato alle " + tempo + '\n' + "Dati "  + '\n' + 'Nome pc ' + hostname + '\n' + 'IP del pc ' + IPAddr + '\n' + 'OS ' + platform.platform())
                testate.close()
                exit()
                
def bannare(): #banna solo admin
    with open('ban.txt') as file:
        contents = file.read()
        banned = open('ban.txt', 'a')
        utente = input("inserire utente ")
        banned.write('\n' + utente)
        banned.close()
def lista():
    with open('ban.txt') as file:
        f = open('ban.txt','r')
        giocatori = file.read()
        print('lista: ')
        print(giocatori)
        file.close()
def unban(): 
    x=str(input("utente da sbannare "))
    with open("ban.txt", "r") as f:
        lines = f.readlines()
    with open("ban.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != x:
                f.write(line)
def ammonizioni():
    f=open("ammonizioni.txt","r")
    a=f.readline()
    a=int(a)
    f.close()
    f=open("ammonizioni.txt","w")
    ab=a+1
    f.write(str(ab))
    f.close()
def admin():
    lista()
    scelta = int(input("1-ban,2-sban 3.ammonizioni"))
    if scelta == 1:
        bannare()
    elif scelta == 2:
        unban()
    elif scelta == 3:
        ammonizioni()

def main():
    try:
        logadmin()
    except UnboundLocalError:
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
