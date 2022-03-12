# Pedir la cantidad de grados y convertirlos a °C, °F y K.
# Para convertir de ºC a ºF use la fórmula:   ºF = ºC x 1.8 + 32.
# Para convertir de ºF a ºC use la fórmula:   ºC = (ºF-32) ÷ 1.8.
# Para convertir de K a ºC use la fórmula:   ºC = K – 273.15
# Para convertir de ºC a K use la fórmula: K = ºC + 273.15.
# Para convertir de ºF a K use la fórmula: K = 5/9 (ºF – 32) + 273.15.
# Para convertir de K a ºF use la fórmula:   ºF = 1.8(K – 273.15) + 32.

#ENTRADA

grados_C = float(input("Grados C: "))

#PROCESO

de_c_a_f = (grados_C * 1.8) + 32
de_c_a_k = grados_C + 273.15
de_k_a_c = de_c_a_k -273.15



#SALIDA

print("Grados C =", grados_C )
print("Grados F =", de_c_a_f )
print("Grados K =", de_c_a_k )
print("Grados C =", de_k_a_c )