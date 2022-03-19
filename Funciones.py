#  ENFOQUE O PARADIGMAS DE PROGRAMACION
#   ESTRUCTURADO 
#       SECUENCIAL
#           ENTRDADA DE DATOS - PROCESOS - SALIDA DE DATOS

#       SELECTIVA (USO DE CONDICIONALES)

#       REPETITIVA (USO DE CICLOS)
#       FUNCIONAL O MODULAR
#           CREACION DE FUNCIONES PROPIAS


#FUNCION (TAREA A EJECUTAR)
# SINTAXIS:
# def Nombre_de_la_funcion (Parámetros o Argumentos) :
# El nombre de la definicion debe iniciar con Mayusculas y definir como verbo (ar, er o ir) tarea a ejecutar

from argparse import RawDescriptionHelpFormatter


def Sumar(a, b, c, d, e): #Obtener o recibir los parametros o argumentos
    suma = a + b + c + d + e
    return suma #return: Devolver, retonar, o regresar un valor

def Restar(a, c, e):
    resta = a - c - e
    return resta

def Multiplicar(b, e):
    multiplica = b * e
    return multiplica

def Dividir(d, a):
    division = d / a
    return division



#Mandar a llamar o invocar una funcion

i = int(input("i: "))
j = int(input("j: "))
k = int(input("k: "))
l = int(input("l: "))
m = int(input("m: "))

res_sumar = Sumar(i, j, k, l, m) #Envian o pasan los argumentos
res_restar = Restar (i, k , m)
res_multiplicar = Multiplicar(j, l)
res_dividir = Dividir(l, j)

#SALIDA
print(f"La suma = {res_sumar}")
print(f"La resta = {res_restar}")
print(f"La multiplicacion = {res_multiplicar}")
print(f"La division = {res_dividir}")