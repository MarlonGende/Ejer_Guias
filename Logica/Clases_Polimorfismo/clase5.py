from abc import ABC, abstractmethod

# EJERCICIO: Superclase abstracta Empleado(nombre) con el método abstracto sueldo_mensual(), subclase EmpleadoPorHoras que computa la remuneración multiplicando horas laboradas por tarifa, y subclase EmpleadoFijo con salario constante, incorporando una extensión adicional en la jerarquía.

# 1. Análisis del problema
# Datos de entrada: Nombre del trabajador, cantidad de horas laboradas y valor por hora para personal por horas, salario mensual base para personal fijo, y parámetros para determinar comisiones.
# Procesamiento: Declarar la superclase abstracta Empleado con el contrato abstracto sueldo_mensual(), desarrollar EmpleadoPorHoras y EmpleadoFijo satisfaciendo dicho contrato, e incorporar un método resumen_pago() junto con la subclase EmpleadoComision para extender el esquema salarial.
# Resultado esperado: Remuneración mensual obtenida y detalle de pago de cada trabajador impresos en pantalla.

# 2. Diseño en pseudocódigo
# Importar ABC y abstractmethod del módulo abc
# Declarar superclase abstracta Empleado(ABC) con propiedad nombre y firma @abstractmethod sueldo_mensual()
# Incorporar la función resumen_pago() en Empleado para imprimir nombre y remuneración obtenida
# Definir EmpleadoPorHoras(Empleado) con horas_trabajadas y tarifa_hora, retornando horas * tarifa en sueldo_mensual()
# Definir EmpleadoFijo(Empleado) con sueldo_fijo, devolviendo self.sueldo_fijo en sueldo_mensual()
# Se incorpora la subclase EmpleadoComision(Empleado) con sueldo_base, ventas y porcentaje_comision
# Crear instancias de los distintos trabajadores e imprimir su salario mensual y resumen de pago

# 3. Identificación de la lógica
# Se implementa abstracción con ABC y @abstractmethod para exigir que toda clase derivada codifique sueldo_mensual().
# Se emplea polimorfismo al manipular diversas categorías de trabajadores bajo la firma uniforme sueldo_mensual().
# Se aprovecha la superclase Empleado para añadir nuevas modalidades salariales sin modificar las ya existentes.

# 4. Implementación en Python

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def sueldo_mensual(self):
        pass

    # Se incorpora el método resumen_pago para imprimir el desglose salarial mensual del trabajador
    def resumen_pago(self):
        print(f"Empleado: {self.nombre} | Sueldo mensual: ${self.sueldo_mensual():.2f}")


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def sueldo_mensual(self):
        return self.horas_trabajadas * self.tarifa_hora


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo_fijo):
        super().__init__(nombre)
        self.sueldo_fijo = sueldo_fijo

    def sueldo_mensual(self):
        return self.sueldo_fijo


# Se añade la subclase EmpleadoComision derivada de Empleado codificando sueldo_mensual
class EmpleadoComision(Empleado):
    def __init__(self, nombre, sueldo_base, ventas, porcentaje_comision):
        super().__init__(nombre)
        self.sueldo_base = sueldo_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def sueldo_mensual(self):
        return self.sueldo_base + (self.ventas * self.porcentaje_comision / 100)


# --- Ejemplos de ejecución ---
emp_horas = EmpleadoPorHoras("Carla", 160, 12.5)
emp_fijo = EmpleadoFijo("Mateo", 1100)
# Se crea un objeto EmpleadoComision para validar la nueva clase derivada
emp_comision = EmpleadoComision("Valeria", 600, 5000, 8)

empleados = [emp_horas, emp_fijo, emp_comision]

for emp in empleados:
    # Se invoca el método resumen_pago durante la iteración polimórfica
    emp.resumen_pago()
