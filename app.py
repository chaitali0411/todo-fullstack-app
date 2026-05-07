from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)



tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/add", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data["task"])
    return jsonify({"message": "Task added"})

@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Invalid index"})

if __name__ == "__main__":
    app.run(debug=True)