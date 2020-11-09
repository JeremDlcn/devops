import random
# Créez un script qui créeer un json et l'envoie au controlleur (envoie de données via les sockets dockers)
import json
import time

response = {}

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

            response["unite"] = num_auto
            response["machine"] = type_auto
            response["content"] = temp_cuv

        str_response = json.dumps(response)

        count += 1
        donnees = str_response
        with open("fichier%d.json" % (count), "w") as file:
            json.dump(donnees, file)

        print(str_response)
        time.sleep(10)


# Création d'un json


# envoie automatique du json


# Socket Python
