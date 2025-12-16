function bookTicket() {
    var trainNo = document.getElementById("train").value;

    fetch("/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            train_no: trainNo
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            document.getElementById("result").innerHTML =
                "✅ Ticket Booked<br>" +
                "Train: " + data.train + "<br>" +
                "Fare: ₹" + data.fare + "<br>" +
                "PNR: " + data.pnr;
        }
    });
}


