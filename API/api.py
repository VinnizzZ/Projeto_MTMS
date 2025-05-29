import json
from flask import Flask, jsonify, request
import mtms
import os
import requests
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Conexão com o DB
load_dotenv()
usuario = os.getenv("usuario")
senha = os.getenv("senha")
host = os.getenv("host")
porta = os.getenv("porta")
banco = os.getenv("banco")
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

dados = []

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def get_data():
 return jsonify(dados)

# Validação de dados recebidos
def data_is_valid(dados):
  required_keys = ['tempo_viagem', 'horario']

  if all(key in dados for key in required_keys):
    return True
  return False

@app.route('/calculoSaida', methods=['POST'])
def create_saida():

    global nextId

    dado = json.loads(request.data)
    if not data_is_valid(dado):
        return jsonify({ 'erro': 'propriedades inválidas.' }), 400
    
    # Calculo do horario de saída
    horario_saida = mtms.calcularSaida(dado['horario'], dado['tempo_viagem'])

    dado['id'] = nextId
    nextId += 1

    dados.append(dado)
    return jsonify({
       'horario_saida' : horario_saida,
       'tempo_viagem' : dado['tempo_viagem']
    })

@app.route('/calculoChegada', methods=['POST'])
def create_chegada():

    global nextId

    dado = json.loads(request.data)
    if not data_is_valid(dado):
        return jsonify({ 'erro': 'propriedades inválidas.' }), 400
    
    # Calculo do horario de saída
    horario_chegada = mtms.calcularChegada(dado['horario'], dado['tempo_viagem'])

    dado['id'] = nextId
    nextId += 1

    dados.append(dado)
    return jsonify({
       'horario_chegada' : horario_chegada,
       'tempo_viagem' : dado['tempo_viagem']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)