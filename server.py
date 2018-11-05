import sys
from parser import parse_args
from led import LED
from threading import Thread
from bottle import Bottle, route, run, get, post

app = Bottle()

defaultOptions = {
    "emulator": True,
    "graphic": False,
    "scroll": False,
    "message": "",
    "new_message": "new_message",
    "reset": False,
    "time": False
}

led = LED(defaultOptions)
t = Thread(target=led.run, args=())
t.start()

@app.get('/status')
def status():
    return "you're good to go.\n"

@app.get('/scroll')
def scroll():
    if led.runner.options.get('scroll'):
        led.runner.options['scroll'] = False
    else:
        led.runner.options['scroll'] = True
    led.runner.options['reset'] = True
    return "scrolling.\n"

@app.get('/time')
def time():
    led.runner.options['time'] = True 
    led.runner.options['reset'] = True
    return "displaying time.\n"

@app.get('/msg/<message>')
def receive(message):
    led.runner.options['message'] = message
    led.runner.options['time'] = False
    led.runner.options['reset'] = True
    return "displaying message.\n"

@app.route('/clear')
def clear():
    led.runner.options['message'] = ""
    led.runner.time['time'] = False
    led.runner.options['reset'] = True
    return "cleared\n"

app.run(host='0.0.0.0', port=5000, debug=False)
