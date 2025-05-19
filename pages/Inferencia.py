import streamlit as st
import replicate
import requests
from PIL import Image
from io import BytesIO
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN no está configurado en las variables de entorno.")

st.set_page_config(page_title="Generador estilo Ghibli", layout="centered")

st.title("Generador de Personajes Estilo Ghibli")

# Entrada del usuario
prompt = st.text_input("Escribe tu prompt:", value="a character in the library")

subject_image_url = st.text_input("URL de la imagen del personaje:", 
    value="https://replicate.delivery/pbxt/Mr9015ajTj5WrUEuW6YyWbxxRifCNCo0SbiA0L0F4vqjQmXS/face.png")


if st.button("Generar Imagen"):
    with st.spinner("Generando imagen..."):
        try:
            output = replicate.run(
                "tuannha/instant-character:df5eed34fa9c812acf62d3ca79874daf9b5e78c2bee11f4ada182a55dd5c1712",
                input={
                    "lora": "ghibli_style",
                    "width": 768,
                    "height": 1344,
                    "prompt": prompt,
                    "subject_image": subject_image_url
                }
            )


            if output:
                # Detectar si es string o lista
                image_url = output[0] if isinstance(output, list) else str(output).strip()

                # Verificamos que empiece con http (mínima validación)
                if image_url.startswith("http"):
                    response = requests.get(image_url)
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption="Imagen generada", use_container_width=True)
                else:
                    st.error(" La URL recibida no parece válida.")
            else:
                st.error("No se recibió ninguna imagen como respuesta.")

        except Exception as e:
            st.error(f"Error durante la inferencia:\n{e}")