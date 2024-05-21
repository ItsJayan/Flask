from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "Contact": u"9987644456",
        "Name": u"Raju",
        "done": False
    },
    {
        "id": 2,
        "Contact": u"9876543222",
        "Name": u"Rahul",
        "done": False
    }
    
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error"
        }, 400
        )
    task = {
        "id": task[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": "tasks"
    })
if (__name__ == "__main__"):
    app.run(debug = True)