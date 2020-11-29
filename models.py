from peewee import *  #importation de l'ORM


# Connexion à la base de données
# et déclaration de l'instance nommée "db"
# db = MySQLDatabase('leonelal_devops', user='leonelal_devops', password='devopspassword', host='mysql-leonelal.alwaysdata.net', port=3306)
db = MySQLDatabase('devops_leonelaboss', user='root', password='root', host='10.44.250.26', port=3306)

class BaseModel(Model):
    """Class permettant de lié l'ORM à l'instance de la base de données

    """
    class Meta:
        database = db


class Data(BaseModel):
    """Class contenant le modèle de la table "measures"
    
    Parameters:
        Basemodel: prendre en compte la connexion avec la base de données
    """
    id = IntegerField(primary_key=True)
    unitNumber = IntegerField()
    robotNumber = IntegerField()
    robotType = CharField()
    tankTemp = FloatField()
    extTemp = FloatField()
    tankWeight = FloatField()
    productWeight = FloatField()
    ph = FloatField()
    kPlus = IntegerField()
    nacl = FloatField()
    salmonellaLevel = IntegerField()
    ecoliLevel = IntegerField()
    listeriaLevel = IntegerField()
    timeStamp = IntegerField()
    
    class Meta:
        """Class de liaison entre la table et le modèle
        """
        table_name = 'measures'




def values(unit, robot):
    """Fonction renvoyant les données de la table measures selon l'unité et l'automate

    Parameters:
        unit (int): numéro de l'unite
        robot (int): numéro de l'automate

    Returns:
        res (dictionnary): renvoi un dictionnaire avec les données pour être piloter facilement par le Javascript
    """

    db.connect() #ouvrir la connexion avec la base de données
    
    #Faire la requête pour récupérer les 60 dernière lignes contenant le bon numéro d'unité et d'automate
    data_list = Data.select().where((Data.unitNumber == unit) & (Data.robotNumber == robot)).limit(60)
    #initialisation du dictionnaire accueillant les données
    res = {
        "info": {
            "unit": 0,
            "robot": 0,
            "timestamp": 0,
        },
        "bar": {},
        "lines": {
            "nacl": [],
            "bacteria": {
                "salmonelle": [],
                "ecoli": [],
                "listeria": []
            }
        },
        "weight": {}
    }

    count = 1 #débuter le compteur à 1
    len_list = len(data_list) #récupérer la longeur de la liste
    for col in data_list:
        if count == len_list: #si on arrive à la dernière ligne on insère les données les plus récentes
            res['info']['unit'] = col.unitNumber
            res['info']['robot'] = col.robotNumber
            res['info']['timestamp'] = col.timeStamp
            res['bar'] = { "tempTank": col.tankTemp, "tempExt": col.extTemp, "ph": col.ph, "k": col.kPlus }
            res['weight'] = { "tank": col.tankWeight, "product": col.productWeight }
        res['lines']['nacl'].append(col.nacl)
        res['lines']['bacteria']['salmonelle'].append(col.salmonellaLevel)
        res['lines']['bacteria']['ecoli'].append(col.ecoliLevel)
        res['lines']['bacteria']['listeria'].append(col.listeriaLevel)
        count += 1
    db.close() #fermer la connexion à la base de données
    return res #retourner le dictionnaire

    





