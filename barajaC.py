import baraja

class Baraja():

    def __init__(self, palos, numeros):
        self.__palos = palos
        self.__numeros = numeros
        self.mazacote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazacote)


    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range(num_jugadores):
            jugadores.append([])

        if num_jugadores*num_cartas > len(self.mazacote):
            print ("No hay suficientes cartas")
        
        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                #carta = self.mazacote.pop(0)
                #jugadores[jugador].append(carta)
                jugadores[jugador].append(self.mazacote.pop(0))

        return jugadores
