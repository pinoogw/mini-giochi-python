from tkinter import messagebox
import tkinter
import os
import time
import tkinter as tk
import requests
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import git 
import sys


def accetta():
    y=os.getcwd()
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("leggi","leggi la nostra eula la trovi in " + y)
    root.destroy()
    x=os.getlogin()
    f = open("eula.txt","w+")
    f.write("caro " + x + " questo programma è un semplice simulatore di casino, il gioco avrà accesso solo al tuo ip per ragioni di sicurezza  è vietato la rivendita di questo programma")
    f.close()
    time.sleep(7)
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.askyesno("condizioni","accetto le condizioni")
    root.destroy()
    if x is True:
        root = tkinter.Tk()
        root.withdraw()
        x=messagebox.showinfo("benvenuto","complimenti l'utente ha accettato le condizioni")
        root.destroy()
    else:
        root = tkinter.Tk()
        root.withdraw()
        x=messagebox.showinfo("benvenuto","conzioni negate procediamo a rimuovere il programma di installazione")
        root.destroy()
        os.remove("eula.txt")
        os.remove("ps.py")


    
class log(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title("log-in")
        self.master.geometry("300x200")
        self.grid()
        self.crea_widgets()
        
    def crea_widgets(self):
        self.lblUsername = tk.Label(self, text = "username")
        self.lblUsername.grid(row = 0, column = 0, sticky = tk.W)

        self.vUsername = tk.StringVar()
        self.txtUsername = tk.Entry(self, textvariable = self.vUsername)
        self.txtUsername.grid(row = 0 , column = 1) 

        self.lblPasswords = tk.Label(self, text = "password")
        self.lblPasswords.grid(row = 1, column = 0, sticky = tk.W)

        self.vPasswords = tk.StringVar()
        self.txtPasswords = tk.Entry(self, textvariable = self.vPasswords)
        self.txtPasswords.grid(row = 1 , column = 1) 
        self.btnInvio = tk.Button(self, text = "enter", command = self.invia)
        self.btnInvio.grid(row = 2, column = 0, columnspan = 2)

    def invia(self):
        c = self.vUsername.get()
        n = self.vPasswords.get()
        if c == "" or n == "":
            messagebox.showwarning("warning","please insert data")
        else:
            f = open("f.txt","w+")
            f.write(c + "\n" + n)
            f.close()
            messagebox.showinfo("ok","congratulation you succefuly log-in")
           


def sig():
    if os.path.exists("f.txt") is False:
        accetta()
        f=log()
        f.mainloop()
    else:
        x=open("f.txt","r")
        f=x.readline()
        x.close()
        messagebox.showwarning("a","welchome dear " + f ) 
        passw=str(input("please insert your own password "))
        x=open("f.txt","r")
        f=x.readlines()
        x.close()
        if passw in f:
            messagebox.showinfo("succes", "login ")
            print("if you want delete your account press 1 for follow the procedure else press any botton")
            f=str(input())
            if f == "1":
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showwarning("conferm","read this if you delete this account it's imposible for reacp")
                root.destroy()
                root = tkinter.Tk()
                root.withdraw()
                x=messagebox.askyesno("sure","are you completly sure you want delete this account")
                root.destroy()
                if x is True:
                    s=100
                    i=0
                    while s>0:
                        sys.stdout.write("\rDoing thing %i" % i+"%")
                        sys.stdout.flush()
                        s=s-1
                        i=1+i
                        time.sleep(0.1)
                    os.remove("eula.txt")
                    os.remove("f.txt")
            else:
                root = tkinter.Tk()
                root.withdraw()
                x=messagebox.askyesno("sure","are you completly sure to download this file")
                root.destroy()
                if x is True:
                    s=100
                    i=0
                    while s>0:
                        sys.stdout.write("\rcompleate %i" % i+"%")
                        sys.stdout.flush()
                        s=s-1
                        i=1+i
                        time.sleep(0.1)
                    git.Git("C:\\Users\\nicho\Desktop\\installazione\\p").clone("https://github.com/Abissues/mini-giochi-python.git")

                
        else:
            messagebox.showerror("fail","password dont match")








def main():
    sig()
    

    
main()



