from peewee import *
from Base_Model import BaseModel

class UbicacionModel(BaseModel):
    id_ubicacion = AutoField()
    nombre = TextField(null=False)
    descripcion = TextField(null=True)
    tipo = TextField(null=True)
    