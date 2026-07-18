# Course: IT3883/Section W01
# Student Name: Shemar Glanville
# Assignment Number: Assignment 5
# Due Date: 07/17/2026
# Purpose:
# This program creates a SQLite database, stores temperature
# readings from an input file into a database table, and then
# calculates the average temperature for Sunday and Thursday.

import sqlite3


def main():
    # Connect to (or create) the database
    connection = sqlite3.connect("TemperatureDatabase.db")
    cursor = connection.cursor()

    # Remove the table if it already exists so the program
    # can be run multiple times without duplicate records.
    cursor.execute("DROP TABLE IF EXISTS Temperatures")

    # Create the temperature table
    cursor.execute("""
        CREATE TABLE Temperatures (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT,
            Temperature_Value REAL
        )
    """)

    # Open the input file and insert each record into the table
    with open("Assignment5input.txt", "r") as infile:
        for line in infile:
            line = line.strip()

            if line == "":
                continue

            parts = line.split()

            day = parts[0]
            temperature = float(parts[1])

            cursor.execute("""
                INSERT INTO Temperatures
                (Day_Of_Week, Temperature_Value)
                VALUES (?, ?)
            """, (day, temperature))

    # Save the inserted records
    connection.commit()

    # Calculate the average for Sunday
    cursor.execute("""
        SELECT AVG(Temperature_Value)
        FROM Temperatures
        WHERE Day_Of_Week = 'Sunday'
    """)

    sunday_average = cursor.fetchone()[0]

    # Calculate the average for Thursday
    cursor.execute("""
        SELECT AVG(Temperature_Value)
        FROM Temperatures
        WHERE Day_Of_Week = 'Thursday'
    """)

    thursday_average = cursor.fetchone()[0]

    # Display the results
    print("Average Temperatures")
    print("--------------------")
    print(f"Sunday:   {sunday_average:.2f}")
    print(f"Thursday: {thursday_average:.2f}")

    # Close the database connection
    connection.close()


# Start the program
main()