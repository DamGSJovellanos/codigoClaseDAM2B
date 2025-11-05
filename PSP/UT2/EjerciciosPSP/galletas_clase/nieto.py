from threading import Condition
import time

class Nieto:
    def __init__(self, tiempo_galleta,limite_hambre, tiempo_descanso, mesa):
        self.tiempo_galleta = tiempo_galleta #tiempo en comer la galleta
        self.limite_hambre = limite_hambre
        self.tiempo_descanso = tiempo_descanso #descanso entre galltas a partir de limite_hambre
        self.mesa = mesa
        self.contador_galletas = 0
    
    def comer_galletas(self):
        while True:
            print(f"El nieto {self} quiere comer galletas")
            while self.mesa.condition:
                while self.mesa.galletas <= 0:
                    self.mesa.condition.wait()
                self.mesa.coger_galleta()
                print(f"El nieto {self} ha cogido galleta")
                self.contador_galletas += 1
                self.mesa.condition.notify_all()
            
            print(f"El nieto {self} se esta comiendo la galleta")
            time.time(self.tiempo_galleta)

            if self.contador_galletas > self.limite_hambre:
                print(f"El nieto tiene mas de {self.limite_hambre} y esta descansando {self.tiempo_descanso}")
                time.time(self.tiempo_descanso)


