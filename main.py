from fastapi import FastAPI

app = FastAPI()

@app.get('/')   # Route for fast api
def index():
    return {"data": {"name": "Sayali"}}

@app.get('/about') # Route for fast api
def about():
    return {"data": "About page"}