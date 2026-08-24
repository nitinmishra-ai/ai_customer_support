from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate

def create_message(db:Session,
                   conversation_id:int,
                   message_data:MessageCreate):
    message = Message(conversation_id=conversation_id,
                      role=message_data.role,
                      content=message_data.content)
    db.add(message)
    db.commit()
    db.refresh(message)

    return message

def get_conversation_messages(db:Session,
                              conversation_id:int):

    messages= db.query(Message).filter(Message.conversation_id==conversation_id,).order_by(Message.created_at.asc()).all()

    return messages