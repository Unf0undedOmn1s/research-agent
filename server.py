from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Run your existing agent.py script with the query
    result = subprocess.run(
        ["python", "agent.py", query],
        capture_output=True,
        text=True
    )

    return jsonify({
        "query": query,
        "output": result.stdout.strip()
    })

@app.route("/", methods=["GET"])
def home():
    return "Research Agent is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
