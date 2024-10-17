from elementos.personajes.personaje import Personaje, Humano, Hobbit, Mago, Ent, Enano, Orco
from elementos.personajes.raza import Raza
from elementos.extra.mascota import Mascota
from elementos.extra.mision import Mision
from elementos.extra.arma import TipoArma, Arma
from graficos.mapa import Mapa
from graficos.dibujable import IDibujable
from elementos.extra.objeto import Objeto


if __name__ == '__main__':
    """
    Programa principal de prueba realista del juego del señor de los anillos
    """

    personajes : list[Personaje] = []  # Lista de personajes creados

    # Creamos un personaje hobbit (PUEDO SEGUIR CREANDO PERSONAJES, AUNQUE NO ES CORRECTO SI YA TENGO SUBCLASES ESPECÍFICAS)
    frodo: Personaje = Personaje(nombre="Frodo", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    personajes.append(frodo)
    print(frodo)

    # Creamos una mascota
    smigol: Mascota = Mascota(nombre="Smigol", raza=Raza.HOBBIT, nivel=5)
    frodo.set_mascota(smigol)
    print(smigol)
    frodo.alimenta_mascota()

    
    ######### CLASE 5: Herencia #########
    # Creamos un personaje humano
    aragorn: Humano = Humano(nombre="Aragorn", raza=Raza.HUMANO, aliado=True, equipo="Comunidad del anillo")
    personajes.append(aragorn)
    print(aragorn)

    # Ahora vamos a crear otro personaje, de tipo Hobbit
    sam: Hobbit = Hobbit(nombre="Sam", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    personajes.append(sam)
    #sam.ataca(fuerza=4.5)    # Si es hobbit, no puede atacar. Esto daría error si se descomenta, pues no necesita parámetros en la subclase Hobbit.
    sam.ataca()               # Este método se ha sobreescrito en la subclase Hobbit y no necesita parámetros. [POLIMORFISMO]
    frodo.ataca(fuerza=4.5)   # Frodo es de tipo Personaje, y sí puede ejecutar el método original. Frodo debería crease de tipo Hobbit. 

    # Creamos un personaje mago
    gandalf: Mago = Mago(nombre="Gandalf", raza=Raza.MAGO, aliado=True, equipo="Comunidad del anillo")
    personajes.append(gandalf)
    print(gandalf)
    gandalf.ataca(hechizo="Rayo")  # Si es de tipo mago, sólo puede atacar con hechizos (parámetro obligatorio ahora!) [POLIMORFISMO]

    # Creamos un personaje ent (barbol)
    barbol: Ent = Ent(nombre="Barbol")  # No necesita más parámetros, ya que no tiene más atributos que el nombre
    personajes.append(barbol)
    barbol.ataca(fuerza=10)            # Los Ents pueden atacar con fuerza, energía o hechizos.
    barbol.ataca(energia=10)
    barbol.ataca(hechizo="Llamas")
    barbol.añade_moneda()              # Los Ents no pueden añadir monedas. Hemos sobreescribido el método en la subclase Ent.
    #barbol.da_moneda(gandalf)         # ERROR. Los Ents heredan el método da_moneda y no lo hemos sobreescrito.

    # Creamos un personaje enano
    gimli: Enano = Enano(nombre="Gimli", equipo="Comunidad del anillo")
    personajes.append(gimli)
    print(gimli)

    # Hacemos misión
    mision: Mision = Mision("Destruir el anillo", 10, "Destruir el anillo en el monte del destino")
    mision = frodo.realiza_mision(mision)

    # Creamos un personaje orco
    orcoJefe: Orco = Orco(jefe=gandalf, nombre="Adar")    # El jefe de un orco no puede ser un mago
    print(orcoJefe)
    orco: Orco = Orco(jefe=orcoJefe, nombre="Adar")    
    print(orco)
    personajes.append(orco)


    ######### CLASE 6: Clases Abstractas ######### 
    # armaAbstracta: Arma = Arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA, dueño=orco) ERORR. No se puede instanciar un objeto de una clase abstracta.

    gandalf.fabrica_arma(nombre="Bastón", tipo=TipoArma.LARGA_DISTANCIA)
    gandalf.usa_arma(objetivo=orco)  # Gandalf ataca a un orco con su bastón

    orco.fabrica_arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA)
    orco.usa_arma(objetivo=gandalf)  # El orco ataca a Gandalf con su espada
    orco.mejora_arma()               
    orco.usa_arma(objetivo=frodo)      

    frodo.fabrica_arma(nombre="Magnum", tipo=TipoArma.FUEGO)
    frodo.usa_arma(objetivo=orco)

    # Mostramos el número de personajes creados
    print(f"Personajes creados: {Personaje.get_num_personajes()}")


    #### CLASE 7: Interfaces ######### 
    # Uso del MAPA para mover los elementos y que interactúen entre ellos
    # El mapa gestiona objetos dibujables, las clases que quieran ser dibujables deben implementar la interfaz IDibujable

    # Creamos un mapa
    mapa: Mapa = Mapa()

    # Añadimos los personajes al mapa
    for personaje in personajes:   # todos los personajes son de tipo IDibujable (implementan la interfaz)
        mapa.agregar_elemento(personaje)
    
    mapa.agregar_elemento(Objeto("Anillo", "Anillo único", 10, 10))   # un objeto también es Dibujable


    # Movemos a Frodo
    nueva_posicion: tuple[int, int] = (10, 10)
    mapa.mover_elemento(frodo, nueva_posicion)     # Frodo se mueve a la posición (10, 10), donde está el anillo y lo recogerá

    # Movemos a Gandalf
    nueva_posicion = (5, 5)
    mapa.mover_elemento(gandalf, nueva_posicion)
    mapa.mover_elemento(orco, nueva_posicion)       # El orco se mueve a la posición (5, 5), donde está Gandalf y lo atacará


    # Movemos a Frodo y Sam a la misma posición, donde hablarán
    nueva_posicion = (3, 7)
    mapa.mover_elemento(frodo, nueva_posicion)
    mapa.mover_elemento(sam, nueva_posicion)

    
    # Añadimos una nueva mascota al mapa, que interactúa con un orco
    mascota: Mascota = Mascota(nombre="Lobo", raza=Raza.ORCO, nivel=5)
    mapa.agregar_elemento(mascota)
    nueva_posicion = (1, 1)
    mapa.mover_elemento(orco, nueva_posicion)   
    mapa.mover_elemento(mascota, nueva_posicion)  # La mascota interactua con el orco, convirtiendose en su mascota

    # Dibujamos el mapa actualizado
    mapa.dibujar_mapa()

    
    

