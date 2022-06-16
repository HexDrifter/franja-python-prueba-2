# Ejercicio 1 (30 puntos): Escribir un programa que contenga una función que 
# reciba una lista de palabras y devuelva la más larga. Imprimir por pantalla 
# la palabra resultante.
def palabraMasLarga(lista):
    masLarga = 0
    for palabra in lista:
        largoPalabra = len(palabra)
        if largoPalabra > masLarga:
            masLarga = largoPalabra
            palabraSelect = palabra
    print("La palabra mas larga es:",palabraSelect)

def main():
    listaPalabras = ['uno','Sopaipillas','dos','tres', 'veintiuno']
    palabraMasLarga(listaPalabras)
    

    # Hasta acá cumple con lo que se pide, de aquí en adelante se añade código
    # extra para verificar la funcionalidad de la función programada
    nuevaLista = []
    continuarIngreso = True
    while continuarIngreso:
        ingresoPalabra = input("Ingrese palabras, para terminar no ingrese nada:")
        print(len(ingresoPalabra))
        if len(ingresoPalabra)>=1:
            nuevaLista.append(ingresoPalabra)
        else:
            continuarIngreso = False

    palabraMasLarga(nuevaLista)



if __name__ == '__main__':
    main()