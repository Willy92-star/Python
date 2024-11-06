# Ordena los números ingresados de mayor a menor

N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

if N1 > N2 and N1 > N3 and N2 > N3:
    print("Los números de mayor a menor son:", N1, N2, N3)

elif N1 > N2 and N1 > N3 and N2 < N3:
    print("Los números de mayor a menor son:", N1, N3, N2)

elif N2 > N1 and N2 > N3 and N3 > N1:
    print("Los números de mayor a menor son:", N2, N3, N1)

elif N2 > N1 and N2 > N3 and N3 < N1:
    print("Los números de mayor a menor son:", N2, N1, N3)

elif N3 > N1 and N3 > N2 and N2 > N1:
    print("Los números de mayor a menor son:", N3, N2, N1)

elif N3 > N1 and N3 > N2 and N2 < N1:
    print("Los números de mayor a menor son:", N3, N1, N2)

else:
    print("Los números deben ser diferentes entre sí")