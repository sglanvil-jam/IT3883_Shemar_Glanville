# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Shemar Glanville
# Assignment Number: Assignment 4
# Due Date: 07/12/2026
# Purpose:
# This program waits for a message from another program.
# It converts the received text to uppercase and sends it back.
# Resources Used: Python socket documentation and class notes.

import socket

HOST = "127.0.0.1"
PORT = 41237

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Program B is waiting for a connection...")

connection, address = server_socket.accept()

print("Connected by:", address)

incoming_text = connection.recv(1024).decode()

uppercase_text = incoming_text.upper()

print("Received and converted:")
print(uppercase_text)

connection.send(uppercase_text.encode())

connection.close()
server_socket.close()