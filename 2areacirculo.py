#Calcular el área y perímetro de un círculo.
# Área = π . R2
#Perímetro de un círculo = π x d
# ENTRADA DE DATOS

PI = 3.1416
radio = float(input("radio: "))
diametro = float(input("diametro: "))


# PROCESO

area = PI * pow(radio,2)
perimetro = PI * diametro

# SALIDA

print("Area circulo = ", area)
print("Permímetro =", perimetro)
