"""
Módulo que define la interfaz Dibujable.

La interfaz Dibujable define los métodos que deben implementar los objetos que se pueden dibujar en un mapa.
"""
from abc import ABC, abstractmethod

class IDibujable(ABC):

    @abstractmethod
    def dibujar(self):
        """Dibuja el objeto en el mapa."""
        pass

    @abstractmethod
    def obtener_posicion(self) -> tuple[int, int]:
        """Devuelve la posición del objeto en el mapa."""
        pass

    @abstractmethod
    def mover(self, nueva_posicion: tuple[int, int]):
        """Mueve el objeto a una nueva posición en el mapa."""
        pass

    @abstractmethod
    def interactuar(self, otro: 'Dibujable'):
        """Interacción entre este objeto y otro en el mapa."""
        pass