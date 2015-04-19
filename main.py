'''

@author: Jason Carrete
'''
from flask import Flask, request, redirect
import twilio.twiml, threading, pygame, sys
from pygame.locals import *

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

@app.route("/", methods=['GET', 'POST'])
def server():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)
