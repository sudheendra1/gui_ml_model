from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get('symptoms', [])
    print(symptoms)

    if not symptoms or len(symptoms) < 4 or len(symptoms) > 6:
        return jsonify({'error': 'Please provide between 4 to 6 symptoms.'}), 400
    
    response = requests.post('https://pharmcare-dpv2-deployment.onrender.com/predict_disease', json=data)

    if response.status_code == 200:
        print("Response Data:", response.json())
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to get prediction.'}), response.status_code

if __name__ == '__main__':
    app.run()
