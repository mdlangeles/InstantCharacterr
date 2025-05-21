import streamlit as st
import os
import base64
from styles import aplicar_estilos

# Aplica estilos generales (si tienes algo definido en styles.py)
aplicar_estilos()

# 💜 CSS personalizado: centrar tabs, colores suaves, efecto hover
st.markdown("""
<style>
/* Centrar las tabs horizontalmente */
[data-testid="stTabs"] > div {
    justify-content: center;
}

/* Estilo base de las tabs */
[data-testid="stTab"] {
    background-color: #eef0fc;
    border-radius: 10px;
    margin: 0 5px;
    padding: 8px 16px;
    transition: all 0.3s ease;
    color: #3b3b98;
    font-weight: 500;
    font-size: 0.95rem;
}

/* Hover con animación */
[data-testid="stTab"]:hover {
    background-color: #dfe3fb;
    transform: scale(1.03);
}

/* Tab activa */
[data-testid="stTab"][aria-selected="true"] {
    background-color: #a29bfe;
    color: white;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("""
<h1 style='text-align: center; color: #3b3b98; font-size: 3rem; margin-top: 20px;'>
    Arquitectura Utilizada
</h1>
""", unsafe_allow_html=True)

# Imagen
ruta_imagen = os.path.join("data", "Arquitectura.png")
if os.path.isfile(ruta_imagen):
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin: 20px 0;">
    """, unsafe_allow_html=True)
    
    st.image(ruta_imagen, caption="Arquitectura Instant Character", use_container_width=False)
    
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.error("La imagen 'Arquitectura.png' no fue encontrada en la carpeta 'data'.")

# Subtítulo
st.markdown("""
<h2 style='text-align: center; font-size: 2.2rem; color: #3b3b98;'>
    Explicación de la Arquitectura
</h2>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Centrar los tabs y ajustar margen izquierdo */
    div[data-baseweb="tab-list"] {
        justify-content: center;
        margin-left: 1%;
    }

    /* Cambiar tamaño de la fuente en los tabs */
    button[data-baseweb="tab"] {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Tabs
tabs = st.tabs([
    "🔹 **Entrada de Datos**",
    "🔹 **Adaptador Visual**",
    "🔹 **Fusión Texto-Imagen**",
    "🔹 **Modelo Principal**",
    "🔹 **Entrenamiento**"
])

# 🌈 Estilo uniforme del contenido
tab_style = """
<div style="text-align: center; font-size: 1.2rem; line-height: 1.7; max-width: 900px; margin: auto;">
"""

# Contenido de cada tab
tab_style = "font-size: 1.2rem; line-height: 1.7; max-width: 900px; margin: auto; text-align: center;"

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

with tabs[0]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>1. Entrada de Datos (Data: Same Character Images)</b>
        </div>
    """, unsafe_allow_html=True)

    ruta_entrada = os.path.join("data", "Entrada.png")
    if os.path.isfile(ruta_entrada):
        img_base64 = image_to_base64(ruta_entrada)
        st.markdown(f"""
            <div style="text-align: center; margin-right: 0px;">
                <img src="{img_base64}" width="150" alt="Entrada de Datos">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("La imagen 'Entrada.png' no fue encontrada.")

    st.markdown(f"""
        <div style="{tab_style}">
            Se utilizan múltiples imágenes del mismo personaje en distintas posiciones o escenas.<br><br>
            Estas imágenes enseñan al modelo cómo se ve un personaje específico en diferentes contextos.
        </div>
    """, unsafe_allow_html=True)

        
with tabs[1]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>2. Adaptador Visual (Visual Adapter)</b>
        </div>
    """, unsafe_allow_html=True)

    ruta_adaptador = os.path.join("data", "Adaptador.png")
    if os.path.isfile(ruta_adaptador):
        img_base64 = image_to_base64(ruta_adaptador)
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{img_base64}" width="500" alt="Adaptador Visual">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("La imagen 'Adaptador.png' no fue encontrada.")

    st.markdown(f"""
        <div style="{tab_style}">
            Se seleccionan imágenes aleatorias del personaje, redimensionadas y recortadas.<br><br>
            Se procesan con un backbone visual como <b>Siglip</b> o <b>DinoV2</b>.<br><br>
            Dentro del Adaptador Visual:
            <ul style='text-align: left; max-width: 700px; margin: auto;'>
                <li>Transformers y MLPs procesan las representaciones.</li>
                <li>El <b>Time Resampler</b> unifica la secuencia temporal o espacial.</li>
                <li>Se combinan tokens: <code>cat</code>, <code>mean</code> y <code>linear</code>.</li>
            </ul>
            El objetivo es obtener una <b>representación unificada del personaje</b>.
        </div>
    """, unsafe_allow_html=True)

with tabs[2]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>3. Fusión Texto-Imagen (Cross Attention)</b>
        </div>
    """, unsafe_allow_html=True)

    ruta_fusion = os.path.join("data", "Fusion.png")
    if os.path.isfile(ruta_fusion):
        img_base64 = image_to_base64(ruta_fusion)
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{img_base64}" width="500" alt="Fusión Texto-Imagen">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("La imagen 'Fusion.png' no fue encontrada.")

    st.markdown(f"""
        <div style="{tab_style}">
            Se combinan los <b>embeddings visuales</b> con las descripciones textuales mediante <b>Cross Attention</b>.<br><br>
            Por ejemplo: <code>"a character is lying on beach"</code> se alinea con las features visuales del personaje.
        </div>
    """, unsafe_allow_html=True)


with tabs[3]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>4. Modelo Principal (Transformer)</b><br><br>
            Integra la info visual y textual en un Transformer.<br><br>
            Este modelo genera una <b>representación conjunta</b> que puede utilizarse para tareas como generación o edición de imágenes.
        </div>
    """, unsafe_allow_html=True)

with tabs[4]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>5. Entrenamiento (Training Stages)</b>
        </div>
    """, unsafe_allow_html=True)

    ruta_entrenamiento = os.path.join("data", "Entrenamiento.png")
    if os.path.isfile(ruta_entrenamiento):
        img_base64 = image_to_base64(ruta_entrenamiento)
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{img_base64}" width="900" alt="Entrenamiento">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("La imagen 'Entrenamiento.png' no fue encontrada.")

    st.markdown(f"""
        <div style="{tab_style}">
            El entrenamiento ocurre en tres etapas:
            <ul style='text-align: left; max-width: 700px; margin: auto; font-size: 1.1rem; line-height: 1.6;'>
                <li><b>Etapa 1:</b> Imágenes de baja resolución (single). El modelo aprende la identidad básica.</li>
                <li><b>Etapa 2:</b> Imágenes pareadas (paired) para capturar consistencia en expresiones y poses.</li>
                <li><b>Etapa 3:</b> Imágenes de alta resolución para mejorar fidelidad y detalles.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


