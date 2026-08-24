from fastapi import APIRouter, Depends, HTTPException,status

from sqlalchemy.orm import Session


from app.db.database import get_db
from app.services.conversation_service import create_conversation,get_user_conversations,get_conversation

from app.models.user import User
from app.core.dependencies import get_current_user


router = APIRouter(prefix="/conversations",
                   tags=["Conversations"])

@router.post("/")
def create_conversation_endpoint(title:str,
                                 current_user:User = Depends(get_current_user),
                                 db:Session =Depends(get_db)):
    return create_conversation(db,current_user.id,title)

@router.get("/")
def get_conversations(current_user:User=Depends(get_current_user),
db:Session =Depends(get_db)):
    return get_user_conversations(db,current_user.id)

@router.get("/{conversation_id}")
def get_single_conversation(conversation_id: int,current_user:User = Depends(get_current_user),
db:Session = Depends(get_db)):

    conversation = get_conversation(db,conversation_id,current_user.id)
    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )
    return conversation
