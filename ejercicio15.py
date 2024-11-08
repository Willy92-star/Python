# Evalúa la formula cuadrática o general

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

D = b**2 - 4*a*c

from math import sqrt

if D > 0:
    X1 = (-b + sqrt(D)) / 2*a
    X2 = (-b - sqrt(D)) / 2*a
    print("La ecuación cuenta con dos soluciones reales:", X1, "y", X2)

elif D == 0:
    X1 = -b / 2*a
    print("La ecuación cuenta con una única solución:", X1)

else:
    D < 0
    ParteReal = -b / (2*a)
    ParteImaginaria = sqrt(-D) / (2*a)
    X1 = ParteReal + ParteImaginaria * 1j
    X2 = ParteReal - ParteImaginaria * 1j
    print("La ecuación cuenta con dos soluciones complejas:", X1, "y", X2)
