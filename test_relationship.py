from app.db.database import sessionlocal

from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message

db = sessionlocal()

try:
    user = User(
        username ="testuser",
        email = "testuser@example.com",
        password_hash ="Hashed_password",
        role= "user"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print("user created", user.id)

finally:
    db.close()