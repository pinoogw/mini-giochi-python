import random
import time
print("benvenuto nel blackjack")
giocatore=0
giocatore=int(giocatore)

banco = random.randint(10,21)
if banco != 21:
    banco = banco + 1
    print("mescolando")
    time.sleep(2)
    giocata =  random.randint(0,13)
    print("il numuero pescato è ",giocata)
    print("il totale è " ,giocatore)
    if giocata == 0:
        penalita = random.randint(0,7)
        giocatore=giocatore-penalita
    giocatore = giocatore +  giocata
    continuare = str(input("continuare "))
    while continuare == "si":
        if giocatore > 21:
            print("hai superato 21 ")
            break
        continuare = str(input("continuare "))
    if continuare != "si":
        if banco > giocatore or giocatore > 21:
            print("hai perso")
        else:
            print("hai vinto")
