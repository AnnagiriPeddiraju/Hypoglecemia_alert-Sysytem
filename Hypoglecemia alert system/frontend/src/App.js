import React, { useState } from "react";

function App() {
  const [inputs, setInputs] = useState(Array(12).fill(""));
  const [risk, setRisk] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (idx, value) => {
    const newInputs = [...inputs];
    newInputs[idx] = value;
    setInputs(newInputs);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setRisk(null);
    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          data: [inputs.map(Number)]
        })
      });
      const result = await response.json();
      setRisk(result.risk);
    } catch (error) {
      setRisk("Error: " + error.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 500, margin: "auto", padding: 20 }}>
      <h2>Hypoglycemia Risk Predictor</h2>
      <form onSubmit={handleSubmit}>
        <div>
          {inputs.map((val, idx) => (
            <input
              key={idx}
              type="number"
              step="any"
              value={val}
              onChange={e => handleChange(idx, e.target.value)}
              placeholder={`Glucose ${idx + 1}`}
              style={{ width: 70, margin: 5 }}
              required
            />
          ))}
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict Risk"}
        </button>
      </form>
      {risk !== null && (
        <div style={{ marginTop: 20 }}>
          <strong>Predicted Risk:</strong>{" "}
          {typeof risk === "number"
            ? `${(risk * 100).toFixed(1)}%`
            : risk}
        </div>
      )}
    </div>
  );
}

export default App;