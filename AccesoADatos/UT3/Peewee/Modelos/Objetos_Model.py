from peewee import *
from .Base_Model import BaseModel

from .Ubicaciones_Model import UbicacionModel
from .Personajes_Model import PersonajeModel
from .Enemigos_Model import EnemigoModel

class ObjetoModel(BaseModel):
    id_objeto = AutoField()
    nombre = TextField(null=False)
    descripcion = TextField(null=True)
    rareza = TextField(null=True, default="comun",constraints=[Check("rareza IN ('comun', 'raro', 'epico', 'legendario')")])
    id_ubicacion = ForeignKeyField(UbicacionModel, backref='ubicacion_objeto', null=True)
    id_personaje_dropea = ForeignKeyField(PersonajeModel, backref='personaje_dropea', null=True)
    id_enemigo_dropea = ForeignKeyField(EnemigoModel, backref='enemigo_dropea', null=True)

