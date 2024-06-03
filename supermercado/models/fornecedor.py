from sqlalchemy import Column, Integer, String
from shared.database import Base


class Fornecedor(Base):
    __tablename__="fornecedores"
    id_fornecedor=Column(Integer, primary_key=True, autoincrement=True)
    nome=Column(String(30))
    email=Column(String(30))
    telefone=Column(String(90))