from peewee import *
from Base_Model import BaseModel

from Personajes_Model import PersonajeModel
from Objetos_Model import ObjetoModel

class EnemigoObjetoModel(BaseModel):
    id_personaje = ForeignKeyField(PersonajeModel, backref='objeto_de_enemigo', on_delete='CASCADE')
    id_objeto = ForeignKeyField(ObjetoModel, backref='ubicacion_objeto', on_delete='CASCADE')
    cantidad = FloatField(default=1, null=True)
