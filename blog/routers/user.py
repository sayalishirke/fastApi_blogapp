from fastapi import APIRouter, Depends, status, HTTPException
from .. import  schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import uuid


router = APIRouter(
    prefix ="/user",
    tags=['Users'])
get_db=database.get_db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    hashPassword = pwd_context.hash(request.password)
    new_user = models.User(id=str(uuid.uuid4()),username=request.username, email=request.email, password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{email}', status_code=200, response_model=schemas.ShowUser)
def show(email: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f'Blog with id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with email {email} is not available')

    return user