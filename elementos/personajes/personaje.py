import random
from elementos.personajes.raza import Raza
from elementos.extra.mision import Mision
from elementos.extra.mascota import Mascota
from elementos.extra.arma import Arma, TipoArma, ArmaCorta, ArmaLarga, ArmaFuego
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

        self._vida = 100                                        # vida del personaje, no se puede acceder desde fuera de la clase


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
    
    def get_arma(self) -> Arma:
        """
        Devuelve el arma del personaje

        Returns:
        Arma -- arma del personaje
        """
        return self._arma

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

    
    def fabrica_arma(self, nombre: str, tipo: TipoArma) -> bool:
        """
        Crea un arma para el personaje (RELACIÓN DE COMPOSICIÓN). Sólo se puede tener un arma y se desecha cuando se destruye el personaje.
        Se indica el nombre y tipo de arma a crear.

        Parámetros:
        nombre: str -- nombre del arma
        tipo: TipoArma -- tipo del arma

        Returns:
        bool -- True si se ha podido crear el arma, False en caso contrario
        """

        print(f"Fabricando arma: {nombre}")
        
        if tipo == TipoArma.CORTA_DISTANCIA:
            self._arma = ArmaCorta(nombre=nombre, dueño=self, estocadas=3)
        elif tipo == TipoArma.LARGA_DISTANCIA:
            self._arma = ArmaLarga(nombre=nombre, dueño=self)
        elif tipo == TipoArma.FUEGO:
            self._arma = ArmaFuego(nombre=nombre, dueño=self, balas = random.randint(1, 10))
        else:
            print("Tipo de arma no válido")
            return False
        
        print(f"Arma creada: {self._arma}")
        return True
  
    
    def alimenta_mascota(self):
        """
        Alimenta a la mascota del personaje si no tiene energía

        Returns:
        bool -- True si ha alimentado a la mascota, False en caso contrario
        """
        if self._mascota and not self._mascota.tiene_energia():   # no necesito saber su energia, sólo si tiene  (delego esa comprobación)
            self._mascota.alimentar()                             # no necesito saber cómo lo hace, sólo que lo hace (delego esa funcionalidad)
     
    # Cambiamos el método dispara() por usa arma
    def usa_arma(self, objetivo: 'Personaje') -> bool:
        """
        Usa el arma del personaje.

        Returns:
        bool -- True si ha podido usarla, False en caso contrario
        """
        if self._arma:
            return self.get_arma().usar(objetivo=objetivo)  # delegación
        else:
            print("No tengo arma!")
            return False
        
    def mejora_arma(self):
        """
        Mejora el arma del personaje
        """
        if self._arma:
            self.get_arma().mejorar()  # delegación

    def recibe_daño(self, daño: int):
        """
        Recibe daño en la vida

        Parámetros:
        daño: int -- daño a recibir
        """
        if self._vida == 0:
            print(f"{self._nombre} ya está muerto")

        else: 
            self._vida -= daño
            if self._vida <= 0:
                self._vida = 0
                print(f"{self._nombre} ha recibido {daño} puntos de daño y ha muerto")
            else:
                print(f"{self._nombre} ha recibido {daño} puntos de daño. Vida restante: {self._vida}")
                


### Practicamos diferentes situaciones de herecia y polimorfismo ###

## SOBRECARGA DE MÉTODOS ##

# Clase humano heredando absolutamente todo de la clase Personaje (no sobreescribe métodos ni atributos)
class Humano(Personaje):
    """
    Representa a un personaje de tipo humano.
    """
    pass


# Clase hobbit, heredando de personaje pero particularmente, los hobbits no atacan
class Hobbit(Personaje):
    """
    Representa a un personaje de tipo hobbit.
    """

    # Sobreescribimos el método ataca() para un comportamiento particular. Ahora en esta subclase se ejecuta este método sin parámetros.
    # Los atributos y demás métodos se siguen heredando igual
    def ataca(self):
        """
        Aunque se lo indiques, los hobbits son seres tranquilos que no atacan
        """
        print("Los hobbits no atacan")


# Clase mago heredando de Personaje, sobreescribiendo el método ataca
class Mago(Personaje):
    """
    Representa a un personaje de tipo mago.
    """

    # Sobeescribimos el método ataca para refinarlo. Este método se ejecutará para el tipo Mago.
    # Los atributos y demás métodos se siguen heredando igual
    def ataca(self, hechizo: str):
        """
        Ataca al enemigo con hechizo.

        Parámetros:
        hechizo: str -- hechizo a utilizar
        """
        super().ataca(hechizo=hechizo)  # llamamos al método de la clase padre (reutilización)
        print("Recuerda, el valor no es saber cuando quitar una vida, sino cuando perdonarla.")  # extensión, añadimos funcionalidad extra al método


## HERENCIA DE ATRIBUTOS Y OCULTACIÓN ##

