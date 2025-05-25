from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://todo_fastapi_rd7q_user:SDgliZ5mv4fITkOMvX2tBj6hDlUlCb17@dpg-d0pcmh0dl3ps73alhhjg-a.singapore-postgres.render.com/todo_fastapi_rd7q"
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
