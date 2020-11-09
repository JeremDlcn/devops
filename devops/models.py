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



class Facility(BaseModel):
    id = IntegerField(primary_key=True)
    temperature = IntegerField()
    nbMachine = IntegerField()
    name = CharField()

    class Meta:
        table_name = 'automate'

def init_db():
	db.connect()

def value():
    print(Facility.select())

def close():
    db.close()