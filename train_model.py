import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simulated data: Heart rate, Temperature, SpO2 vs health risk
data = {
    'heart_rate': [58, 62, 75, 85, 95, 100, 105, 110, 120, 130],
    'temperature': [36.5, 36.7, 37.0, 37.2, 37.5, 38.0, 38.2, 38.4, 38.5, 39.0],  # in Celsius
    'spO2': [98, 99, 97, 96, 95, 94, 93, 92, 91, 90],  # SpO2 in %
    'risk': ['Low', 'Low', 'Low', 'Low', 'Moderate', 'Moderate', 'High', 'High', 'High', 'High']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features (Heart rate, Temperature, SpO2)
X = df[['heart_rate', 'temperature', 'spO2']]  
# Target (Health risk)
y = df['risk']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'extended_health_risk_model.pkl')

print("Model trained and saved as 'extended_health_risk_model.pkl'")
