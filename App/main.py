from fastapi import FastAPI
from .routers import auth, inventory, prediction

app = FastAPI()

app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(prediction.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Smart Inventory Manager API"}
