class Persona:
    def __init__(self, nombre: str, apellido: str, direccion: str, celular: str, edad: int, correo: str):
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._celular = celular
        self._edad = edad
        self._correo = correo

    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_direccion(self) -> str:
        return self._direccion

    def get_celular(self) -> str:
        return self._celular

    def get_edad(self) -> int:
        return self._edad

    def get_correo(self) -> str:
        return self._correo

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_apellido(self, apellido: str):
        self._apellido = apellido

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def set_celular(self, celular: str):
        self._celular = celular

    def set_edad(self, edad: int):
        self._edad = edad

    def set_correo(self, correo: str):
        self._correo = correo
class Empleado(Persona):
    def __init__(self, nombre: str, apellido: str, direccion: str, celular: str, edad: int, correo: str,
                 salario: float, jefe_inmediato: str, años_experiencia: int):
        super().__init__(nombre, apellido, direccion, celular, edad, correo)
        self._salario = salario
        self._jefe_inmediato = jefe_inmediato
        self._años_experiencia = años_experiencia
        self._nombre_cargo = self.calcular_cargo()

    def get_salario(self) -> float:
        return self._salario

    def get_jefe_inmediato(self) -> str:
        return self._jefe_inmediato

    def get_años_experiencia(self) -> int:
        return self._años_experiencia

    def get_nombre_cargo(self) -> str:
        return self._nombre_cargo
    
    def set_salario(self, salario: float):
        self._salario = salario
        self._nombre_cargo = self.calcular_cargo()

    def set_jefe_inmediato(self, jefe_inmediato: str):
        self._jefe_inmediato = jefe_inmediato

    def set_años_experiencia(self, años_experiencia: int):
        self._años_experiencia = años_experiencia
        self._nombre_cargo = self.calcular_cargo()

    def calcular_cargo(self) -> str:
        if self._salario >= 5000000 and self._años_experiencia >= 5 and 25 <= self.get_edad() <= 45:
            return "Senior"
        elif 900000 <= self._salario <= 1200000 and 1 <= self._años_experiencia <= 2 and 18 <= self.get_edad() <= 22:
            return "Junior"
        else:
            return "Empleado"

    def __str__(self):
        return (f"Nombre: {self.get_nombre()} {self.get_apellido()}\n"
                f"Dirección: {self.get_direccion()}\n"
                f"Celular: {self.get_celular()}\n"
                f"Edad: {self.get_edad()}\n"
                f"Correo: {self.get_correo()}\n"
                f"Salario: {self.get_salario()}\n"
                f"Jefe Inmediato: {self.get_jefe_inmediato()}\n"
                f"Años de Experiencia: {self.get_años_experiencia()}\n"
                f"Cargo: {self.get_nombre_cargo()}")
def main():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    direccion = input("Ingrese la dirección: ")
    celular = input("Ingrese su numero celular: ")
    edad = int(input("Ingrese la edad: "))
    correo = input("Ingrese el correo: ")
    salario = float(input("Ingrese el salario: "))
    jefe_inmediato = input("Ingrese el nombre del jefe inmediato: ")
    años_experiencia = int(input("Ingrese los años de experiencia: "))

    empleado = Empleado(nombre, apellido, direccion, celular, edad, correo, salario, jefe_inmediato, años_experiencia)
    print("\nDetalles del Empleado:")
    print(empleado)


if __name__ == "__main__":
    main()
