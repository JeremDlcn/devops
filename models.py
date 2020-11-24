from peewee import *


# instance de bdd
db = MySQLDatabase('leonelal_devops', user='leonelal_devops', password='devopspassword', host='mysql-leonelal.alwaysdata.net', port=3306)
# db = MySQLDatabase('devops_leonelaboss', user='root', password='root', host='10.44.250.24', port=3306)

class BaseModel(Model):
    """
    docstring
    """
    class Meta:
        database = db


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




def values(unit, robot):
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

    





