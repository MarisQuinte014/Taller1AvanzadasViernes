frutas = []
fruta = {}

for n in reversed(range(10)):
    fruta['nombre'] = input("Digite el nombre de la fruta: ")
    fruta['color'] = input("Digite el color de su fruta: ")
    fruta['valor'] = float(input("Digite el valor de su fruta: "))

    frutas.append(fruta)

print(frutas)
