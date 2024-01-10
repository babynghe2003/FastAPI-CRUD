from fastapi import FastAPI
from .db import init_db_connection

from .routers import users

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    db, mongo_client = init_db_connection()
    app.mongo_client = mongo_client
    app.mongodb = db

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongo_client.close()

@app.get("/")
async def root():
    return {"message": f"Hello World"}

app.include_router(users.router, prefix="/users", tags=["users"])
