from sqlalchemy import Column, Integer, String
from database import Base

class Project(Base):
   __tablename__="projects"

   id = Column(Integer, primary_key=True, index=True)
   name=Column(String)
   description=Column(String)
   start_date=Column(String)
   end_date=Column(String)
   tl_name=Column(String)

   