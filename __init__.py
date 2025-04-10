from cryptography.fernet import Fernet
from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Bienvenue sur le serveur de chiffrement !"

Génération d'une clé (pour test uniquement)
@app.route('/generate-key')
def generate_key():
    return Fernet.generate_key().decode()

Chiffrement avec clé personnalisée
@app.route('/encrypt/<key>/<valeur>')
def encrypt_valeur(key, valeur):

        f = Fernet(key.encode())
        token = f.encrypt(valeur.encode())
        return f"Token : {token.decode()}"


Déchiffrement avec clé personnalisée
@app.route('/decrypt/<key>/<path:token>')
def decrypt_valeur(key, token):

        f = Fernet(key.encode())
        valeur = f.decrypt(token.encode())
        return f"Valeur décryptée : {valeur.decode()}"
