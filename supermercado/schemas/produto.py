from pydantic import BaseModel
from supermercado.schemas.fornecedor import FornecedorResponse

class ProdutoResponse(BaseModel):
    id_produto: int
    nome: str
    disponivel: bool
    quantidade: int
    fornecedor: FornecedorResponse | None = None
    class Config:
        from_attributes = True


class ProdutoRequest(BaseModel):
    nome: str
    disponivel: bool
    quantidade: int
    fornecedor_id: int | None = None