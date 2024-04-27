# Serveur Bob

## Description
Serveur Bob est un service Flask conçu pour récupérer et mettre en cache les données de disponibilité des Vélibs à Paris via l'API Open Data de Paris. Ce serveur agit comme un intermédiaire entre l'API externe et le Serveur Alice, fournissant les données nécessaires sans surcharger l'API externe.

## Fonctionnalités
- Récupération des données de l'API Open Data de Paris
- Mise en cache des données pour minimiser les requêtes à l'API
- Fourniture des données au Serveur Alice via une API interne

## Technologies Utilisées
- Flask
- Requests pour les requêtes HTTP

## Installation

### Prérequis
- Python 3
- pip

### Configuration de l'environnement
```bash
# Création d'un environnement virtuel
python -m venv venv
```

# Activation de l'environnement virtuel
```bash
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate  # Sur Windows
```

# Installation des dépendances
```bash
pip install -r requirements.txt
```
# Lancement de l'application
```bash
# Lancement du serveur
flask run --port=5001
```
### Usage

Le serveur fonctionne en arrière-plan et répond aux requêtes de données venant du Serveur Alice. Il n'est pas destiné à être utilisé directement par les utilisateurs finaux.

### Contribution

Les contributions sont encouragées pour améliorer la fonctionnalité ou la performance du serveur. Veuillez suivre les normes de développement Flask pour proposer des changements.

### Licence

Ce projet est distribué sous une licence open source, permettant sa libre utilisation et modification.

