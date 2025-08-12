# Keep Alive had to be flagged as a comment in order for .html file to be displayed.
# from keep_alive import keep_alive
from flask import Flask, request, jsonify, send_from_directory
from agent import search_google
import os

# keep_alive()

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
    results = search_bing(query)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
