# MicroImage

## Descrizione: 
Microimage è un microservizio che data in input un immagine è in grado di rilevare se all'interno è presente un viso o meno, operante attraverso il micro-framework Flask, realizzato in Python e con l'ausilio di SQLite per la persistenza dei dati.
Microimage utilizza JWT (JSON Web Token) per effettuare l'autenticazione e consentire l'utilizzo del microservizio da parte dell'utente.
Sarà possibile utilizzare Microimage sia attraverso un container docker, sia attraverso un semplice VENV di python (Virtual Environments).

## Installazione: 

Questa versione di Microimage è stata sviluppata e testata sulla versione 3.11.0 di Python, quindi onde evitare errori di compatibilità si prega di utilizzare la stessa versione di Python

Usando VENV:
```
git clone https://github.com/pier2298/Microimage.git
cd Microimage
python -m venv venv

source venv/bin/activate  # per sistemi basati su Unix
.\venv\Scripts\activate  # per sistemi Windows

pip install -r requirements.txt
python run.py
```

Prima di procedere bisogna installare docker sul proprio sistema
Usando Docker:
```
git clone https://github.com/pier2298/Microimage.git
cd Microimage

# sostituire nome_immagine con il nome da dare al container
docker build -t nome_immagine .   
docker run -p 5000:5000 nome_immagine
```

Se l'installazione è andata a buon fine si visualizzerà una schermata simile alla seguente:

![Installazione andata a buon fine](/demo/ok.png)

Prendere nota dell'indirizzo da utilizzare per usufruire delle API.
I due indirizzi fanno riferimento rispettivamente all'indirizzo locale (localhost) , e all' indirizzo con il quale si può accedere esternamente all'interno della LAN. 
Inoltre l'api è stata anche testata esposta su Internet tramite Ngrok e utilizzando docker, con esito positivo.

## Utilizzo

Per utilizzare le api del microservizio è possibile utilizzare la piattaforma postman, oppure è possibile utilizzare l'interfaccia grafica progettata e sviluppata per l'utilizzo esclusivo di Microimage.

Le api vengono esposte nel seguente modo, ovviamente è necessario cambiare "endpoint.com" con il proprio indirizzo

```
http://endpoint.com/api/register
http://endpoint.com/api/login
http://endpoint.com/api/images/upload
```
