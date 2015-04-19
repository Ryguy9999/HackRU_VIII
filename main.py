'''

@author: Jason Carrete
'''

import twilio.twiml, threading, pygame, sys
from flask import Flask, request, redirect
from pygame.locals import *
from twilio.rest import TwilioRestClient
from flask import request

def game():
    pygame.init()
    display = pygame.display.set_mode((640, 480), 0, 32)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
gameThread = threading.Thread(target = game)
gameThread.start()

app = Flask(__name__)

account_sid = "PNdfd2b6f558dc8ff0e72877df59a1a63b"
auth_token = "fe17ee3c605d7e44cb2462556f986b99"

@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): #respond to text
    resp = twilio.twiml.Response()

    body = request.form['Body']

    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
