from flask import Flask
import piface.pfio as pfio

app = Flask(__name__)


@app.route('/single', methods=['GET'])
def one_press():
    print('single')
    pfio.digital_write(0, 1)


@app.route('/double', methods=['GET'])
def two_presses():
    print('double')
    pfio.digital_write(1, 1)


@app.route('/long', methods=['GET'])
def long_press():
    print('long')
    pfio.digital_write(1, 0)
    pfio.digital_write(0, 0)


if __name__ == '__main__':
    pfio.init()
    app.run(host='0.0.0.0', threaded=True, port=5000)
