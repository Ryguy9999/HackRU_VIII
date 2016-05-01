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

commandsU = "WASDBF"
commandsL = "wasdbf"

@app.route('/', methods=["GET", "POST"])
def hello_monkey(): #respond to text
    resp = twilio.twiml.Response()
    body = request.form["Body"]
    print body
    if body in commandsU or body in commandsL:
        commandsQueue.put(body)
        return ""
    else:
        resp.message("Invalid Command")
        return str(resp)

app.run()
