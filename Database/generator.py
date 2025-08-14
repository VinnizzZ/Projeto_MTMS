from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date
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
Base = declarative_base()

# Definindo a tabela como classe
class horarios(Base):
    __tablename__ = 'horarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    saida = Column(String(8))
    chegada = Column(String(8))

# Criar a tabela no banco se não existir
Base.metadata.create_all(engine)

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()

session.commit()
session.close()