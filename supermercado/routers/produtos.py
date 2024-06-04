from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from supermercado.models.produto import Produto
from shared.dependencies import get_db
from supermercado.schemas.produto import ProdutoRequest, ProdutoResponse
from shared.exceptions import NotFound
from supermercado.models.fornecedor import Fornecedor

router = APIRouter(prefix="/produtos")

@router.post("", response_model=ProdutoResponse, status_code=201)
async def criar_produto(produto_request:ProdutoRequest, db:Session=Depends(get_db)) -> ProdutoResponse:
    validar_fornecedor(produto_request.fornecedor_id, db)
    produto = Produto(**produto_request.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

@router.get("/", response_model=List[ProdutoResponse], status_code=200)
async def listar_produtos(db:Session=Depends(get_db)) -> List[ProdutoResponse]:
    return db.query(Produto).all()

@router.get("/{id_produto}", response_model=ProdutoResponse, status_code=200)
async def obter_produto(id_produto:int, db:Session=Depends(get_db)) -> ProdutoResponse:
    produto = buscar_produto_id(id_produto, db)
    return produto
    


def buscar_produto_id(id_produto:int, db:Session) -> Produto:
    produto = db.query(Produto).get(id_produto)
    if produto is None:
        raise NotFound("Produto não encontrado")
    return produto


def validar_fornecedor(fornecedor_id, db):
    if fornecedor_id is not None:
        produto = db.query(Fornecedor).get(fornecedor_id)
        if produto is None:
            raise NotFound("Este fornecedor não existe no banco de dados")
        return produto
