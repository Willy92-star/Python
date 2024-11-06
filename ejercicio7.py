# Indica si es un hombre casado mayor de 50, o una mujer soltera menor de 40

N = str(input("Ingrese el nombre de la persona: "))
E = int(input("Ingrese la edad: "))
S = str(input("Ingrese tipo de sexo: M = masculino o F = femenino: "))
EC = str(input("Ingrese su estado civil: C = casado o S = soltero: "))

if E > 40 and (S == "M" or S == "m") and (EC == "C" or EC == "c"):
    print(N, "es un hombre casado mayor de 40 años")

elif E < 50 and (S == "F" or S == "f") and (EC == "S" or EC == "s"):
    print(N, "es una mujer soltera menor de 50 años")