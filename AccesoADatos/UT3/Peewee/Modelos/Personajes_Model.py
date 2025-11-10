from peewee import *
from .Base_Model import BaseModel
from .Ubicaciones_Model import UbicacionModel

class PersonajeModel(BaseModel):
    id_personaje = AutoField()
    nombre = TextField(null=False)
    descripcion = TextField(null=True)
    id_ubicacion = ForeignKeyField(UbicacionModel, backref='ubicacion_personaje', null=True)
    da_objeto = BooleanField(default=False)  # True o False
    rol = TextField(null=True)

