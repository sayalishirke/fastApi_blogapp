from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

#("/")-> path , get -> operation on path, index() -> path operation function, @app -> path operation function decorater
@app.get('/')           # Route for fast api  
def index():
    return {"data": 'blog list'}

@app.get('/blog')          
def blog(limit = 10, published: bool=True, sort: Optional[str]=None):
    if published:
        return {"data": f'{limit} published blogs from blog list'}
    else:
        return {"data": f'{limit} blogs from blog list'}

# execute code line by line hence not reaching, write it before dynamic route
@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished"}

# type conversion and validation done by pydantic
@app.get('/blog/{id}')      #  {id} dynamic routing, id-> path parameter
def about(id:int):          #  accept it in function, default is string convert it to int
    return {"data": id}




@app.get('/blog/{id}/comments') 
def comments(id,limit=10):
    return {"data":{'1','2'} }


class Blog(BaseModel):
    # id: int
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {"data": f"blog created with {request.title}"}


