import sys
from parser import parse_args
from led import LED

from flask import Flask
app = Flask(__name__)

defaultOptions = {
    "emulator": True,
    "graphic": False,
    "scroll": True,
    "message": ""
}

@app.route('/status')
def status():
    return "good to go.\n"

@app.route('/<message>')
def receive(message):
    return print(message)

def print(message):
    try:
        options = defaultOptions
        options['message'] = message
        led = LED(options)
        led.print(options.get('message'))
    except KeyboardInterrupt:
        pass

    return "done."