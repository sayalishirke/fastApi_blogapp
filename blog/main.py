from fastapi import FastAPI
from . import  schemas, models
from .database import engine
from .routers import blog, user, authentication, files

app = FastAPI( 
)

models.Base.metadata.create_all(engine) # create all models

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(files.router)


# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create(request:schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body =request.body, user_id=2)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
# def all( db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs'])
# def show_blogs(id: int,response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"details": f'Blog with id {id} is not available'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')

#     return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def destroy(id:int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return "done"

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update_blog(id:int, request:schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
#     blog.update(request)
#     db.commit()
#     return 'updated'
   

# @app.post('/user', response_model=schemas.ShowUser, tags=['Users'])
# def create_user(request:schemas.User, db: Session = Depends(get_db)):
#     hashPassword = pwd_context.hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password=hashPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', status_code=200, response_model=schemas.ShowUser, tags=['Users'])
# def show(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"details": f'Blog with id {id} is not available'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not available')

#     return user