from elementos.personajes.personaje import Personaje, Humano, Hobbit, Mago, Ent, Enano, Orco
from elementos.personajes.raza import Raza
from elementos.extra.mascota import Mascota
from elementos.extra.mision import Mision
from elementos.extra.arma import TipoArma, Arma


if __name__ == '__main__':
    """
    Programa principal de prueba realista del juego del señor de los anillos
    """

    # Creamos un personaje hobbit (PUEDO SEGUIR CREANDO PERSONAJES, AUNQUE NO ES CORRECTO SI YA TENGO SUBCLASES ESPECÍFICAS)
    frodo: Personaje = Personaje(nombre="Frodo", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    print(frodo)

    # Creamos una mascota
    smigol: Mascota = Mascota(nombre="Smigol", raza=Raza.HOBBIT, nivel=5)
    frodo.set_mascota(smigol)
    print(smigol)
    frodo.alimenta_mascota()

    # Creamos un personaje humano
    aragorn: Humano = Humano(nombre="Aragorn", raza=Raza.HUMANO, aliado=True, equipo="Comunidad del anillo")
    print(aragorn)

    # Ahora vamos a crear otro personaje, de tipo Hobbit
    sam: Hobbit = Hobbit(nombre="Sam", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    #sam.ataca(fuerza=4.5)    # Si es hobbit, no puede atacar. Esto daría error si se descomenta, pues no necesita parámetros en la subclase Hobbit.
    sam.ataca()               # Este método se ha sobreescrito en la subclase Hobbit y no necesita parámetros. [POLIMORFISMO]
    frodo.ataca(fuerza=4.5)   # Frodo es de tipo Personaje, y sí puede ejecutar el método original. Frodo debería crease de tipo Hobbit. 

    # Creamos un personaje mago
    gandalf: Mago = Mago(nombre="Gandalf", raza=Raza.MAGO, aliado=True, equipo="Comunidad del anillo")
    print(gandalf)
    gandalf.ataca(hechizo="Rayo")  # Si es de tipo mago, sólo puede atacar con hechizos (parámetro obligatorio ahora!) [POLIMORFISMO]

    # Creamos un personaje ent (barbol)
    barbol: Ent = Ent(nombre="Barbol")  # No necesita más parámetros, ya que no tiene más atributos que el nombre
    barbol.ataca(fuerza=10)            # Los Ents pueden atacar con fuerza, energía o hechizos.
    barbol.ataca(energia=10)
    barbol.ataca(hechizo="Llamas")
    barbol.añade_moneda()              # Los Ents no pueden añadir monedas. Hemos sobreescribido el método en la subclase Ent.
    #barbol.da_moneda(gandalf)         # ERROR. Los Ents heredan el método da_moneda y no lo hemos sobreescrito.

    # Creamos un personaje enano
    gimli: Enano = Enano(nombre="Gimli", equipo="Comunidad del anillo")
    print(gimli)

    # Hacemos misión
    mision: Mision = Mision("Destruir el anillo", 10, "Destruir el anillo en el monte del destino")
    mision = frodo.realiza_mision(mision)

    # Creamos un personaje orco
    orcoJefe: Orco = Orco(jefe=gandalf, nombre="Adar")    # El jefe de un orco no puede ser un mago
    print(orcoJefe)
    orco: Orco = Orco(jefe=orcoJefe, nombre="Adar")    
    print(orco)

    # Batalla

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