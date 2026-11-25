# EJERCICIO: Superclase Animal(nombre) con el método hablar() que imprime "(sonido)" y subclases que redefinen hablar() con su vocalización característica, incorporando una extensión adicional en la jerarquía.

# 1. Análisis del problema
# Datos de entrada: Nombre identificativo de cada animal y la instrucción de vocalizar para cada objeto o colección de animales.
# Procesamiento: Declarar la superclase Animal con la propiedad nombre y el método hablar() que imprime "(sonido)", implementar subclases como Perro y Gato sobrescribiendo hablar(), e incorporar una nueva subclase Vaca junto con un método describir() en la clase padre.
# Resultado esperado: Salidas en consola mostrando la descripción y el sonido específico de cada animal.

# 2. Diseño en pseudocódigo
# Declarar la clase Animal con la propiedad nombre
# Implementar hablar() en Animal mostrando "(sonido)"
# Incorporar la función describir() en Animal para imprimir el nombre del ejemplar
# Definir Perro(Animal) redefiniendo hablar() con "Guau"
# Definir Gato(Animal) redefiniendo hablar() con "Miau"
# Se incorpora la subclase Vaca(Animal) redefiniendo hablar() con "Muu"
# Crear objetos de prueba e invocar describir() y hablar() sobre cada uno

# 3. Identificación de la lógica
# Se implementa polimorfismo a través de la sobrescritura de métodos (method overriding) en las clases derivadas de Animal.
# La firma común hablar() se adapta según la especie concreta sin modificar la interfaz de invocación.
# Se aprovechan tanto el atributo nombre como la funcionalidad base por medio de herencia.

# 4. Implementación en Python

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("(sonido)")

    # Se incorpora el método describir para imprimir el nombre identificativo del animal
    def describir(self):
        print(f"Animal llamado {self.nombre}")


class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Guau")


class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Miau")


# Se añade la subclase Vaca derivada de Animal redefiniendo el comportamiento de hablar
class Vaca(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Muu")


# --- Ejemplos de ejecución ---
generico = Animal("Criatura")
perro = Perro("Rex")
gato = Gato("Michi")
# Se instancia un objeto de tipo Vaca para validar la extensión de la jerarquía
vaca = Vaca("Lola")

animales = [generico, perro, gato, vaca]

for a in animales:
    a.describir()
    a.hablar()
