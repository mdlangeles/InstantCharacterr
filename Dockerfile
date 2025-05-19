# Usa una imagen base ligera con Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto por defecto de Streamlit
EXPOSE 8501

# Comando para correr la app principal
CMD ["streamlit", "run", "Inicio.py", "--server.port=8501", "--server.address=0.0.0.0"]
