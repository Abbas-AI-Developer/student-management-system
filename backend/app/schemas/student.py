from pydantic import BaseModel ,EmailStr

class Studentcreate(BaseModel):

    name:str
    email:EmailStr
    age:int
    course:str
    city:str


    model_config = {
        "from_attributes": True
    }
