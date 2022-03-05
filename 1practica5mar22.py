# COMENTARIOS

#si se requiere alguna funcion especifica de alguna libreria, se tiene que importar la libreria que se requiere al inicio del desarrollo
import math

# DEFINIR O CREAR VARIABLES
numero1 = 5
numero2 = 4


# PROCESOS (CALCULO U OPERACIONES MATEMATICAS Y LOGICAS)
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia1 = numero1 ** numero2
poetncia2 = pow(numero1, numero2)
cuadrado = numero1 ** 2
cubo = pow(numero1, 3)
raiz_cuadrado1 = pow(numero1,1/2)
raiz_cuadrado2 = math.sqrt(numero1)
raiz_cubo = pow(numero2, 1/3)
moduloresiduo = numero1 % numero2

# SALIDA DE DATOS
print("La suma", suma) #SE MUESTRA LA SALIDA EN LA COMBINACION SE COLOCA "," y el proceso que se requiere
print("La suma" + str(suma)) #concatenado de texto mas funcion, se tiene que adicionar signo de "+" funcion "str(abreviacion string)" + str(funcion)
print(f"La suma {suma}") #inetrpolacion de texto y funcion inicio "f" y uso de {}
print("La suma", suma, "\nLa resta", resta) # uso en la misma linea 
print("La multiplicacion", multiplicacion) #SE MUESTRA LA SALIDA EN LA COMBINACION SE COLOCA "," y el proceso que se requiere
print("La division", division) #SE MUESTRA LA SALIDA EN LA COMBINACION SE COLOCA "," y el proceso que se requiere
print("La potencia", potencia1)
print("La potencia", poetncia2)
print("El cuadrado ", cuadrado)
print("El cubo ", raiz_cuadrado1)
print("El cubo ", raiz_cuadrado2)
print("El cubo ", raiz_cubo)
print("El residuo", moduloresiduo)
