from fastapi import FastAPI
from app.routers import building, fire_system

app = FastAPI(title="Fire Protection Intelligence API")

app.include_router(building.router)
app.include_router(fire_system.router)



@app.get("/")
def root():
    return {"message": "API running"}