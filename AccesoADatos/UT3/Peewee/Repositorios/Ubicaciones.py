from peewee import *
from Modelos.Base_Model import BaseModel
from Modelos.Ubicaciones_Model import UbicacionModel

@staticmethod
def insertar_Ubicaciones(dicc):
    for data in dicc:
        UbicacionModel.create(**dicc)