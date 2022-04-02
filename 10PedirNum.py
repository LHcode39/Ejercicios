#Pedir números enteros en un ciclo mientras sean positivos y en caso de
#que un número sea negativo cerrar el ciclo y al final promediar los
#números positivos ingresados por el usuario.

#creacion de una lista donde se incorpore la información solicitada
import statistics


lista = []


while True:
    numero = float(input("Ingresa un número (ingresa uno negativo para terminar): "))
    if numero >= 0:
        lista.append(numero)
        promedio = statistics.mean(lista)
    else:
        break
print(promedio)
print (lista)

#En este ejemplo solo se solicitan los numero se la lista, pero no se conserva la lista para actualización
#Eliminando o adicinando valores

