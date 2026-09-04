async function scanData() {

    const text = document.getElementById("inputText").value;

    if (text.trim() === "") {

        alert("Please enter some text");

        return;
    }

    document.getElementById("loading").innerText =
        "Scanning...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/detect",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: text
                })
            }
        );

        const data = await response.json();

        displayResults(data);

    } catch (error) {

        console.log(error);

        alert("Could not connect to the backend.");

    }

    document.getElementById("loading").innerText = "";
}


function displayResults(data) {

    const risk = document.getElementById("risk");

    const detectedData =
        document.getElementById("detectedData");

    risk.innerText =
        "Risk Level: " + data.risk;

    detectedData.innerHTML = "";

    if (data.count === 0) {

        detectedData.innerHTML =
            "<p>No sensitive data detected.</p>";

        return;
    }

    data.detected_data.forEach(function(item) {

        const div = document.createElement("div");

        div.className = "detected";

        div.innerHTML =
            "<strong>Type:</strong> " +
            item.type +
            "<br>" +
            "<strong>Value:</strong> " +
            item.value;

        detectedData.appendChild(div);

    });
}