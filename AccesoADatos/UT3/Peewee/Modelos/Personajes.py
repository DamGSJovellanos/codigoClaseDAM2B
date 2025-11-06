from peewee import *
from Base_Model import BaseModel

from Ubicaciones import Ubicacion

class Personaje(BaseModel):
    id_personaje = AutoField()
    nombre = TextField(null=False)
    descripcion = TextField(null=True)
    id_ubicacion = ForeignKeyField(Ubicacion, backref='ubicacion_personaje')
    da_objeto = BooleanField(null=False, default=False)  # True o False
    rol = TextField(null=True)

