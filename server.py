'''

@author: Jason Carrete
'''
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
'''import twilio.twiml, socket
from flask import Flask, request, redirect
server = socket.socket()
host = socket.gethostname()
port = 9999
server.bind((host, port))
server.listen(5)
print "Listening"
client, address = server.accept()
print "Accepted"
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

app.run()'''
