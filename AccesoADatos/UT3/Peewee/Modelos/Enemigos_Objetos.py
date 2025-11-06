from peewee import *
from Base_Model import BaseModel

from Enemigos import Enemigo
from Objetos import Objeto

class Enemigo_Objeto(BaseModel):
    id_enemigo = ForeignKeyField(Enemigo, backref='objeto_de_enemigo')
    id_objeto = ForeignKeyField(Objeto, backref='ubicacion_objeto')
    probabilidad = FloatField(default=1.0, null=False)

