import sys
print(sys.path)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, inventory, prediction
app = FastAPI(
    title="Smart Inventory API",
    description="API para gestión de inventario inteligente",
    version="1.0.0"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(prediction.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido al Smart Inventory Manager"}