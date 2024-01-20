from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import datetime
import time

OUTPUT_PATH = Path(_file_).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image_1.png")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def countdown_label(): 
    end_date = datetime.datetime(2025, 1, 25, 0, 0, 0)

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

    # Schedule the function to run after 1000 milliseconds (1 second)
    canvas.after(1000, update_label)


window = Tk()
window.geometry("1920x1080")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    540.0,
    image=image_image_1
)


day_text = canvas.create_text(
    413.0,
    362.0,
    anchor="nw",
    text="",
    fill="#D9291C",
    font=("MontserratRoman Medium", 140 * -1)
)

hour_text = canvas.create_text(
    401.0,
    469.0,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=("Outfit Bold", 256 * -1)
)

minute_text = canvas.create_text(
    816.0,
    469.0,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=("Outfit Bold", 256 * -1)
)

second_text = canvas.create_text(
    1244.0,
    469.0,
    anchor="nw",
    text="",
    fill="#FFB81D",
    font=("Outfit Bold", 256 * -1)
)

# Set up the initial countdown values
update_label()

window.attributes('-fullscreen', True)
window.mainloop()
