from peewee import *
from Modelos.Ubicaciones_Model import UbicacionModel


class UbicacionRepository:
    #Asignar campos de la tabla
    def asignarData(nom, des, type):
        return {"nombre":nom, "descripcion": des, "tipo":type}

    #CRUD
    @staticmethod
    def create(data):
        return UbicacionModel.create(**data)

    @staticmethod
    def get_by_id(id):
        return UbicacionModel.get_or_none(UbicacionModel.id_ubicacion == id)

    @staticmethod
    def update(id, data):
        query = UbicacionModel.update(**data).where(UbicacionModel.id_ubicacion == id)
        return query.execute()

    @staticmethod
    def delete(id):
        query = UbicacionModel.delete().where(UbicacionModel.id_ubicacion == id)
        return query.execute()

    #Metodos adicionales
    @staticmethod # Insercion Multiple, encapsular el metodo en with db.atomic():
    def insertar_ubicaciones(lista_dicc):
        # Opción 1: insertar uno a uno
        for data in lista_dicc:
            UbicacionModel.create(**data)
        # Opción 2 (más eficiente):
            # UbicacionModel.insert_many(lista_dicc).execute()