from fastapi import APIRouter, FastAPI

from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])


app = FastAPI()
app.include_router(api_router) 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}