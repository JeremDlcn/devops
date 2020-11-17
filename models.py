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
    ID = IntegerField(primary_key=True, column_name='id')
    TimeStamp = IntegerField(column_name='horaire')
    TankTemp = FloatField(column_name='temperature_cuve')
    extTemp = FloatField(column_name='temperature_exterieure')
    tankWeight = FloatField(column_name='poids_lait_cuve')
    productWeight = FloatField(column_name='poids_final')
    phLevel = FloatField(column_name='mesure_pH')
    kplusLevel = IntegerField(column_name='mesure_Kplus')
    naclConcentration = FloatField(column_name='concentration_NaCl')
    salmonellLevel = IntegerField(column_name='niveau_bacterie_salmonelle')
    ecoliLevel = IntegerField(column_name='niveau_bacterie_Ecoli')
    listeriaLevel = IntegerField(column_name='niveau_bacterie_listeria')
    
    class Meta:
        table_name = 'donnees'


def init_db():
	db.connect()

def values():
    f = Data.select()
    for cf in f:     
        print(cf.ID, cf.extTemp, cf.naclConcentration)

def close():
    db.close()



