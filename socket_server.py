import socket
import select
import json
import csv
import os
import shutil
import time
import mysql.connector


hote = ''
port = 2222

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
                                                       [], [], 0.05)

    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)

    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                                                     [], [], 0.05)
    except select.error:
        pass
    else:
        # We go through the list of customers to read
        for client in clients_a_lire:
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            print(msg_recu)
            mydict = json.loads(json.dumps(eval(msg_recu)))

            columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())            
            conn = mysql.connector.connect( 
                host="mysql-leonelal.alwaysdata.net",
                user="leonelal_devops", 
                password="devopspassword",
                database="leonelal_devops"
            )
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO resultats( %s ) VALUES ( %s );""" % (columns, values))
            conn.commit()
            # Close the connection
            conn.close()
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
