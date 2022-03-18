# Pedir el nivel del agua en metros de una cisterna. Revisar imagen classroom
#Si llega a mas de 6 m - desbordamiento
# nivel a 6m - apagar bomba
# entre 4 y 6 m - desacelerar bomba
# entre 2 y 4 m - bomba trabajando
# entre 0 y 2 m - acelerar bomba de agua
# nivel 0 - encender bomba de agua
# menor a 0 - fuga de cisterna


#Entrada

nivel = float(input("nivel: "))

#Proceso
if (nivel < 0):
    print("Fuga de cisterna")

elif (nivel == 0):
    print("Encender Bomba")

elif (nivel >0 and nivel <= 2):
    print("acelerar bomba de agua")

elif (nivel >2 and nivel <= 4):
    print("bomba trabajando")

elif (nivel >4 and nivel < 6):
    print("desacelerar bomba")

elif (nivel == 6):
    print("apagar bomba")

elif (nivel >6):
    print("desbordamiento de agua en cisterna")




