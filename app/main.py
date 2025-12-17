from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Toan lop 3 API",
    description="API for Toan lop 3 application",
    version="1.0.0",
    root_path="/math/api/",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Toan lop 3 API!"}