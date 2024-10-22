from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    username: str
    hash_password: str

class UserResponce(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str