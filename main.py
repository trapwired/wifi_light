import time
from time import sleep
from flask import Flask
import pifacedigitalio

app = Flask(__name__)
pfd = pifacedigitalio.PiFaceDigital()

single = False
double = False
long = False

@app.route('/single', methods=['GET'])
def one_press():
    print('single')
    single = True
    return 'I got you'


@app.route('/double', methods=['GET'])
def two_presses():
    print('double')
    double = True
    return 'I got you'


@app.route('/long', methods=['GET'])
def long_press():
    print('long')
    long = True
    return 'I got you'


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
    while True:
        if single:
            pfd.relays[0].value = 1
        elif double:
            pfd.relays[1].value = 1
        elif long:
            pfd.relays[0].value = 0
            pfd.relays[1].value = 0
            single = False
            double = False
            long = False
        time.sleep(1)
        pfd.relays[0].value = 0
        pfd.relays[1].value = 0
        time.sleep(1)
