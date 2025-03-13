import streamlit as st
import requests

def get_recommendations(product_id, num_recommendations=5):
    url = f"http://127.0.0.1:8000/recomendaciones/{product_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        recommendations = response.json()
        return recommendations[:num_recommendations]  # Tomar solo los primeros 5 productos
    except requests.exceptions.RequestException as e:
        st.error(f"Error en la llamada a la API: {e}")
        return []
#product id en imput y guardar
# Información del producto principal
product_id = 230
product_name = "Harry Potter and The Sorcerer's Stone"
product_image = "https://img-9gag-fun.9cache.com/photo/a0R8EbQ_460s.jpg"
product_description = "Descripción del producto va aquí. Este texto puede ser una descripción más detallada del producto."
product_price = "$39.99"

# Mostrar producto principal
st.title(product_name)
st.image(product_image, width=200)
st.write(product_description)
st.subheader(f"Precio: {product_price}")

# Obtener y mostrar productos recomendados
st.subheader("Productos recomendados")
recommended_products = get_recommendations(product_id)

if recommended_products:
    cols = st.columns(len(recommended_products))
    for i, product in enumerate(recommended_products):
        with cols[i]:
            st.image(product["image"], width=100)
            st.write(f"Similitud: {product['similitud']:.2f}")
            st.link_button("Ver producto", url=f"https://tusitio.com/product/{product['id2']}")
else:
    st.write("No hay recomendaciones disponibles.")