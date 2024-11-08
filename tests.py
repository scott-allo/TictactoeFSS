from random import*
import threading
import time

#on construit le tableau
# Create the game board
# Create a 3x3 game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# Display the game board
for row in board:
    # Print a horizontal line
    print('-------------')
  
    # Print the row with vertical separators
    print('|', end=' ')
    for cell in row:
        print(cell, end=' | ')
    print()
# Print the final horizontal line
print('-------------')

#definition des joueurs
print("welcome to tictactoe game")
a=player1=input ("choose your player beetween a to b : ")
b=player2=input ("choose your player beetween a to b : ")
#c=ai_player=input ("choose your player beetween a to b : ")

your_choise=(a or b)
print(a, "player1")
print(b, "player2")
#print(c, "ai_player")


print("Determining which player will go first...")
#from random import randint
# first = print(random.randint(1,2))

current_player = randint(1, 2)
print("player{} will go first.".format(current_player))

first = a or b
if first == int(1) :
   print(player1 + " will go first.")

if first == int(2):
   print(player2 + " will go first.")


