'''

@author: Jason Carrete
'''
from flask import Flask, request, redirect
import twilio.twiml
import threading, game
thread = Thread(target = gameFunc)
thread.start()

app = Flask(__name__)

commands = "ABRID"

@app.route('/', methods=["GET", "POST"])
def hello_monkey(): #respond to text
    body = request.form["Body"]
    if body in commands:
        game.giveCommand(body)
    return ""

if __name__ == "__main__":
    app.run(debug=True)
