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
    model_rf_model = joblib.load('model_rf_model')
    prediction = model.predict(x)
    prediction_rf = model_rf_model.predict(x)
    result = prediction[0]
    result_rf = prediction_rf[0]

    resposta = {f'Preco_estimado pela regressão {int(result)}. Preco_estimado pelo Random Forest: {int(result_rf)}'}
    return jsonify(resposta)
app.run(port=5000, debug = 'development')