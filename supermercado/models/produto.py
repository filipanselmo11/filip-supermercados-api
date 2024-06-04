from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from shared.database import Base
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__="produtos"
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    disponivel = Column(Boolean)
    quantidade = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id_fornecedor"))
    fornecedor = relationship("Fornecedor")