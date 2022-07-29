from fastapi import FastAPI,HTTPException,Depends
from database import Base,engine,get_db
import models.users as model
import models.projects as model
from requests import Session, session
import schemas,crud
from typing import List
from models.users import User
from datetime import datetime
from sqlalchemy import func

model.Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user) 


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/date_filter")
def filters(db:session=Depends(get_db)):
    tempDate=datetime.strptime(
    "2022-07-28",
    "%Y-%m-%d")
    print(type(tempDate))

    tempList=[]
    dbquery=db.query(User).all()
    print(len(dbquery))
    for i in dbquery:
        if(datetime.strptime(str(i.dt.date()),"%Y-%m-%d")==tempDate):
            tempList.append(i)
    return(tempList)
