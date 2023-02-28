from db import Base
from sqlalchemy import column, String, Integer


class User(Base):
    __tablename__ = 'users'

    id = column(Integer, primary_key=True)
    email = column(String, unique=True)
    username = column(String)
    password = column(String)
    
