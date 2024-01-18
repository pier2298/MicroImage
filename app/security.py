
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2

def analyze_image(image_path):
    try:
        # Carica l'immagine con OpenCV
        img = cv2.imread(image_path)

        # Converti l'immagine in scala di grigi (il riconoscimento facciale funziona meglio su immagini in scala di grigi)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Utilizza il classificatore Haar per il riconoscimento facciale
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            return "Volto rilevato nell'immagine"

        return "Sembrerebbero non esserci volti nell'immagine"  # Nessun problema rilevato

    except Exception as e:
        return f"Errore durante l'analisi dell'immagine: {str(e)}"