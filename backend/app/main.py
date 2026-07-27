from fastapi import FastAPI

from app.database.database import Base ,engine

from app.models.student import Student

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management System API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Student Management System API is running 🚀"
    }