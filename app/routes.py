# app/routes.py

from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import get_jwt_identity
from werkzeug.utils import secure_filename
import os
from app import app, db
from app.models import User
from flask_jwt_extended import jwt_required
from app.security import analyze_image
from flask_cors import CORS

CORS(app)  # Aggiunge l'estensione CORS all'app Flask
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username e password sono richiesti'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username già in uso'}), 400

    new_user = User(username=username, password=generate_password_hash(password, method='scrypt'))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Utente registrato con successo'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Credenziali non valide'}), 401



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/images/upload', methods=['POST'])
@jwt_required()
def upload_image():
    current_user = get_jwt_identity()
    if 'image' not in request.files:
        return jsonify({'message': 'Nessun file trovato'}), 400
    
    image_file = request.files['image']

    if image_file.filename == '' or not allowed_file(image_file.filename):
        return jsonify({'message': 'Nome del file non valido o formato non supportato'}), 400

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        
    filename = secure_filename(image_file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Salva l'immagine
    image_file.save(filepath)

    return jsonify(analyze_image(filepath)),200

    

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({'message': e.description})
    response.content_type = 'application/json'
    return response

#route di prova per verificare il token
@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200