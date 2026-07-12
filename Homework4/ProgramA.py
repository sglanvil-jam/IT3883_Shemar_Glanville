# Program Name: ProgramA.py
# Course: IT3883/Section W01
# Student Name: Shemar Glanville
# Assignment Number: Assignment 4
# Due Date: 07/12/2026
# Purpose:
# This program asks the user for a message, sends it to Program B,
# waits for the modified message, and displays the response.
# Resources Used: Python socket documentation and class notes.


import socket

HOST = "127.0.0.1"
PORT = 41237

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

user_message = input("Enter a message: ")

client_socket.send(user_message.encode())

reply = client_socket.recv(1024).decode()

print("Message returned from Program B:")
print(reply)

client_socket.close()