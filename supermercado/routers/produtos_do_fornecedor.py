from typing import List
from fastapi import APIRouter, Depends
from shared.dependencies import get_db
from supermercado.schemas.produto import ProdutoResponse
from sqlalchemy.orm import Session
from supermercado.models.produto import Produto

router = APIRouter(prefix="/fornecedores")

@router.get("/{fornecedor_id}/produtos", response_model=List[ProdutoResponse], status_code=200)
async def listar_produtos_fornecedor(fornecedor_id:int, db:Session=Depends(get_db))->List[ProdutoResponse]:
    response_db = db.query(Produto).filter_by(fornecedor_id=fornecedor_id).all()
    return response_db