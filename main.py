'''

@author: Jason Carrete
'''
from flask import Flask, request, redirect
import twilio.twiml, threading, game
thread = Thread(target = gameFunc)
thread.start()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def server():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)
