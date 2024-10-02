import random
from elementos.raza import Raza
from elementos.extra.mision import Mision
from elementos.extra.mascota import Mascota
from elementos.extra.arma import Arma, TipoArma
from elementos.extra.objeto import Objeto

class Personaje:
    """
    Representa a un personaje del juego
    """

    num_personajes = 0

    @classmethod
    def get_num_personajes(cls)->int:
        """
        Devuelve el número de personajes creados

        Returns:
        int -- número de personajes creados hasta ahora
        """
        return cls.num_personajes

    @staticmethod
    def describe_razas():
        """
        Muestra las razas de personaje disponibles
        """
        print("Existen las siguientes razas:")
        for raza in Raza:
            print(raza.name)

    # Constructor explícito sobrecargado
    def __init__(self, raza: Raza, aliado: bool = None, equipo: str = None, nombre=None, mascota: Mascota = None):
        """
        Constructor de la clase Personaje. Sobrecargado para permitir diferentes formas de creación

        Parámetros:
        raza: Raza -- raza del personaje
        aliado: bool -- indica si el personaje es aliado o enemigo
        equipo: str -- equipo al que pertenece el personaje
        nombre: str -- nombre del personaje
        """
        self.raza : Raza  = raza                                # publico, puede ser accedido desde fuera de la clase
        self._aliado : bool = aliado
        self._equipo : str = equipo
        self._dinero : int = 0
        self._nombre : str = nombre
        self.__id_base_datos : int = random.randint(0, 99999)   # privado para gestionarlo de manera segura solo desde esta clase

        self._amigos : list['Personaje'] = []                   # lista de amigos (asociación)
        self.set_mascota(mascota)                               # si tenemos el método set_mascota, podemos usarlo en el constructor         
        self._inventario: list[Objeto] = []                     # lista de objetos (agregación), no se puede tener objetos al principio
        self._arma: Arma = None                                 # sólo se puede tener un arma si se la fabrica para él mismo (composición)

        Personaje.num_personajes += 1

        self.__guarda_datos()                                   # llamada a un método privado (no se puede acceder desde fuera de la clase)


    # Método mágico para representar el objeto como string
    def __str__(self) -> str:
        """
        Representación del personaje como cadena de texto

        Returns:
        str -- cadena de texto con la representación del personaje
        """
        return f"Personaje {self._nombre} de raza {self.raza.name} ({self._equipo})"

    # Método sobrecargado
    def ataca(self, energia: float = None, hechizo: str = None, fuerza: float = None):
        """
        Ataca al enemigo con energía, o hechizo o fuerza (sobrecarga). Si no se especifica nada, no se puede atacar

        Parámetros:
        energia: float -- cantidad de energía a utilizar
        hechizo: str -- hechizo a utilizar
        fuerza: float -- fuerza a utilizar
        """

        assert (energia and not hechizo and not fuerza) or (hechizo and not energia and not fuerza) or (fuerza and not energia and not hechizo), "Sólo se puede atacar con un tipo de ataque"

        if energia:
            print(f"Atacando con {energia} julios de energía")
        elif hechizo:
            print(f"Atacando con el hechizo {hechizo}")
        elif fuerza:
            print(f"Atacando con {fuerza} newton de fuerza")
        else:
            print("No puedo atacar!")

    
    # Métodos get y set necesarios hasta ahora

    def get_nombre(self) -> str:
        """
        Devuelve el nombre del personaje

        Returns:
        str -- nombre del personaje
        """
        return self._nombre

    def get_raza(self) -> Raza:
        """
        Devuelve la raza del personaje

        Returns:
        Raza -- raza del personaje
        """
        return self.raza

    def _get_dinero(self) -> int:           # sólo se puede acceder al dinero desde dentro de la clase/subclases
        """
        Devuelve el dinero del personaje

        Returns:
        int -- dinero del personaje
        """
        return self._dinero

    def _set_dinero(self, dinero: int):     # sólo se puede modificar el dinero desde dentro de la clase/subclases
        """
        Establece el dinero del personaje

        Parámetros:
        dinero: int -- dinero del personaje
        """
        self._dinero = dinero

    def __get_id_base_datos(self) -> int:   # sólo se puede acceder al id de la base de datos desde dentro de la clase
        """
        Devuelve el id de la base de datos del personaje
        """
        return self.__id_base_datos
    
    def set_mascota(self, mascota: Mascota):
        """
        Añade una mascota al personaje (RELACIÓN DE AGREGACIÓN)
        """
        self._mascota : Mascota = None      # nos aseguramos de que siempre creamos el atributo de instancia (aunque sea None)
        if mascota:
            self._mascota: Mascota = mascota
            mascota.add_dueño(self)         # añadimos al personaje como dueño de la mascote (BIDIRECCIONALIDAD)
            print(f"¡Bienvenido, {self._mascota.get_nombre()}!")

    # Otros métodos de instancia
    def __guarda_datos(self):
        """
        Guarda los datos del personaje en la base de datos
        """ 
        # print(f"Guardando datos con id = {self.__get_id_base_datos()}")
        pass

    def añade_moneda(self): # solo pueden añadirme monedas de uno en uno
        """
        Añade una moneda al personaje (sólo se puede añadir una moneda a la vez)
        """
        self._set_dinero(self._dinero+1)    # sólo YO me añado realmente monedas
        

    def tiene_dinero(self) -> bool: # solo pueden saber externamente si tengo dinero o no (pero no la cantidad)
        """
        Comprueba si el personaje tiene dinero

        Returns:
        bool -- True si tiene dinero, False en caso contrario
        """
        return self._get_dinero() > 0

    def da_moneda(self, otro_personaje: 'Personaje') -> bool:              # si permito que un personaje pueda dar moneda a otro
        """
        El personaje se quita una moneda para dársela a otro personaje. Si no tiene monedas, no se puede dar.

        Parámetros:
        otro_personaje: Personaje -- personaje al que se le da la moneda

        Returns:
        bool -- True si se ha podido dar la moneda, False en caso contrario
        """
        if self.tiene_dinero():
            self._quitar_moneda()            # sólo YO me quito realmente monedas
            otro_personaje.añade_moneda()    # sólo el otro se añade realmente monedas
            return True
        return False

    def _quita_moneda(self) -> bool:               # no quiero que ninguna clase externa pueda directamente quitar dinero
        """
        Quita una moneda al personaje. Si no tiene monedas, no se puede quitar.

        Returns:
        bool -- True si se ha podido quitar la moneda, False en caso contrario
        """
        if self.tiene_dinero():
            self._set_dinero(self._get_dinero()-1)
            return True
        return False
        
    def realiza_mision(self, mision: Mision):
        """
        Simula la realización de una misión (RELACIÓN DE USO). 

        Parámetros:
        mision: Mision -- misión a realizar
        """
        print(f"Realizando misión: {str(mision)}")

    def añade_amigo(self, amigo: 'Personaje') -> bool:
        """
        Añaade un amigo al personaje (RELACIÓN DE ASOCIACIÓN)

        Parámetros:
        amigo: Personaje -- amigo a añadir

        Returns:
        bool -- True si se ha añadido el amigo, False en caso
        """
        if amigo not in self._amigos:
            self._amigos.append(amigo)
            amigo.añadir_amigo(self)    # bidireccionalidad
            return True
        return False

    def recoge_objeto(self, objeto: Objeto):
        """
        Añade un objeto al inventario del personaje (RELACIÓN DE AGREGACIÓN)

        Parámetros:
        objeto: Objeto -- objeto a añadir al inventario
        """
        print(f"Recogiendo objeto: {str(objeto)}")
        self._inventario.append(objeto)
    
    def fabrica_arma(self, nombre: str, tipo: TipoArma):
        """
        Crea un arma para el personaje (RELACIÓN DE COMPOSICIÓN). Sólo se puede tener un arma y se desecha cuando se destruye el personaje.
        Se indica el nombre y tipo de arma a crear. El daño se genera aleatoriamente entre 0 y 100.

        Parámetros:
        nombre: str -- nombre del arma
        tipo: TipoArma -- tipo del arma
        """
        print(f"Fabricando arma: {nombre}")
        self._arma = Arma(nombre=nombre, daño=random.randint(0,100), tipo=tipo, dueño=self) # composición, el arma se destruirá con el personaje

    
    def dispara(self) -> bool:
        """
        Dispara el arma del personaje, si tiene una

        Returns:
        bool -- True si ha disparado, False en caso contrario
        """
        if self._arma:
            return self._arma.dispara()   # delego en el arma, no necesito saber cómo lo hace o el número de balas
        else:
            print("No tengo arma")
            return False
                        
    
    def alimenta_mascota(self):
        """
        Alimenta a la mascota del personaje si no tiene energía

        Returns:
        bool -- True si ha alimentado a la mascota, False en caso contrario
        """
        if self._mascota and not self._mascota.tiene_energia():   # no necesito saber su energia, sólo si tiene  (delego esa comprobación)
            self._mascota.alimentar()                             # no necesito saber cómo lo hace, sólo que lo hace (delego esa funcionalidad)