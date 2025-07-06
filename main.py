import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Uid(BaseModel):
    uid: str


app = FastAPI()

data = []


@app.get("/arduino/data")
async def getdata():
    return data


@app.get("/arduino")
async def root():
    return {"message": "Hello World"}


@app.post("/arduino")
async def post(uid: Uid):
    data.append(uid)
    return uid


if __name__ == "__main__":
    uvicorn.run(app, port=59000)
