from graficos.dibujable import IDibujable

class Objeto(IDibujable):
    
    def __init__(self, nombre: str, descripcion: str, x: int, y: int):
        """
        Crea un objeto con un nombre y una descripción

        Parámetros:
        nombre: str -- nombre del objeto
        descripcion: str -- descripción
        x: int -- posición x en el mapa
        y: int -- posición y en el mapa
        """
        self._nombre: str = nombre
        self._descripcion: str = descripcion
        self._x: int = x
        self._y: int = y

    def __str__(self):
        """
        Devuelve el objeto en formato string
        """
        return f"{self._nombre}: {self._descripcion}"
    

    # Métodos de la interfaz Dibujable
    def dibujar(self):
        """
        Dibuja el objeto en el mapa.
        """
        print(f"Dibujando {self._nombre} en la posición ({self._x}, {self._y})")

    def obtener_posicion(self) -> tuple[int, int]:
        """
        Devuelve la posición del objeto en el mapa.
        """
        return self._x, self._y
    
    def mover(self, nueva_posicion: tuple[int, int]):
        """
        Un objeto no se mueve.

        Parámetros:
        nueva_posicion: tuple[int, int] -- nueva posición del objeto
        """
        return
    
    def interactuar(self, otro: 'IDibujable'):
        """
        Un objeto no interactúa con otros dibujables.
        """
        return