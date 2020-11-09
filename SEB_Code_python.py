# Créez un script qui créeer un json et l'envoie au controlleur (envoie de données via les sockets dockers)
import json

response = {}

response["unite"] = 5
response["machine"] = "Lait"
response["content"] = 5.5

str_response = json.dumps(response)
print(str_response)

donnees = str_response
with open("C:/Users/Public/DevOps/devops/fichier.json", "w") as file:
    json.dump(donnees, file)

# Socket Python
