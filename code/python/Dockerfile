# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación
COPY main.py .
COPY test_calculator.py .

# Comando por defecto para ejecutar la calculadora
CMD ["python", "main.py"]
