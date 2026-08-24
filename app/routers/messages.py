from fastapi import APIRouter , Depends, HTTPException,status

from app.services.message_service import create_message,get_conversation_messages

from app.core.dependencies import get_current_user

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User
from app.models.conversation import Conversation

from app.schemas.message import MessageCreate, MessageResponse


router = APIRouter(prefix="/messages",
                   tags=["Messages"])

@router.post("/{conversation_id}/messages",
             response_model=MessageResponse)
def create_message_endpoint(conversation_id:int,
    message_data:MessageCreate,
    current_user:User = Depends(get_current_user),
    db:Session = Depends(get_db)
                            ):

    conversation = (db.query(Conversation).filter(Conversation.id== conversation_id,
    Conversation.user_id== current_user.id).first())

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="conversation not found"
        )
    return create_message(db,conversation_id,message_data)

@router.get("/{conversation_id}/messages")
def get_messages(
    conversation_id:int,
    current_user:User = Depends(get_current_user),
    db:Session = Depends(get_db)
):

    conversation= (db.query(Conversation).filter(Conversation.id== conversation_id,
    Conversation.user_id== current_user.id).first())

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )
    
    return get_conversation_messages(db,conversation_id)