from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

trains = {
    101: {"name": "Rajdhani Express", "seats": 5},
    102: {"name": "Shatabdi Express", "seats": 5}
}

tickets = {}

def generate_pnr():
    return "PNR" + str(random.randint(10000, 99999))

@app.route("/")
def home():
    return render_template("index.html", trains=trains)

@app.route("/book", methods=["POST"])
def book_ticket():
    data = request.json
    train_no = int(data["train_no"])
    name = data["name"]
    age = data["age"]

    if trains[train_no]["seats"] <= 0:
        return jsonify({"error": "No seats available"})

    pnr = generate_pnr()
    tickets[pnr] = {
        "name": name,
        "age": age,
        "train": trains[train_no]["name"]
    }
    trains[train_no]["seats"] -= 1

    return jsonify({"pnr": pnr})

if __name__ == "__main__":
    print("Starting Railway Ticket App...")
    app.run(host="127.0.0.1", port=5000, debug=True)

