from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///inventory.db"

engine = create_engine(
    DATABASE_URL,
    echo=True  #  shows SQL queries in terminal
)

SessionLocal = sessionmaker(bind=engine)
