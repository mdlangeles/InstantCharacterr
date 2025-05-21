import streamlit as st
import os
from styles import aplicar_estilos

aplicar_estilos()
# ============================

st.markdown("<h1>Galería de Imágenes</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# === SECCIÓN 1: Comparación ===
st.subheader("Comparación: Imagen de Referencia vs Generadas")

REFERENCIA_PATH = "data"
RESULTADOS_PATH = os.path.join(REFERENCIA_PATH, "resultados")

referencias = [f for f in os.listdir(REFERENCIA_PATH)
               if os.path.isfile(os.path.join(REFERENCIA_PATH, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for ref in referencias:
    nombre_ref = os.path.splitext(ref)[0]
    carpeta_resultados = os.path.join(RESULTADOS_PATH, nombre_ref)

    if not os.path.exists(carpeta_resultados):
        continue

    imagenes_generadas = [f for f in os.listdir(carpeta_resultados)
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    total_columnas = 1 + len(imagenes_generadas)
    columnas = st.columns(total_columnas)

    # Imagen de referencia
    with columnas[0]:
        st.image(os.path.join(REFERENCIA_PATH, ref), caption="Referencia", use_container_width=True)

    # Imágenes generadas
    for i, imagen in enumerate(imagenes_generadas):
        img_path = os.path.join(carpeta_resultados, imagen)
        prompt = os.path.splitext(imagen)[0].replace("_", " ")
        with columnas[i + 1]:
            st.image(img_path, caption=f"Prompt: {prompt}", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# === SECCIÓN 2: Últimas generadas ===
st.subheader("Tus Últimas Creaciones")

ruta_generadas = "imagenes_generadas"

if not os.path.exists(ruta_generadas):
    os.makedirs(ruta_generadas)

archivos = sorted(os.listdir(ruta_generadas), reverse=True)

if archivos:
    cols = st.columns(4)

    for i, archivo in enumerate(archivos[:12]):
        if archivo.endswith(".png"):
            ruta_imagen = os.path.join(ruta_generadas, archivo)
            estilo = archivo.split("_")[-2] if "_" in archivo else archivo.replace(".png", "")
            with cols[i % 4]:
                st.image(ruta_imagen, use_container_width=True)
                st.markdown(f"<p class='stMarkdown'>Estilo: {estilo}</p>", unsafe_allow_html=True)
else:
    st.info("Aún no hay imágenes generadas.")
