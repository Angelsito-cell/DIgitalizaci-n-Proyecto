from statistics import LinearRegression
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime
from typing import Optional
import os

router = APIRouter(prefix="/prediction", tags=["Prediction"])

# Configuración
MODEL_DIR = Path("ml_models")
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "sales_model.joblib"

# Cargar modelo al inicio (si existe)
model = None
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)

@router.post("/train")
async def train_model(file: UploadFile = File(...)):
    try:
        data = pd.read_csv(file.file)
        if not all(col in data.columns for col in ['month', 'marketing_budget', 'sales']):
            raise HTTPException(status_code=400, detail="CSV debe contener columnas: month, marketing_budget, sales")
        
        global model
        model = LinearRegression()
        model.fit(data[['month', 'marketing_budget']], data['sales'])
        
        joblib.dump(model, MODEL_PATH)
        return {"message": "Modelo entrenado y guardado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al entrenar: {str(e)}")

@router.get("/predict")
def predict_sales(month: int, budget: float):
    if not model:
        raise HTTPException(status_code=400, detail="Modelo no entrenado. Sube datos primero.")
    try:
        prediction = model.predict([[month, budget]])
        return {"predicted_sales": round(float(prediction[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en predicción: {str(e)}")