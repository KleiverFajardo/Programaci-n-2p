def crear_persona(lista):
    nombre = input("Ingresa un nombre: ")
    lista.append(nombre)
    print(f"Persona '{nombre}' agregada .")
def eliminar_persona(lista):
    if not lista:
        print("lista vacía.")
        return
    print("Lista de personas:")
    for i, persona in enumerate(lista):
        print(f"{i}: {persona}")
    try:
        indice = int(input("Ingrese el numero de la persona a eliminar: "))
        if 0 <= indice < len(lista):
            persona_eliminada = lista.pop(indice)
            print(f"Persona '{persona_eliminada}' eliminada.")
        else:
            print("Error.")
    except ValueError:
        print("Ingresa un valor valido.")
def listar_personas(lista):
    if not lista:
        print("La lista está vacía.")
        return
    print("Lista de personas:")
    for persona in lista:
        print(persona)
def buscar_persona(lista):
    if not lista:
        print("La lista está vacía.")
        return
    nombre_buscar = input("Ingresa el nombre de la persona: ")
    if nombre_buscar in lista:
        print(f"La persona '{nombre_buscar}' fue encontrada.")
    else:
        print(f"La persona '{nombre_buscar}' no fue encontrada.")

personas = []

while True:
    print("\nMenú:")
    print("1. Crear persona")
    print("2. Eliminar persona")
    print("3. Listar personas")
    print("4. Buscar persona")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        crear_persona(personas)
    elif opcion == "2":
        eliminar_persona(personas)
    elif opcion == "3":
        listar_personas(personas)
    elif opcion == "4":
        buscar_persona(personas)
    elif opcion == "5":
        break
    else:
        print("Opción no valida")
