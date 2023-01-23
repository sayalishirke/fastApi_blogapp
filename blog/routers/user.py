from fastapi import APIRouter, Depends, status, HTTPException
from .. import  schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix ="/user",
    tags=['Users'])
get_db=database.get_db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    hashPassword = pwd_context.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f'Blog with id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not available')

    return user