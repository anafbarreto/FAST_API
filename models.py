from pydantic import BaseModel
from uuid import UUID, uuid4 # Cria um identificador unico e o uuid4 gera um identificador unico aleatório
from typing import Optional, List # Permite que o retorno seja de tipos diferentes em um unico argumento
from enum import Enum # Enum para trabalhar com lista

class Role(str, Enum):
    role_1 = "admin"
    role_2 = "aluna"
    role_3 = "instrutora"

class User(BaseModel):
    id: Optional[UUID] = uuid4() # Cria um id aleatorio
    first_name: str
    last_name: str
    email: str
    role: List[Role]