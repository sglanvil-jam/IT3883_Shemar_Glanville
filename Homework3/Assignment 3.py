# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Shemar Glanville
# Assignment Number: Assignment 3
# Due Date: 06/26/2026
# Purpose:
# This program converts fuel from mpg
# to (km/L). The conversion updates automatically
# Invalid input is handled without
# crashing the program.
#
# Resources Used:
# Course notes and Python Tkinter documentation.

from tkinter import *


# Conversion constant provided in the instructions
MPG_TO_KML = 0.425143707


def refresh_conversion(*args):
    """
    This is called whenever a user types in the entry field.
    Converts MPG to km/L and updates the results.
    """

    current_text = mpg_input.get().strip()

    # Handle blank entry
    if current_text == "":
        result_text.set("")
        return

    try:
        fuel_rating = float(current_text)
        converted_value = fuel_rating * MPG_TO_KML

        result_text.set(f"{converted_value:.3f} km/L")

    except ValueError:
        # Handle letters and invalid characters
        result_text.set("Please enter a numeric value")


# Main window
window = Tk()
window.title("MPG to km/L Conversion")
window.geometry("340x160")

# Variable connected to entry widget
mpg_input = StringVar()

# Variable connected to output label
result_text = StringVar()

# Watch for changes in the entry box
mpg_input.trace_add("write", refresh_conversion)

# Input label
Label(window,
      text="Miles Per Gallon (MPG):").pack(pady=10)

# Entry field
Entry(window,
      textvariable=mpg_input,
      width=30).pack()

# Result heading
Label(window,
      text="Kilometers Per Liter:").pack(pady=10)

# Output label
Label(window,
      textvariable=result_text,
      font=("Arial", 12, "bold")).pack()

window.mainloop()