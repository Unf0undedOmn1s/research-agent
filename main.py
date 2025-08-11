from keep_alive import keep_alive
from server import app

keep_alive()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
