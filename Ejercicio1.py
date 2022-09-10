tamañoLista = int(input("Digite la cantidad de veces que desea recorre esta lista: "))
cantidadDeMultiplosDeDos = 0
cantidadDeMultiplosDeTres = 0


for n in range(tamañoLista):
    numero = int(input("Digite un número: "))
    multiploDeDos = numero % 2
    multiploDeTres = numero % 3

    if(multiploDeDos == 0):
        cantidadDeMultiplosDeDos += 1
    elif(multiploDeTres == 0):
        cantidadDeMultiplosDeTres += 1
    else:
        print("Digite una opción valida")

print(f'Digitaste {cantidadDeMultiplosDeDos} números multiplos de 2 y {cantidadDeMultiplosDeTres} números multiplos de 3')

