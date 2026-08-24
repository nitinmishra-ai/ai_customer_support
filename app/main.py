from fastapi import FastAPI

from app.routers.health import router as health_router
from app.core.config import settings
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.conversations import router as conversation_router
from app.routers.messages import router as message_router
app = FastAPI(title=settings.app_name,
              version="1.0.0",
              description="AI-powered customer support system")


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(conversation_router)
app.include_router(message_router)

