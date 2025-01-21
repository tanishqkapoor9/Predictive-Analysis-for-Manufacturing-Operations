from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import os
import logging

app = Flask(__name__)
model = None

# Ensure directories exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')
if not os.path.exists('models'):
    os.makedirs('models')

# Logging setup
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return "Welcome to the Predictive Analysis API!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)
    logging.info(f"File uploaded to {filepath}")
    return jsonify({"message": "File uploaded successfully"})

@app.route('/train', methods=['POST'])
def train_model():
    global model
    try:
        data = pd.read_csv(request.json['filepath'])
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    joblib.dump(model, 'models/decision_tree.pkl')
    logging.info("Model trained and saved.")
    return jsonify({"accuracy": accuracy})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if not model:
        model_path = 'models/decision_tree.pkl'
        if os.path.exists(model_path):
            model = joblib.load(model_path)
        else:
            return jsonify({"error": "Model not found"}), 400
    data = request.json
    prediction = model.predict([[data['Temperature'], data['Run_Time']]])
    return jsonify({"Downtime": "Yes" if prediction[0] else "No"})

if __name__ == '__main__':
    app.run(debug=True)
