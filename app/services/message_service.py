from sqlalchemy.orm import Session

from app.models.message import Message
from app.models.conversation import Conversation
from app.schemas.message import MessageCreate

def create_message(db:Session,
                   conversation_id:int,
                   user_id:int,
                   message_data:MessageCreate):
    conversation =(db.query(Conversation).filter(
    Conversation.id==conversation_id,
    Conversation.user_id== user_id).first())
    if not conversation:
        return None
    message = Message(conversation_id=conversation_id,
                      role=message_data.role,
                      content=message_data.content)
    db.add(message)
    db.commit()
    db.refresh(message)

    return message

def get_conversation_messages(db:Session,
                              conversation_id:int,
                              user_id:int):

    conversation = (db.query(Conversation).filter(Conversation.id==conversation_id,
    Conversation.user_id==user_id).first())

    if not conversation:
        return None

    messages= db.query(Message).filter(Message.conversation_id==conversation_id,).order_by(Message.created_at.asc()).all()

    return messages