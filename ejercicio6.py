# Convertir centígrados a kelvin y decir si el número ingresado es mayor a 10.5, o decir si es un caracter

N1 = input("Digite los grados centígrados: ")

K = N1 + 273.15
print("La conversión a grados Kelvin es: ", K)

if N1 > 10.5:
    print("El número", N1, "es mayor que 10.5")