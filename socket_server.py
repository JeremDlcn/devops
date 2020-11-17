import socket
import select
import json
import csv
import os
import shutil
import time

hote = ''
port = 2222

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # We will check that new clients do not ask to connect
    # For this, we listen to the main_connection for reading
    # We wait a maximum of 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
                                                       [], [], 0.05)

    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # Add the connected socket to the list of clients
        clients_connectes.append(connexion_avec_client)

    # Now, we listen to the list of connected clients
    # The clients returned by select are those to be read (recv)
    # We wait there again 50ms maximum
    # We enclose the call to select.select in a try block
    # Indeed, if the list of connected clients is empty, an exception
    # Can be lifted
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                                                     [], [], 0.05)
    except select.error:
        pass
    else:
        # We go through the list of customers to read
        for client in clients_a_lire:
            # Client is socket type
            msg_recu = client.recv(1024)
            # May crash if message contains special characters
            msg_recu = msg_recu.decode()
            x = msg_recu.replace("'", "\"")
            y = json.loads(x)

            data_file = open('test.csv', 'w')
            csv_writer = csv.writer(y)
            count = 0
            for emp in employee_data:
                if count == 0:

                    # Writing headers of CSV file
                    header = emp.keys()
                    csv_writer.writerow(header)
                    count += 1

                # Writing data of CSV file
                csv_writer.writerow(emp.values())

            data_file.close()

            print(y["emp_details"])
            print(type(y))
            print(type(data))
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
