from flask import Flask, request, jsonify
from calculator import dodawanie,dzielenie,odejmowanie,mnozenie
import numpy as np

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    liczba1 = data['liczba1']
    liczba2 = data['liczba2']
    result = float(dodawanie(liczba1, liczba2))
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    liczba1 = data['liczba1']
    liczba2 = data['liczba2']
    result = float(odejmowanie(liczba1, liczba2))
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    liczba1 = data['liczba1']
    liczba2 = data['liczba2']
    result = float(mnozenie(liczba1, liczba2))
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    liczba1 = data['liczba1']
    liczba2 = data['liczba2']
    result = float(dzielenie(liczba1, liczba2))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)