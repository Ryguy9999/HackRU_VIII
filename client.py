'''

@author: Jason Carrete
'''
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "45.33.88.126" # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
'''import threading, game, socket
from flask import Flask, request, redirect
from threading import Thread
from game import gameFunc
from Queue import Queue

commandsQueue = Queue()
def netcode(commandsQueue):
    host = "45.33.88.126"
    port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    while True:
        string = client.recv(4096)
        for char in string:
            commandsQueue.put(char)
netThread = Thread(target = netcode, args=(commandsQueue,))
thread = Thread(target = gameFunc, args=(commandsQueue,))
netThread.start()
thread.start()
'''
