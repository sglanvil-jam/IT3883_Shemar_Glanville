# Program Name: Assignment1.py
# Course: IT3883/Section 52337
# Student Name: Shemar Glanville
# Assignment Number: Assignment 1
# Due Date: 06/12/2026
# Purpose:
# This program implements a text-based menu that presents the user
# with four options. The options include adding text in a buffer, clear the buffer, display the input
# buffer, or exit the program.
#
# Resources Used:
# - Course notes and content
# - Assignment instructions

# Variable used to hold text user enters
saved_text = ""

# Controls the loop so the menu displays continuously
program_running = True

while program_running:
    # Display the menu options
    print("\n----- Text Buffer Menu -----")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get the user's menu selection
    user_choice = input("Enter your choice (1-4): ")

    # Option 1: Add text to the existing buffer
    if user_choice == "1":
        new_entry = input("Enter text to add: ")

        # Add a space between entries if the buffer already has text
        if saved_text != "":
            saved_text += " "

        saved_text += new_entry
        print("Text added to the buffer.")

    # Option 2: Clear everything from the buffer
    elif user_choice == "2":
        saved_text = ""
        print("The input buffer has been cleared.")

    # Option 3: Show the current contents of the buffer
    elif user_choice == "3":
        if saved_text == "":
            print("The input buffer is currently empty.")
        else:
            print("Current buffer contents:")
            print(saved_text)

    # Option 4: Exit the program
    elif user_choice == "4":
        print("Exiting program. Goodbye for now! :)")
        program_running = False

    # Handle invalid menu selections
    else:
        print("Invalid entry. Please select a number from 1 to 4.")
