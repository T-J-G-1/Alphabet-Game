# Imports tkinter for GUI and random for selecting random letters
from tkinter import *
import random

# List of all letters
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Function to reset the background color
def reset_background():
    root.config(bg="black")

# Function to handle user input
def right_letter(event):
    user_input = event.char
    if not user_input.isalpha():
        return
# Check if the input is correct
    if difficulty == "easy":
        correct_input = user_input.lower() == letter_label["text"].lower()
    else:
        correct_input = user_input == letter_label["text"]

    if correct_input:
        root.config(bg="green")
        letter_label.config(text=random.choice(alphabet))
    else:
        root.config(bg="red")

    # Clear the input field immediately after processing the input
    input_entry.delete(0, END)

    root.after(500, reset_background)

# Function to start the game
def start_game(selected_difficulty):
    global difficulty
    difficulty = selected_difficulty

    for widget in root.winfo_children():
        widget.destroy()
    
    # Create the GUI elements
    root.configure(background="black")

    title_label = Label(root, text="ALPHABET GAME", font=("Arial", 30), bg="black", fg="white")
    global letter_label
    letter_label = Label(root, text=random.choice(alphabet), font=("Arial", 150, "bold"), bg="black", fg="white")
    
    global input_entry
    input_entry = Entry(root, font=("Arial", 50), justify="center")
    input_entry.pack(pady=20)

    # Places the elements on the screen
    title_label.place(x=30, y=50)
    letter_label.place(x=150, y=100)
    input_entry.place(x=200, y=400, anchor="center")
    input_entry.focus_set()

    input_entry.bind("<KeyRelease>", right_letter)

    close_button = Button(root, text="Close", command=root.destroy)
    close_button.place(x=350, y=10)

# Function to handle the drag of the window
def on_start(event):
    global startX, startY
    startX = event.x
    startY = event.y

def on_drag(event):
    x = event.x_root - startX
    y = event.y_root - startY
    root.geometry(f"+{x}+{y}")

# Main function
# Creates the window
# Creates the GUI elements
def main():
    global root
    root = Tk()
    root.title("Typing Speed Test")
    root.configure(background="black")
    root.minsize(400, 550)
    root.maxsize(400, 550)
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    root.bind("<Escape>", lambda e: root.destroy())

    root.bind("<ButtonPress-1>", on_start)
    root.bind("<B1-Motion>", on_drag)

    title_label = Label(root, text="SELECT DIFFICULTY", font=("Arial", 20), bg="black", fg="white")
    title_label.pack(pady=20)

    easy_button = Button(root, text="Easy", font=("Arial", 20), bg="green", fg="white", width=10,
                         command=lambda: start_game("easy"))
    easy_button.pack(pady=10)

    hard_button = Button(root, text="Hard", font=("Arial", 20), bg="red", fg="white", width=10,
                         command=lambda: start_game("hard"))
    hard_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
