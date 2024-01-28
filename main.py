from flask import Flask
import pifacedigitalio

app = Flask(__name__)
pfd = pifacedigitalio.PiFaceDigital()

@app.route('/single', methods=['GET'])
def one_press():
    print('single')
    pfd.relays[0].value = 1


@app.route('/double', methods=['GET'])
def two_presses():
    print('double')
    pfd.relays[0].value = 2


@app.route('/long', methods=['GET'])
def long_press():
    print('long')
    pfd.relays[0].value = 1
    pfd.relays[0].value = 2


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
