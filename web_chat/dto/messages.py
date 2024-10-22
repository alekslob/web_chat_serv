from pydantic import BaseModel, ConfigDict
from datetime import datetime
from .user import UserResponce

class Message(BaseModel):
    content: str
    user_id: int
    
    class Config:
        orm_mode = True

class MessageResponce(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    create_time: datetime
    user: UserResponce


    
