from flask import Flask
import os
import time
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/', methods=['GET'])
def home():
    try:
        time.sleep(0.5)
        count = cache.incr('visits')
        return f"Hello World! I have been seen {count} times."
    except redis.exceptions.ConnectionError:
        return "Hello World! Redis is not available."

