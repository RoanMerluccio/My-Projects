import tkinter as tk
import random
from PIL import Image, ImageTk

dice_images = [
    "dice1.png",
    "dice2.png",
    "dice3.png",
    "dice4.png",
    "dice5.png",
    "dice6.png",
    "dice20.jpg"
]

def roll_dice():
    num_dice = int(num_dice_entry.get())  # Get the number of dice from the entry
    results = []
    
    for _ in range(num_dice):
        result = random.randint(1, 6)  # Set the result to a random integer between 1 and 6
        results.append(result)
    
    # Display the results as text
    result_text.set("You rolled: " + ", ".join(map(str, results)))

    # Display the results as images (optional)
    image_paths = [dice_images[result - 1] for result in results]
    images = [Image.open(image_path).resize((20, 20)) for image_path in image_paths]
    photos = [ImageTk.PhotoImage(image) for image in images]
    
    for i, photo in enumerate(photos):
        dice_labels[i].config(image=photo)
        dice_labels[i].image = photo

    # Disable the "Roll 20-sided Dice" button and enable the "Roll Dice" button
    roll_20_button.config(state="normal")
    roll_button.config(state="disabled")
    roll_button.focus()

def roll_20_dice():
    result = random.randint(1, 20)  # Set the result to a random integer between 1 and 20
    result_text.set("You rolled: " + str(result))
    image_path = dice_images[-1]  # Use the last image in the list for the 20-sided dice
    image = Image.open(image_path).resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    dice_labels[0].config(image=photo)
    dice_labels[0].image = photo

    # Hide the 6-sided dice images
    for i in range(1, 6):
        dice_labels[i].config(image=None)
        dice_labels[i].image = None

    # Disable the "Roll Dice" button and enable the "Roll 20-sided Dice" button
    roll_button.config(state="normal")
    roll_20_button.config(state="disabled")
    roll_20_button.focus()

app = tk.Tk()
app.title("Dice Roller")

num_dice_label = tk.Label(app, text="Enter number of dice:")
num_dice_label.pack()

num_dice_entry = tk.Entry(app)
num_dice_entry.pack()

roll_button = tk.Button(app, text="Roll Dice", command=roll_dice)
roll_button.pack()

roll_20_button = tk.Button(app, text="Roll 20-sided Dice", command=roll_20_dice)
roll_20_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text)
result_label.place(x=20,y=20)

# Create labels for displaying dice images
dice_labels = [tk.Label(app) for _ in range(6)]
for label in dice_labels:
    label.pack()

app.mainloop()