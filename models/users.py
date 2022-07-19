from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    working_hours=Column(Integer)
    name=Column(String)
    phone_no=Column(String,unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin=Column(Boolean,default=False)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
