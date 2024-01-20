from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import datetime
import time
import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def countdown_label(): 
    end_date = datetime.datetime(2025, 1, 20, 19, 48, 0)

    # Calculate the time difference
    time_difference = end_date - datetime.datetime.now()

    # Convert the time difference to seconds and round to the nearest integer
    my_time = round(time_difference.total_seconds())

    # Calculate days, hours, minutes, and seconds
    seconds = my_time % 60
    minutes = int(my_time / 60) % 60
    hours = int(my_time / 3600) % 24
    days = int(my_time / 86400)

    return days, hours, minutes, seconds

def update_label():
    days, hours, minutes, seconds = countdown_label()

    # Format the values to ensure they have two digits
    formatted_hours = str(hours).zfill(2)
    formatted_minutes = str(minutes).zfill(2)
    formatted_seconds = str(seconds).zfill(2)

    # Update the canvas text for days, hours, minutes, and seconds
    canvas.itemconfig(day_text, text=f"{days}")
    canvas.itemconfig(hour_text, text=f"{formatted_hours}")
    canvas.itemconfig(minute_text, text=f"{formatted_minutes}")
    canvas.itemconfig(second_text, text=f"{formatted_seconds}")

    # Check if the countdown has reached 0
    if days == hours == minutes == seconds == 0:
        # Add animation when the countdown hits 0
        animate_confetti()

    # Schedule the function to run after 1000 milliseconds (1 second)
    canvas.after(1000, update_label)

def animate_confetti():
    confetti_colors = ["#FFD700", "#FF4500", "#008000", "#1E90FF", "#FF1493"]  # Different confetti colors
    confetti_size = 5  # Diameter of the confetti pieces
    confetti_speed = 2  # Speed of confetti falling

    for _ in range(100):  # Create 100 confetti pieces
        x = random.uniform(0, canvas_width)  # Random x-coordinate within the canvas width
        y = 0  # Start the confetti at the top of the canvas

        color = random.choice(confetti_colors)  # Random confetti color

        # Create oval (confetti piece) at the specified position and with the specified color
        confetti_piece = canvas.create_oval(x, y, x + confetti_size, y + confetti_size, fill=color, outline=color)

        # Animate the confetti falling
        animate_confetti_piece(confetti_piece)

def animate_confetti_piece(confetti_piece):
    # Move the confetti piece down the canvas
    canvas.move(confetti_piece, 0, 5)

    # Schedule the function to run after 30 milliseconds for a smooth animation
    canvas.after(30, lambda: animate_confetti_piece(confetti_piece))

window = Tk()

# Get the original resolution (1920x1080)
original_width = 1920
original_height = 1080

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the scaling factors
width_scale = screen_width / original_width
height_scale = screen_height / original_height

# Choose the smaller scaling factor for font size calculations
font_scale = min(width_scale, height_scale)

# Apply the scaling factors to adjust the canvas size and text positions
canvas_width = int(original_width * width_scale)
canvas_height = int(original_height * height_scale)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=canvas_height,
    width=canvas_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_2_path = relative_to_assets("image_2.png")
image_2 = PhotoImage(file=image_2_path)
image_2_obj = canvas.create_image(canvas_width / 2, canvas_height / 2, image=image_2)

day_text = canvas.create_text(
    canvas_width * 0.22,
    canvas_height * 0.37,
    anchor="nw",
    text="",
    fill="#D9291C",
    font=('Outfit Bold', int(canvas_height * 0.12 * font_scale) * -1)
)

hour_text = canvas.create_text(
    canvas_width * 0.22,
    canvas_height * 0.48,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=('Outfit Bold', int(canvas_height * 0.22 * font_scale) * -1)
)

minute_text = canvas.create_text(
    canvas_width * 0.43,
    canvas_height * 0.48,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=("Outfit Bold", int(canvas_height * 0.22 * font_scale) * -1)
)

second_text = canvas.create_text(
    canvas_width * 0.645,
    canvas_height * 0.48,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=("Outfit Bold", int(canvas_height * 0.22 * font_scale) * -1)
)

# Set up the initial countdown values
update_label()

# Bind the escape key to the on_escape function
window.bind('<Escape>', lambda e: window.destroy())

window.attributes('-fullscreen', True)
window.mainloop()
