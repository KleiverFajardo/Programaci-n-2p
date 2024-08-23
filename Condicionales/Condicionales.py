def evaluar_persona():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (M/F): ")

    if edad >= 18:
        print(f"{nombre} {apellido} es mayor de edad.")
        print("Ya eres legal")
    else:
        print(f"{nombre} {apellido} es menor de edad.")
        print("No eres legal")

    if sexo.upper() == "M":
        print("Es un hombre.")
    elif sexo.upper() == "F":
        print("Es una mujer.")


evaluar_persona()
