import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# IMPORTACIÓN DE DATOS
bdd = pd.read_csv("wishlist.csv")

# Eliminamos NaN en la columna 'image' y renombramos la columna 'review/score'
bdd.dropna(subset=["image"], inplace=True)
bdd.rename(columns={'review/score': 'review'}, inplace=True)

# Convertimos la columna 'review' a tipo entero
bdd['review'] = bdd['review'].astype(int)

# PREPARACIÓN DE DATOS
print(bdd['review'].value_counts().sort_index())  # Verificación de valores
print(bdd.head())  # Visualización de los primeros datos

# Creación de la matriz item-usuario con los datos necesarios
item_user = bdd.pivot_table(index='Id', columns='User_id', values='review', fill_value=0)

# Almacenar información de imagen por cada 'Id'
images = bdd[['Id', 'image']].drop_duplicates().set_index('Id')

# CÁLCULO DE LA SIMILITUD DE ITEMS
similaridad = cosine_similarity(item_user.values)

# CREACIÓN DE LA MATRIZ DE RECOMENDACIONES
matriz_recomendaciones = pd.DataFrame(similaridad, index=item_user.index, columns=item_user.index)

# Conversión a formato largo y filtrado de duplicados
matriz_recomendaciones = (
    matriz_recomendaciones.stack()
    .reset_index()
    .rename(columns={0: 'similitud'})  # Renombrar la columna correctamente
    .query("id1 < id2")  # Evita duplicados y autocomparaciones
    .join(images, on='id2')  # Agrega información de imagen
)


# GUARDAR LA MATRIZ DE RECOMENDACIÓN
matriz_recomendaciones.to_pickle("matriz_recomendaciones.pkl") #se utilizan para guardar cookies scraping
