from pydantic import BaseModel

class User(BaseModel):
    username: str
    hash_password: str