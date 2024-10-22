from pydantic import BaseModel

class AuthSchema(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    token: str