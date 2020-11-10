from peewee import *
from .views import app


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


def init_db():
	db.connect()

def value():
    # only one row
    # d = Unit.get(Unit.numero_unite==2)
    # print(d.numero_unite, d.nom_unite)
    # multiple rows
    f = Unit.select()
    for cf in f:     
        print(cf.numero_unite, cf.nom_unite)

def close():
    db.close()