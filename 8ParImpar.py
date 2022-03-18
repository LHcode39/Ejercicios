# Pedir un número y decir si es par o impar

from sqlite3 import paramstyle


par = int(input("Numero: ")) % 2

if (par == 0) :
    print("Es par")

if (par != 0 ) :
    print("Es impar")
