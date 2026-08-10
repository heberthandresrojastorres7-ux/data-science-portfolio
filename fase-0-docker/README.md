\# Imagen base oficial de Python

FROM python:3.11-slim



\# Directorio de trabajo dentro del contenedor

WORKDIR /app



\# Copiar el script al contenedor

COPY hola\_docker.py .



\# Comando por defecto al ejecutar el contenedor

CMD \["python", "hola\_docker.py"]

