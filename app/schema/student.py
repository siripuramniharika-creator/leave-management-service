from pydantic import BaseModel

class AddStudent(BaseModel):
    name:str
    email:str
    roll_no:str
    department:str
    contact_number:str
    date_of_birth:str
    age:int

class UpdateStudent(BaseModel):
    name:str
    email:str
    department:str
    contact_number:str
    date_of_birth:str
    age:int