from fastapi import  FastAPI
from app.api.cData import cData
app=FastAPI()

app.include_router(cData)
