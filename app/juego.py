from elementos.personaje import Personaje
from elementos.raza import Raza
from elementos.extra.mascota import Mascota
from elementos.extra.mision import Mision
from elementos.extra.arma import TipoArma


if __name__ == '__main__':
    """
    Programa principal de prueba realista del juego del señor de los anillos
    """

    # Creamos un personaje hobbit
    frodo: Personaje = Personaje(nombre="Frodo", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    print(frodo)

    # Creamos un personaje humano
    aragorn: Personaje = Personaje(nombre="Aragorn", raza=Raza.HUMANO, aliado=True, equipo="Comunidad del anillo")
    print(aragorn)

    # Creamos un personaje mago
    gandalf: Personaje = Personaje(nombre="Gandalf", raza=Raza.MAGO, aliado=True, equipo="Comunidad del anillo")
    print(gandalf)

    # Creamos un personaje enano
    gimli: Personaje = Personaje(nombre="Gimli", raza=Raza.ENANO, aliado=True, equipo="Comunidad del anillo")
    print(gimli)

    # Creamos una mascota
    smigol: Mascota = Mascota(nombre="Smigol", raza=Raza.HOBBIT, nivel=5)
    frodo.set_mascota(smigol)
    print(smigol)
    frodo.alimenta_mascota()

    # Hacemos misión
    mision: Mision = Mision("Destruir el anillo", 10, "Destruir el anillo en el monte del destino")
    mision = frodo.realiza_mision(mision)

    # Creamos un personaje orco
    orco = Personaje(nombre="Adar", raza=Raza.ORCO, aliado=False, equipo="Orcos de las tierras del Sur")
    print(orco)

    # Batalla
    orco.fabrica_arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA)
    orco.dispara()      # Si no es de tipo fuego, no se puede disparar

    gandalf.fabrica_arma(nombre="Bastón", tipo=TipoArma.LARGA_DISTANCIA)
    gandalf.dispara()   # Si no es de tipo fuego, no se puede disparar

    frodo.fabrica_arma(nombre="Magnum", tipo=TipoArma.FUEGO)
    frodo.dispara()

    # Mostramos el número de personajes creados
    print(f"Personajes creados: {Personaje.get_num_personajes()}")





    