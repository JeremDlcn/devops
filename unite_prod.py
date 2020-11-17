import random
import json
import time
from datetime import datetime

# Créez un script qui créer un json et l'envoie au controlleur (envoie de données via les sockets dockers)


def random_json(numero_unite):
    num_machine = 1
    # Génération  de code aléatoire
    for n in range(10):
        dt = int(time.time())
        num_auto = numero_unite
        type_auto = num_machine
        temp_cuv = random.uniform(1, 10)
        personneDict = {"emp_details": [
            {"unite": num_auto, "machine": type_auto, "type_auto": temp_cuv}]}
        with open("JSON_Files/paramunite_%d_%d_%d.json" % (numero_unite, num_machine, dt), "w") as jsonFile:
            json.dump(personneDict, jsonFile)
        num_machine += 1
    return("Exports reussis")


for x in range(1, 6):
    random_json(x)

# Création d'un json

# envoie automatique du json

# Socket Python
