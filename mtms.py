from sqlalchemy import create_engine, text
import datetime
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# Conexão com o DB
usuario = 'root'
senha = ''
host = 'localhost'
porta = 3306
banco = 'Horas'
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

# Testar se a conexão está funcionando
with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT * from horarios"))
    versao = resultado.fetchall()
    for x in versao:
        print(x)

df = pd.read_sql('horarios', con=engine)

df['saida'] = pd.to_timedelta(df['saida']).dt.total_seconds()
df['ponto1'] = pd.to_timedelta(df['ponto1']).dt.total_seconds()
df['ponto2'] = pd.to_timedelta(df['ponto2']).dt.total_seconds()
df['ponto3'] = pd.to_timedelta(df['ponto3']).dt.total_seconds()
df['ponto4'] = pd.to_timedelta(df['ponto4']).dt.total_seconds()
df['chegada'] = pd.to_timedelta(df['chegada']).dt.total_seconds()

#print(df.info())

saida_mean = int(np.mean(df['saida']))
ponto1_mean = int(np.mean(df['ponto1']))
ponto2_mean = int(np.mean(df['ponto2']))
ponto3_mean = int(np.mean(df['ponto3']))
ponto4_mean = int(np.mean(df['ponto4']))
chegada_mean = int(np.mean(df['chegada']))

tempo_viagem = round((chegada_mean - saida_mean))
tempo_viagem = timedelta(seconds = tempo_viagem)

tipo_calculo = input('Calculo de saida ou destino? S/D\n')

match tipo_calculo.lower():
    case 's':
        horario_destino = input('Qual horário você precisa chegar no seu destino?\n')
        hora_destino, minuto_destino = horario_destino.split(':')
        hora_destino = int(hora_destino)
        minuto_destino = int(minuto_destino)
        hora_destino = timedelta(hours=hora_destino, minutes=minuto_destino)
        hora_saida = hora_destino - tempo_viagem
        print(hora_saida)
        print(tempo_viagem)

    case 'd':
        horario_saida = input('Qual horário você vai sair?\n')
        hora_saida, minuto_saida = horario_saida.split(':')
        hora_saida = int(hora_saida)
        minuto_saida = int(minuto_saida)
        hora_saida = timedelta(hours=hora_saida, minutes=minuto_saida)
        hora_saida = hora_saida + tempo_viagem
        print(hora_saida)
        print(tempo_viagem)

    case _:
        print('Entrada invalida, digite S ou D')