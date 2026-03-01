from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey,
    Date, LargeBinary, Table, Numeric, Boolean, Time
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Engine = create_engine("mysql+pymysql://root:2008fsfc@localhost:3306/site_game")
Base = declarative_base()
_Session = sessionmaker(bind=Engine)

class Jogos(Base):
    __tablename__ = 'jogos'

    id_jogos = Column(Integer, primary_key=True)
    nome = Column(String(255),unique=True, nullable=True)
    tipo = Column(String(255), nullable=True)

class Endereco(Base):

    __tablename__ = 'endereco'

    id_endereco = Column(Integer, primary_key=True)
    logradouro = Column(String(255), nullable=True)
    bairro = Column(String(255), nullable=True)
    cidade = Column(String(255), nullable=True)
    estado = Column(String(255), nullable=True)
    numero = Column(Integer, nullable=True)

class Usuario(Base):

    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=True)
    username = Column(String(255), nullable=True, unique=True)
    genero = Column(String(1), nullable=True)
    data_nascimento = Column(Date, nullable=True)
    senha = Column(String(255), nullable=True)
    nivel = Column(Integer)
    id_endereco = Column(Integer, ForeignKey('endereco.id_endereco'), nullable=True)


Historico = Table('historico', Base.metadata, Column('id_usuario',Integer,ForeignKey('usuario.id_usuario'),primary_key=True),
                  Column('id_jogos', Integer, ForeignKey('jogos.id_jogos'), primary_key=True), Column('vitorias', Integer), Column('derrotas', Integer), Column('soma_jogos', Integer))