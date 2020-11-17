import socket
import random
import json
import time
from datetime import datetime

hote = "localhost"
port = 2222

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":

    num_machine = 1

    # Random code generation
    for n in range(10):
        dt = int(time.time())
        num_auto = 1
        type_auto = num_machine
        temp_cuv = random.uniform(1, 10)
        personneDict = {"emp_details": [
            {"unite": num_auto, "machine": type_auto, "type_auto": temp_cuv}]}
        print(type(personneDict))
        with open("JSON_Files/paramunite_%d_%d_%d.json" % (num_auto, num_machine, dt), "w") as jsonFile:
            json.dump(personneDict, jsonFile)
        num_machine += 1
        msg_a_envoyer = str(personneDict)
        msg_a_envoyer = msg_a_envoyer.encode()
        connexion_avec_serveur.send(msg_a_envoyer)
        time.sleep(10)
    time.sleep(60)

print("Fermeture de la connexion")
connexion_avec_serveur.close()
