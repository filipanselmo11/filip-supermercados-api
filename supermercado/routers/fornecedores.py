from typing import List
from fastapi import APIRouter, Depends
from shared.dependencies import get_db
from supermercado.schemas.fornecedor import FornecedorRequest, FornecedorResponse
from sqlalchemy.orm import Session
from supermercado.models.fornecedor import Fornecedor
from shared.exceptions import NotFound

router = APIRouter(prefix="/fornecedores")

@router.post("", response_model=FornecedorResponse, status_code=201)
async def criar_fornecedor(fornecedor_request:FornecedorRequest, db:Session=Depends(get_db)) -> FornecedorResponse:
    fornecedor = Fornecedor(**fornecedor_request.model_dump())
    db.add(fornecedor)
    db.commit()
    db.refresh(fornecedor)
    return fornecedor

@router.get("/", response_model=List[FornecedorResponse], status_code=200)
async def listar_produtos(db:Session=Depends(get_db)) -> List[FornecedorResponse]:
    return db.query(Fornecedor).all()

@router.get("/{id_fornecedor}", response_model=FornecedorResponse, status_code=200)
async def obter_fornecedor(id_fornecedor:int, db:Session=Depends(get_db)) -> FornecedorResponse:
    fornecedor = buscar_fornecedor_id(id_fornecedor, db)
    return fornecedor


def buscar_fornecedor_id(id_fornecedor:int, db:Session) -> Fornecedor:
    fornecedor = db.query(Fornecedor).get(id_fornecedor)
    if fornecedor is None:
        raise NotFound("Fornecedor não encontrado")
    return fornecedor