# Determinar la edad de una persona conociendo el año actual y el año de nacimiento
#se tiene que importar siempre la libreria al inicio de nuestro trabajo
# año = datetime.dat.today().year
import datetime

#ENTRADA DE DATOS



año_nacimiento = float(input("Año nacimiento: "))
año_actual = float(input("Año acutal: "))
año = float(datetime.date.today().year)

#PROCESO

edad1 = año_actual - año_nacimiento
edad2 = año - año_nacimiento



#SALIDA DE DATOS

print("Edad1 ", edad1)
print("Edad2 ", edad2)