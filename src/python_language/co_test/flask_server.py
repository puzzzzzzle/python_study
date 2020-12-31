from flask import Flask
import time
import logging
import consts

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(2)
    logger.info("get one")
    return 'Hello! index'


@app.route('/<name>')
def hello_world(name):
    time.sleep(2)
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(threaded=True)
