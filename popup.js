async function fetchBudget() {
  const dest = document.getElementById('destination').value;
  const response = await fetch(`https://your-backend-url.onrender.com/analyze?destination=${encodeURIComponent(dest)}`);
  const data = await response.json();
  document.getElementById('results').innerHTML = `
    <h3>Low Cost ($0 - $500)</h3><p>${data.low}</p>
    <h3>Mid Tier ($600 - $999)</h3><p>${data.mid}</p>
    <h3>Top Tier ($1,000 - $20,000)</h3><p>${data.high}</p>
  `;
}