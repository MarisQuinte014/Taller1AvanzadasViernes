print(f'--- Digita 1 si desea agregar un producto ---')
print(f'--- Digita 2 para ver los productos ---')
print(f'--- Digita 3 para buscar por codigo y editar el precio ---')
print(f'--- Digita 4 para buscar por codigo y eliminar el precio ---')
print(f'--- Digita 0 para SALIR ---')

opcion = 100
productos = []

while opcion != 0:
    producto = {}
    opcion = int(input("Digite la opcion que desee: "))
    if opcion == 1:
        codigo = input("Digite el codigo del producto: ")
        producto['codigo'] = codigo
        producto['nombre'] = input("Digite el nombre del producto: ")
        producto['precio'] = float(input("Digite el precio del producto: "))

        productos.append(producto)
        print('Producto agregado con exito')
    elif opcion == 2:
        print(productos)

    elif opcion == 3:
        codigoDigitado = input("Digite el codigo del producto que desea buscar: ")
        # if codigoDigitado == codigo:
        #     productos.
        
    elif opcion == 4:
        codigoDigitado = input("Digite el codigo del producto que desea buscar: ")
        if codigoDigitado == codigo:
            productos.remove(productos[2])


        

       


       


        
