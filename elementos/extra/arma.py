from enum import Enum

class TipoArma(Enum):
    """
    Enumerado para los tipos de armas
    """
    FUEGO = "Arma de Fuego"
    CORTA_DISTANCIA = "Arma de corta distancia"
    LARGA_DISTANCIA = "Arma de larga distancia"

class Arma:
    """
    Representa un arma del juego
    """

    def __init__(self, nombre: str, daño: float, tipo: TipoArma, dueño: 'Personaje'):
        """
        Crea un arma con un nombre, daño, tipo, dueño y balas

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        tipo: TipoArma -- tipo del arma
        dueño: Personaje -- personaje dueño del arma
        """
        self._nombre = nombre
        self._daño = daño
        self._tipo = tipo
        self._dueño = dueño
        
        if TipoArma.FUEGO == tipo:
            self._balas = 10        # solo si es Arma de Fuego
        else:
            self._balas = 0


    def __str__(self):
        return f"Arma: {self._nombre} - Daño: {self._daño} - Tipo: {self._tipo}"
    
    # funcionalidad que comprueba si hay arma y dispara
    def dispara(self) -> bool:
        """
        Dispara el arma, si tiene balas. Si dispara, resta una bala.

        Returns:
        bool -- True si ha disparado, False en caso contrario
        """
        if self._balas > 0:
            print(f"{self._dueño.get_nombre()} ha disparado con el arma {self._nombre}")
            self._balas -= 1
            return True
        else:
            print(f"{self._dueño.get_nombre()} no tiene balas en el arma {self._nombre}")
            return False