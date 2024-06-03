from pydantic import BaseModel

class FornecedorResponse(BaseModel):
    id_fornecedor: int
    nome: str
    email: str
    telefone: str
    class Config:
        from_attributes = True


class FornecedorRequest(BaseModel):
    nome: str
    email: str
    telefone: str