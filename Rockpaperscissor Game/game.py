# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# print("Welcome to Rock, Paper, Scissors!")
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])
# computer_choice = random.randint(0, 2)
# print("Computer chose ")
# print(game_images[computer_choice]) 

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2    :
#     print("You win")

# elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
# elif computer_choice > user_choice:
#     print("You lose")
# elif user_choice > computer_choice:
#     print("You win")
# elif computer_choice == user_choice:
#     print("It's a draw")
import tkinter as tk
import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

# Game logic
def play(choice):
    user_choice = choice
    computer_choice = random.randint(0, 2)

    result_text = ""
    if user_choice == computer_choice:
        result_text = "It's a Draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result_text = "You Win!"
    else:
        result_text = "You Lose!"

    # Update UI
    user_label.config(text=f"You chose {choices[user_choice]}:\n{game_images[user_choice]}")
    computer_label.config(text=f"Computer chose {choices[computer_choice]}:\n{game_images[computer_choice]}")
    result_label.config(text=result_text)

# Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x600")
root.config(bg="black")

title = tk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 20, "bold"), fg="white", bg="black")
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play(0))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play(1))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play(2))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Labels for output
user_label = tk.Label(root, text="Your Choice:", font=("Courier", 12), fg="lightgreen", bg="black", justify="left")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer Choice:", font=("Courier", 12), fg="lightblue", bg="black", justify="left")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="Result will appear here", font=("Arial", 16, "bold"), fg="yellow", bg="black")
result_label.pack(pady=20)

root.mainloop()
