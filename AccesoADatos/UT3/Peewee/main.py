from data_base import db
from ingesta import ingesta

from Modelos.Ubicaciones_Model import UbicacionModel
from Modelos.Personajes_Model import PersonajeModel
from Modelos.Enemigos_Model import EnemigoModel
from Modelos.Objetos_Model import ObjetoModel


from Repositorios.Ubicaciones import UbicacionRepository
# (añadirás aquí más repositorios después)

def main():
    # Conexión a la base de datos
    db.connect()

    ingesta(db)
    

    # Consultar por id
    ubicacion = UbicacionRepository.get_by_id(1)
    if ubicacion:
        print(f"Ubicación encontrada: {ubicacion.nombre}")
    else:
        print("No se encontró la ubicación con ID 1.")

    # Actualizar
    ubicacion = UbicacionRepository.get_by_id(3)
    print(f"Ubicación encontrada pre acta: {ubicacion.descripcion}")

    UbicacionRepository.update(3, {"descripcion": "Capital del reino"})
    ubicacion = UbicacionRepository.get_by_id(3)
    print(f"Ubicación actualizada: {ubicacion.descripcion}")

    # Eliminar
    UbicacionRepository.delete(3)
    print("Ubicación con ID 3 eliminada.\n")

    # Cerrar conexión
    db.close()
    print("Conexión cerrada correctamente.")

if __name__ == "__main__":
    main()
