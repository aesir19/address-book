from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import models
from data_store.db_config import engine, Base
from routers import places


app = FastAPI(title='Address Book')

Base.metadata.create_all(bind=engine)

app.include_router(places.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)
