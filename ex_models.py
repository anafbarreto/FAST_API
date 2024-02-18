from  fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role # Dados do arquivo models.py
from uuid import UUID, uuid4


app = FastAPI()

db: List[User] = [ # Lista de usuarios em um "banco de dados"
    User(id=UUID("dab40374-f41c-4abe-ae93-a2f71c8b6084"), 
         first_name="Ana", 
         last_name="Barreto", 
         email="anabarreto@example.com", 
         role=[Role.role_1,]
    ),
    User(id=UUID("9dba9226-6ec3-4912-b10b-8abb8030f2ff"),
         first_name="Manu",
         last_name="Barreto",
         email="manu@example.com",
         role=[Role.role_2,]
    ),
    User(id=UUID("0108543f-1643-400c-a536-f44c542263de"),
         first_name="Camila",
         last_name="Silva",
         email="Camila@example.com",
         role=[Role.role_3,]
    )                  
]

@app.get("/") # Rota principal
async def root():
    return {"message": "Hello World"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}") # Rota para buscar um usuario pelo id
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"} # Retorna o erro 404

@app.post("/api/users") # post = criar
async def add_users(user: User): # Seguindo a classe User que já desenhamos
    db.append(user)
    return {f"message: {user.id} created"}

@app.delete("/api/users/{id}") # delete = deletar usuario
async def delete_user(id: UUID): # Seguindo o UUID para encontrar o user
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found") # Tratamento de exceções, a forma "correta" de exibir erros

