from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time/')
def current_time():
    current_date_and_time = datetime.now()
    return 'The current time is {:%b %d, %Y %H:%M:%S}'.format(current_date_and_time)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
