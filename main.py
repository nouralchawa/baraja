import barajaC

#import baraja

palos = ['o', 'c', 'e', 'b']
numeros = ['A','2','3','4','5','6','7','S','C','R']

#ordenada = baraja.creaBaraja(palos, numeros)
#print ("Esta es la primera baraja:", ordenada)

#desordenada = baraja.creaBaraja(palos, numeros)
#print("Esta es la segunda baraja nada mas crearla:", desordenada)
#baraja.barajar(desordenada)
#print("Y ahora la he barajado:", desordenada)

miBaraja = barajaC.Baraja(palos, numeros)

print (miBaraja.mazacote)

# Reparto mi baraja ordenada
print (miBaraja.repartir(3, 5))

miBaraja.barajar()
#print (miBaraja.mazacote)

# Reparto la baraja barajada
miBaraja = barajaC.Baraja(palos, numeros)
miBaraja.barajar()
print (miBaraja.mazacote)
print (miBaraja.repartir(3, 5))
