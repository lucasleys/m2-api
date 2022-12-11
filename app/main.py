from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddlewares
import pymongo

app = FastAPI()

origins = [
     "http://localhost",
     "http://localhost:8080",
     "https://localhost.tiangolo.com",
     "http://127.0.0.1:5500",
     "http://milestone2.local:30001"
 ]

app.add_middleware(
    CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )


myclient = pymongo.MongoClient("mongodb://root:test123@192.168.56.5:27017/")

mydb = myclient["user"]
mycol = mydb["collection"]

for i in mycol.find_one():
    if i == "name":
        retrieved_user = mycol.find_one()['name']





@app.get("/user")
async def get_user():
    return {"name": retrieved_user}