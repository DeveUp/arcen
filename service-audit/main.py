from fastapi import FastAPI
from src.route.Routes import routes

app = FastAPI()
app = routes
