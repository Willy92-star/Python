# Rechaza una pieza de varilla si no cumple que: 
# 9cm >= longitud > 7.5cm, 1.3cm > diámetro > 0.5cm y masa < 5.8cm

L = float(input("Ingrese la longitud de la pieza: "))
D = float(input("Ingrese el diámetro de la pieza: "))

M = D * L / 3.5

if L > 7.5 and L <= 9 and D >= 0.5 and D <= 1.3 and M > 0 and M <= 5.8:
    print("La pieza cumple o satisface las condiciones de fabricación")

else:
    print("La pieza no cumple con las condiciones de fabricación")