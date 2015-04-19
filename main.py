'''

@author: Jason Carrete
'''
import twilio.twiml
import threading, game
from flask import Flask, request, redirect
from threading import Thread
from game import gameFunc
from Queue import Queue

commandsQueue = Queue()
thread = Thread(target = gameFunc, args=(commandsQueue,))
thread.start()

app = Flask(__name__)

commands = "ABRID"

@app.route('/', methods=["GET", "POST"])
def hello_monkey(): #respond to text
    body = request.form["Body"]
    if body in commands:
        commandsQueue.put(body)
    return ""
