from fastapi import FastAPI
from typing import Union # Union permite que o retorno seja de tipos diferentes em um unico argumento
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
@app.get("/") # Rota principal
async def root(): # Metodo assincrono
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, busca: Union[str, int] = None): # Recebendo uma string e int
    return {"item_id": item_id, "busca": busca}

@app.put("/items/{item_id}") # PUT = Atualizar
def update_item(item_id: int, item: Item): # Recebendo uma string e int
    return {"item_name": item.name, "item_id": item_id}