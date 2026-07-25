import random
import tkinter as tk
from tkinter import messagebox

# Choices for the game
CHOICES = ["Rock", "Paper", "Scissors"]


def play_game(user_choice):
    """Function to determine the winner and update the GUI."""
    computer_choice = random.choice(CHOICES)

    # Conditional statements to determine the winner
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 💻"

    # Update labels with choices and result
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")


def reset_game():
    """Function to reset the game display."""
    user_choice_label.config(text="Your Choice: -")
    computer_choice_label.config(text="Computer Choice: -")
    result_label.config(text="Result: -")


# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#f0f4f8")

# Title Label
title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Helvetica", 18, "bold"),
    bg="#f0f4f8",
    fg="#333333",
)
title_label.pack(pady=15)

# Frame for Choice Buttons
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

# Creating buttons using a loop
for choice in CHOICES:
    btn = tk.Button(
        button_frame,
        text=choice,
        font=("Helvetica", 12, "bold"),
        width=10,
        height=2,
        bg="#4a90e2",
        fg="white",
        activebackground="#357abd",
        activeforeground="white",
        command=lambda c=choice: play_game(c),
    )
    btn.pack(side=tk.LEFT, padx=5)

# Status Labels
user_choice_label = tk.Label(
    root,
    text="Your Choice: -",
    font=("Helvetica", 12),
    bg="#f0f4f8",
    fg="#555555",
)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(
    root,
    text="Computer Choice: -",
    font=("Helvetica", 12),
    bg="White" ,
    fg="Black",
)
computer_choice_label.pack(pady=5)

result_label = tk.Label(
    root, text="Result: -", font=("Helvetica", 14, "bold"), bg="#f0f4f8", fg="#222222"
)
result_label.pack(pady=15)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Reset",
    font=("Helvetica", 10, "bold"),
    bg="Red",
    fg="white",
    command=reset_game,
)
reset_btn.pack(pady=5)

# Start Tkinter Event Loop
root.mainloop()