from pydantic import BaseModel

class AddStaff(BaseModel):
    name:str
    email:str
    username:str
    department:str
    designation:str
    contact_no:str
    staff_id:str
    date_of_birth:str
    age:int

class UpdateStaff(BaseModel):
    name:str
    email:str
    username:str
    department:str
    designation:str
    contact_no:str
    date_of_birth:str
    age:int