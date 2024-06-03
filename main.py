from fastapi import FastAPI
from shared.exceptions_handler import not_found_handler
from supermercado.routers import fornecedores, produtos
from shared.exceptions import NotFound

app = FastAPI()

@app.get("/")
async def root():
    return "Olá mundo"


app.include_router(produtos.router)
app.include_router(fornecedores.router)
app.add_exception_handler(NotFound, not_found_handler)