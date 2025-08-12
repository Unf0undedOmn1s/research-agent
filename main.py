from flask import Flask, request, jsonify, send_from_directory
from agent import search_duckduckgo
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Serve research-agent.html from the same directory as this file
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'research-agent.html')

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"results": []})
    results = search_duckduckgo(query)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
