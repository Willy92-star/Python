# Se ingresan 3 números y se indica si alguno es divisible del otro

N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

if N1%N2 == 0 and N1%N3 == 0:
    print("El número", N1, "es divisible por", N2, "y", N3)

elif N1%N2 == 0:
    print("El número", N1, "es divisible por", N2)

elif N1%N3 == 0:
    print("El número", N1, "es divisible por", N3)

elif N2%N1 == 0 and N2%N3 == 0:
    print("El número", N2, "es divisible por", N1, "y", N3)

elif N2%N1 == 0:
    print("El número", N2, "es divisible por", N1)

elif N2%N3 == 0:
    print("El número", N2, "es divisible por", N3)

elif N3%N1 == 0 and N3%N2 == 0:
    print("El número", N3, "es divisible por", N1, "y", N2)

elif N3%N1 == 0:
    print("El número", N3, "es divisible por", N1)

elif N3%N2 == 0:
    print("El número", N3, "es divisible por", N2)

else:
    print("Los números no son divisibles entre sí")