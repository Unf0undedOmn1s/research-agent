from keep_alive import keep_alive
from server import app
from flask import Flask, request, jsonify, send_from_directory
from agent import search_bing

keep_alive()

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('.', 'research-agent.html')

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"results": []})
    results = search_bing(query)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
