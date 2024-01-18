# run.py

from app import app,db

# Aggiungi questa parte alla fine del tuo file run.py
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='5000')
