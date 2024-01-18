# MicroImage

## Descrizione: 
Microimage è un microservizio operante attraverso il micro-framework Flask, realizzato in Python e con l'ausilio di SQLite per la persistenza dei dati.
Sarà possibile utilizzare Microimage sia attraverso un container docker, sia attraverso un semplice VENV di python (Virtual Environments).

## Installazione: 

Questa versione di Microimage è stata sviluppata e testata sulla versione 3.11.0 di Python, quindi onde evitare errori di compatibilità si prega di utilizzare la stessa versione di Python

Usando VENV:
```
git clone https://github.com/pier2298/Microimage.git
cd Microimage
python -m venv venv
source venv/bin/activate  # per sistemi basati su Unix
# o
.\venv\Scripts\activate  # per sistemi Windows

pip install -r requirements.txt
python run.py
```

Prima di procedere bisogna installare docker sul proprio sistema
Usando Docker:
```
git clone https://github.com/pier2298/Microimage.git
cd Microimage
docker build -t nome_immagine .
docker run -p 5000:5000 nome_immagine
```

## Utilizzo

