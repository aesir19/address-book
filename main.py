from fastapi import FastAPI
import uvicorn

import models
from data_store.db_config import engine
from routers import places

models.Base.metadata.create_all(engine)

app = FastAPI(title='Address Book')

app.include_router(places.router)

if __name__ =="__main__":
    uvicorn.run("main:app", host="localhost", reload=True)