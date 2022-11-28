import time
from queue import Queue
from threading import Thread

from flask import Flask


def get_queue_data(queue):
    try:
        return queue.get(block=False)
    except queue.Empty:
        return None


def main_light_loop(queue):
    while True:
        data = get_queue_data(queue)
        print("Data: +" + str(data))
        time.sleep(1)


q = Queue()
app = Flask(__name__)


@app.route("/")
def hello_world():
    q.put("data")
    return "<p>Hello, World!</p>"


Thread(target=main_light_loop, args=(q,)).start()
