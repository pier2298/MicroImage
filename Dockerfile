# Usa un'immagine base di Python
FROM python:3.11

# Imposta il lavoro di lavoro
WORKDIR /app

# Copia il codice sorgente nella directory di lavoro
COPY . /app

# Installa le dipendenze
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r requirements.txt

# Esporta la porta su cui l'app Flask sarà in ascolto
EXPOSE 5000

# Avvia l'app Flask
CMD ["python", "run.py"]
