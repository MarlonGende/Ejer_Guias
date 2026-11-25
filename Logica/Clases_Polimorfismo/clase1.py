# EJERCICIO: Implementar la subclase Tripulante(Empleado) incorporando un rol (piloto, copiloto, azafata)
# y el seguimiento de horas de vuelo dentro de la estructura de herencia Persona -> Pasajero / Empleado.

# 1. Análisis del problema
# Datos de entrada: Información personal (nombre, cédula), información laboral (código de empleado, salario),
# cargo asignado al tripulante (piloto, copiloto o azafata) y horas de vuelo a sumar.
# Procesamiento: Declarar la clase Tripulante como hija de Empleado, ejecutar super().__init__(),
# comprobar y guardar el rol, iniciar el contador horas_vuelo en 0, crear un método para
# acumular horas de vuelo y redefinir el método __str__.
# Resultado esperado: Un objeto Tripulante operativo con tanto sus métodos propios como los heredados,
# desplegando sus datos formateados en pantalla.

# 2. Diseño en pseudocódigo
# Declarar clase Tripulante(Empleado)
# Invocar a super().__init__(nombre, cedula, codigo_emp, salario)
# Verificar que el rol pertenezca a ("piloto", "copiloto", "azafata") y asignarlo a self.rol
# Establecer self.horas_vuelo = 0.0
# Implementar registrar_horas_vuelo(horas) para incrementar las horas si el valor es válido
# Redefinir __str__ agregando el rol y las horas acumuladas
# Realizar pruebas instanciando un Tripulante, ejecutando métodos heredados y propios, e imprimiendo el estado

# 3. Identificación de la lógica
# Se emplea herencia multinivel (Persona -> Empleado -> Tripulante) aprovechando atributos y comportamientos previos mediante super().
# La verificación del cargo y el conteo de horas_vuelo quedan encapsulados en la clase derivada.
# Se implementa polimorfismo al sobrescribir __str__ para adaptar la salida textual a cada tipo de objeto.

# 4. Implementación en Python

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)         # delega la inicialización de atributos a la superclase
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"


class Tripulante(Empleado):
    ROLES_VALIDOS = ("piloto", "copiloto", "azafata")

    def __init__(self, nombre, cedula, codigo_emp, salario, rol):
        super().__init__(nombre, cedula, codigo_emp, salario)
        rol_limpio = rol.strip().lower()
        if rol_limpio not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido '{rol}'. Roles permitidos: {', '.join(self.ROLES_VALIDOS)}")
        self.rol = rol_limpio
        self.horas_vuelo = 0.0

    def registrar_horas_vuelo(self, horas):
        if horas > 0:
            self.horas_vuelo += horas

    def __str__(self):
        return (
            f"Tripulante {self.nombre} [{self.codigo_emp}] · Rol: {self.rol} · "
            f"{self.horas_vuelo:.1f} h · ${self.salario:.2f}"
        )


# --- Ejemplos de ejecución ---
p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)
t = Tripulante("Carlos", "0955512345", "TRIP-04", 2500, "piloto")

p.sumar_millas(500)
e.aumentar_salario(10)
t.registrar_horas_vuelo(12.5)
t.aumentar_salario(5)

# Todas las instancias comparten el método presentarse() heredado de Persona:
p.presentarse()                                 
e.presentarse()                                   
t.presentarse()                                   

# Sin embargo, cada clase responde de forma distinta al invocar __str__:
print(p)                                         
print(e)                                         
print(t)                                         

