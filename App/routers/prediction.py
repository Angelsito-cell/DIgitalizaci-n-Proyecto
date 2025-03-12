from fastapi import APIRouter
import pandas as pd
from sklearn.linear_model import LinearRegression

router = APIRouter(prefix="/prediction", tags=["Prediction"])

@router.get("/predict")
def predict_sales():
    data = pd.read_csv("sales.csv")
    model = LinearRegression()
    model.fit(data[['month']], data['sales'])
    prediction = model.predict([[12]])
    return {"predicted_sales": int(prediction[0])}
