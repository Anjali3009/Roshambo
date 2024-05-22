from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Roshambo")

# Resizing images
def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

# Define image paths
image_rock1 = resize_image("rock1.jpg", 150, 150)
image_paper1 = resize_image("paper1.jpg", 150, 150)
image_scissor1 = resize_image("scissor1.jpg", 150, 150)
image_rock2 = resize_image("rock2.jpg", 150, 150)
image_paper2 = resize_image("paper2.jpg", 150, 150)
image_scissor2 = resize_image("scissor2.jpg", 150, 150)

# Labels to display player and computer choices
label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=2, column=0)
label_player.grid(row=2, column=4)

# Labels to display scores
computer_score = Label(window, text=0, font=('arial', 30, "bold"), fg="blue")
player_score = Label(window, text=0, font=('arial', 30, "bold"), fg="blue")
computer_score.grid(row=2, column=1)
player_score.grid(row=2, column=3)

# Labels for indicators
player_indicator = Label(window, font=("arial", 20, "bold"), text="PLAYER", bg="orange", fg="brown")
computer_indicator = Label(window, font=("arial", 20, "bold"), text="COMPUTER", bg="orange", fg="brown")
computer_indicator.grid(row=1, column=1)
player_indicator.grid(row=1, column=3)

# Label to display result
final_message = Label(window, font=("arial", 20, "bold"), bg="red", fg="white")
final_message.grid(row=5, column=2)

# Counter for rounds
rounds_played = 1

# Function to update the game
def choice_update(a):
    global rounds_played
    

    if rounds_played >= 5:
        final_message.config(text="Game Over!")
        button_rock.config(state=DISABLED)
        button_paper.config(state=DISABLED)
        button_scissor.config(state=DISABLED)
        play_again_button.grid(row=5, column=1)
        exit_button.grid(row=5, column=3)
        return
    else:
        rounds_played += 1

    choice_computer = to_select[randint(0, 2)]
    update_images(a, choice_computer)
    winner_check(a, choice_computer)
    update_round_labels()

# Function to update player and computer choices
def update_images(player_choice, computer_choice):
    if computer_choice == "rock":
        label_computer.configure(image=image_rock1)
    elif computer_choice == "paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)

    if player_choice == "rock":
        label_player.configure(image=image_rock2)
    elif player_choice == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor2)

# Function to update scores and display winner
def winner_check(player_choice, computer_choice):
    if player_choice == computer_choice:
        update_message("It's a tie")
    elif player_choice == "rock":
        if computer_choice == "paper":
            update_message("Computer Wins !!!")
            Computer_Update()
        else:
            update_message("Player Wins !!!")
            Player_Update()
    elif player_choice == "paper":
        if computer_choice == "scissor":
            update_message("Computer Wins !!!")
            Computer_Update()
        else:
            update_message("Player Wins !!!")
            Player_Update()
    elif player_choice == "scissor":
        if computer_choice == "rock":
            update_message("Computer Wins !!!")
            Computer_Update()
        else:
            update_message("Player Wins !!!")
            Player_Update()

# Function to update computer score
def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

# Function to update player score
def Player_Update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

# Function to display the result
def update_message(message):
    final_message.config(text=message)

# List of choices
to_select = ["rock", "paper", "scissor"]

# Function to reset the game
def play_again():
    global rounds_played
    rounds_played = 0
    final_message.config(text="")
    computer_score.config(text="0")
    player_score.config(text="0")
    button_rock.config(state=NORMAL)
    button_paper.config(state=NORMAL)
    button_scissor.config(state=NORMAL)
    play_again_button.grid_forget()
    exit_button.grid_forget()

def update_round_labels():
    round_label.config(text=f"Round {rounds_played}/5")

def start_game():
    global player_name
    player_name = name_entry.get()
    if player_name:
        name_entry.config(state=DISABLED)
        start_button.config(state=DISABLED)
        button_rock.grid(row=3, column=1)
        button_paper.grid(row=3, column=2)
        button_scissor.grid(row=3, column=3)
        round_label.grid(row=4, column=2)
        update_round_labels()
    else:
        name_error.config(text="Please enter your name.")

# Labels and Entry for user name input
name_label = Label(window, text="Enter your name:", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = Entry(window, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

name_error = Label(window, text="", font=("Arial", 10), fg="red")
name_error.grid(row=0, column=2, padx=5, pady=5)

start_button = Button(window, text="Start Game", command=start_game)
start_button.grid(row=0, column=3, padx=5, pady=5)

# Play again button
play_again_button = Button(window, width=16, height=3, text="Play Again", bg="yellow", command=play_again)

# Exit button
exit_button = Button(window, width=16, height=3, text="Exit", bg="yellow", command=window.quit)

# Buttons for player choices
button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 14, "bold"), bg="yellow", fg="green", command=lambda: choice_update("rock"))
button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 14, "bold"), bg="yellow", fg="green", command=lambda: choice_update("paper"))
button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 14, "bold"), bg="yellow", fg="green", command=lambda: choice_update("scissor"))

# Buttons grid layout
button_rock.grid(row=4, column=1)
button_paper.grid(row=4, column=2)
button_scissor.grid(row=4, column=3)

round_label = Label(window, text=f"Round {rounds_played}/5", font=("arial", 12, "bold"))
round_label.grid(row=6, column=2)

# Set window size
window.geometry("925x400")

# Run the Tkinter event loop
window.mainloop()
