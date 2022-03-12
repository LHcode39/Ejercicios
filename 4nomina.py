#Calcular la nómina para un empleado en el mes de Enero del 2022 conociendo

#ENTRADA

nombre = "JUAN LOPEZ"

SUELDODIARIO = 250
dias = float(input("dias trabajados: "))
IVA = 0.16
RET_ISR = 0.10
RET_IVA = 0.10666
sueldo_bruto = SUELDODIARIO * dias  

#PROCESO

pago_nomina = sueldo_bruto + round(sueldo_bruto * IVA,2) - round(sueldo_bruto * RET_ISR, 2) - round(sueldo_bruto * RET_IVA,2)

#SALIDA

print("El sueldo base del mes es " , sueldo_bruto)
print("el sueldo neto a pagar de ", nombre , "es ", pago_nomina)