'''

@author: Jason Carrete
'''
import twilio.twiml, socket
from flask import Flask, request, redirect
server = socket.socket()
host = socket.gethostname()
port = 5000
server.bind((host, port))
server.listen(5)
client = None
while client == None:
    client, address = server.accept()
app = Flask(__name__)

commandsU = "ABRIDS"
commandsL = "abrids"

@app.route('/', methods=["GET", "POST"])
def hello_monkey(): #respond to text
    resp = twilio.twiml.Response()
    body = request.form["Body"]
    if body in commandsU or body in commandsL:
        client.send(body)
        return ""
    else:
        resp.message("Invalid Command")
        return str(resp)

app.run()
