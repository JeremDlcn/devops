import random
import json
import time

# Créez un script qui créer un json et l'envoie au controlleur (envoie de données via les sockets dockers)

# Génération  de code aléatoire

# def random_json() :
count = 0
numéro_unité = 1
while True:
    for n in range(10):
         num_auto = random.randint(1, 10)
         type_auto = random.randint(1, 10)
         temp_cuv = random.uniform(1, 10)
         print(numéro_unité)
         print(num_auto, type_auto, temp_cuv)
         
    personneDict = {"emp_details": [{ "unite": num_auto, "machine":type_auto, "type_auto": type_auto }]}
    count += 1
    with open("JSON_Files/fichier%d.json" % (count), "w") as jsonFile:
        json.dump(personneDict, jsonFile)

    time.sleep(10)


# Création d'un json
"""
response["unite"] = num_auto
response["machine"] = type_auto
response["type_auto"] = type_auto
str_response = json.dumps(response)
count += 1
donnees = str_response
with open("JSON_Files/fichier%d.json" % (count), "w") as file:
    json.dump(donnees, file)
print(str_response)
"""

# envoie automatique du json

# Socket Python
