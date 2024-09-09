class Usuario:
    def __init__(self, nombre_completo, nickname, clave, tipo, fecha_creacion):
        self.datos = {
            'nombre_completo': nombre_completo,
            'nickname': nickname,
            'clave': clave,
            'tipo': tipo,
            'fecha_creacion': fecha_creacion
        }

    def __str__(self):
        return f"Usuario({self.datos})"

usuarios = []

def agregar_usuario():
    nombre_completo = input("Ingrese el nombre completo: ")
    nickname = input("Ingrese el nickname: ")
    clave = input("Ingrese la clave: ")
    tipo = input("Ingrese el tipo: ")
    fecha_creacion = input("Ingrese la fecha de creación: ")
    usuario = Usuario(nombre_completo, nickname, clave, tipo, fecha_creacion)
    usuarios.append(usuario)
    print("Usuario agregado exitosamente.")

def buscar_usuario(value):
    for usuario in usuarios:
        if value in usuario.datos.values():
            return usuario
    return None

def eliminar_usuario(value):
    global usuarios
    usuarios = [usuario for usuario in usuarios if value not in usuario.datos.values()]
    print("Usuario eliminado exitosamente.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            value = input("Ingrese el valor a buscar: ")
            usuario = buscar_usuario(value)
            if usuario:
                print(f"Usuario encontrado: {usuario}")
            else:
                print("Usuario no encontrado.")
        elif opcion == '3':
            value = input("Ingrese el valor a eliminar: ")
            eliminar_usuario(value)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
