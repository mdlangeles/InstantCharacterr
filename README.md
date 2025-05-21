<<<<<<< HEAD
#  InstantCharacter - Implementación sencilla

![InstantCharacter](data/Image_1_readme.png)
=======
# 🎭 InstantCharacter - Implementación sencilla
>>>>>>> d521a818fed16f0ab9826d9c11417842ba950c5d

Este proyecto es una **implementación simplificada** del artículo _"InstantCharacter: Personaliza cualquier personaje con un marco transformador de difusión escalable"_, utilizando **Streamlit** para la inferencia visual y **Docker** para su despliegue local en un entorno completamente aislado.

La aplicación permite cargar una imagen de referencia y una instrucción textual para generar una nueva imagen personalizada del personaje.

---

## 🧠 ¿Qué hace InstantCharacter?

**InstantCharacter** es un modelo generativo basado en **Diffusion Transformers (DiT)**, que permite:

- Capturar la **identidad visual** de un personaje desde una sola imagen.
- Aplicar esa identidad a nuevos escenarios, acciones, poses o estilos.
- Mantener **consistencia visual**, estilo y control desde texto.
- Generar imágenes de alta calidad sin necesidad de reentrenamiento por personaje.

---

## 🧠 Resumen teórico y arquitectura

- El modelo reemplaza la clásica arquitectura **U-Net** con un **transformador de difusión (DiT)** para mayor capacidad y flexibilidad.
- Integra un **adaptador escalable**, compuesto por transformadores apilados, que refina progresivamente las características del personaje.
- Emplea atención cruzada (Q, K, V) para fusionar la imagen de referencia con el texto durante la generación.
- Se separa la **identidad del personaje** del **contenido generado**, permitiendo una personalización precisa sin ajustes costosos.
- Este enfoque logra resultados de **alta fidelidad y control textual**, incluso con personajes no vistos en el entrenamiento.

---

## 🚀 Ejecución con Docker (recomendado)

<<<<<<< HEAD
Install Python : [Python Downloads](https://www.python.org/downloads/)   
=======
Install Python : [Python Downloads](https://www.python.org/downloads/)  
Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)  
>>>>>>> d521a818fed16f0ab9826d9c11417842ba950c5d

Antes de ejecutar la aplicación, es **necesario obtener un token API** para el servicio:

1. Ve a la página:  
   [https://internal.replicate.com/tuannha/instant-character](https://internal.replicate.com/tuannha/instant-character)  
2. Inicia sesión y genera tu **API token** en la sección correspondiente.

3. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (reemplaza `tu_token_aqui` con tu token real):

```env
REPLICATE_API_TOKEN=tu_token_aqui
```

No necesitas lanzar Streamlit manualmente ni activar un entorno virtual. Todo se gestiona automáticamente desde Docker.
Pero si es de tu preferencia puedes crear el entorno virtual con el comando 

```bash
python -m venv venv
```

Activar entorno virtual
**En Windows:**
```bash
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

### 🐳 Paso a paso:
<<<<<<< HEAD
=======
(Recuerda tener Docker Desktop abierto en una ventana)
>>>>>>> d521a818fed16f0ab9826d9c11417842ba950c5d

1. **Construye la imagen:**

```bash
docker build -t instant-character-app .
```

2. **Ejecuta el contenedor:**

```bash
docker run -p 8501:8501 instant-character-app
```

3. **Abre tu navegador en:**  
👉 `http://localhost:8501`

---

4. **Usa la app:**

   - Escoge uno de los estilos disponibles: **Makoto** o **Ghibli**.
   - Sube una imagen del personaje que quieres personalizar.
   - Escribe un *prompt* con la situación o escenario en el que quieres ver a tu personaje  
     *(por ejemplo: `"en una biblioteca"` o `"tocando el piano"`)*.


## 📁 Estructura del proyecto

```
InstantCharacter/
│
<<<<<<< HEAD
├── data/                         # Carpeta para datos de entrada
├── imagenes_generadas/          # Carpeta donde se guardan las imágenes generadas
│
├── pages/                        # Scripts para navegación en múltiples vistas de Streamlit
│   ├── 1_Arquitectura.py         # Explicación visual de la arquitectura
│   ├── 2_Inferencia.py           # Lógica de inferencia y generación de imágenes
│   └── 3_Galeria.py              # Galería de imágenes generadas
│
├── venv/                         # Entorno virtual (no se versiona normalmente)
│
├── .env                          # Variables de entorno
├── .gitignore                    # Archivos/Carpetas ignoradas por Git
├── Dockerfile                    # Configuración para contenedor Docker
├── Inicio.py                     # Punto de entrada principal de la app Streamlit
├── README.md                     # Documentación del proyecto
├── requirements.txt              # Lista de dependencias del proyecto
└── styles.py                     # Archivo con estilos CSS personalizados

=======
├── InstantCharacter/
│   ├── app.py             # Código principal de la app Streamlit
│   └── output.png         # Imagen de ejemplo generada
│
├── .gitignore
├── requirements.txt       # Dependencias del proyecto
├── Dockerfile             # Dockerfile para despliegue
└── README.md
>>>>>>> d521a818fed16f0ab9826d9c11417842ba950c5d
```

---

## 👩‍💻 Autoras del proyecto

Este proyecto fue desarrollado por:

- **María de los Ángeles Amú Moreno**
- **Manuela Mayorga Rojas**
- **Mariana Mera Gutierrez**

Como parte de una implementación práctica del artículo _"InstantCharacter"_ enfocada en la fase de inferencia y visualización con herramientas accesibles.

---

## 📚 Referencia

📄 Tao, J., Zhang, Y., Wang, Q., et al. (2024). *InstantCharacter: Personaliza cualquier personaje con un marco transformador de difusión escalable*.  
🔗 [Repositorio oficial del paper](https://github.com/Tencent/InstantCharacter)

<<<<<<< HEAD
Si tienes alguna duda no dudes en contactarnos ✨
=======
Si tienes alguna duda no dudes en contactarnos ✨
>>>>>>> d521a818fed16f0ab9826d9c11417842ba950c5d
