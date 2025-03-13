
from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

# Carga la matriz de recomendaciones del disco
matriz_recomendaciones = pd.read_pickle("matriz_creada.pkl")

@api.get("/recomendaciones/{id_item}")
async def hacer_recomendacion(id_item: int, n: int = 5):
    # Verifica que el item exista en la matriz
    if id_item in matriz_recomendaciones['id1'].unique():
        # Filtra donde 'id1' sea igual al item proporcionado
        recomendaciones = matriz_recomendaciones[matriz_recomendaciones['id1'] == id_item]
        
        # Ordena por similitud de manera descendente y selecciona los primeros n resultados
        recomendaciones = recomendaciones.sort_values(by='similitud', ascending=False).head(n)
        
        return recomendaciones.to_dict(orient="records")
    else:
        raise HTTPException(status_code=404, detail=f"Error: El ID {id_item} no se encuentra en las columnas del DataFrame.")

#uvicorn mini_api:api --reload
#streamlit run web_demo.py

"""añadir un sidebar con submenús, meter stats, graficos de columnas generales, totales, columnas
genero, autores...
"""