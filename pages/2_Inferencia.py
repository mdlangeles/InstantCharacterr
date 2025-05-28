import streamlit as st
import replicate
import requests
from PIL import Image
from io import BytesIO
import os
import base64
import time
from dotenv import load_dotenv



from styles import aplicar_estilos

aplicar_estilos()

load_dotenv()
# ============================

# Crear carpeta si no existe
if not os.path.exists("imagenes_generadas"):
    os.makedirs("imagenes_generadas")

# API Token
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    st.error("La variable de entorno REPLICATE_API_TOKEN no está configurada.")
    st.stop()

# Título y subtítulo
st.markdown("<h1>Generador de Personajes Estilo Animado</h1>", unsafe_allow_html=True)
st.markdown("<p>Convierte tu imagen en arte con el estilo de tus estudios favoritos</p>", unsafe_allow_html=True)

# Inputs
prompt = st.text_input("Describe tu idea:", value="a character in a forest")
estilo = st.selectbox("Selecciona un estilo:", options=["ghibli_style", "makoto_shinkai"])
uploaded_file = st.file_uploader("Sube la imagen del personaje (PNG o JPG)", type=["png", "jpg", "jpeg"])

# Botón y proceso
if st.button("Generar Imagen"):
    if uploaded_file:
        with st.spinner("Generando imagen, un momento..."):
            try:
                image = Image.open(uploaded_file).convert("RGB")
                image = image.resize((668, 768))
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
                data_url = f"data:image/png;base64,{base64_image}"

                output = None
                for intento in range(3):
                    try:
                        output = replicate.run(
                            "tuannha/instant-character:df5eed34fa9c812acf62d3ca79874daf9b5e78c2bee11f4ada182a55dd5c1712",
                            input={
                                "lora": estilo,
                                "width": 668,
                                "height": 768,
                                "prompt": prompt,
                                "subject_image": data_url
                            }
                        )
                        break
                    except Exception as e:
                        st.warning(f"Intento {intento+1} fallido: {e}")
                        time.sleep(2)

                if output:
                    url = output[0] if isinstance(output, list) else str(output).strip()
                    gen_response = requests.get(url, timeout=60)
                    gen_image = Image.open(BytesIO(gen_response.content))

                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(image, caption="Imagen de referencia", use_container_width=True)
                    with col2:
                        st.image(gen_image, caption=f"Estilo aplicado: {estilo}", use_container_width=True)

                    prompt_limpio = "".join(c for c in prompt if c.isalnum() or c in [' ', '-', '_']).replace(" ", "")[:50]
                    filename = f"imagenes_generadas/{prompt_limpio}_{estilo}.png"
                    gen_image.save(filename)
                    st.success("Imagen generada y guardada exitosamente.")

                else:
                    st.error("No se pudo generar la imagen tras varios intentos.")

            except Exception as e:
                st.error(f"Error al generar la imagen: {e}")
    else:
        st.warning("Por favor, sube una imagen primero.")
