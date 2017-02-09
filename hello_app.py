# Hello World app
# If you use double-quotes you're going to have a bad time!

from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(80))
