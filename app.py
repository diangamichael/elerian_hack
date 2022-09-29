import os
from flask import Flask, request
from sms import *

app = Flask(__name__)

#TODO: create incoming messages route

#TODO: create delivery reports route.

if __name__ == "__main__":
    #TODO: Call send message function
    sms().sending()
    app.run(debug=True, port = os.environ.get("PORT"))