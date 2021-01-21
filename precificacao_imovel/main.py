from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/submit-data', methods = ['POST'])
def getdata():
    request.headers.get("X-Requested-With") == "XMLHttpRequest"
    data = request.get_json()

    x = np.array([[data['Qualidade'], data['AnoConstrucao'], data['Banheiros'], data['Comodos'], data['Garagem']]])

    model = joblib.load('model')
    prediction = model.predict(x)
    result = prediction[0]

    resposta = {'Preco_estimado': int(result)}
    return jsonify(resposta)
app.run(port=5000, debug = 'development')