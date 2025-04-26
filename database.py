import os

from dotenv import load_dotenv
from sqlmodel import SQLModel,create_engine,Session
from .models import Item
load_dotenv()

#Step 1: Create a SQLAlchemy engine
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
   DATABASE_URL, connect_args={"check_same_thread":False}
)
SQLModel.metadata.create_all(engine)


#Dependency
def get_db():
    with Session(engine) as session:
        yield session