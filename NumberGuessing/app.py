import tkinter as tk
import random
from tkinter import messagebox

# --- main window setup ---
root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("400x400")
root.config(bg="#000000")  # black background

# --- global variables ---
attempts = 0
number = 0

# --- functions ---
def start_game(difficulty):
    global attempts, number
    number = random.randint(1, 100)
    attempts = 10 if difficulty == "easy" else 5
    info_label.config(text=f"Guess a number between 1 and 100!")
    tries_label.config(text=f"Attempts left: {attempts}")
    
    # Hide difficulty buttons
    easy_btn.pack_forget()
    hard_btn.pack_forget()
    
    # Show guess input and submit button
    guess_entry.pack(pady=10)
    guess_btn.pack(pady=5)
    result_label.config(text="")

def check_guess(event=None):  # event=None allows Enter key usage
    global attempts
    try:
        guess = int(guess_entry.get())
    except:
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")
        return
    
    if guess < 1 or guess > 100:
        messagebox.showwarning("Out of Range", "Enter a number between 1 and 100.")
        return
    
    if guess > number:
        result_label.config(text="📈 Too high!", fg="#ff6b6b")
    elif guess < number:
        result_label.config(text="📉 Too low!", fg="#48cae4")
    else:
        messagebox.showinfo("🎉 You Win!", f"You got it! The number was {number}.")
        reset_game()
        return
    
    attempts -= 1
    if attempts == 0:
        messagebox.showinfo("😢 Game Over", f"You ran out of attempts! The number was {number}.")
        reset_game()
    else:
        tries_label.config(text=f"Attempts left: {attempts}")
    
    guess_entry.delete(0, tk.END)

def reset_game():
    guess_entry.pack_forget()
    guess_btn.pack_forget()
    result_label.config(text="")
    tries_label.config(text="")
    info_label.config(text="Choose a difficulty to start:")
    easy_btn.pack(pady=5)
    hard_btn.pack(pady=5)

# --- UI Elements ---
title_label = tk.Label(root, text="🎯 Welcome to the Number Guessing Game!", 
                       font=("Arial", 13, "bold"), bg="#000000", fg="#ffffff")
title_label.pack(pady=15)

info_label = tk.Label(root, text="Choose a difficulty to start:", 
                      font=("Arial", 11), bg="#000000", fg="#f1faee")
info_label.pack()

# Difficulty buttons
easy_btn = tk.Button(root, text="😊 Easy (10 tries)", command=lambda: start_game("easy"), 
                     width=18, bg="#06d6a0", fg="black", font=("Arial", 10, "bold"))
easy_btn.pack(pady=5)

hard_btn = tk.Button(root, text="🔥 Hard (5 tries)", command=lambda: start_game("hard"), 
                     width=18, bg="#ffb703", fg="black", font=("Arial", 10, "bold"))
hard_btn.pack(pady=5)

# Game widgets (hidden initially)
guess_entry = tk.Entry(root, width=10, font=("Arial", 12), justify="center", bg="#1a1a1a", fg="#ffffff", insertbackground="white")
guess_entry.bind("<Return>", check_guess)  # allows Enter key submission

guess_btn = tk.Button(root, text="Submit Guess", command=check_guess, 
                      width=15, bg="#118ab2", fg="white", font=("Arial", 10, "bold"))

tries_label = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#000000", fg="#fcbf49")
tries_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#000000")
result_label.pack(pady=10)

# Run the game
root.mainloop()
