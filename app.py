from flask import Flask, jsonify
import random
import joblib

# Load the extended model
model = joblib.load('extended_health_risk_model.pkl')

app = Flask(__name__)

@app.route('/api/vital-signs')
def vital_signs():
    # Simulate heart rate, temperature, and SpO2
    heart_rate = random.randint(60, 130)
    temperature = round(random.uniform(36.5, 39.0), 1)  # Simulated temp between 36.5°C and 39°C
    spO2 = random.randint(90, 100)  # Simulated SpO2 between 90% and 100%

    # Predict the health risk based on vital signs
    risk = model.predict([[heart_rate, temperature, spO2]])[0]
    
    return jsonify({
        "heart_rate": heart_rate,
        "temperature": temperature,
        "spO2": spO2,
        "risk": risk
    })

if __name__ == '__main__':
    print("Starting Flask API...")
    app.run(debug=True)
