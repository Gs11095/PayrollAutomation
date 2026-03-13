# Usa un'immagine Python ufficiale
FROM python:3.11-slim

# Setta la working directory dentro il container
WORKDIR /app

# Copia tutti i file del progetto dentro il container
COPY . /app

# Installa Flask
RUN pip install --no-cache-dir flask

# Espone la porta 5000 (quella che usa Flask)
EXPOSE 5000

# Comando per far partire l'app
CMD ["python", "app.py"]