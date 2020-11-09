import random
# Créez un script qui créeer un json et l'envoie au controlleur (envoie de données via les sockets dockers)
import json

response = {}

# Créez un script qui créer un json et l'envoie au controlleur (envoie de données via les sockets dockers)

# Génération  de code aléatoire

# def random_json() :

numéro_unité = 1

for n in range(10):
    num_auto = random.randint(1, 10)
    type_auto = random.randint(1, 10)
    temp_cuv = random.randint(1, 10)
    print(numéro_unité)
    print(num_auto, type_auto, temp_cuv)


# Création d'un json


# envoie automatique du json
response["unite"] = 5
response["machine"] = "Lait"
response["content"] = 5.5

str_response = json.dumps(response)
print(str_response)

donnees = str_response
with open("C:/Users/Public/DevOps/devops/fichier.json", "w") as file:
    json.dump(donnees, file)

# Socket Python