# Clase ent heredando de personaje, ocultando todos los atributos pues no los necesita
class Ent(Personaje):
    """
    Representa a un personaje de tipo ent (árbol viviente)
    """
    
    # No heredamos los atributos de la clase padre, no los necesitamos.
    # El personaje de tipo Ent sólo necesita un nombre. 
    # Por ejemplo, no tiene dinero, ni es aliado ni pertenece a un equipo.
    # Tampoco tendrá listado de amigos ni inventario de objetos, ni arma.
    def __init__(self, nombre: str):
        """
        Constructor de la clase Ent

        Parámetros:
        nombre: str -- nombre del ent
        """
        self._nombre = nombre
        self._tipo = Raza.ENT    # Ocultación de atributos, no se heredan de la clase padre

    # IMPORTANTE: El resto de métodos y funcionalidades de la clase padre se heredan igualmente
    # Las funcionalidades relacionadas con los atributos que hemos ocultado pueden fallar (no existen). 
    # Por ejemplo, no se puede dar monedas, ni quitar monedas, ni comprobar si tiene dinero.
    # Habría que sobreescribirlos en esta clase y devolver que no es posible:

    # Por ejemplo, sobreescritura: 
    def añade_moneda(self) -> bool:
        """
        Intenta añadir una moneda al Ent (no se puede hacer)
        """
        print("Los Ents no saben lo que es el dinero")
        return False
    
    # ¿Debería ser realmente la clase Ent una subclase Personaje si no se va a beneficiar de todo lo que tiene un personaje?
    # ¿Es un Ent realmente una particularización de un personaje?


# Clase enano heredando de Personaje, ocultando el atributo dinero
class Enano(Personaje):
    """
    Representa a un personaje de tipo enano
    """
    
    # Los enanos pueden tener un nombre, un equipo y una macota.
    def __init__(self, equipo: str = None, nombre=None, mascota: Mascota = None):
        """
        Constructor de la clase Enano

        Parámetros:
        equipo: str -- equipo al que pertenece el enano
        nombre: str -- nombre del enano
        mascota: Mascota -- mascota del enano
        """
        # Llamamos al constructor de la clase padre, pasándole los parámetros necesarios
        # Observa como aquí pasamos la raza y que son siempre aliados.
        super().__init__(raza=Raza.ENANO, aliado=True, equipo=equipo, nombre=nombre, mascota=mascota)
        # Recuerda que tendremos dinero, un inventario de objetos, amigos, mascota, arma, etc.
        self._dinero = 1000 # como buenos comerciantes, los enanos podría iniciarse con 1000 monedas (ocultación del atributo del padre con el mismo nombre)


# Clase orco heredando de Personaje, ocultando el atributo dinero
class Orco(Personaje):
    """
    Representa a un personaje de tipo orco
    """

    lances_por_ataque = 2
    
    # Los orcos siempre tienen un jefe, y pueden tener un nombre si tienen suerte.
    def __init__(self, jefe: Personaje, nombre: str =None):
        """
        Constructor de la clase Orco
        
        Parámetros:
        jefe: Orco -- jefe del orco
        nombre: str -- nombre del orco
        """

        # Llamamos al constructor de la clase padre, pasándole los parámetros necesarios
        # Observa como aquí pasamos la raza y que son siempre enemigos.
        super().__init__(raza=Raza.ORCO, aliado=False, nombre=nombre, equipo="Ejército de Mordor") # no hay ocultación
        
        # Un orco sólo puede tener un jefe de tipo Orco
        if isinstance(jefe, Orco) or type(jefe) == Orco:  # ambos son equivalentes en este caso
            self._jefe : Orco = jefe    # atributo propio de la clase Orco
        else:
            print("El jefe de un orco debe ser otro orco")
            self._jefe : Orco = None    # si no es un orco, no tiene jefe
        
        self._amigos.append(jefe)   # añadimos al jefe como amigo (el listado de amigos vacío se hereda de la clase padre)
        
        self.set_mascota(Mascota(nombre="Lobo", raza=Raza.HUARGO, nivel=5))  # todos los orcos tiene asociado un Huargo
        # RECUERDA. Tenemos acceso a todos los métodos heredados (públicos y privados) de la clase Personaje, como set_mascota()

    # refinamiento del método mágico str, pues hemos añadidos atributos propios
    def __str__(self) -> str:
        """
        Método mágico para representar el objeto como string
        """
        if self._jefe:
            return f"Orco {self._nombre} de raza {self.raza.name} ({self._equipo}) con jefe {self._jefe.get_nombre()}"
        else:
            return f"Orco {self._nombre} de raza {self.raza.name} ({self._equipo}) sin jefe"
        
    
    # un orco usa el arma 2 veces, en lugar de una como el resto
    def usa_arma(self, objetivo: 'Personaje') -> bool:
        """
        Usa el arma del orco. En este caso, el orco la usa varias veces seguidas
        """

        print(f"{self._nombre} ataca {Orco.lances_por_ataque} veces a {objetivo.get_nombre()} con su arma")
        i=0
        while i<Orco.lances_por_ataque and super().usa_arma(objetivo):
            i+=1