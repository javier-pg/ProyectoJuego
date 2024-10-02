class Mascota:
    """
    Representa a una mascota del juego
    """

    def __init__(self, nombre: str, raza: str, nivel: int, dueño: 'Personaje' = None):
        """
        Crea una mascota con un nombre, raza, nivel y dueño

        Parámetros:
        nombre: str -- nombre de la mascota
        raza: str -- raza de la mascota
        nivel: int -- nivel de la mascota
        dueño: Personaje -- dueño de la mascota (si tiene)
        """
        self._nombre = nombre
        self._raza = raza
        self._nivel = nivel
        self._dueño = dueño
        self._energia = 100
    
    def __str__(self):
        """
        Devuelve la mascota en formato string
        """
        if self._dueño: 
            return f"{self._nombre} es una mascota de nivel {self._nivel} de raza {self._raza} y su dueño es {self._dueño.get_nombre()}"
        else:
            return f"{self._nombre} es una mascota de nivel {self._nivel} de raza {self._raza} y no tiene dueño"

    def get_nombre(self) -> str:
        """
        Devuelve el nombre de la mascota

        Returns:
        str -- nombre de la mascota
        """
        return self._nombre
    
    def add_dueño(self, dueño):
        """
        Añade un dueño a la mascota

        Parámetros:
        dueño: Personaje -- dueño de la mascota
        """
        self._dueño = dueño
    
    def alimenta(self):
        """
        Alimenta a la mascota, aumentando su energía en 10
        """
        self._energia += 10
        print(f"{self._nombre} ha sido alimentado y ahora tiene {self._energia} de energía")
    
    def tiene_energia(self) -> bool:
        """
        Devuelve si la mascota tiene energía

        Returns:
        bool -- True si tiene energía, False en caso contrario
        """
        return self._energia > 0