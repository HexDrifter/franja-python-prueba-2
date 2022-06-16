# Ejercicio 3 (30 puntos): Escribir una función que calcule el
# área de un círculo y otra que calcule el volumen de un 
# cilindro usando la primera función.
import math as mt

def calcularArea(radio):
    return float(mt.pi * (radio*radio))

def calcularVolumen(altura, radio):
    return calcularArea(radio)*altura


def main():
    radio = int(input("Ingrese el rádio del círculo: "))
    areaCirculo = calcularArea(radio)
    print("El área del círculo es: ", round(areaCirculo,3))
    altura = int(input("Ingrese la altura del dicho cilíndro: "))
    volumen= calcularVolumen(altura, radio)

    print("El volumen del cilíndro de radio", radio, "es:", round(volumen,3))

if __name__ == '__main__':
    main()