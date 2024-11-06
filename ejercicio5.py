# Mostrar el número mayor, menor, cuáles son iguales o si son diferentes

N1 = int(input("Ingrese el primer número: " ))
N2 = int(input("Ingrese el segundo número: " ))
N3 = int(input("Ingrese el tercer número: " ))

if N1 > N2 and N1 > N3 and N2 < N3:
    print("El número mayor es:", N1)
    print("El número menor es:", N2)
    print("Los números ingresados son diferentes entre sí")

elif N1 > N2 and N1 > N3 and N2 > N3:
    print("El número mayor es:", N1)
    print("El número menor es:", N3)
    print("Los números ingresados son diferentes entre sí")

elif N2 > N1 and N2 > N3 and N1 < N3:
    print("El número mayor es:", N2)
    print("El número menor es:", N1)
    print("Los números ingresados son diferentes entre sí")

elif N2 > N1 and N2 > N3 and N1 > N3:
    print("El número mayor es:", N2)
    print("El número menor es:", N3)
    print("Los números ingresados son diferentes entre sí")

elif N3 > N1 and N3 > N2 and N2 > N1:
    print("El número mayor es:", N3)
    print("El número menor es:", N1)
    print("Los números ingresados son diferentes entre sí")

elif N3 > N1 and N3 > N2 and N2 < N1:
    print("El número mayor es:", N3)
    print("El número menor es:", N2)
    print("Los números ingresados son diferentes entre sí")

elif N1 > N2 and N1 > N3 and N2 == N3:
    print("El número mayor es:", N1)
    print("El número menor es:", N2)
    print("El segundo y tercer números son iguales")

elif N1 < N2 and N1 < N3 and N2 == N3:
    print("El número mayor es:", N2)
    print("El número menor es:", N1)
    print("El segundo y tercer números son iguales")

elif N2 > N1 and N2 > N3 and N1 == N3:
    print("El número mayor es:", N2)
    print("El número menor es:", N1)
    print("El primero y tercer números son iguales")

elif N2 < N1 and N2 < N3 and N1 == N3:
    print("El número mayor es:", N1)
    print("El número menor es:", N2)
    print("El primero y tercer números son iguales")

elif N3 > N1 and N3 > N2 and N1 == N2:
    print("El número mayor es:", N3)
    print("El número menor es:", N2)
    print("El primero y segundo números son iguales")

elif N3 < N1 and N3 < N2 and N1 == N2:
    print("El número mayor es:", N1)
    print("El número menor es:", N3)
    print("El primero y segundo números son iguales")

else:
    print("Los números ingresados son iguales")