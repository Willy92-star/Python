# Reconoce el número medio entre un conjunto de 3 números

N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

if N1 > N2 and N1 < N3 or N1 > N3 and N1 < N2:
    print("El número medio es:", N1)

elif N2 > N1 and N2 < N3 or N2 > N3 and N2 < N1:
    print("El número medio es:", N2)

elif N3 > N1 and N3 < N2 or N3 < N1 and N3 > N2:
    print("El número medio es:", N3)

else:
    print("Los números deben ser diferentes entre sí")