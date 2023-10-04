from fastapi import FastAPI
import random

app = FastAPI()

# Función para generar datos aleatorios con nombres descriptivos
def generate_random_data():
    return {
        "temperatura": random.uniform(-10.0, 40.0),  # Ejemplo: Temperatura en grados Celsius
        "humedad": random.uniform(0.0, 100.0),  # Ejemplo: Humedad relativa en porcentaje
        "calidad_aire": random.choice(["Buena", "Moderada", "Mala"])  # Ejemplo: Calidad del aire
    }

# Ruta para generar un lote de 50 datos aleatorios
@app.get("/data")
async def generar_datos_aleatorios():
    datos_aleatorios = [generate_random_data() for _ in range(50)]
    return {"datos": datos_aleatorios}
