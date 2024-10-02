class Mision:
    """
    Representa una misión a realizar
    """

    def __init__(self, nombre: str, dificultad: int, descripcion: str):
        """
        Crea una misión con un nombre, dificultad y descripción

        Parámetros:
        nombre: str -- nombre de la misión
        dificultad: int -- dificultad de la misión
        descripcion: str -- descripción de la misión
        """
        self._nombre = nombre
        self._dificultad = dificultad
        self._descripcion = descripcion

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la misión
        """
        return f"Misión: {self._nombre} - Dificultad: {self._dificultad} - Descripción: {self._descripcion}"