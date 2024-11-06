# Calcula el promedio con las 2 notas más altas de las 3 notas dadas.

N1 = float(input("Ingrese la primera nota: "))
N2 = float(input("Ingrese la segunda nota: "))
N3 = float(input("Ingrese la tercera nota: "))

if (N1 > N2 and N1 > N3 and N2 > N3) or (N2 > N1 and N2 > N3 and N1 > N3) or (N2 == N3 and N1 > N2) :
    P = (N1 + N2) / 2
    print("El promedio del estudiante es:", P)

elif (N1 > N2 and N1 > N3 and N3 > N2) or (N3 > N1 and N3 > N2 and N1 > N2) or (N1 == N2 and N3 > N1):
    P = (N1 + N3) / 2
    print("El promedio del estudiante es:", P)

elif (N2 > N1 and N2 > N3 and N3 > N1) or (N3 > N1 and N3 > N2 and N2 > N1) or (N3 == N1 and N2 > N3):
    P = (N2 + N3) / 2
    print("El promedio del estudiante es:", P)

else:
    print("El promedio del estudiante es:", N1)