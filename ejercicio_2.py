# Ejercicio 2 (30 puntos): Escriba un programa que pida dos palabras y 
# diga si riman o no. Si coinciden las últimas tres letras tiene que 
# decir que riman. Si coinciden sólo las últimas dos tiene que decir 
# que riman un poco. Y si no coinciden, decir que no riman. Validar 
# que las palabras tengan al menos tres letras. Nota: Utilizar slices

def compararRima(word1, word2):

    nword1 = word1.upper()
    nword2 = word2.upper()
    retroceso1 = len(word1)
    retroceso2 = len(word2)
    countletra = int(0)
    for i in range(3):
        if nword1[retroceso1-1 -i] == nword2[retroceso2-1 -i]:
            countletra +=1

    if countletra == 3:
        print("Las palabras riman")
    elif countletra ==2:
        print("las palabras rima un poquito")   
    else: 
        print("las palabras no riman") 


def main():
    palabra1=input("Ingrese una palabra:")
    palabra2=input("Ingrese otra:")

    compararRima(palabra1,palabra2)



if __name__ == '__main__':
    main()
