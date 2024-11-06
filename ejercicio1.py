# Si se ingresa un número negativo, se mostrará el mismo número y su positivo

N = int(input("Ingrese el número: "))

if N < 0:
    print("El número ingresado es:", N, "y su positivo es: ", N * -1)