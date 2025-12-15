function bookTicket() {
    fetch("/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            train_no: document.getElementById("train").value,
            name: document.getElementById("name").value,
            age: document.getElementById("age").value
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
        } else {
            document.getElementById("result").innerText =
                "Ticket Booked Successfully! PNR: " + data.pnr;
        }
    });
}
