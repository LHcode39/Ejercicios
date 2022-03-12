#Obtener valores para: a, b y c. Calcular la fórmula general. 

import math

#ENTRADA

valor_a = float(input("Valor a: "))
valor_b = float(input("Valor b: "))
valor_c = float(input("Valor c: "))


#PROCESO

raiz = math.sqrt(pow(valor_b,2) - (4 * valor_a * valor_c))
_2a = 2 * valor_a
x1 = (-(valor_b)-raiz) /_2a
x2 = (-(valor_b)+raiz) /_2a

#SALIDA

print("Datos de origen")
print(valor_a)
print(valor_b)
print(valor_c)
print("resultado x1 ", x1)
print("resultado x2 ", x2)