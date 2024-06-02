from sqlalchemy import Boolean, Column, Integer, String
from shared.database import Base

class Produto(Base):
    __tablename__="produtos"
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    disponivel = Column(Boolean)
    quantidade = Column(Integer)