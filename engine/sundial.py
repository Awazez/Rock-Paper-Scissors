#--------------------------------------------------#
#  sundial.py is the engine of the                 #
#  rock/paper/scissors is named after              #
#  the earliest type of timekeeping device         #
#--------------------------------------------------#

import random


#This algorithm for computer playing is a bit dumb. Machine learning is on the way ! 
def dumb_algo():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

#To improve the algorithm we can use win combination 
#player_win_combination = {0: 2, 1: 0, 2: 1}

def determine_winner(player_choice, computer_choice):
# We check the tie first to get rid of 3 cases : 
# Rock against Rock, Paper against Paper, Scissors against Scissors

    if player_choice == computer_choice:
        return "Tie"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win"
    else:
        return "Computer Wins"

def play_round(player_choice):
    computer_choice = dumb_algo()
    result = determine_winner(player_choice, computer_choice)
    return result

