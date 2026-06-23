async function extractMetrics() {

    const fileInput =
        document.getElementById("pdfFile");

    const formData = new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    const response = await fetch(
        "http://127.0.0.1:8000/extract",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    document.getElementById("metrics")
        .textContent =
        JSON.stringify(data, null, 2);
}

async function askQuestion() {

    const question =
        document.getElementById("question").value;

    const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question
            })
        }
    );

    const data = await response.json();

    document.getElementById("answer")
        .innerHTML =
        `<h3>${data.answer}</h3>`;
}