from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

    

class UserResponse(BaseModel):
    id: int
    username:str
    email:EmailStr
    role:str
    model_config={
            "from attributes":True
        }

class UserLogin(BaseModel):
    email:EmailStr
    password:str

    