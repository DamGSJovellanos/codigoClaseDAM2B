from peewee import Model
from data_base import db  # Importas la conexión

class BaseModel(Model):
    """Modelo base para todos los modelos"""
    class Meta:
        database = db 