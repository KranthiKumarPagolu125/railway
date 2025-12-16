from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Train data
trains = {
    101: {
        "name": "Tirupathi Express",
        "from": "Vijayawada",
        "to": "Tirupathi",
        "fare": 450,
        "seats": 5
    },
    102: {
        "name": "Godavari Express",
        "from": "Visakhapatnam",
        "to": "Hyderabad",
        "fare": 750,
        "seats": 5
    }
}

def generate_pnr():
    return "PNR" + str(random.randint(10000, 99999))

@app.route("/")
def home():
    return render_template("index.html", trains=trains)

@app.route("/book", methods=["POST"])
def book_ticket():
    data = request.get_json()
    train_no = int(data["train_no"])

    if trains[train_no]["seats"] <= 0:
        return jsonify({"error": "No seats available"})

    trains[train_no]["seats"] -= 1

    return jsonify({
        "pnr": generate_pnr(),
        "fare": trains[train_no]["fare"],
        "train": trains[train_no]["name"]
    })

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
