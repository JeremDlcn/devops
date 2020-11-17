import socket

hote = "localhost"
port = 2222

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    # May crash if you type special characters
    msg_a_envoyer = msg_a_envoyer.encode()
    # We send the message
    connexion_serveur.send(msg_a_envoyer)

print("Fermeture de la connexion")
connexion_serveur.close()
