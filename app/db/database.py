from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.database_url,pool_pre_ping=True)

Sessionlocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit= False
)

def get_db():
    db = Sessionlocal()

    try:
        yield db
    finally:
        db.close()


