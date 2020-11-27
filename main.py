# Importation des bibliothèques
from flask import Flask, render_template, url_for, request
import json

# importation de la fonction values de models
from models import values

#configuration de Flask
app = Flask(__name__)


# Routes
@app.route('/')
def dashboard():
    """Route d'accès au tableau de bord
    
    Returns:
        template index.html contenant la vue et gérer en Javascript
    """
    return render_template("index.html")



@app.route('/data')
def data():
    """Route de récupération des données pour le lancement du tableau de bord

    Returns:
        data (json): retourne un tableau contenant les données des 5 unités
    """
    data = []
    for i in range(1,6):
        data.append(values(i,1))
    return json.dumps(data)



@app.route('/robot')
def unit():
    """Route utilisé en Javascript permettant de récupérer les données d'un automate

    Parameters: (dans l'url)
        unit(int): le numéro de l'unité
        robot(int): le numéro de l'automate
    """

    #récupéraiton des paramètres en URL
    unit = request.args.get('unit') 
    robot = request.args.get('robot')

    #récupération des données, prise sur la fonction values du modèle
    data = values(unit, robot)
    return data



# Lancement de l'application sur le port 2900
if __name__ == "__main__":
    app.run(port=2900, debug=True)