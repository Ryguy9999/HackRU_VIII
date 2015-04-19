'''

@author: Jason Carrete
'''
from flask import Flask, request, redirect
import twilio.twiml
#import threading, game
#thread = Thread(target = gameFunc)
#thread.start()

app = Flask(__name__)

account_sid = "PNdfd2b6f558dc8ff0e72877df59a1a63b"
auth_token = "fe17ee3c605d7e44cb2462556f986b99"

@app.route('/', methods=["GET", "POST"])
def hello_monkey(): #respond to text
    body = request.form["Body"]
    print("{}".format(body))
    return ""

if __name__ == "__main__":
    app.run(debug=True)
