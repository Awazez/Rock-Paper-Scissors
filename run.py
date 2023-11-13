#--------------------------------------------------#
#  main.py is the main file of the                 #
#  rock/paper/scissors                             #
#--------------------------------------------------#


import tkinter as tk
from tkinter import PhotoImage, messagebox
from engine import sundial

def on_image_click(choice):
    result = sundial.play_round(choice)
    update_scores(result)

def update_scores(result):
    if result == "You Win":
        player_score["value"] += 1
    elif result == "Computer Wins":
        computer_score["value"] += 1
    else:
        tie_score["value"] += 1

    update_score_labels()

    # Vérifier si l'un des joueurs a atteint 3 victoires
    if player_score["value"] >= 3 or computer_score["value"] >= 3:
        end_game(result)

def update_score_labels():
    # Mettez tous les scores sur une seule ligne
    scores_text = f"Player: {player_score['value']} | Computer: {computer_score['value']} | Ties: {tie_score['value']}"
    score_label.config(text=scores_text)

def end_game(result):
    play_again = messagebox.askyesno("Game Over", f"{result}\nDo you want to play again?")
    if play_again:
        reset_game()
    else:
        root.quit()

def reset_game():
    player_score["value"] = 0
    computer_score["value"] = 0
    tie_score["value"] = 0
    update_score_labels()

# Initialisation
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Chargement des images
rock_image = PhotoImage(file="assets/rock.png")
paper_image = PhotoImage(file="assets/paper.png")
scissors_image = PhotoImage(file="assets/scissors.png")

# Scores
player_score = {"value": 0}
computer_score = {"value": 0}
tie_score = {"value": 0}

# Labels pour afficher les scores
score_label = tk.Label(root, text=f"Player: {player_score['value']} | Computer: {computer_score['value']} | Ties: {tie_score['value']}")
score_label.pack(pady=10)

# Création des étiquettes cliquables avec les images
rock_label = tk.Label(root, image=rock_image, cursor="hand2")
rock_label.pack(padx=10, pady=10)
rock_label.bind("<Button-1>", lambda event, choice="Rock": on_image_click(choice))

paper_label = tk.Label(root, image=paper_image, cursor="hand2")
paper_label.pack(padx=10, pady=10)
paper_label.bind("<Button-1>", lambda event, choice="Paper": on_image_click(choice))

scissors_label = tk.Label(root, image=scissors_image, cursor="hand2")
scissors_label.pack(padx=10, pady=10)
scissors_label.bind("<Button-1>", lambda event, choice="Scissors": on_image_click(choice))

# I define the size of the width and the height 3 and 4 times the original size. 
width = root.winfo_reqwidth() * 3
height = root.winfo_reqheight() * 4
root.geometry(f"{width}x{height}")

root.mainloop()