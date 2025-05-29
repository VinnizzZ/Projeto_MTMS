from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import generator
import os
from dotenv import load_dotenv

# Conexão com o DB
load_dotenv()
usuario = os.getenv("usuario")
senha = os.getenv("senha")
host = os.getenv("host")
porta = os.getenv("porta")
banco = os.getenv("banco")
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

# Pegando as informações de horário
lista = []

for i in range(2):
    horas = input()
    lista.append(horas)

# Inserindo os dados na tabela do DB

novo_horario = generator.horarios(
    saida = lista[0],
    chegada = lista[1]
)

Session = sessionmaker(bind=engine)
session = Session()

session.add(novo_horario)
session.commit()
session.close()