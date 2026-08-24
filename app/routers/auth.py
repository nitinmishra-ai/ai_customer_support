from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse,UserLogin

from app.db.database import get_db

from app.services.user_services import create_user,login_user


from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth",
                   tags=["Authentication"],)

@router.post("/register",
             response_model=UserResponse)

def register(user_data: UserCreate,
             db:Session = Depends(get_db)):

    return create_user(db,user_data)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    return login_user(
        db,
        form_data.username,
        form_data.password
    )





