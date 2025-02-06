import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar variables de entorno (crea un archivo .env)
load_dotenv()

# Simulación de datos para ML
data = {
    'month': [1, 2, 3, 4, 5],
    'sales': [200, 300, 400, 350, 500]
}
df = pd.DataFrame(data)

# Modelo de ML
model = LinearRegression()
model.fit(df[['month']], df['sales'])
prediction = model.predict([[8]])

print(f"Predicción para el mes 6: {prediction[0]:.0f} unidades")