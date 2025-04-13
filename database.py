from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://todo_backend_postgres_user:RjZpTQtSnuJy1wmalFni7qWATfH0964E@dpg-cvnthq9r0fns73ehbdj0-a.singapore-postgres.render.com/todo_backend_postgres"
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
