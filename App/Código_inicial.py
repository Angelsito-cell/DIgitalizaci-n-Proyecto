import os
import boto3
import jwt
import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración AWS
AWS_ACCESS_KEY = os.getenv('ABC1')
AWS_SECRET_KEY = os.getenv('ABC12')
S3_BUCKET = os.getenv('Angelsito-cell')
JWT_SECRET = os.getenv('A12346536')

def authenticate(user_id):
    """Genera un token de autenticación JWT."""
    payload = {
        'exp': datetime.utcnow() + timedelta(hours=1),
        'user_id': user_id
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def scan_product(product_id):
    """Simula el escaneo de un producto y lo sube a AWS S3."""
    if not product_id.isalnum():
        raise ValueError("ID de producto inválido")
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    data = f"{datetime.now().isoformat()} - Producto: {product_id}\n"
    filename = f'scans/{product_id}_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
    
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=data,
        ServerSideEncryption='AES256'
    )
    return {"status": "success", "product_id": product_id, "file": filename}

def train_demand_model(csv_file='sales.csv'):
    """Entrena un modelo de regresión lineal para predecir la demanda."""
    data = pd.read_csv(csv_file)
    X = data[['month', 'marketing_budget']]
    y = data['sales']
    
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_sales(model, month, budget):
    """Predice las ventas con el modelo entrenado."""
    prediction = model.predict([[month, budget]])
    return round(prediction[0], 2)

if __name__ == "__main__":
    user_token = authenticate("admin_123")
    print(f"Token de acceso: {user_token}")
    
    product_scan = scan_product("P-2024-XYZ")
    print(f"Escaneo completado: {product_scan}")
    
    model = train_demand_model()
    prediction = predict_sales(model, 12, 5000)
    print(f"Predicción de ventas: {prediction} unidades")
