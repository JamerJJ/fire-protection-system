from fastapi import FastAPI

app = FastAPI(title="Fire Protection Intelligence API")

@app.get("/health")
def health():
    return {"status": "ok"}