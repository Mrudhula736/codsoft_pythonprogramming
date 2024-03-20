import random
import tkinter as tk
from tkinter import messagebox

user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}\nYour score: {user_score}\nComputer score: {computer_score}")
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        return
    else:
        root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

btn_rock = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
btn_rock.pack()

btn_paper = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
btn_paper.pack()

btn_scissors = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
btn_scissors.pack()

root.mainloop()
