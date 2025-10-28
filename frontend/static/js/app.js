const form = document.getElementById('predictForm');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Convertir valores a números
    data.pclass = Number(data.pclass);
    data.age = Number(data.age);
    data.sibsp = Number(data.sibsp);
    data.parch = Number(data.parch);
    data.fare = Number(data.fare);

    try {
        const response = await fetch('/api/predict/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const json = await response.json();
        const texto = json.prediction === 1 ? "Sobreviviría" : "No sobreviviría";
        result.textContent = `${texto} (Probabilidad: ${(json.probability*100).toFixed(2)}%)`;
    } catch (err) {
        result.textContent = 'Error: ' + err;
    }
});
