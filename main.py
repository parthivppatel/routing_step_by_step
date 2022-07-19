from fastapi import FastAPI
from database import Base,engine
import models.users as model
import models.projects as model

model.Base.metadata.create_all(bind=engine)
app=FastAPI()
