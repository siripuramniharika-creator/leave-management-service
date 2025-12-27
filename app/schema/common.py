from pydantic import BaseModel

class UpdatePassword(BaseModel):
    role:str
    password:str
    security_question:str
    answer:str