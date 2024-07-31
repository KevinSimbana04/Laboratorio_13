import random

detalleCompra = [[], [], [], [], [], [], [], []]

def menuOpciones():
    while True:
        print("¿Qué acción desea realizar?")
        print('*  1) Registrar pedidos')
        print('*  2) Mostrar pedidos')
        print('*  3) Mostrar detalle de un pedido')
        print('*  4) Salir del sistema')
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                print("Opción inválida. Debe ser un número del 1 al 4.")
        except ValueError:
            print("Opción inválida. Debe ingresar un número del 1 al 4.")

def ingresarPedido():
    print("\n\t\t Ingresar los datos del cliente \n")
    
    # Validando Nombre del Cliente
    while True:
        nombre_cliente = input("Nombre (3-10 caracteres, sin números): ").strip()
        if len(nombre_cliente) >= 3 and len(nombre_cliente) <= 10 and nombre_cliente.isalpha():
            break
        else:
            print("Nombre inválido. Debe tener entre 3 y 10 letras.")

    # Validando Apellido del Cliente
    while True:
        apellido_cliente = input("Apellido (3-10 caracteres, sin números): ").strip()
        if len(apellido_cliente) >= 3 and len(apellido_cliente) <= 10 and apellido_cliente.isalpha():
            break
        else:
            print("Apellido inválido. Debe tener entre 3 y 10 letras.")

    # Validando Teléfono del Cliente
    while True:
        telefono_cliente = input("Teléfono (máximo 10 dígitos numéricos): ").strip()
        if telefono_cliente.isdigit() and len(telefono_cliente) <= 10:
            break
        else:
            print("Teléfono inválido. Debe contener máximo 10 dígitos numéricos.")

    print("\n\t\t Ingresar los datos de la policrush \n")
    
    # Validando Nombre de la Policrush
    while True:
        nombre_policrush = input("Nombre (3-10 caracteres, sin números): ").strip()
        if len(nombre_policrush) >= 3 and len(nombre_policrush) <= 10 and nombre_policrush.isalpha():
            break
        else:
            print("Nombre de policrush inválido. Debe tener entre 3 y 10 letras.")

    # Validando Dependencia de la Policrush
    while True:
        lugar_policrush = input("Dependencia (5-15 caracteres, sin números): ").strip()
        if len(lugar_policrush) >= 5 and len(lugar_policrush) <= 15 and lugar_policrush.isalpha():
            break
        else:
            print("Dependencia inválida. Debe tener entre 5 y 15 letras.")

    # Validando Teléfono de la Policrush
    while True:
        celular_policrush = input("Teléfono (máximo 10 dígitos numéricos): ").strip()
        if celular_policrush.isdigit() and len(celular_policrush) <= 10:
            break
        else:
            print("Teléfono de policrush inválido. Debe contener máximo 10 dígitos numéricos.")

    detalleCompra[0].append(nombre_cliente)
    detalleCompra[1].append(apellido_cliente)
    detalleCompra[2].append(telefono_cliente)
    detalleCompra[3].append(nombre_policrush)
    detalleCompra[4].append(lugar_policrush)
    detalleCompra[5].append(celular_policrush)
    detalleCompra[6].append(random.randint(1000, 9999))

    print("\n\t\t Selección del regalo \n")
    print("1) Opción 1: Poliflor + Polipeluche = $2.50")
    print("2) Opción 2: Poliflor + Policarta = $1.50")
    print("3) Opción 3: Poliflor + Polillavero = $2.00")
    print("4) Opción 4: Poliflor + Polivaso = $2.75")
    
    # Validando Opción del Regalo
    while True:
        try:
            opcion = int(input("Ingrese la opción (1-4): "))
            if opcion in [1, 2, 3, 4]:
                break
            else:
                print("Opción inválida. Debe ser un número del 1 al 4.")
        except ValueError:
            print("Opción inválida. Debe ingresar un número del 1 al 4.")

    if opcion == 1:
        detalleCompra[7].append(2.50 + (0.1 * 2.50))
    elif opcion == 2:
        detalleCompra[7].append(1.50 + (0.1 * 1.50))
    elif opcion == 3:
        detalleCompra[7].append(2.00 + (0.1 * 2.00))
    elif opcion == 4:
        detalleCompra[7].append(2.75 + (0.1 * 2.75))

    print("\n-------- Pedido registrado con éxito --------\n")

def mostrarPedido(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompra[0][i])
    print("\t\t\t * Apellido:", detalleCompra[1][i])
    print("\t\t\t * Teléfono:", detalleCompra[2][i])
    print("\t\t\n Datos de la policrush")
    print("\t\t\t * Nombre:", detalleCompra[3][i])
    print("\t\t\t * Dependencia:", detalleCompra[4][i])
    print("\t\t\t * Teléfono:", detalleCompra[5][i])
    print("\t\t\n Datos del pedido")
    print("\t\t\t * Código del pedido:", detalleCompra[6][i])
    print("\t\t\t * Pago final: $", detalleCompra[7][i])

# Main program flow
print("------------ MI POLICRUSH -------------")
print("\n\t\t * Bienvenido(a) *\n")

opcion = menuOpciones()

while opcion != 4:
    if opcion == 1:
        print("\n----- Nuevo pedido -----")
        ingresarPedido()
        opcion = menuOpciones()
    
    elif opcion == 2:
        if len(detalleCompra[0]) == 0:
            print("-------------------------------------\n")
            print("No existen pedidos registrados\n")
            print("-------------------------------------\n")
            opcion = menuOpciones()
        else:
            print("\n------- Detalle de todos los pedidos ----------\n")
            for i in range(len(detalleCompra[0])):
                print("-------------------------------------")
                print("Detalle del pedido", i + 1)
                mostrarPedido(i)
                print("-------------------------------------")
            opcion = menuOpciones()

    elif opcion == 3:
        while True:
            codigo_input = input("\nIngrese el código del pedido (solo números, 4 dígitos): ").strip()
            if codigo_input.isdigit() and len(codigo_input) == 4:
                codigo = int(codigo_input)
                if codigo in detalleCompra[6]:
                    dato = detalleCompra[6].index(codigo)
                    print("\t\t\t\n Pedido encontrado")
                    print("-------------------------------------")
                    print("Detalle")
                    mostrarPedido(dato)
                    print("-------------------------------------")
                else:
                    print("\n\n *** ERROR ***\n")
                    print("No existe ese código de pedido registrado\n")
                break
            else:
                print("Código inválido. Debe ser un número de 4 dígitos.")
        
        opcion = menuOpciones()

print("Muchas gracias")
