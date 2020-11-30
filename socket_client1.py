import socket
import random
import json
import time
from datetime import datetime

hote = "10.44.250.26"
port = 2222
#Socket launch
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":

    num_machine = 1

    # Random data generation
    for n in range(10):
        num_auto = 1 #Unit number
        num_machine = num_machine
        type_machine = "0X0000BA20"
        temp_cuv = random.uniform(2.5, 4)
        temp_ext = random.uniform(8, 14)
        poids_cuv = random.randint(3512, 4607)
        poids_cuv2 = random.randint(3512, 4607)
        poids_final = (poids_cuv + poids_cuv2) / 2
        ph = random.uniform(6.8, 7.2)
        kPlus = random.randint(35, 47)
        NaCI = random.uniform(1, 1.7)
        salmonelle = random.randint(17, 37)
        ecoli = random.randint(35, 49)
        listeria = random.randint(28, 54)
        dt = int(time.time())
        #Data dictionnary creation
        personneDict ={ "unitNumber": num_auto,
                    "robotNumber": num_machine,
                    "robotType": type_machine,
                    "tankTemp": temp_cuv,
                    "extTemp": temp_ext,
                    "tankWeight": poids_cuv,
                    "productWeight": poids_final,
                    "ph": ph,
                    "kPlus": kPlus,
                    "nacl": NaCI,
                    "salmonellaLevel": salmonelle,
                    "ecoliLevel": ecoli,
                    "listeriaLevel": listeria,
                    "timeStamp": dt}
        print(personneDict)
        #JSON file creation
        with open("JSON_Files/paramunite_%d_%d_%d.json" % (num_auto, num_machine, dt), "w") as jsonFile:
            json.dump(personneDict, jsonFile)
        num_machine += 1
        #Modify and send data via socket
        msg_a_envoyer = str(personneDict)
        msg_a_envoyer = msg_a_envoyer.encode()
        connexion_avec_serveur.send(msg_a_envoyer)
        time.sleep(0.5)
    #Loop send data   
    time.sleep(60)
print("Fermeture de la connexion")
connexion_avec_serveur.close()