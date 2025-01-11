import time
from datetime import datetime

from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Response(stream(), mimetype='text/event-stream')

def stream():
    while True:
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield f'{current_date}\n\n'
        time.sleep(1)


if __name__ == '__main__':
    app.run()
