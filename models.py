from sqlalchemy import Column, Integer, String, JSON
from database import Base

class User(Base):
    __tablename__ = "users"

    name = Column(String)
    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, unique=True)
    age = Column(Integer, nullable=True)
    recommendations = Column(JSON) 
    ZIP = Column(Integer, nullable = True)
