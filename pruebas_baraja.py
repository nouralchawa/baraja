import random
barajita = [1,2,3,4,5,6]

for i in range(len(barajita)):
    posicion_al_azar = random.randrange(len(barajita)) 
    aux = barajita[posicion_al_azar]
    barajita[posicion_al_azar]= barajita[i]
    barajita[i]= aux

print (barajita)


