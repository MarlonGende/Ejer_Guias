import math

# EJERCICIO 38: Superclase Figura con los métodos area() y perimetro(). Subclases
# Rectangulo, Circulo, Triangulo y Cuadrado (derivada de Rectangulo) aplicadas de forma polimórfica.

# 1. Análisis del problema
# Datos de entrada: Medidas geométricas correspondientes a cada figura (base y altura en Rectangulo y Triangulo,
# radio en Circulo, lado en Cuadrado, y lados extra en Triangulo para obtener el perímetro completo).
# [MEJORA] Se añade perimetro() a la definición base y a los resultados de la jerarquía de figuras.
# Procesamiento: Declarar en Figura los métodos area() y perimetro() lanzando NotImplementedError,
# sobrescribirlos en Rectangulo, Circulo, Triangulo y Cuadrado (subclase de Rectangulo),
# e iterar sobre una lista polimórfica de figuras computando sus áreas y perímetros.
# Resultado esperado: Imprimir en pantalla el área y perímetro individual de cada figura, junto con la suma total de áreas.

# 2. Diseño en pseudocódigo
# Importar el módulo math para emplear math.pi y math.hypot
# En Figura, declarar area() y perimetro() generando NotImplementedError
# Codificar area() y perimetro() en Rectangulo(Figura)
# Codificar area() y perimetro() en Circulo(Figura)
# Codificar area() y perimetro() en Triangulo(Figura)
# [MEJORA] Incorporar en el diseño la clase Cuadrado(Rectangulo) delegando el constructor a super()
# Validar el polimorfismo recorriendo una colección de figuras e imprimiendo area() y perimetro()
# Obtener e imprimir la sumatoria de áreas acumulando f.area()

# 3. Identificación de la lógica
# Se implementa polimorfismo: múltiples clases responden a las mismas firmas (area() y perimetro()) aplicando su propia ecuación.
# Se integra herencia simple y multinivel (Figura -> Rectangulo -> Cuadrado) para aprovechar lógica previa sin redundancia.
# Se unifica la interfaz común directamente en la superclase Figura.

# 4. Implementación en Python

class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

    # [MEJORA] Se incorpora la firma base perimetro() dentro de Figura
    def perimetro(self):
        raise NotImplementedError("Cada figura debe implementar perimetro()")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    # [MEJORA] Se define el cálculo de perimetro() en Rectangulo
    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    # [MEJORA] Se define el cálculo de perimetro() (longitud de circunferencia) en Circulo
    def perimetro(self):
        return 2 * math.pi * self.radio


class Triangulo(Figura):
    def __init__(self, base, altura, lado2=None, lado3=None):
        self.base = base
        self.altura = altura
        # [MEJORA] Se incorporan parámetros opcionales para los demás lados con el fin de computar el perímetro
        self.lado2 = lado2 if lado2 is not None else altura
        self.lado3 = lado3 if lado3 is not None else math.hypot(base, altura)

    def area(self):
        return (self.base * self.altura) / 2

    # [MEJORA] Se define el cálculo de perimetro() en Triangulo
    def perimetro(self):
        return self.base + self.lado2 + self.lado3


# [MEJORA] Se define la subclase Cuadrado derivada de Rectangulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.lado = lado


# --- Ejecución polimórfica ---
figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3),
    # [MEJORA] Se agrega un objeto Cuadrado dentro de la colección polimórfica
    Cuadrado(4)
]

for f in figuras:
    # [ACTUALIZACIÓN] Se muestran en consola tanto el área como el perímetro de cada elemento
    print(f"{type(f).__name__} -> Área: {f.area():.2f} | Perímetro: {f.perimetro():.2f}")

# También es posible acumular el área global de todas las figuras
total = sum(f.area() for f in figuras)
print(f"Área total: {total:.2f}")

