from flask import Flask

app = Flask(__name__)


@app.route('/one_press', methods=['GET'])
def one_press():
    print('one_press')


@app.route('/two_presses', methods=['GET'])
def two_presses():
    print('two_presses')


@app.route('/long_press', methods=['GET'])
def long_press():
    print('long press')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
