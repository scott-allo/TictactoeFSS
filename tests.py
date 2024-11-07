import sys
import random
import math

#definition des joueurs
print("welcome to tictactoe game")
a=player1=input ("choose your player beetween a to c :")
b=player2=input ("choose your player beetween a to c :")
c=ai_player=input ("choose your player beetween a to c :")
list = [a, b, c]

your_choise=(a or b or c)
print(a, "player1")
print(b, "player2")
print(c, "ai_player")


print("Determining which player will go first...")
#from random import randint
# first = print(random.randint(1,2))
from random import*
from tkinter import*
import threading
import time
current_player = randint(1, 2)
print("player{} will go first.".format(current_player))

first = a or b
if first == int(1) :
   print(player1 + " will go first.")

if first == int(2):
   print(player2 + " will go first.")

"""nouveaujeu = "nouvelle partie"
coup = nouveaujeu
coup = ('.', '.', '.', '.', '.', '.', '.', '.', '.')
print(coup)"""

# permet d’afficher un jeu
def affiche ():
   return jeu [0]
print (jeu [0] , jeu [1] , jeu [2])
print (jeu [3] , jeu [4] , jeu [5])
print (jeu [6] , jeu [7] , jeu [8])

print ("affiche jeu (vide)")