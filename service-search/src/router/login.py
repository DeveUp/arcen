from fastapi import FastAPI
import uvircorn

app = FastAPI()

@app.get("/")
def mensaje():
    return {"Hello":"World"}