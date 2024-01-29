import time
from time import sleep
from flask import Flask
import pifacedigitalio
import threading

app = Flask(__name__)
pfd = pifacedigitalio.PiFaceDigital()

green = 0
red = 1


@app.route('/single', methods=['GET'])
def one_press():
    print('single')
    t = threading.Thread(target=one_press_action)
    t.start()
    return 'I got you'


def one_press_action():
    for i in range(10):
        pfd.relays[green].value = 1
        time.sleep(0.1)
        pfd.relays[green].value = 0
        time.sleep(0.1)
    reset_all_lights()


@app.route('/double', methods=['GET'])
def two_presses():
    print('double')
    t = threading.Thread(target=double_press_action)
    t.start()
    return 'I got you'


def double_press_action():
    for i in range(10):
        pfd.relays[red].value = 1
        pfd.relays[green].value = 0
        time.sleep(0.1)
        pfd.relays[red].value = 0
        pfd.relays[green].value = 1
        time.sleep(0.1)
    reset_all_lights()


@app.route('/long', methods=['GET'])
def long_press():
    print('long')
    t = threading.Thread(target=long_press_action)
    t.start()
    return 'I got you'


def long_press_action():
    for i in range(10):
        pfd.relays[red].value = 1
        time.sleep(0.1)
        pfd.relays[red].value = 0
        time.sleep(0.1)
    reset_all_lights()


def reset_all_lights():
    pfd.relays[green].value = 0
    pfd.relays[red].value = 0


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
