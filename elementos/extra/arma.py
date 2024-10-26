from enum import Enum
from abc import ABC, abstractmethod

from elementos.errores.errores import ArmaError, ArmaVaciaError


class TipoArma(Enum):
    """
    Enumerado para los tipos de armas
    """
    FUEGO = "Arma de fuego"
    CORTA_DISTANCIA = "Arma de corta distancia"
    LARGA_DISTANCIA = "Arma de larga distancia"

class Arma(ABC):
    """
    Representa una clase abstracta para las armas del juego
    """

    def __init__(self, nombre: str, tipo: TipoArma, dueño: 'Personaje'):
        """
        Crea un arma con un nombre, daño, tipo, y dueño.

        Parámetros:
        nombre: str -- nombre del arma
        tipo: TipoArma -- tipo del arma
        dueño: Personaje -- personaje dueño del arma
        """
        self._nombre = nombre
        self._tipo = tipo
        self._dueño = dueño
        self._daño = None  # depende del tipo de arma que se instancie (subclase)
        self._nivel = 1

    def get_nombre(self) -> str:
        """
        Devuelve el nombre del arma

        Returns:
        str -- nombre del arma
        """
        return self._nombre
    
    def get_daño(self) -> float:
        """
        Devuelve el daño del arma

        Returns:
        float -- daño del arma
        """
        return self._daño
    
    def get_tipo(self) -> TipoArma:
        """
        Devuelve el tipo del arma

        Returns:
        TipoArma -- tipo del arma
        """
        return self._tipo
    
    def get_dueño(self) -> 'Personaje':
        """
        Devuelve el dueño del arma

        Returns:
        Personaje -- personaje dueño del arma
        """
        return self._dueño

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del arma
        """
        return f"Arma: {self._nombre} - Daño: {self._daño} - Tipo: {self._tipo.name} - Nivel: {self._nivel}"
    
    
    @abstractmethod
    def usar(self, objetivo: 'Personaje') -> bool:      # CADA ARMA SE USA DE UNA MANERA DIFERENTE
        """
        Usa el arma contra un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo
        """
        pass

    @abstractmethod
    def mejorar(self):                           # CADA ARMA SE MEJORA DE UNA MANERA DIFERENTE
        """
        Mejora el arma
        """
        pass


class ArmaLarga(Arma):
    """
    Representa un arma de larga distancia
    """

    def __init__(self, nombre: str, dueño: 'Personaje'):
        """
        Crea un arma de larga distancia

        Parámetros:
        nombre: str -- nombre del arma
        dueño: Personaje -- personaje dueño del arma
        """
        super().__init__(nombre,TipoArma.LARGA_DISTANCIA, dueño)
        self._daño = 30     # ocultación

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        print(f"{self._dueño.get_nombre()} ataca a {objetivo.get_nombre()} con {self._nombre}")
        objetivo.recibe_daño(self._daño)
        return True

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 10
        self._nivel += 1
        print(f"{self._nombre} ha sido mejorada a nivel {self._nivel}")


class ArmaCorta(Arma):
    """
    Representa un arma de corta distancia
    """

    def __init__(self, nombre: str, dueño: 'Personaje', estocadas: int):
        """
        Crea un arma de corta distancia

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        dueño: Personaje -- personaje dueño del arma
        estocada: int -- número de estocadas por uso
        """
        super().__init__(nombre, TipoArma.CORTA_DISTANCIA, dueño)
        self._daño = 10  # ocultación
        self._estocadas = estocadas

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        print(f"{self._dueño.get_nombre()} ataca con {self._estocadas} estocadas a {objetivo.get_nombre()} con {self._nombre}")
        for _ in range(self._estocadas):
            objetivo.recibe_daño(self._daño)
        return True

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 5
        self._estocadas += 1
        self._nivel += 1
        print(f"{self._nombre} ha sido mejorada a nivel {self._nivel}")
    
    def __str__(self):  # SOBREESCRITURA DE MÉTODO (extensión)
        """
        Devuelve una representación en forma de cadena del arma
        """
        return super().__str__() + f" - Estocadas: {self._estocadas}"
        
class ArmaFuego(Arma):
    """
    Representa un arma de fuego
    """

    def __init__(self, nombre: str, dueño: 'Personaje', balas: int):
        """
        Crea un arma de fuego

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        dueño: Personaje -- personaje dueño del arma
        balas: int -- número de balas
        """
        super().__init__(nombre, TipoArma.FUEGO, dueño)
        self._daño = 40   # ocultación
        self._balas = balas  # nuevo atributo

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        if self._balas > 0:
            objetivo.recibe_daño(self._daño)
            self._balas -= 1
            return True
        else:
            raise ArmaVaciaError(dueño=self.get_dueño(), arma=self)
            return False # esto vuelve?

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 20
        self._nivel += 1
        print(f"{self._nombre} ha sido mejorada a nivel {self._nivel}")

    def recargar(self, balas: int):
        """
        Recarga el arma con balas

        Parámetros:
        balas: int -- número de balas
        """
        self._balas += balas
    
    def __str__(self):
        """
        Devuelve una representación en forma de cadena del arma
        """
        return super().__str__() + f" - Balas: {self._balas}"   # extensión del método __str__