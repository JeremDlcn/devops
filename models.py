from peewee import *


# instance de bdd
db = MySQLDatabase('leonelal_devops', user='leonelal_devops', password='devopspassword', host='mysql-leonelal.alwaysdata.net', port=3306)

class BaseModel(Model):
    """
    docstring
    """
    class Meta:
        database = db



class Unit(BaseModel):
    numero_unite = IntegerField(primary_key=True)
    nom_unite = CharField()

    class Meta:
        table_name = 'unites'
    def value():
        # only one row
        # d = Unit.get(Unit.numero_unite==2)
        # print(d.numero_unite, d.nom_unite)
        # multiple rows
        f = Unit.select()
        for cf in f:     
            print(cf.numero_unite, cf.nom_unite)
        return 2


class Data(BaseModel):
    """
    docstring
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
        table_name = 'measures'


# def init_db():
# 	db.connect()

# def close():
#     db.close()


def customValues(unit, robot):
    db.connect()
    data_list = Data.select().where((Data.unitNumber == unit) & (Data.robotNumber == robot)).limit(60)
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

    count = 1
    len_list = len(data_list)
    for col in data_list:
        if count == len_list:
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
    db.close()
    return res


# take all values for initialisation

# def initValues():
#     db.connect()

    # data = {
    #     "bar": {
    #         "tempTank": col.tempTank,
    #         "tempExt": col.tem,
    #         "ph": 7,
    #         "k": 40
    #     },
    #     "lines": {
    #         "nacl": [1.5, 1.9, 1.8, 2.0],
    #         "bacteria": {
    #             "salmonelle": [17.5, 22.5, 22.8, 19.0, 43.0, 22.8, 14.0],
    #             "ecoli": [21.2, 30.0, 18.8, 38.8, 23.9, 20.0, 16.0],
    #             "listeria": [16.0, 21.0, 19.5, 17.8, 20.2, 44.0, 20.2]
    #         }
    #     },
    #     "weight": {
    #         "tank": 2500,
    #         "product": 200
    #     }
    # }
    #
    #
    # lst.append(data)
    # db.close()
    # return lst
    





