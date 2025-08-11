import threading
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Agent is running!"

def ping_self():
    while True:
        try:
            requests.get("https://YOUR-RENDER-APP-URL.onrender.com")
        except:
            pass
        time.sleep(600)  # ping every 10 minutes

threading.Thread(target=ping_self).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
