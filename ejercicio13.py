# Calcula la nota definitiva, e indica si aprueba o no

N1 = float(input("Ingrese la primera nota: "))
N2 = float(input("Ingrese la segunda nota: "))
N3 = float(input("Ingrese la tercera nota: "))

if (N1 + N2 + N3) / 3 >= 3:
    print("El estudiante ganó la materia")

else:
    print("El estudiante reprobó la materia")

