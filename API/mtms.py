from sqlalchemy import create_engine, text
import datetime
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
import json

# Conexão com o DB
load_dotenv()
usuario = os.getenv("usuario")
senha = os.getenv("senha")
host = os.getenv("host")
porta = os.getenv("porta")
banco = os.getenv("banco")
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

df = pd.read_sql('horarios', con=engine)

df['saida'] = pd.to_timedelta(df['saida']).dt.total_seconds()
df['chegada'] = pd.to_timedelta(df['chegada']).dt.total_seconds()

saida_mean = int(np.mean(df['saida']))
chegada_mean = int(np.mean(df['chegada']))

tempo_viagem = round((chegada_mean - saida_mean))
tempo_viagem = timedelta(seconds = tempo_viagem)

def calcularSaida(horario_chegada, tempo_viagem):
    hora_chegada, minuto_destino = horario_chegada.split(':')
    hora_chegada = int(hora_chegada)
    minuto_destino = int(minuto_destino)

    hora_chegada = timedelta(hours=hora_chegada, minutes=minuto_destino)
    horario_saida = hora_chegada - tempo_viagem

    return(horario_saida)

def calcularChegada(horario_origem, tempo_viagem):
    hora_origem, minuto_saida = horario_origem.split(':')
    hora_origem = int(hora_origem)
    minuto_saida = int(minuto_saida)

    hora_origem = timedelta(hours=hora_origem, minutes=minuto_saida)
    horario_destino = hora_origem + tempo_viagem

    return(horario_destino)