from flask import Flask
from threading import Thread
import requests
import time

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def ping_self():
    while True:
        try:
            requests.get("https://<YOUR-RENDER-APP-URL>")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(600)  # ping every 10 min

def keep_alive():
    t1 = Thread(target=run)
    t2 = Thread(target=ping_self)
    t1.start()
    t2.start()
