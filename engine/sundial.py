#--------------------------------------------------#
#  sundial.py is the engine of the                 #
#  rock/paper/scissors is named after              #
#  the earliest type of timekeeping device         #
#--------------------------------------------------#

import random

def dumb_algo():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
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

