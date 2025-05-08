from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, inventory, prediction
import logging
from .database import engine, Base
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart Inventory Manager API",
    description="API REST para gestión de inventario con IoT, nube y ML",
    version="1.0.0",
)

# Configurar CORS si es necesario
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware global de captura de errores
@app.middleware("http")
async def catch_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        # Loguear la excepción completa en consola
        logging.exception("Error en request %s %s", request.method, request.url)
        # Devolver detalle en JSON
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)}
        )

# Incluir routers
app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(prediction.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido al Smart Inventory Manager API"}
