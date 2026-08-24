from fastapi import HTTPException,status

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate,UserResponse
from app.core.security import hash_password,verify_password
from app.core.jwt import create_access_token
from app.models.user import User



def create_user(db:Session,
                user_data:UserCreate
                ):
    user = User(username=user_data.username,
                email= user_data.email,
                password_hash=hash_password(user_data.password))

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db:Session, email:str, password:str):

    user = db.query(User).filter(User.email == email).first()


    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email and password"
        )
    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "sub": user.email,
        "user_id": user.id
    })

    return{
        "access_token": access_token,
        "token_type": "bearer"
    }


