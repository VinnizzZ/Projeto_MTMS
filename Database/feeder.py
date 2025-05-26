from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import generator

# Conexão com o DB
usuario = 'root'
senha = ''
host = 'localhost'
porta = 3306
banco = 'Horas'
engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

# Pegando as informações de horário
lista = []

for i in range(6):
    horas = input()
    lista.append(horas)

# Inserindo os dados na tabela do DB

novo_horario = generator.horarios(
    saida = lista[0],
    ponto1 = lista[1],
    ponto2 = lista[2],
    ponto3 = lista[3],
    ponto4 = lista[4],
    chegada = lista[5]
)

Session = sessionmaker(bind=engine)
session = Session()

session.add(novo_horario)
session.commit()
session.close()