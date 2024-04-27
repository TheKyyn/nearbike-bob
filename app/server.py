from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

#on stock dans le cache les données et le timestamp de la dernière màj
cache = {
    'data': None,
    'last_updated': 0
}

def fetch_data():
    """ Récupère les données de l'API et les met en cache """
    response = requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=')
    cache['data'] = response.json()
    cache['last_updated'] = time.time()

@app.route('/data')
def data():
    #vérif des 5 minutes pour le refresh du cache
    if time.time() - cache['last_updated'] > 300:
        fetch_data()
    return jsonify(cache['data'])

@app.route('/')
def index():
    return "Le serveur Bob marche bien. Bob."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
