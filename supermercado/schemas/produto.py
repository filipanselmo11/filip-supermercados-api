from pydantic import BaseModel

class ProdutoResponse(BaseModel):
    id_produto: int
    nome: str
    disponivel: bool
    quantidade: int
    class Config:
        from_attributes = True


class ProdutoRequest(BaseModel):
    nome: str
    disponivel: bool
    quantidade: int