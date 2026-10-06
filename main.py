productos = []


while True:
    print("="*40) 
    print("Sistema de getion de productos") 
    print("="*40) 
    print("1. Agregar productos")
    print("2. Mostrar productos")        
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegi una opción del 1 al 5: ").strip()  

    if opcion == "1":
        
        print("--- Agregar producto ---")

        nombre = input("Nombre del producto: ").strip().lower()
        while nombre == "":
            print("\nError: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip().lower()

        categoria = input("Categoria del producto: ").strip() 
        while categoria == "":
            print("\nError: la categoria no puede estar vacia.\n")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("\nError: ingresa solo numeros positivos.\n")
            precio_str = input("\nPrecio (sin centavos): \n").strip()
        precio = int(precio_str)

        productos.append([nombre,categoria,precio])

    elif opcion == "2":  
        if len(productos) == 0:
            print("\nTodavia no hay productos cargados.\n")
        else:
            print("--- lista de productos ---") 
            for i in range(len(productos)):  
                print(f"-{i+1}: \n-Nombre: {productos[i][0].capitalize()}\n-Categoria: {productos[i][1].capitalize()}\n-Precio: ${productos[i][2]}")

    elif opcion == "3":

        if len(productos) == 0:
            print("\nTodavia no hay productos cargados.\n")
            continue
        
        print("--- Buscar producto ---")
        finder = input("\nBuscar producto por nombre:").strip().lower()
        coincidencias = 0

        while finder == "":
            print("\ndebes ingresar un nombre de producto para buscarlo.\n")
            finder = input("Buscar producto por nombre:").strip().lower()

        for i in range(len(productos)):  
            if productos[i][0].startswith(finder):
                print(f"\n-Nombre: {productos[i][0].capitalize()}\n-Categoria: {productos[i][1].capitalize()}\n-Precio: ${productos[i][2]}")  
                coincidencias += 1

        if coincidencias == 0:
            print("no se encontraron coincidencias.\n")
            
    elif opcion == "4":
        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
            continue

        print("--- lista de productos ---")
        for i in range(len(productos)):
            print(f"-{i+1}: \n-Nombre: {productos[i][0].capitalize()}\n-Categoria: {productos[i][1].capitalize()}\n-Precio: ${productos[i][2]}\n")

        producto_a_eliminar = input("ingresa el numero del producto a eliminar:").strip()
        while not producto_a_eliminar.isdigit() or not (1 <= int(producto_a_eliminar) <= len(productos)):
            print(f"\nError: ingresa un numero entre 1 y {len(productos)}.\n")
            producto_a_eliminar = input("ingresa el numero del producto a eliminar:").strip()
        eliminable = int(producto_a_eliminar)

        eliminado = productos.pop(eliminable - 1)
        print(f"Producto '{eliminado[0].capitalize()}' eliminado.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("\nOpcion invalida. Elegi un numero del 1 al 5.")
        input("Presiona Enter para volver al menu...")
        continue