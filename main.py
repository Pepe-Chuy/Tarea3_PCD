from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Optional
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    name: str = Field(min_length=1)
    user_id: int
    user_email: str = Field(min_length=1)
    age: Optional[int] = Field(gt = 1, lt = 99) , None
    recommendations: list[str] = Field(min_items=1)
    ZIP: Optional[int] = Field(ge=10000, le=99999), None

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/")
def create_user(user: User, db: Session = Depends(get_db)):

    query_user = db.query(models.User).filter(models.User.user_email == user.user_email).first()
    if query_user:
        raise HTTPException(status_code=400, detail="The email is already used")
    
    user_model = models.User()
    user_model.name = user.name
    user_model.user_id = user.user_id
    user_model.user_email = user.user_email
    user_model.age = user.age
    user_model.recommendations = user.recommendations
    user_model.ZIP = user.ZIP

    db.add(user_model)
    db.commit()

    return user

@app.get("/{user_id}")
def query_user(user_id: int, user: User, db: Session = Depends(get_db)):
    query_user = db.query(models.User).filter(models.User.user_id == user.user_id).first()

    if query_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {user_id} : Does not exist"
        )
    query_user.user_id = user_id
    query_user.name = user.name
    query_user.user_email = user.user_email
    query_user.age = user.age
    query_user.recommendations = user.recommendations
    query_user.ZIP = user.ZIP

    return query_user

@app.put("/{user_id}")
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):

    query_user = db.query(models.User).filter(models.User.user_id == user.user_id).first()

    if query_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {user_id} : Does not exist"
        )
    
    query_user.name = user.name
    query_user.user_email = user.user_email
    query_user.age = user.age
    query_user.recommendations = user.recommendations
    query_user.ZIP = user.ZIP

    db.add(query_user)
    db.commit()

    return user

@app.delete("/{user_id}")
def delete_user(user_id: int, user: User, db: Session = Depends(get_db)):
    query_user = db.query(models.User).filter(models.User.user_id == user.user_id).first()

    if query_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {user_id} : Does not exist"
        )
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()

    return f"user {user_id} deleted succesfully"

if __name__ == "__main__":
    uvicorn.run(app, port=4444)