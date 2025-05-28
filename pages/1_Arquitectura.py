import streamlit as st
import os
import base64
from PIL import Image
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
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Imagen
ruta_imagen = os.path.join("data", "arq.jpg")
if os.path.isfile(ruta_imagen):
    img_base64 = image_to_base64(ruta_imagen)
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="data:image/jpg;base64,{img_base64}" 
                 style="width: 1000px; height: 500px; object-fit: fill; border-radius: 12px;" 
                 alt="Arquitectura Instant Character">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("La imagen 'arq.jpg' no fue encontrada en la carpeta 'data'.")






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
    " **1. Entrada de Datos**",
    " **2. Adaptador Visual**",
    " **3. Fusión Texto-Imagen**",
    " **Mecanismo de Atención**"
])

#  Estilo uniforme del contenido
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
            <b>Entrada de Datos</b>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])  # puedes ajustar las proporciones si quieres

    with col1:
        ruta_entrada = os.path.join("data", "random.jpg")
        if os.path.isfile(ruta_entrada):
            img_base64 = image_to_base64(ruta_entrada)
            st.markdown(f"""
                <div style="text-align: center;">
                    <img src="{img_base64}" width="400" alt="Entrada de Datos">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("La imagen 'Entrada.png' no fue encontrada.")

    with col2:
        st.markdown(f"""
        <div style="{tab_style} text-align: justify;">
            Se seleccionan aleatoriamente varias imágenes del mismo personaje y se procesan para que el sistema pueda aprender su identidad visual.<br><br>
            <b>Pasos clave:</b><br>
            <b><i>1. Random Select:</i></b> selecciona al azar varias imágenes del mismo personaje.<br>
            <b><i>2. Resize + Crop:</i></b> normaliza el tamaño y encuadre para procesarlas mejor.<br><br>
             <b><i>Objetivo:</i></b> “dame lo esencial de cómo luce este personaje en distintas posturas/ángulos”.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        
with tabs[1]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>Adaptador Visual (Visual Adapter)</b>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: justify; margin-top: 15px;">
            Este es el corazón del sistema. Aquí se extraen y refinan las características del personaje para proyectarlas al modelo base (DiT).
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        ruta_adaptador = os.path.join("data", "adaptadorr.jpg")
        if os.path.isfile(ruta_adaptador):
            img_base64 = image_to_base64(ruta_adaptador)
            st.markdown(f"""
                <div style="text-align: center; margin-top: 20px;">
                    <img src="{img_base64}" width="600" alt="Adaptador Visual">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("La imagen 'adaptadorr.jpg' no fue encontrada en la carpeta 'data'.")

    with col2:
        st.markdown(f"""
    <div style="{tab_style}; font-size: 16px; line-height: 1.6;">
    
    <p style="margin-bottom: 20px; text-align: justify;"><b> Subcomponentes:</b></p>

    <p style="text-align: justify;"><b> a. SigLIP y DINOv2</b><br>
    &nbsp;&nbsp;&nbsp;• Dos encoders preentrenados que extraen características del personaje.<br>
    &nbsp;&nbsp;&nbsp;• <b>SigLIP:</b> entiende la relación imagen-texto.<br>
    &nbsp;&nbsp;&nbsp;• <b>DINOv2:</b> extrae información visual de bajo y alto nivel (textura, silueta, pose).<br>
    &nbsp;&nbsp;&nbsp;• Ambos outputs se concatenan (<code>cat channel</code>) = representación rica del personaje.</p>

    <p style="text-align: justify;"><b> b. MLP y Transformer (Intermedios)</b><br>
    &nbsp;&nbsp;&nbsp;• Procesan jerárquicamente las características visuales.<br>
    &nbsp;&nbsp;&nbsp;• Aplican un <i>Time Resampler</i>, que permite ubicar al personaje en el tiempo del proceso de difusión (como si fuera un paso dentro de la generación de imagen).</p>


    </div>
    """, unsafe_allow_html=True)


with tabs[2]:
    st.markdown(f"""
        <div style="{tab_style}">
            <b>Fusión Texto-Imagen (Cross Attention)</b>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        ruta_fusion = os.path.join("data", "fusionn.jpg")
        if os.path.isfile(ruta_fusion):
            img_base64 = image_to_base64(ruta_fusion)
            st.markdown(f"""
                <div style="text-align: center; margin-top: 20px;">
                    <img src="{img_base64}" width="600" alt="Fusión Texto-Imagen">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("La imagen 'fusionn.jpg' no fue encontrada.")

    with col2:
        st.markdown(f"""
    <div style="{tab_style}; font-size: 16px; line-height: 1.6;">

    <p style="margin-bottom: 20px; text-align: justify;">
        <b>Este bloque representa al modelo generador principal (Diffusion Transformer).</b>
    </p>

    <p style="margin-bottom: 20px; text-align: justify;">
        <b>Cross Attention:</b><br>
        &nbsp;&nbsp;&nbsp;Le dice al modelo “esto es cómo se ve el personaje, y esto es lo que debe estar haciendo según el texto.”
    </p>

    <p style="margin-bottom: 20px; text-align: justify;">
        &nbsp;&nbsp;&nbsp;● Cada bloque azul es una capa Transformer.<br>
        &nbsp;&nbsp;&nbsp;● El texto es embebido con una capa de Text Embedding.<br>
        &nbsp;&nbsp;&nbsp;● El personaje (ya representado visualmente) y el texto interactúan mediante atención cruzada para generar la imagen final.
    </p>

    <p style="margin-bottom: 5px; text-align: justify;">
        <b>Ejemplo textual:</b> “a character is lying on beach”
    </p>
    <p style="text-align: justify;">
        ➡ El modelo fusiona esa instrucción con la identidad visual para generar una imagen coherente y modificada.
    </p>

    </div>
    """, unsafe_allow_html=True)




with tabs[3]:
    st.markdown(f'<h3 style="text-align: center;">Atención Cruzada</h3>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        img = Image.open("data/tensor.png")
        st.image(img, width=1200)

    col1, col2 = st.columns(2)

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
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

with col1:
    st.markdown("""
    <div class="guia" style="font-size:16px; line-height:1.6; text-align: justify; padding-right:15px;">
        <h3>¿Qué hace?</h3>
        <p style="margin-bottom: 15px; text-align: justify;">
            Usa los vectores <b>Q (Query)</b>, <b>K (Key)</b> y <b>V (Value)</b> para combinar texto e imagen de manera inteligente.
        </p>
        <h3>Creación de tensores Q, K y V:</h3>
        <p style="margin-bottom: 15px; text-align: justify;">
            Los tensores <b>Q (Query)</b>, <b>K (Key)</b> y <b>V (Value)</b> se generan a partir de las representaciones embebidas del texto y la imagen. 
            El texto se convierte en vectores a través de una capa de embedding que captura la semántica de la instrucción. 
            La imagen, por otro lado, se procesa mediante encoders visuales que extraen características espaciales y temporales del personaje o la escena.
        </p>
        <h3>Manejo de relaciones espaciales y temporales:</h3>
        <p style="margin-bottom: 15px; text-align: justify;">
            La arquitectura Scalable Diffusion Transformer, a través de su mecanismo de atención, modela explícitamente las relaciones espaciales y temporales dentro de la imagen. 
            Esto se logra utilizando las posiciones relativas de los píxeles o tokens visuales y temporalizando la atención para capturar cómo el personaje evoluciona o se sitúa en el tiempo durante el proceso de difusión. 
            Así, el modelo entiende qué partes de la imagen deben modificarse o mantenerse coherentes a lo largo de la generación o edición.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="guia" style="font-size:16px; line-height:1.6; text-align: justify; padding-left:15px;">
        <h3>¿De dónde viene cada uno?</h3>
        <ul>
            <li><span>Q (Query):</span> Viene del texto, es la consulta que representa la instrucción o lo que quieres que pase en la imagen (ejemplo: “el personaje está en la nieve”).</li>
            <li><span>K (Key):</span> Viene de la imagen, es la información visual que describe el personaje (pose, color, ropa, etc).</li>
            <li><span>V (Value):</span> También viene de la imagen, pero contiene la esencia visual a aplicar, es decir, lo que realmente se va a modificar o mantener.</li>
        </ul>
        <h3>¿Cómo funciona?</h3>
        <p style="margin-bottom: 15px; text-align: justify;">
            El modelo “pregunta” con <b>Q</b> al conjunto de claves <b>K</b> para identificar qué partes visuales son relevantes según el texto, y luego usa <b>V</b> para generar o modificar la imagen respetando esa interacción.
        </p>
        <h3>¿Qué aprende?</h3>
        <p style="margin-bottom: 15px; text-align: justify;">
            Aprende a “atender” solo a las partes del texto que deben cambiar la imagen y cómo aplicar esos cambios de forma visual coherente, respetando la identidad previa del personaje.
        </p>
    </div>
    """, unsafe_allow_html=True)















