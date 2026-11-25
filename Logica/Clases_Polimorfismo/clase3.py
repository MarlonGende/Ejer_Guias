# EJERCICIO: Superclase Vehiculo(marca, modelo) junto con las subclases Auto (puertas) y Moto (cilindraje), incorporando en cada una su propio __str__ y una propiedad o método extra.

# 1. Análisis del problema
# Datos de entrada: Marca y modelo del transporte, número de puertas en Auto, cilindrada en Moto e información operativa como el kilometraje.
# Procesamiento: Declarar la superclase Vehiculo con propiedades generales y comportamiento compartido, derivar Auto y Moto empleando super().__init__(), sobrescribir __str__ en cada subclase e incorporar una función para acumular distancia y reflejar su estado.
# Resultado esperado: Descripción formateada de cada vehículo y el progreso de su odómetro impresos en pantalla.

# 2. Diseño en pseudocódigo
# Definir la clase Vehiculo con marca, modelo y kilometraje inicializado en 0
# Incorporar la función recorrer(km) en Vehiculo para acumular distancias válidas
# Definir la subclase Auto(Vehiculo) con la propiedad puertas y su representación __str__
# Definir la subclase Moto(Vehiculo) con la propiedad cilindraje y su representación __str__
# Crear instancias de Auto y Moto, incrementar sus kilómetros y mostrar ambas por consola

# 3. Identificación de la lógica
# Se emplea herencia simple de Vehiculo hacia Auto y Moto para aprovechar marca, modelo y lógica compartida.
# Cada clase derivada personaliza __str__ para exponer sus rasgos distintivos como puertas o cilindrada.
# Se incorpora un comportamiento común en la superclase para ampliar capacidades sin redundancia de código.

# 4. Implementación en Python

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Se incorpora el atributo kilometraje para controlar la distancia acumulada
        self.kilometraje = 0

    # Se implementa el método recorrer para añadir kilómetros positivos al odómetro
    def recorrer(self, km):
        if km > 0:
            self.kilometraje += km

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.kilometraje} km)"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo}, {self.puertas} puertas, {self.kilometraje} km"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo}, {self.cilindraje} cc, {self.kilometraje} km"


# --- Ejemplos de ejecución ---
auto1 = Auto("Toyota", "Corolla", 4)
moto1 = Moto("Yamaha", "MT-07", 689)

# Se invoca el método recorrer para incrementar el odómetro de cada unidad
auto1.recorrer(150)
moto1.recorrer(85)

print(auto1)
print(moto1)

