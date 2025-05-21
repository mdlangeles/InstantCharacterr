import streamlit as st
import os
import base64
from styles import aplicar_estilos

st.set_page_config(page_title="Inicio", layout="wide")
aplicar_estilos()

# === Función para convertir imagen a base64 ===
def imagen_a_base64(path):
    with open(path, "rb") as f:
        datos = f.read()
    return base64.b64encode(datos).decode()

# === Rutas para la imagen destacada ===
BASE_PATH = "data/resultados/referencia_2"
NOMBRE_IMAGEN = "a_character_sitting_by_a_lake_autumn_leaves_falling_makoto_shinkai.png"
imagen_6_path = os.path.join(BASE_PATH, NOMBRE_IMAGEN)

# === Layout con dos columnas ===
col1, col2 = st.columns([3, 1])  # Más espacio para texto

# === Columna 1: Texto + imagen pequeña ===
with col1:
    if os.path.isfile(imagen_6_path):
        imagen_base64 = imagen_a_base64(imagen_6_path)
        html_content = f"""
        <div style="
            display: flex;
            background-color: #f9fafb;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            padding: 25px;
            color: #333333;
            line-height: 1.7;
            align-items: flex-start;
            gap: 20px;
            max-width: 100%;
        ">
            <div style="flex: 2; text-align: justify;">
                <h1 style="
                    font-size: 2.8rem;
                    text-align: center;
                    color: #3b3b98;
                    margin-bottom: 1.5rem;
                    margin-top: 0;
                    padding-left: 20%;
                ">Generador de Personajes Estilo Animado</h1>
                <p>
                    En esta plataforma puedes transformar imágenes comunes en <strong>personajes animados de alta calidad</strong>,
                    usando inteligencia artificial e inspiración estética de los grandes del cine animado japonés 🎌.<br><br>
                    Desde paisajes melancólicos al estilo <em>Makoto Shinkai</em>, hasta mundos encantadores como los de
                    <em>Studio Ghibli</em>, esta app te permite subir tu imagen, elegir un estilo visual y generar automáticamente
                    una versión artística de tu personaje o escena.<br><br>
                    Además, puedes ver ejemplos generados por otros usuarios, comparar estilos y usar descripciones personalizadas
                    (prompts) para influir en el resultado final. Ideal para ilustradores, creadores de contenido, fans del anime
                    o simplemente personas curiosas con ganas de explorar la magia del arte asistido por IA.
                </p>
            </div>
            <div style="flex: 1; display: flex; justify-content: center; align-items: flex-end; padding-top: 180px;">
                <img src="data:image/png;base64,{imagen_base64}" 
                     alt="Imagen 6" 
                     style="width: 280px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
            </div>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.warning("No se encontró la imagen especificada.")

# === Columna 2: Guía de navegación ===
with col2:
    st.markdown("""
    <style>
    .guia {
        background-color: #f1f5f9;
        border-left: 6px solid #6366f1;
        padding: 1.2rem;
        border-radius: 12px;
        margin-top: 2rem;
        animation: fadeIn 1.2s ease-in-out;
    }
    .guia h3 {
        color: #4338ca;
        margin-bottom: 1rem;
    }
    .guia ul {
        list-style-type: none;
        padding-left: 0;
    }
    .guia li {
        margin-bottom: 0.8rem;
        line-height: 1.6;
    }
    .guia li span {
        font-weight: bold;
        color: #111827;
    }
    </style>

    <div class='guia'>
        <h3>¿Cómo navegar en esta app?</h3>
        <ul>
            <li><span>Arquitectura:</span> En la barra lateral encontrarás la arquitectura interna del modelo, explicando cómo pasa de imagen + texto a ilustración mágica ✨.</li>
            <li><span>Inferencia:</span> Aquí puedes subir tu imagen, escribir un prompt y seleccionar el estilo deseado. Al hacer clic en "Generar", el modelo procesará tu creación en segundos.</li>
            <li><span>Galería:</span> Visualiza los resultados generados por otros usuarios. Inspírate, admira y encuentra nuevas ideas para tu próximo personaje.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === SECCIÓN DE EJEMPLOS ===
st.subheader("✨ Algunos Ejemplos de lo que puedes crear")

REFERENCIA_PATH = "data"
RESULTADOS_PATH = os.path.join(REFERENCIA_PATH, "resultados")

referencias = [f for f in os.listdir(REFERENCIA_PATH)
               if os.path.isfile(os.path.join(REFERENCIA_PATH, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

imagenes_ejemplo = []

for ref in referencias:
    nombre_ref = os.path.splitext(ref)[0]
    carpeta_resultados = os.path.join(RESULTADOS_PATH, nombre_ref)

    if not os.path.exists(carpeta_resultados):
        continue

    imagenes_generadas = [f for f in os.listdir(carpeta_resultados)
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for imagen in imagenes_generadas:
        img_path = os.path.join(carpeta_resultados, imagen)

        nombre_archivo = os.path.splitext(imagen)[0]
        partes = nombre_archivo.split("_")
        if len(partes) >= 3:
            estilo = " ".join(partes[-2:])
            prompt = " ".join(partes[:-2])
        else:
            estilo = "Desconocido"
            prompt = nombre_archivo

        imagenes_ejemplo.append((img_path, prompt, estilo))

# Limitar a los primeros 5 ejemplos
imagenes_ejemplo = imagenes_ejemplo[:5]

if imagenes_ejemplo:
    cols = st.columns(5)
    for idx, (img_path, prompt, estilo) in enumerate(imagenes_ejemplo):
        with cols[idx % 5]:
            st.image(img_path, use_container_width=True)
            st.markdown(f"""
                <div style='text-align: center; font-size: 14px; margin-top: 8px'>
                    <strong>Prompt:</strong><br> {prompt}<br>
                    <strong>Estilo:</strong><br> <span style='color:#4A90E2'>{estilo}</span>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("Aún no hay ejemplos generados. ¡Sé el primero en crear magia! 🪄")
