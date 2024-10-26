"""
Modulo que contiene las clases de errores que se pueden lanzar en el juego
"""

class ArmaError(Exception):
    """
    Representa un error en el uso de un arma
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)


class ArmaVaciaError(ArmaError):
    """
    Representa un error en el uso de un arma vacia
    """

    def __init__(self, dueño: 'Personaje', arma: 'Arma'):
        super().__init__(f"El personaje {dueño.get_nombre()} se ha quedado sin balas en {arma.get_nombre()}")