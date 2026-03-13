from fastapi import FastAPI
from app.routers import building

app = FastAPI(title="Fire Protection Intelligence API")

app.include_router(building.router)

@app.get("/")
def root():
    return {"status": "ok"}