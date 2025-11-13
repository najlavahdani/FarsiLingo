from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .core.database import get_db

app = FastAPI()

@app.get("/")
def test_connection(db: Session = Depends(get_db)):
    return {"message": "Database connected successfully!"}
