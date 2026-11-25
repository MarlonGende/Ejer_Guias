# USO DEL PARÁMETRO KEY EN PYTHON

# El parámetro key actúa como el criterio bajo el cual se comparan los elementos.
#
# Suele emplearse en funciones integradas tales como:
#
# - max()
# - min()
# - sorted()
#
# con el fin de indicarle al intérprete:
#
# "¿Qué atributo o valor específico debe tomarse en cuenta al comparar?"

# CASO PRÁCTICO:
def libro_mas_largo(self):

    if len(self.libros) == 0:
        return None

    return max(self.libros, key=self.libros.get)

# -------------------------------------------------

# CASO PRÁCTICO SIN EL PARÁMETRO KEY

numeros = [5, 10, 2, 8]

mayor = max(numeros)

print(mayor)

# El intérprete evalúa los valores numéricos de manera directa:
#
# 5, 10, 2, 8
#
# Valor obtenido:
# 10


# -------------------------------------------------

# CASO PRÁCTICO EMPLEANDO KEY

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Monitor", "precio": 300}
]


producto_caro = max(
    productos,
    key=lambda producto: producto["precio"]
)


print(producto_caro)


# En este caso no se comparan los diccionarios en su totalidad.
#
# Se apoya en key para identificar el campo exacto a evaluar.
#
# La función anónima extrae:
#
# Laptop  -> 850
# Mouse   -> 25
# Monitor -> 300
#
# De este modo, max() evalúa:
#
# 850, 25, 300
#
# y retorna el artículo cuyo precio resulte más alto.


# -------------------------------------------------

# Sin especificar key, el intérprete desconoce qué criterio aplicar:

# Caso práctico:

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25}
]


# max(productos)
#
# Carece de una regla definida de comparación:
#
# ¿Debe evaluar por nombre?
# ¿Debe evaluar por precio?
# ¿Debe comparar la estructura completa?


# Por tal motivo se emplea:

max(
    productos,
    key=lambda producto: producto["precio"]
)


# -------------------------------------------------

# EMPLEO DE KEY JUNTO A SORTED()

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 18},
    {"nombre": "Carlos", "edad": 30}
]


ordenadas = sorted(
    personas,
    key=lambda persona: persona["edad"]
)


# Clasifica tomando como referencia la edad:
#
# Luis   18
# Ana    25
# Carlos 30


# -------------------------------------------------

# SÍNTESIS:
#
# key = "toma este dato como referencia de comparación"
#
# Caso práctico:
#
# max(lista, key=lambda x: x["precio"])
#
# se interpreta como:
#
# "Localiza el ítem de mayor valor,
# tomando el precio como criterio de decisión."

# FUNCIONES ANÓNIMAS (LAMBDA) EN PYTHON

# Una expresión lambda permite definir funciones breves
# en una única instrucción.
#
# Sintaxis general:
#
# lambda parametros: resultado
#
# Caso práctico:

duplicar = lambda numero: numero * 2

print(duplicar(5))

# Resultado en consola:
# 10
#
# Su comportamiento equivale a declarar una función convencional:

def duplicar(numero):
    return numero * 2


# -------------------------------------------------

# APLICACIÓN HABITUAL DE LAMBDA:
#
# Las expresiones lambda resultan ideales cuando un método
# requiere una función auxiliar de uso inmediato.
#
# Aplicación junto a max():

productos = [
    {"nombre": "Laptop", "precio": 850},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Monitor", "precio": 300}
]


producto_caro = max(
    productos,
    key=lambda producto: producto["precio"]
)


print(producto_caro)


# ¿Cómo se interpreta?
#
# La función max() requiere conocer qué dato evaluar.
#
# Cada ítem de la colección es un diccionario:
#
# {
# "nombre": "Laptop",
# "precio": 850
# }
#
# Por ello se especifica:
#
# lambda producto: producto["precio"]
#
# Lo cual equivale a indicar:
#
# "Toma cada artículo y extrae su precio
# para emplearlo como base de comparación."


# Internamente, el intérprete realiza una asociación equivalente a:

# Laptop  -> 850
# Mouse   -> 25
# Monitor -> 300
#
# Posteriormente, max() coteja dichos montos
# y retorna el artículo con el valor más elevado.


# -------------------------------------------------

# APLICACIÓN JUNTO A MIN()

producto_barato = min(
    productos,
    key=lambda producto: producto["precio"]
)


# Retorna:
# {"nombre": "Mouse", "precio": 25}


# -------------------------------------------------

# APLICACIÓN JUNTO A sorted()

productos_ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"]
)


# Clasifica los artículos de forma ascendente según su precio.


# Para obtener un ordenamiento descendente:

productos_ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"],
    reverse=True
)


# -------------------------------------------------

# CASO PRÁCTICO CON LISTAS SIMPLES

numeros = [5, 10, 2, 8]

mayor_cuadrado = max(
    numeros,
    key=lambda numero: numero ** 2
)


# Evalúa cada número tomando en cuenta su potencia al cuadrado:
#
# 5  -> 25
# 10 -> 100
# 2  -> 4
# 8  -> 64
#
# Valor obtenido:
# 10


# -------------------------------------------------

# PAUTA CLAVE PARA RECORDAR:
#
# Siempre que encuentres:
#
# key=lambda x: algo
#
# Interprétalo como:
#
# "Toma determinado atributo de cada elemento como criterio."
#
#
# Casos prácticos:
#
# max(personas, key=lambda p: p["edad"])
#
# Localiza a la persona de mayor edad.
#
#
# min(productos, key=lambda p: p["precio"])
#
# Encuentra el artículo de menor costo.
#
#
# sorted(nombres, key=lambda n: len(n))
#
# Clasifica los nombres de acuerdo con su cantidad de caracteres.

class NumeroPrimo:

    # Propiedad de clase (compartida entre todas las instancias creadas)
    primos_verificados = []

    def __init__(self):
        self.historial = []

    def es_primo(self, numero):

        self.historial.append(numero)

        primo = True

        if numero < 2:
            primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

        if primo:
            NumeroPrimo.primos_verificados.append(numero)

        return primo

    def primos_en_rango(self, *args):

        primos = []

        for numero in args:

            if self.es_primo(numero):
                primos.append(numero)

        return primos

    def cantidad_verificados(self):

        return len(self.historial)

    def obtener_primos_verificados(self):

        return NumeroPrimo.primos_verificados


obj = NumeroPrimo()

print(obj.es_primo(7))
print(obj.es_primo(10))

print(obj.primos_en_rango(11, 12, 13, 14, 15, 16, 17))

print("Historial:", obj.historial)
print("Cantidad verificados:", obj.cantidad_verificados())
print("Primos verificados:", obj.obtener_primos_verificados())

# PRÁCTICA 1: Control y promedio de calificaciones
# Implementar la clase Calificador con: (1) un método validar_nota(nota) que devuelva True cuando 0 ≤ nota ≤ 100, False en caso contrario
# (2) incorpore el método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista
# (3) cuente con el método promedio() que devuelva el promedio de notas almacenadas.

class Calificador:

    def __init__ (self):
        self.notas = []

    def validar_nota(self, nota):
        return 0<= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas      
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas)/len(self.notas)

estudiante1 = Calificador()
estudiante1.cargar_notas(90,-67,78,90,78,96)
print(estudiante1.notas)
print(estudiante1.promedio())



# 1. Suprimir una calificación puntual
# Suprime una calificación puntual siempre que se encuentre registrada.

def eliminar_nota(self, nota):

    if nota in self.notas:
        self.notas.remove(nota)



# 2. Limpiar el registro completo de calificaciones
# Vacía por completo el registro de calificaciones.

def limpiar_notas(self):

    self.notas.clear()



# 3. Consultar la calificación máxima
# Retorna la calificación más alta registrada.

def nota_maxima(self):

    if len(self.notas) == 0:
        return 0

    return max(self.notas)


# ==========================================================
# 4. Consultar la calificación mínima
# ==========================================================
# Retorna la calificación más baja registrada.

def nota_minima(self):

    if len(self.notas) == 0:
        return 0

    return min(self.notas)


# ==========================================================
# 5. Obtener el total de calificaciones registradas
# ==========================================================
# Retorna el total de notas almacenadas.

def cantidad_notas(self):

    return len(self.notas)


# ==========================================================
# 6. Evaluar si el alumno alcanza la aprobación
# ==========================================================
# Retorna True en caso de que el promedio es mayor o igual a 70.

def aprobado(self):

    return self.promedio() >= 70


# ==========================================================
# 7. Verificar la presencia de una calificación
# ==========================================================
# Retorna True en caso de que la nota está almacenada.

def buscar_nota(self, nota):

    return nota in self.notas


# ==========================================================
# 8. Clasificar las calificaciones en orden ascendente
# ==========================================================
# Clasifica las calificaciones en orden ascendente.

def ordenar_notas(self):

    self.notas.sort()


# ==========================================================
# 9. Clasificar las calificaciones en orden descendente
# ==========================================================
# Clasifica las calificaciones en orden descendente.

def ordenar_descendente(self):

    self.notas.sort(reverse=True)


# ==========================================================
# 10. Desplegar el listado completo de calificaciones
# ==========================================================
# Retorna la colección íntegra.

def mostrar_notas(self):

    return self.notas


# ==========================================================
# 11. Calcular la sumatoria total de calificaciones
# ==========================================================
# Retorna la sumatoria completa.

def suma_notas(self):

    return sum(self.notas)


# ==========================================================
# 12. Actualizar el valor de una calificación existente
# ==========================================================
# Localiza una calificación existente y la sustituye por otra.

def reemplazar_nota(self, vieja, nueva):

    if vieja in self.notas and self.validar_nota(nueva):

        indice = self.notas.index(vieja)
        self.notas[indice] = nueva


# ==========================================================
# 13. Incorporar una calificación individual
# ==========================================================
# Análogo a cargar_notas(), pero procesando un único valor.

def agregar_nota(self, nota):

    if self.validar_nota(nota):

        self.notas.append(nota)


# ==========================================================
# 14. Contabilizar calificaciones aprobatorias
# ==========================================================
# Contabiliza el número de notas son mayores o iguales a 70.

def contar_aprobadas(self):

    contador = 0

    for nota in self.notas:

        if nota >= 70:
            contador += 1

    return contador


# ==========================================================
# 15. Contabilizar calificaciones reprobatorias
# ==========================================================
# Contabiliza el número de notas son menores a 70.

def contar_reprobadas(self):

    contador = 0

    for nota in self.notas:

        if nota < 70:
            contador += 1

    return contador


# ==========================================================
# 16. Filtrar y obtener únicamente calificaciones aprobadas
# ==========================================================
# Retorna una colección con notas >= 70.

def notas_aprobadas(self):

    lista = []

    for nota in self.notas:

        if nota >= 70:
            lista.append(nota)

    return lista


# ==========================================================
# 17. Filtrar y obtener únicamente calificaciones reprobadas
# ==========================================================
# Retorna una colección con notas < 70.

def notas_reprobadas(self):

    lista = []

    for nota in self.notas:

        if nota < 70:
            lista.append(nota)

    return lista


# ==========================================================
# 18. Determinar la tasa porcentual de aprobación
# ==========================================================
# Retorna la proporción porcentual de notas aprobadas.

def porcentaje_aprobacion(self):

    if len(self.notas) == 0:
        return 0

    return self.contar_aprobadas() * 100 / len(self.notas)


# ==========================================================
# 19. Generar un reporte resumido de calificaciones
# ==========================================================
# Retorna una estructura clave-valor con información importante.

def resumen(self):

    return {
        "cantidad": len(self.notas),
        "promedio": self.promedio(),
        "maxima": self.nota_maxima(),
        "minima": self.nota_minima()
    }


# 20. Restablecer el estado inicial de la instancia

# Suprime la totalidad de calificaciones almacenadas.

def reiniciar(self):

    self.notas = []

# Contador de palabras únicas
# Implementar la clase AnalizadorTexto de modo que:
# (1) disponga del método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden)
# (2) incorpore el método contar_palabras() que devuelva cuántas palabras únicas hay
# (3) cuente con el método agregar_multiples(*args) que reutilice agregar_palabra para varios.

class AnalizarTexto:
    def __init__(self):
        self.palabra_conjunto = set()
        self.palabra_lista = []

    def agregar_palabra(self, palabra):
        self.palabra_conjunto.add(palabra)
        self.palabra_lista.append(palabra)

    def contar_palabras_unicas(self):
        return len(self.palabra_conjunto)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

        return self.palabra_lista

texto = AnalizarTexto()

texto.agregar_multiples("hola", "python", "hola", "clase")

print(texto.palabra_lista)
print(texto.palabra_conjunto)
print(texto.contar_palabras_unicas())


# 1. Función de clase para comprobar si una palabra existe
# Comprueba si el término ya se encuentra registrado en el set

def existe_palabra(self, palabra):
    return palabra in self.palabra_conjunto


# 2. Función de clase para suprimir una palabra
# Suprime el término tanto del conjunto como de la lista

def eliminar_palabra(self, palabra):
    if palabra in self.palabra_conjunto:
        self.palabra_conjunto.remove(palabra)

    if palabra in self.palabra_lista:
        self.palabra_lista.remove(palabra)


# 3. Función de clase para contabilizar todas las palabras ingresadas
# Contabiliza el total de términos sin excluir duplicados

def contar_total_palabras(self):
    return len(self.palabra_lista)


# 4. Función de clase para desplegar todas las palabras sin repetir
# Retorna los ítems del conjunto en formato de lista

def mostrar_unicas(self):
    return list(self.palabra_conjunto)


# 5. Función de clase para vaciar todos los datos
# Limpia simultáneamente la lista y el conjunto

def limpiar_texto(self):
    self.palabra_conjunto.clear()
    self.palabra_lista.clear()


# 6. Función de clase para transformar todas las palabras a minúsculas
# Unifica la capitalización para evitar duplicados por mayúsculas

def convertir_minusculas(self):
    self.palabra_lista = [palabra.lower() for palabra in self.palabra_lista]
    self.palabra_conjunto = set(self.palabra_lista)


# 7. Función de clase para localizar palabras por letra inicial
# Retorna los términos que comienzan con una letra específica

def buscar_por_letra(self, letra):
    resultado = []

    for palabra in self.palabra_lista:
        if palabra.startswith(letra):
            resultado.append(palabra)

    return resultado


# 8. Función de clase para contabilizar cuántas veces aparece una palabra
# Se apoya en la lista dado que el conjunto descarta repeticiones

def frecuencia_palabra(self, palabra):
    return self.palabra_lista.count(palabra)


# 9. Función de clase para extraer la palabra más larga

def palabra_mas_larga(self):
    if len(self.palabra_lista) == 0:
        return ""

    return max(self.palabra_lista, key=len)


# 10. Función de clase para clasificar palabras alfabéticamente

def ordenar_palabras(self):
    return sorted(self.palabra_lista)

class CarroCompras: 
    def __init__(self): 
        self.productos = dict() 

    def agregar_articulo(self, nombre, precio): 
        self.productos[nombre] = precio 

    def total_carrito(self): 
        return sum(self.productos.values()) 

    def articulos_por_rango(self, minimo, maximo): 
        rango_precio = [] 

        for nombre, precio in self.productos.items(): 
            if minimo <= precio <= maximo: 
                rango_precio.append(nombre) 

        return rango_precio 


producto1 = CarroCompras()

producto1.agregar_articulo("Arroz", 45)
producto1.agregar_articulo("Laptop", 800)
producto1.agregar_articulo("Mouse", 20)

print(producto1.total_carrito())

# VARIANTE 1: Eliminar un articulo
# Borra un artículo del registro identificándolo por su nombre.

def eliminar_articulo(self, nombre):
    if nombre in self.productos:
        del self.productos[nombre]
        return True
    return False


# VARIANTE 2: Actualizar precio
# Actualiza el costo de un artículo registrado.

def actualizar_precio(self, nombre, nuevo_precio):
    if nombre in self.productos:
        self.productos[nombre] = nuevo_precio
        return True
    return False


# VARIANTE 3: Buscar producto
# Verifica si un producto existe en el diccionario.

def buscar_producto(self, nombre):
    return nombre in self.productos


# VARIANTE 4: Cantidad de artículos
# Retorna el número de productos registrados.

def cantidad_articulos(self):
    return len(self.productos)


# VARIANTE 5: Producto más caro
# Retorna el nombre del artículo de mayor precio.

def producto_mas_caro(self):
    if len(self.productos) == 0:
        return None

    return max(self.productos, key=self.productos.get)


# VARIANTE 6: Producto más barato
# Retorna el nombre del artículo de menor precio.

def producto_mas_barato(self):
    if len(self.productos) == 0:
        return None

    return min(self.productos, key=self.productos.get)


# VARIANTE 7: Mostrar productos
# Imprime cada artículo junto con su valor respectivo.

def mostrar_productos(self):
    for nombre, precio in self.productos.items():
        print(nombre, precio)


# VARIANTE 8: Promedio de precios
# Determina la media de precios del catálogo.

def promedio_precios(self):
    if len(self.productos) == 0:
        return 0

    return sum(self.productos.values()) / len(self.productos)


# VARIANTE 9: Aplicar rebaja porcentual
# Aplica una rebaja porcentual al costo de un artículo.

def aplicar_descuento(self, nombre, porcentaje):
    if nombre in self.productos:
        descuento = self.productos[nombre] * porcentaje / 100
        self.productos[nombre] -= descuento


# VARIANTE 10: Ordenar productos por precio
# Retorna los artículos clasificados de menor a mayor precio.

# Clasifica los artículos del diccionario por costo extrayendo pares clave-valor con items().
# La expresión lambda extrae el índice [1] de cada tupla (correspondiente al precio) como criterio de orden.

def ordenar_productos(self):
    return sorted(self.productos.items(), key=lambda producto: producto[1])

class InversorSecuencia:

    def invertir_lista(self, lista):

        lista_invertida = []

        for i in range(len(lista)-1, -1, -1):

            lista_invertida.append(lista[i])

        return lista_invertida


    def invertir_multiples(self, *listas):

        resultado = {}

        for lista in listas:

            invertida = self.invertir_lista(lista)

            resultado[tuple(lista)] = invertida

        return resultado

inversor = InversorSecuencia()


lista1 = [1, 2, 3, 4]

print(inversor.invertir_lista(lista1))

resultado = inversor.invertir_multiples(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(resultado)

# VARIANTE 1: Implementación de invertir_con_texto(lista)
# Revierte una lista y devuelve una cadena descriptiva del resultado.

def invertir_con_texto(self, lista):

    invertida = self.invertir_lista(lista)

    return f"La lista {lista} invertida es {invertida}"


# VARIANTE 2: Implementación de contar_elementos(lista)
# Retorna el número de elementos que tiene una lista.

def contar_elementos(self, lista):

    return len(lista)


# VARIANTE 3: Implementación de verificar_palindromo(lista)
# Verifica si una lista es igual al revés de sí misma.

def verificar_palindromo(self, lista):

    invertida = self.invertir_lista(lista)

    return lista == invertida


# VARIANTE 4: Implementación de invertir_desde_posicion(lista, posicion)
# Revierte un segmento de la lista a partir de un índice dado.

def invertir_desde_posicion(self, lista, posicion):

    resultado = []

    for i in range(posicion, -1, -1):

        resultado.append(lista[i])

    return resultado


# VARIANTE 5: Implementación de unir_listas(*listas)
# Concatena múltiples listas en una única colección.

def unir_listas(self, *listas):

    resultado = []

    for lista in listas:

        resultado.extend(lista)

    return resultado


# VARIANTE 6: Implementación de eliminar_repetidos(lista)
# Filtra valores duplicados apoyándose en un set y devuelve una lista.

def eliminar_repetidos(self, lista):

    return list(set(lista))


# VARIANTE 7: Implementación de mayor_elemento(lista)
# Retorna el valor máximo de una lista.

def mayor_elemento(self, lista):

    return max(lista)


# VARIANTE 8: Implementación de menor_elemento(lista)
# Retorna el valor mínimo de una lista.

def menor_elemento(self, lista):

    return min(lista)


# VARIANTE 9: Implementación de ordenar_lista(lista)
# Clasifica una lista en orden ascendente.

def ordenar_lista(self, lista):

    return sorted(lista)


# VARIANTE 10: Implementación de frecuencia_elementos(lista)
# Contabiliza la frecuencia de aparición de cada elemento usando un diccionario.

def frecuencia_elementos(self, lista):

    frecuencia = {}

    for elemento in lista:

        if elemento in frecuencia:
            frecuencia[elemento] += 1

        else:
            frecuencia[elemento] = 1

    return frecuencia


# VARIANTE 11: Implementación de separar_pares_impares(lista)
# Divide una secuencia numérica en sublistas de pares e impares.

def separar_pares_impares(self, lista):

    pares = []
    impares = []

    for numero in lista:

        if numero % 2 == 0:
            pares.append(numero)

        else:
            impares.append(numero)

    return pares, impares


# VARIANTE 12: Implementación de buscar_elemento(lista, elemento)
# Verifica si un elemento existe dentro de la lista.

def buscar_elemento(self, lista, elemento):

    return elemento in lista

# PRÁCTICA 5: Clasificación de valores pares e impares
# Implementar la clase AnalizadorNumeros con: (1) un método es_par(numero) que devuelva un valor booleano (True o False)
# (2) incorpore el método separar(*numeros) que devuelva un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par
# (3) cuente con el método cantidad_pares_impares() que devuelva una tupla (cant_pares, cant_impares).

class AnalizarNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        return False

    def separar(self, *numeros):

        diccionario = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:

            if self.es_par(numero):

                diccionario["pares"].append(numero)
                self.pares.append(numero)

            else:

                diccionario["impares"].append(numero)
                self.impares.append(numero)

        return diccionario

    def cantidad_pares_impares(self):

        return len(self.pares), len(self.impares)
                           

# VARIANTE 1: Implementación de suma_pares()
# Calcula la sumatoria de todos los números pares almacenados en la clase y retorna el resultado.

def suma_pares(self):

    return sum(self.pares)


# VARIANTE 2: Implementación de suma_impares()
# Calcula la sumatoria de todos los números impares almacenados en la clase y retorna el resultado.

def suma_impares(self):

    return sum(self.impares)


# VARIANTE 3: Implementación de mayor_numero()
# Retorna el valor numérico más alto entre todos los números ingresados.

def mayor_numero(self):

    todos = self.pares + self.impares

    return max(todos)


# VARIANTE 4: Implementación de menor_numero()
# Retorna el valor numérico más bajo entre todos los números ingresados.

def menor_numero(self):

    todos = self.pares + self.impares

    return min(todos)


# VARIANTE 5: Implementación de promedio()
# Obtiene la media aritmética del conjunto de números.

def promedio(self):

    todos = self.pares + self.impares

    return sum(todos) / len(todos)


# VARIANTE 6: Implementación de cantidad_total()
# Retorna el conteo global de números analizados.

def cantidad_total(self):

    return len(self.pares) + len(self.impares)


# VARIANTE 7: Implementación de buscar_numero(numero)
# Verifica si un número existe dentro de los pares o impares.

def buscar_numero(self, numero):

    return numero in self.pares or numero in self.impares


# VARIANTE 8: Implementación de limpiar_datos()
# Reinicia las colecciones numéricas internas.

def limpiar_datos(self):

    self.pares.clear()
    self.impares.clear()


# VARIANTE 9: Implementación de ordenar_numeros()
# Retorna la secuencia numérica clasificada de menor a mayor.

def ordenar_numeros(self):

    todos = self.pares + self.impares

    return sorted(todos)


# VARIANTE 10: Implementación de separar_negativos_positivos()
# Agrupa los valores según su signo (positivos y negativos).

def separar_negativos_positivos(self):

    positivos = []
    negativos = []

    todos = self.pares + self.impares

    for numero in todos:

        if numero >= 0:
            positivos.append(numero)

        else:
            negativos.append(numero)

    return {
        "positivos": positivos,
        "negativos": negativos
    }


# VARIANTE 11: Implementación de porcentaje_pares()
# Determina la proporción porcentual de valores pares.

def porcentaje_pares(self):

    total = len(self.pares) + len(self.impares)

    return (len(self.pares) / total) * 100


# VARIANTE 12: Implementación de frecuencia_numeros()
# Contabiliza la frecuencia de aparición de cada número utilizando un diccionario.

def frecuencia_numeros(self):

    frecuencia = {}

    todos = self.pares + self.impares

    for numero in todos:

        if numero in frecuencia:
            frecuencia[numero] += 1

        else:
            frecuencia[numero] = 1

    return frecuencia
# PRÁCTICA 6: Análisis estadístico de temperaturas
# Implementar la clase GestorTemperatura con: (1) un método registrar_temperatura(temp) que registre los valores en una lista
# (2) incorpore el método minima()`, `maxima()`, `promedio() que calculen estadísticas
# (3) cuente con el método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []


    def registrar_temperatura(self, temp):

        self.temperaturas.append(temp)


    def minima(self):

        return min(self.temperaturas)


    def maxima(self):

        return max(self.temperaturas)


    def promedio(self):

        return sum(self.temperaturas) / len(self.temperaturas)


    def registrar_multiples(self, *temps):

        for temp in temps:

            self.registrar_temperatura(temp)



# Datos de prueba para ejecución

clima = GestorTemperatura()

clima.registrar_temperatura(25)

clima.registrar_multiples(30, 18, 22, 27, 35)


print(clima.temperaturas)

print("Temperatura mínima:", clima.minima())

print("Temperatura máxima:", clima.maxima())

print("Promedio:", clima.promedio())

# VARIANTE 1: Implementación de temperatura_promedio_diaria()
# Obtiene la temperatura media correspondiente a una jornada.

def temperatura_promedio_diaria(self):

    return sum(self.temperaturas) / len(self.temperaturas)


# VARIANTE 2: Implementación de contar_temperaturas()
# Retorna el número de temperaturas registradas.

def contar_temperaturas(self):

    return len(self.temperaturas)


# VARIANTE 3: Implementación de eliminar_temperatura(temp)
# Suprime un registro térmico puntual de la colección.

def eliminar_temperatura(self, temp):

    if temp in self.temperaturas:
        self.temperaturas.remove(temp)


# VARIANTE 4: Implementación de buscar_temperatura(temp)
# Verifica si una temperatura existe dentro de los registros.

def buscar_temperatura(self, temp):

    return temp in self.temperaturas


# VARIANTE 5: Implementación de ordenar_temperaturas()
# Clasifica los registros térmicos en orden ascendente.

def ordenar_temperaturas(self):

    return sorted(self.temperaturas)


# VARIANTE 6: Implementación de rango_temperatura()
# Retorna la amplitud o resta entre la temperatura máxima y mínima.

def rango_temperatura(self):

    return max(self.temperaturas) - min(self.temperaturas)


# VARIANTE 7: Implementación de clasificar_temperaturas()
# Clasifica las lecturas térmicas respecto a un umbral dado.

def clasificar_temperaturas(self, limite):

    altas = []
    bajas = []

    for temp in self.temperaturas:

        if temp >= limite:
            altas.append(temp)

        else:
            bajas.append(temp)

    return {
        "altas": altas,
        "bajas": bajas
    }


# VARIANTE 8: Implementación de convertir_fahrenheit()
# Convierte todas las temperaturas Celsius a Fahrenheit.

def convertir_fahrenheit(self):

    resultado = []

    for temp in self.temperaturas:

        fahrenheit = (temp * 9/5) + 32

        resultado.append(fahrenheit)

    return resultado


# VARIANTE 9: Implementación de temperatura_mas_repetida()
# Retorna la lectura térmica con mayor frecuencia.

def temperatura_mas_repetida(self):

    frecuencia = {}

    for temp in self.temperaturas:

        if temp in frecuencia:

            frecuencia[temp] += 1

        else:

            frecuencia[temp] = 1

    return max(frecuencia, key=frecuencia.get)


# VARIANTE 10: Implementación de limpiar_registros()
# Borra todos los registros térmicos guardados.

def limpiar_registros(self):

    self.temperaturas.clear()


# VARIANTE 11: Implementación de agregar_lista(lista)
# Incorpora múltiples lecturas térmicas recibidas como lista.

def agregar_lista(self, lista):

    for temp in lista:

        self.registrar_temperatura(temp)


# VARIANTE 12: Implementación de estado_clima()
# Retorna una síntesis de los datos registrados usando un diccionario.

def estado_clima(self):

    return {
        "minima": self.minima(),
        "maxima": self.maxima(),
        "promedio": self.promedio(),
        "cantidad": len(self.temperaturas)
    }

# PRÁCTICA 7: Registro y filtrado por edades
# Implementar la clase GestorPersonas con: (1) un método agregar_persona(nombre, edad) que almacene los datos en un diccionario
# (2) incorpore el método personas_mayores(edad_minima) que devuelva una lista de nombres cuya edad sea ≥
# (3) cuente con el método edad_promedio() que devuelva el promedio de edades.

class GestorPersonas: 
    def __init__(self):
        self.edades=[]
    def agregar_personas(self, nombre, edad):
        personas = {
            "nombre": "",
            "edad": 0
        }
        personas["nombre"]= nombre
        personas["edad"]= edad

        self.edades.append(personas)
    def personas_mayores(self, edad_minima):
        mayores = []
        for persona in self.edades:
            if persona["edad"] >= edad_minima:
                mayores.append(persona["nombre"])
        return mayores
    def edad_promedio(self):
        if len(self.edades) == 0:
            return 0
        
        suma = 0
        
        for persona in self.edades:
            suma += persona["edad"]
        return suma / len(self.edades)

# VARIANTE 1: Implementación de buscar_persona()
# Localiza a una persona por nombre y devuelve su registro.

def buscar_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            return persona

    return None


# VARIANTE 2: Implementación de eliminar_persona()
# Suprime el registro de una persona buscando por su nombre.

def eliminar_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            self.edades.remove(persona)

            return True

    return False


# VARIANTE 3: Implementación de actualizar_edad()
# Actualiza el valor de edad de un registro.

def actualizar_edad(self, nombre, nueva_edad):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            persona["edad"] = nueva_edad

            return True

    return False


# VARIANTE 4: Implementación de contar_personas()
# Retorna el número de personas registradas.

def contar_personas(self):

    return len(self.edades)


# VARIANTE 5: Implementación de persona_mayor()
# Retorna el registro de la persona de mayor edad.

def persona_mayor(self):

    return max(self.edades, key=lambda persona: persona["edad"])


# VARIANTE 6: Implementación de persona_menor()
# Retorna el registro de la persona de menor edad.

def persona_menor(self):

    return min(self.edades, key=lambda persona: persona["edad"])


# VARIANTE 7: Implementación de ordenar_por_edad()
# Clasifica a las personas de forma ascendente según su edad.

def ordenar_por_edad(self):

    return sorted(self.edades, key=lambda persona: persona["edad"])


# VARIANTE 8: Implementación de ordenar_por_nombre()
# Clasifica los registros de personas en orden alfabético.

def ordenar_por_nombre(self):

    return sorted(self.edades, key=lambda persona: persona["nombre"])


# VARIANTE 9: Implementación de mayores_de_edad()
# Retorna exclusivamente las personas de 18 años o más.

def mayores_de_edad(self):

    resultado = []

    for persona in self.edades:

        if persona["edad"] >= 18:

            resultado.append(persona)

    return resultado


# VARIANTE 10: Implementación de menores_de_edad()
# Retorna exclusivamente las personas menores de 18 años.

def menores_de_edad(self):

    resultado = []

    for persona in self.edades:

        if persona["edad"] < 18:

            resultado.append(persona)

    return resultado


# VARIANTE 11: Implementación de existe_persona()
# Verifica si una persona ya está registrada.

def existe_persona(self, nombre):

    for persona in self.edades:

        if persona["nombre"] == nombre:

            return True

    return False


# VARIANTE 12: Implementación de limpiar_personas()
# Borra el registro completo de personas.

def limpiar_personas(self):

    self.edades.clear()

# PRÁCTICA 8: Gestión de equipos y participantes
# Implementar la clase Equipos con: (1) un método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario
# (2) incorpore el método agregar_jugador(equipo, jugador) que añada el jugador al equipo
# (3) cuente con el método equipo_mayor_integrantes() que devuelva el nombre del equipo con más jugadores.

class Equipos:

    def __init__(self):

        self.equipos = {}

    def crear_equipo(self, equipo):

        self.equipos[equipo] = []

    def agregar_jugador(self, equipo, jugador):

        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):

        mayor = ""
        cantidad = 0

        for equipo, jugadores in self.equipos.items():

            if len(jugadores) > cantidad:

                cantidad = len(jugadores)

                mayor = equipo

        return mayor

# VARIANTE 1: Implementación de eliminar_jugador(equipo, jugador)
# Retira a un participante determinado de su equipo.

def eliminar_jugador(self, equipo, jugador):

    if jugador in self.equipos[equipo]:

        self.equipos[equipo].remove(jugador)

        return True

    return False


# VARIANTE 2: Implementación de cantidad_jugadores(equipo)
# Retorna el número de jugadores que tiene un equipo.

def cantidad_jugadores(self, equipo):

    return len(self.equipos[equipo])


# VARIANTE 3: Implementación de listar_jugadores(equipo)
# Retorna el listado de jugadores de un equipo.

def listar_jugadores(self, equipo):

    return self.equipos[equipo]


# VARIANTE 4: Implementación de buscar_jugador(jugador)
# Localiza el equipo al que pertenece un participante.

def buscar_jugador(self, jugador):

    for equipo, jugadores in self.equipos.items():

        if jugador in jugadores:

            return equipo

    return None


# VARIANTE 5: Implementación de eliminar_equipo(nombre_equipo)
# Suprime el registro íntegro de un equipo.

def eliminar_equipo(self, equipo):

    if equipo in self.equipos:

        del self.equipos[equipo]

        return True

    return False


# VARIANTE 6: Implementación de cantidad_equipos()
# Retorna el total de equipos existen.

def cantidad_equipos(self):

    return len(self.equipos)


# VARIANTE 7: Implementación de equipos_con_mas_jugadores(cantidad)
# Retorna equipos que tienen una cantidad mínima de jugadores.

def equipos_con_mas_jugadores(self, cantidad):

    resultado = []

    for equipo, jugadores in self.equipos.items():

        if len(jugadores) >= cantidad:

            resultado.append(equipo)

    return resultado


# VARIANTE 8: Implementación de ordenar_equipos()
# Retorna los equipos clasificados por cantidad de jugadores.

def ordenar_equipos(self):

    return sorted(
        self.equipos.items(),
        key=lambda equipo: len(equipo[1]),
        reverse=True
    )


# VARIANTE 9: Implementación de transferir_jugador(jugador, equipo_actual, equipo_nuevo)
# Transfiere un participante desde su equipo actual hacia otro.

def transferir_jugador(self, jugador, equipo_actual, equipo_nuevo):

    if jugador in self.equipos[equipo_actual]:

        self.equipos[equipo_actual].remove(jugador)

        self.equipos[equipo_nuevo].append(jugador)

        return True

    return False


# VARIANTE 10: Implementación de equipo_menor_integrantes()
# Retorna el equipo con menos jugadores.

def equipo_menor_integrantes(self):

    menor = ""
    cantidad = float("inf")

    for equipo, jugadores in self.equipos.items():

        if len(jugadores) < cantidad:

            cantidad = len(jugadores)

            menor = equipo

    return menor

# PRÁCTICA 9: Análisis y clasificación de caracteres
# Implementar la clase AnalizadorString con: (1) un método solo_vocales(letra) que devuelva True cuando es vocal
# (2) incorpore el método contar_por_tipo(texto) que devuelva un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} apoyándose en los métodos previos;
# (3) conserve un atributo que registre el texto más largo analizado.

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        vocales = "aeiouAEIOU"
        return letra in vocales
    
    def contar_por_tipo(self, texto):
        contador = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
              }
        
        for letra in texto:
            if self.solo_vocales(letra):
                contador["vocales"] += 1
            elif letra.isdigit():
                contador["digitos"] += 1
            elif letra.isalpha():
                contador["consonantes"] += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        return contador

    # VARIANTE 1: Implementación de es_digito(numero)
# Evalúa de forma explícita si un carácter es un número.

def es_digito(self, letra):

    digitos = "0123456789"

    return letra in digitos


# VARIANTE 2: Implementación de es_letra(letra)
# Evalúa de forma explícita si un carácter pertenece al alfabeto.

def es_letra(self, letra):

    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return letra in letras


# VARIANTE 3: Implementación de es_consonante(letra)
# Determina si una letra es consonante apoyándose en los métodos previos;.

def es_consonante(self, letra):

    if self.es_letra(letra) and not self.solo_vocales(letra):

        return True

    return False



# VARIANTE 4: Reemplazar isdigit() e isalpha()
# Dentro de contar_por_tipo(), sustituir:

# elif letra.isdigit():

# por:

# elif self.es_digito(letra):


# Y cambiar:

# elif letra.isalpha():

# por:

# elif self.es_consonante(letra):



# VARIANTE 5: Implementación de contar_mayusculas()
# Contabiliza el número de letras mayúsculas tiene el texto.

def contar_mayusculas(self, texto):

    cantidad = 0

    for letra in texto:

        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            cantidad += 1

    return cantidad


# VARIANTE 6: Implementación de contar_minusculas()
# Contabiliza el número de letras minúsculas tiene el texto.

def contar_minusculas(self, texto):

    cantidad = 0

    for letra in texto:

        if letra in "abcdefghijklmnopqrstuvwxyz":

            cantidad += 1

    return cantidad


# VARIANTE 7: Implementación de eliminar_espacios()
# Retorna el texto sin espacios.

def eliminar_espacios(self, texto):

    nuevo_texto = ""

    for letra in texto:

        if letra != " ":

            nuevo_texto += letra

    return nuevo_texto


# VARIANTE 8: Implementación de invertir_texto()
# Revierte la cadena carácter por carácter sin usar reverse().

def invertir_texto(self, texto):

    invertido = ""

    for i in range(len(texto)-1, -1, -1):

        invertido += texto[i]

    return invertido

# VARIANTE 1: Implementación de cantidad_total_caracteres()
# Retorna el total de caracteres tiene el texto.

def cantidad_total_caracteres(self, texto):

    return len(texto)



# VARIANTE 2: Implementación de eliminar_espacios()
# Retorna un nuevo texto sin espacios.

def eliminar_espacios(self, texto):

    resultado = ""

    for letra in texto:

        if letra != " ":

            resultado += letra

    return resultado



# VARIANTE 3: Implementación de invertir_texto()
# Revierte un texto mediante iteración.

def invertir_texto(self, texto):

    invertido = ""

    for letra in texto:

        invertido = letra + invertido

    return invertido



# VARIANTE 4: Implementación de contar_caracter()
# Contabiliza la frecuencia de aparición de un carácter.

def contar_caracter(self, texto, caracter):

    contador = 0

    for letra in texto:

        if letra == caracter:

            contador += 1

    return contador



# VARIANTE 5: Implementación de frecuencia_caracteres()
# Contabiliza las apariciones de cada carácter en un diccionario.

def frecuencia_caracteres(self, texto):

    frecuencia = {}

    for letra in texto:

        if letra in frecuencia:

            frecuencia[letra] += 1

        else:

            frecuencia[letra] = 1

    return frecuencia



# VARIANTE 6: Implementación de guardar_textos()
# Mantiene un registro acumulativo de cadenas evaluadas.

def __init__(self):

    self.texto_mas_largo = ""

    self.textos = []



def guardar_texto(self, texto):

    self.textos.append(texto)



# VARIANTE 7: Implementación de texto_mas_repetido()
# Identifica la cadena con mayor frecuencia de registro.

def texto_mas_repetido(self):

    frecuencia = {}

    for texto in self.textos:

        if texto in frecuencia:

            frecuencia[texto] += 1

        else:

            frecuencia[texto] = 1

    return max(frecuencia, key=frecuencia.get)



# VARIANTE 8: Implementación de separar_caracteres()
# Clasifica caracteres alfabéticos y dígitos en listas independientes.

def separar_caracteres(self, texto):

    letras = []

    numeros = []

    for caracter in texto:

        if caracter in "0123456789":

            numeros.append(caracter)

        else:

            letras.append(caracter)

    return {
        "letras": letras,
        "numeros": numeros
    }
# PRÁCTICA 10: Administración de actividades por nivel de prioridad
# Implementar la clase Tareas con: (1) un método agregar_tarea(descripcion, prioridad) que registre los valores en una lista de tuplas (descripción, prioridad)
# (2) incorpore el método tareas_prioritarias() que devuelva solo las de prioridad alta
# (3) cuente con el método eliminar_completada(descripcion) que borre la tarea de la lista.
class Tareas:

    def __init__(self):

        self.lista_tuplas = []


    def agregar_tarea(self, descripcion, prioridad):

        tarea = (descripcion, prioridad)

        self.lista_tuplas.append(tarea)


    def tareas_prioritarias(self):

        prioritarias = []

        for descripcion, prioridad in self.lista_tuplas:

            if prioridad.lower() == "alta":

                prioritarias.append(descripcion)

        if len(prioritarias) == 0:

            return "No hay actividades con prioridad alta registradas"

        return prioritarias


    def eliminar_completada(self, descripcion):

        for desc, prioridad in self.lista_tuplas:

            if desc == descripcion:

                self.lista_tuplas.remove((desc, prioridad))

                return True

        return False

# VARIANTE 1: Implementación de cantidad_tareas()
# Retorna el conteo global de tareas registradas.

def cantidad_tareas(self):

    return len(self.lista_tuplas)



# VARIANTE 2: Implementación de mostrar_tareas()
# Retorna el listado completo de tareas registradas.

def mostrar_tareas(self):

    return self.lista_tuplas



# VARIANTE 3: Implementación de buscar_tarea()
# Localiza una actividad según su texto descriptivo.

def buscar_tarea(self, descripcion):

    for desc, prioridad in self.lista_tuplas:

        if desc == descripcion:

            return (desc, prioridad)

    return None



# VARIANTE 4: Implementación de cambiar_prioridad()
# Actualiza el nivel de urgencia de una actividad registrada.

def cambiar_prioridad(self, descripcion, nueva_prioridad):

    for i in range(len(self.lista_tuplas)):

        desc, prioridad = self.lista_tuplas[i]

        if desc == descripcion:

            self.lista_tuplas[i] = (desc, nueva_prioridad)

            return True

    return False



# VARIANTE 5: Implementación de eliminar_todas()
# Vacía por completo el listado de actividades.

def eliminar_todas(self):

    self.lista_tuplas.clear()



# VARIANTE 6: Implementación de tareas_por_prioridad()
# Retorna el listado completo de tareas de una prioridad indicada.

def tareas_por_prioridad(self, prioridad_busqueda):

    lista = []

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() == prioridad_busqueda.lower():

            lista.append(descripcion)

    return lista



# VARIANTE 7: Implementación de existe_tarea()
# Verifica si una tarea ya está registrada.

def existe_tarea(self, descripcion):

    for desc, prioridad in self.lista_tuplas:

        if desc == descripcion:

            return True

    return False



# VARIANTE 8: Implementación de cantidad_por_prioridad()
# Contabiliza el número de tareas hay de prioridad Alta, Media y Baja.

def cantidad_por_prioridad(self):

    contador = {
        "Alta": 0,
        "Media": 0,
        "Baja": 0
    }

    for descripcion, prioridad in self.lista_tuplas:

        contador[prioridad.capitalize()] += 1

    return contador



# VARIANTE 9: Implementación de primera_tarea()
# Retorna la actividad ingresada en primer lugar.

def primera_tarea(self):

    if len(self.lista_tuplas) == 0:

        return None

    return self.lista_tuplas[0]



# VARIANTE 10: Implementación de ultima_tarea()
# Retorna la actividad ingresada más recientemente.

def ultima_tarea(self):

    if len(self.lista_tuplas) == 0:

        return None

    return self.lista_tuplas[-1]



# VARIANTE 11: Implementación de ordenar_por_prioridad()
# Clasifica las actividades alfabéticamente tomando su prioridad.

def ordenar_por_prioridad(self):

    return sorted(self.lista_tuplas, key=lambda tarea: tarea[1])



# VARIANTE 12: Implementación de descripcion_mas_larga()
# Retorna el texto descriptivo más extenso.

def descripcion_mas_larga(self):

    if len(self.lista_tuplas) == 0:

        return None

    mayor = self.lista_tuplas[0][0]

    for descripcion, prioridad in self.lista_tuplas:

        if len(descripcion) > len(mayor):

            mayor = descripcion

    return mayor



# VARIANTE 13: Implementación de eliminar_por_prioridad()
# Suprime las actividades que coincidan con la prioridad dada.

def eliminar_por_prioridad(self, prioridad_busqueda):

    nuevas = []

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() != prioridad_busqueda.lower():

            nuevas.append((descripcion, prioridad))

    self.lista_tuplas = nuevas



# VARIANTE 14: Implementación de cantidad_prioritarias()
# Retorna el total de tareas tienen prioridad alta.

def cantidad_prioritarias(self):

    contador = 0

    for descripcion, prioridad in self.lista_tuplas:

        if prioridad.lower() == "alta":

            contador += 1

    return contador



# VARIANTE 15: Implementación de actualizar_descripcion()
# Actualiza el texto descriptivo de una actividad.

def actualizar_descripcion(self, descripcion, nueva_descripcion):

    for i in range(len(self.lista_tuplas)):

        desc, prioridad = self.lista_tuplas[i]

        if desc == descripcion:

            self.lista_tuplas[i] = (nueva_descripcion, prioridad)

            return True

    return False

# PRÁCTICA 11: Cálculo de frecuencias de aparición
# Implementar la clase ContadorFrecuencia con: (1) un método agregar_elemento(elemento) que almacene los datos en un diccionario contando repeticiones
# (2) incorpore el método elemento_mas_frecuente() que devuelva el elemento con mayor frecuencia
# (3) cuente con el método frecuencia_elemento(elemento) que devuelva cuántas veces aparece.

class ContadoeFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        return 0

# VARIANTE 1: Implementación de elemento_mas_frecuente()
# Implementación alternativa sin recurrir a max().

def elemento_mas_frecuente(self):

    mayor = 0

    elemento = None

    for clave, valor in self.frecuencias.items():

        if valor > mayor:

            mayor = valor

            elemento = clave

    return elemento



# VARIANTE 2: Implementación de frecuencia_elemento()
# Implementación alternativa sin recurrir a get().

def frecuencia_elemento(self, elemento):

    if elemento in self.frecuencias:

        return self.frecuencias[elemento]

    return 0



# VARIANTE 3: Implementación de cantidad_elementos()
# Retorna el total de elementos diferentes existen.

def cantidad_elementos(self):

    return len(self.frecuencias)



# VARIANTE 4: Implementación de mostrar_frecuencias()
# Retorna el diccionario íntegro.

def mostrar_frecuencias(self):

    return self.frecuencias



# VARIANTE 5: Implementación de eliminar_elemento()
# Suprime una entrada específica del diccionario.

def eliminar_elemento(self, elemento):

    if elemento in self.frecuencias:

        del self.frecuencias[elemento]

        return True

    return False



# VARIANTE 6: Implementación de reiniciar()
# Vacía completamente el diccionario.

def reiniciar(self):

    self.frecuencias.clear()



# VARIANTE 7: Implementación de existe_elemento()
# Verifica si un elemento está registrado.

def existe_elemento(self, elemento):

    return elemento in self.frecuencias



# VARIANTE 8: Implementación de elementos_repetidos()
# Retorna una colección con aquellos elementos cuya frecuencia sea mayor que 1.

def elementos_repetidos(self):

    repetidos = []

    for elemento, frecuencia in self.frecuencias.items():

        if frecuencia > 1:

            repetidos.append(elemento)

    return repetidos



# VARIANTE 9: Implementación de elementos_unicos()
# Retorna una colección con aquellos elementos que aparecen una sola vez.

def elementos_unicos(self):

    unicos = []

    for elemento, frecuencia in self.frecuencias.items():

        if frecuencia == 1:

            unicos.append(elemento)

    return unicos



# VARIANTE 10: Implementación de suma_frecuencias()
# Retorna la sumatoria de todas las frecuencias.

def suma_frecuencias(self):

    return sum(self.frecuencias.values())



# VARIANTE 11: Implementación de menor_frecuencia()
# Retorna el ítem que posee menor frecuencia usando min().

def menor_frecuencia(self):

    return min(self.frecuencias, key=self.frecuencias.get)



# VARIANTE 12: Implementación de menor_frecuencia()
# Implementación alternativa sin recurrir a min().

def menor_frecuencia(self):

    menor = None

    elemento = None

    for clave, valor in self.frecuencias.items():

        if menor is None or valor < menor:

            menor = valor

            elemento = clave

    return elemento



# VARIANTE 13: Implementación de ordenar_frecuencias()
# Clasifica de forma descendente según la frecuencia.

def ordenar_frecuencias(self):

    return sorted(self.frecuencias.items(), key=lambda dato: dato[1], reverse=True)



# VARIANTE 14: Implementación de promedio_frecuencias()
# Retorna la media aritmética de las frecuencias.

def promedio_frecuencias(self):

    if len(self.frecuencias) == 0:

        return 0

    return sum(self.frecuencias.values()) / len(self.frecuencias)



# VARIANTE 15: Implementación de elemento_menos_frecuente()
# Retorna el ítem que posee menor frecuencia utilizando lógica manual.

def elemento_menos_frecuente(self):

    menor = None

    elemento = None

    for clave, valor in self.frecuencias.items():

        if menor is None or valor < menor:

            menor = valor

            elemento = clave

    return elemento

# PRÁCTICA 12: Generación y consulta de rangos numéricos mediante tuplas
# Implementar la clase SelectorRango con: (1) un método crear_rango(inicio, fin) que devuelva una tupla con números en ese rango
# (2) incorpore el método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.


class SelectorRango:

    def crear_rango(self, inicio, fin):

        return tuple(range(inicio, fin + 1))


    def elementos_en_multiples_rangos(self, *rangos):

        conjunto = set()

        for inicio, fin in rangos:

            for numero in range(inicio, fin + 1):

                conjunto.add(numero)

        return list(conjunto)

# VARIANTE 1: Implementación de crear_rango()
# Implementación alternativa sin recurrir a range().

def crear_rango(self, inicio, fin):

    numeros = []

    while inicio <= fin:

        numeros.append(inicio)

        inicio += 1

    return tuple(numeros)



# VARIANTE 2: Implementación de elementos_en_multiples_rangos()
# Implementación alternativa sin recurrir a set() directamente para eliminar duplicados.

def elementos_en_multiples_rangos(self, *rangos):

    lista = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero not in lista:

                lista.append(numero)

    return lista



# VARIANTE 3: Implementación de buscar_elemento()
# Comprueba si un valor se halla comprendido dentro de los intervalos.

def buscar_elemento(self, numero_buscar, *rangos):

    for inicio, fin in rangos:

        if numero_buscar >= inicio and numero_buscar <= fin:

            return True

    return False



# VARIANTE 4: Implementación de cantidad_elementos()
# Retorna el número de números sin repetir.

def cantidad_elementos(self, *rangos):

    conjunto = set()

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            conjunto.add(numero)

    return len(conjunto)



# VARIANTE 5: Implementación de rango_mayor()
# Retorna el par ordenado con el rango más grande.

def rango_mayor(self, *rangos):

    mayor = 0

    rango_mayor = None

    for inicio, fin in rangos:

        cantidad = fin - inicio + 1

        if cantidad > mayor:

            mayor = cantidad

            rango_mayor = (inicio, fin)

    return rango_mayor



# VARIANTE 6: Implementación de rango_menor()
# Retorna el par ordenado con menos elementos.

def rango_menor(self, *rangos):

    menor = None

    resultado = None

    for inicio, fin in rangos:

        cantidad = fin - inicio + 1

        if menor is None or cantidad < menor:

            menor = cantidad

            resultado = (inicio, fin)

    return resultado



# VARIANTE 7: Implementación de suma_elementos()
# Calcula la sumatoria de todos los números de los rangos sin repetir.

def suma_elementos(self, *rangos):

    conjunto = set()

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            conjunto.add(numero)

    suma = 0

    for numero in conjunto:

        suma += numero

    return suma



# VARIANTE 8: Implementación de elementos_pares()
# Retorna exclusivamente los números pares.

def elementos_pares(self, *rangos):

    pares = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero % 2 == 0 and numero not in pares:

                pares.append(numero)

    return pares



# VARIANTE 9: Implementación de elementos_impares()
# Retorna exclusivamente los números impares.

def elementos_impares(self, *rangos):

    impares = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero % 2 != 0 and numero not in impares:

                impares.append(numero)

    return impares



# VARIANTE 10: Implementación de ordenar_elementos()
# Retorna los ítems ordenados.

def ordenar_elementos(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    return sorted(elementos)



# VARIANTE 11: Implementación de invertir_resultado()
# Retorna los ítems en orden inverso.

def invertir_resultado(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    elementos.reverse()

    return elementos



# VARIANTE 12: Implementación de rango_contiene()
# Verifica si un rango contiene un número.

def rango_contiene(self, inicio, fin, numero):

    if numero >= inicio and numero <= fin:

        return True

    return False



# VARIANTE 13: Implementación de unir_rangos_manual()
# Combina intervalos numéricos sin emplear conjuntos.

def unir_rangos_manual(self, *rangos):

    lista = []

    for inicio, fin in rangos:

        for numero in range(inicio, fin + 1):

            if numero not in lista:

                lista.append(numero)

    return lista



# VARIANTE 14: Implementación de promedio_elementos()
# Retorna la media aritmética de los elementos.

def promedio_elementos(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    if len(elementos) == 0:

        return 0

    suma = 0

    for numero in elementos:

        suma += numero

    return suma / len(elementos)



# VARIANTE 15: Implementación de mayor_elemento()
# Retorna el valor numérico más alto usando lógica manual.

def mayor_elemento(self, *rangos):

    elementos = self.elementos_en_multiples_rangos(*rangos)

    mayor = elementos[0]

    for numero in elementos:

        if numero > mayor:

            mayor = numero

    return mayor

# PRÁCTICA 14: Intercalación y combinación de listas
# Implementar la clase CombinadorListas con: (1) un método intercalar(lista1, lista2) que devuelva una lista alternando elementos de ambas
# (2) incorpore el método intercalar_multiples(*listas) reutilizando la lógica para varias listas.

class CombinadorListas:

    def intercalar(self, lista1, lista2):

        resultado = []

        longitud = min(len(lista1), len(lista2))

        for i in range(longitud):

            resultado.append(lista1[i])

            resultado.append(lista2[i])

        # En caso de que una lista posea mayor longitud que la otra

        if len(lista1) > longitud:

            resultado.extend(lista1[longitud:])


        if len(lista2) > longitud:

            resultado.extend(lista2[longitud:])


        return resultado


    def intercalar_multiples(self, *listas):

        resultado = []

        for lista in listas:

            resultado = self.intercalar(resultado, lista)

        return resultado

# VARIANTES Y EXTENSIONES POSIBLES DE MÉTODOS
# PRÁCTICA 14: Intercalación y combinación de listas


# VARIANTE 1: Intercalar de forma manual sin usar min()

def intercalar(self, lista1, lista2):

    resultado = []

    i = 0

    while i < len(lista1) and i < len(lista2):

        resultado.append(lista1[i])

        resultado.append(lista2[i])

        i += 1


    while i < len(lista1):

        resultado.append(lista1[i])

        i += 1


    while i < len(lista2):

        resultado.append(lista2[i])

        i += 1


    return resultado



# VARIANTE 2: Intercalar múltiples listas con lógica más manual
# (sin reutilizar el método intercalar)

def intercalar_multiples(self, *listas):

    resultado = []

    mayor = 0

    for lista in listas:

        if len(lista) > mayor:

            mayor = len(lista)


    for i in range(mayor):

        for lista in listas:

            if i < len(lista):

                resultado.append(lista[i])


    return resultado



# VARIANTE 3: Implementación de unir_listas()
# Concatena varias listas de forma secuencial.

def unir_listas(self, *listas):

    resultado = []

    for lista in listas:

        resultado.extend(lista)

    return resultado



# VARIANTE 4: Implementación de eliminar_repetidos()
# Devuelve una colección depurada sin duplicados.

def eliminar_repetidos(self, lista):

    resultado = []

    for elemento in lista:

        if elemento not in resultado:

            resultado.append(elemento)

    return resultado



# VARIANTE 5: Implementación de elementos_comunes()
# Identifica los ítems compartidos entre ambas colecciones.

def elementos_comunes(self, lista1, lista2):

    comunes = []

    for elemento in lista1:

        if elemento in lista2:

            comunes.append(elemento)

    return comunes



# VARIANTE 6: Implementación de diferencia_listas()
# Ítems presentes exclusivamente en la primera colección.

def diferencia_listas(self, lista1, lista2):

    diferencia = []

    for elemento in lista1:

        if elemento not in lista2:

            diferencia.append(elemento)

    return diferencia



# VARIANTE 7: Implementación de invertir_lista()
# Revierte una lista mediante recorrido inverso.

def invertir_lista(self, lista):

    invertida = []

    for i in range(len(lista)-1, -1, -1):

        invertida.append(lista[i])

    return invertida



# VARIANTE 8: Implementación de contar_elementos()
# Contabiliza el total de elementos tiene una lista.

def contar_elementos(self, lista):

    contador = 0

    for elemento in lista:

        contador += 1

    return contador



# VARIANTE 9: Implementación de buscar_elemento()
# Evalúa la existencia de un ítem.

def buscar_elemento(self, lista, elemento):

    for dato in lista:

        if dato == elemento:

            return True

    return False



# VARIANTE 10: Implementación de posicion_elemento()
# Retorna el índice correspondiente a un elemento.

def posicion_elemento(self, lista, elemento):

    for i in range(len(lista)):

        if lista[i] == elemento:

            return i

    return -1



# VARIANTE 11: Implementación de lista_mayor()
# Retorna la lista con más elementos.

def lista_mayor(self, *listas):

    mayor = listas[0]

    for lista in listas:

        if len(lista) > len(mayor):

            mayor = lista

    return mayor



# VARIANTE 12: Implementación de lista_menor()
# Retorna la lista con menos elementos.

def lista_menor(self, *listas):

    menor = listas[0]

    for lista in listas:

        if len(lista) < len(menor):

            menor = lista

    return menor



# VARIANTE 13: Implementación de ordenar_lista()
# Clasifica los elementos de una lista.

def ordenar_lista(self, lista):

    return sorted(lista)



# VARIANTE 14: Implementación de separar_pares_impares()
# Particiona una secuencia de números.

def separar_pares_impares(self, lista):

    pares = []

    impares = []

    for numero in lista:

        if numero % 2 == 0:

            pares.append(numero)

        else:

            impares.append(numero)

    return pares, impares



# VARIANTE 15: Implementación de intercalar_tres_listas()
# Implementación particular diseñada para tres colecciones.

def intercalar_tres_listas(self, lista1, lista2, lista3):

    resultado = []

    mayor = max(len(lista1), len(lista2), len(lista3))


    for i in range(mayor):

        if i < len(lista1):

            resultado.append(lista1[i])

        if i < len(lista2):

            resultado.append(lista2[i])

        if i < len(lista3):

            resultado.append(lista3[i])


    return resultado

# PRÁCTICA 14: Asociación de alumnos con sus calificaciones

# Implementar la clase RegistroNotas de modo que:
# (1) disponga del método registrar(estudiante, nota) que almacene los datos en un diccionario
# (2) incorpore el método estudiantes_aprobados(nota_minima) que devuelva lista de estudiantes
# (3) cuente con el método mejor_estudiante() que devuelva nombre y nota del que tiene mayor calificación.


class RegistroNotas:

    def __init__(self):

        self.notas = {}


    def registrar(self, estudiante, nota):

        self.notas[estudiante] = nota



    def estudiantes_aprobados(self, nota_minima):

        aprobados = []

        for estudiante, nota in self.notas.items():

            if nota >= nota_minima:

                aprobados.append(estudiante)

        return aprobados



    def mejor_estudiante(self):

        if len(self.notas) == 0:

            return None

        mayor = 0

        estudiante_mayor = None


        for estudiante, nota in self.notas.items():

            if nota > mayor:

                mayor = nota

                estudiante_mayor = estudiante


        return estudiante_mayor, mayor

# VARIANTES Y EXTENSIONES POSIBLES DE MÉTODOS
# PRÁCTICA: Asociación de alumnos con sus calificaciones


# VARIANTE 1: Registrar varias notas
# Habilita el registro simultáneo de múltiples alumnos.

def registrar_multiples(self, **estudiantes):

    for nombre, nota in estudiantes.items():

        self.notas[nombre] = nota



# Caso práctico:
# registro.registrar_multiples(
# Juan=80,
# Maria=95,
# Pedro=70
# )



# VARIANTE 2: Buscar nota de un estudiante

def buscar_nota(self, estudiante):

    if estudiante in self.notas:

        return self.notas[estudiante]

    return "Estudiante no registrado"



# VARIANTE 3: Modificar nota existente

def modificar_nota(self, estudiante, nueva_nota):

    if estudiante in self.notas:

        self.notas[estudiante] = nueva_nota

        return True

    return False



# VARIANTE 4: Eliminar estudiante

def eliminar_estudiante(self, estudiante):

    if estudiante in self.notas:

        del self.notas[estudiante]

        return True

    return False



# VARIANTE 5: Promedio general de notas

def promedio_notas(self):

    if len(self.notas) == 0:

        return 0


    suma = 0

    for nota in self.notas.values():

        suma += nota


    return suma / len(self.notas)



# VARIANTE 6: Contar aprobados

def cantidad_aprobados(self, nota_minima):

    contador = 0

    for nota in self.notas.values():

        if nota >= nota_minima:

            contador += 1

    return contador



# VARIANTE 7: Contar reprobados

def cantidad_reprobados(self, nota_minima):

    contador = 0

    for nota in self.notas.values():

        if nota < nota_minima:

            contador += 1

    return contador



# VARIANTE 8: Retornar estudiante con menor nota

def peor_estudiante(self):

    if len(self.notas) == 0:

        return None


    menor = None

    estudiante_menor = None


    for estudiante, nota in self.notas.items():

        if menor is None or nota < menor:

            menor = nota

            estudiante_menor = estudiante


    return estudiante_menor, menor



# VARIANTE 9: Lista ordenada de estudiantes por nota

def ordenar_por_nota(self):

    return sorted(
        self.notas.items(),
        key=lambda estudiante: estudiante[1],
        reverse=True
    )



# VARIANTE 10: Separar aprobados y reprobados

def clasificar_estudiantes(self, nota_minima):

    aprobados = []

    reprobados = []


    for estudiante, nota in self.notas.items():

        if nota >= nota_minima:

            aprobados.append(estudiante)

        else:

            reprobados.append(estudiante)


    return aprobados, reprobados



# VARIANTE 11: Nota más repetida

def nota_mas_comun(self):

    frecuencia = {}


    for nota in self.notas.values():

        if nota in frecuencia:

            frecuencia[nota] += 1

        else:

            frecuencia[nota] = 1


    mayor = 0

    nota_repetida = None


    for nota, cantidad in frecuencia.items():

        if cantidad > mayor:

            mayor = cantidad

            nota_repetida = nota


    return nota_repetida



# VARIANTE 12: Buscar estudiantes con una nota exacta

def estudiantes_con_nota(self, nota_buscar):

    estudiantes = []


    for estudiante, nota in self.notas.items():

        if nota == nota_buscar:

            estudiantes.append(estudiante)


    return estudiantes



# VARIANTE 13: Aumentar puntos a todos los estudiantes

def subir_nota(self, puntos):

    for estudiante in self.notas:

        self.notas[estudiante] += puntos



# VARIANTE 14: Mostrar todos los estudiantes

def mostrar_estudiantes(self):

    lista = []


    for estudiante, nota in self.notas.items():

        lista.append(
            (estudiante, nota)
        )


    return lista



# VARIANTE 15: Mejor estudiante usando max()

def mejor_estudiante_max(self):

    if len(self.notas) == 0:

        return None


    estudiante = max(
        self.notas,
        key=self.notas.get
    )


    return estudiante, self.notas[estudiante]

# PRÁCTICA 15: Cálculo de divisores y números perfectos

# Implementar la clase DivisorFinder de modo que:
# (1) disponga del método encontrar_divisores(numero) que devuelva una tupla con todos los divisores
# (2) incorpore el método es_perfecto(numero) que devuelva True cuando la suma de sus divisores (excepto él mismo) es igual a él
# (3) cuente con el método encontrar_multiples_divisores(*numeros) que devuelva un diccionario {número: tupla_divisores}.



class DivisorFinder:

    def encontrar_divisores(self, numero):

        divisores = []

        for i in range(1, numero + 1):

            if numero % i == 0:

                divisores.append(i)

        return tuple(divisores)



    def es_perfecto(self, numero):

        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:

            if divisor != numero:

                suma += divisor


        return suma == numero



    def encontrar_multiples_divisores(self, *numeros):

        resultado = {}


        for numero in numeros:

            resultado[numero] = self.encontrar_divisores(numero)


        return resultado

# VARIANTES Y EXTENSIONES POSIBLES DE MÉTODOS
# PRÁCTICA 15: Cálculo de divisores y números perfectos


# VARIANTE 1: Encontrar divisores sin incluir el mismo número
# Retorna únicamente divisores propios.

def encontrar_divisores_propios(self, numero):

    divisores = []

    for i in range(1, numero):

        if numero % i == 0:

            divisores.append(i)

    return tuple(divisores)



# VARIANTE 2: Encontrar divisores usando lógica más eficiente
# Optimiza la búsqueda iterando únicamente hasta la mitad del valor.

def encontrar_divisores_optimizado(self, numero):

    divisores = []

    for i in range(1, numero // 2 + 1):

        if numero % i == 0:

            divisores.append(i)


    divisores.append(numero)

    return tuple(divisores)



# VARIANTE 3: Contar cantidad de divisores

def cantidad_divisores(self, numero):

    divisores = self.encontrar_divisores(numero)

    return len(divisores)



# VARIANTE 4: Encontrar el divisor más grande

def mayor_divisor(self, numero):

    divisores = self.encontrar_divisores(numero)

    mayor = 0


    for divisor in divisores:

        if divisor > mayor:

            mayor = divisor


    return mayor



# VARIANTE 5: Encontrar el menor divisor diferente de 1

def menor_divisor(self, numero):

    for i in range(2, numero + 1):

        if numero % i == 0:

            return i



# VARIANTE 6: Verificar si un número es primo

def es_primo(self, numero):

    cantidad = 0


    for i in range(1, numero + 1):

        if numero % i == 0:

            cantidad += 1


    return cantidad == 2



# VARIANTE 7: Encontrar números primos dentro de varios números

def filtrar_primos(self, *numeros):

    primos = []


    for numero in numeros:

        if self.es_primo(numero):

            primos.append(numero)


    return primos



# VARIANTE 8: Sumar todos los divisores

def suma_divisores(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        suma += divisor


    return suma



# VARIANTE 9: Verificar si es abundante
# Ocurre cuando la sumatoria de divisores propios supera al número.

def es_abundante(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        if divisor != numero:

            suma += divisor


    return suma > numero



# VARIANTE 10: Verificar si es deficiente
# Ocurre cuando la sumatoria de divisores propios es inferior al número.

def es_deficiente(self, numero):

    divisores = self.encontrar_divisores(numero)

    suma = 0


    for divisor in divisores:

        if divisor != numero:

            suma += divisor


    return suma < numero



# VARIANTE 11: Buscar números perfectos dentro de varios números

def perfectos_en_lista(self, *numeros):

    perfectos = []


    for numero in numeros:

        if self.es_perfecto(numero):

            perfectos.append(numero)


    return perfectos



# VARIANTE 12: Encontrar divisores comunes entre dos números

def divisores_comunes(self, numero1, numero2):

    comunes = []

    divisores1 = self.encontrar_divisores(numero1)

    divisores2 = self.encontrar_divisores(numero2)


    for divisor in divisores1:

        if divisor in divisores2:

            comunes.append(divisor)


    return tuple(comunes)



# VARIANTE 13: Encontrar máximo común divisor (MCD) manual

def mcd(self, numero1, numero2):

    comunes = self.divisores_comunes(numero1, numero2)

    mayor = 0


    for divisor in comunes:

        if divisor > mayor:

            mayor = divisor


    return mayor



# VARIANTE 14: Factorización prima básica

def factores_primos(self, numero):

    factores = []


    divisor = 2


    while numero > 1:

        if numero % divisor == 0:

            factores.append(divisor)

            numero = numero // divisor

        else:

            divisor += 1


    return tuple(factores)



# VARIANTE 15: Encontrar múltiplos de un número

def encontrar_multiplos(self, numero, limite):

    multiplos = []


    for i in range(1, limite + 1):

        if i % numero == 0:

            multiplos.append(i)


    return tuple(multiplos)

# PRÁCTICA 16: Cifrado y descifrado César

# Implementar la clase CodificadorCesar de modo que:
# (1) disponga del método codificar_letra(letra, desplazamiento) que devuelva la letra desplazada en el alfabeto (usar operador %)
# (2) incorpore el método codificar_palabra(palabra, desplazamiento) reutilizando la lógica para toda la palabra
# (3) incluya un diccionario interno destinado al historial de codificaciones.


class CodificadorCesar:

    def __init__(self):

        self.historial = {}



    def codificar_letra(self, letra, desplazamiento):

        alfabeto = "abcdefghijklmnopqrstuvwxyz"


        if letra.lower() in alfabeto:

            posicion = alfabeto.index(letra.lower())


            nueva_posicion = (posicion + desplazamiento) % len(alfabeto)


            return alfabeto[nueva_posicion]


        return letra



    def codificar_palabra(self, palabra, desplazamiento):

        resultado = ""


        for letra in palabra:

            resultado += self.codificar_letra(letra, desplazamiento)


        self.historial[palabra] = resultado


        return resultado

# VARIANTES Y EXTENSIONES POSIBLES DE MÉTODOS
# PRÁCTICA 16: Cifrado y descifrado mediante desplazamiento César


# VARIANTE 1: Codificar sin usar index()
# Implementación explícita localizando el índice mediante un contador.

def codificar_letra_manual(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    posicion = 0


    for caracter in alfabeto:

        if caracter == letra.lower():

            break

        posicion += 1


    nueva_posicion = (posicion + desplazamiento) % len(alfabeto)


    return alfabeto[nueva_posicion]



# VARIANTE 2: Codificar sin usar len()
# Empleando la constante 26 correspondiente al total de letras del alfabeto.

def codificar_letra_sin_len(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"


    posicion = alfabeto.index(letra.lower())


    nueva_posicion = (posicion + desplazamiento) % 26


    return alfabeto[nueva_posicion]



# VARIANTE 3: Decodificar palabra
# Descifra el texto aplicando un corrimiento en sentido inverso.

def decodificar_palabra(self, palabra, desplazamiento):

    resultado = ""


    for letra in palabra:

        resultado += self.codificar_letra(
            letra,
            -desplazamiento
        )


    return resultado



# VARIANTE 4: Guardar historial con más información

def guardar_historial_completo(self, original, desplazamiento, resultado):

    self.historial[original] = {

        "desplazamiento": desplazamiento,

        "resultado": resultado

    }



# Valor obtenido:

# {
# "hola":{
# "desplazamiento":3,
# "resultado":"krod"
# }
# }



# VARIANTE 5: Codificar frases completas
# Conserva intactos los espacios y caracteres no alfabéticos.

def codificar_texto(self, texto, desplazamiento):

    resultado = ""


    for letra in texto:

        resultado += self.codificar_letra(
            letra,
            desplazamiento
        )


    return resultado



# VARIANTE 6: Mantener mayúsculas
# Retorna la letra con el mismo formato original.

def codificar_letra_mayusculas(self, letra, desplazamiento):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    mayuscula = letra.isupper()


    letra = letra.lower()


    posicion = alfabeto.index(letra)


    nueva_posicion = (posicion + desplazamiento) % 26


    nueva_letra = alfabeto[nueva_posicion]


    if mayuscula:

        return nueva_letra.upper()


    return nueva_letra



# VARIANTE 7: Contar codificaciones realizadas

def cantidad_codificaciones(self):

    return len(self.historial)



# VARIANTE 8: Buscar una palabra en historial

def buscar_historial(self, palabra):

    if palabra in self.historial:

        return self.historial[palabra]


    return "No existe en historial"



# VARIANTE 9: Eliminar una codificación del historial

def eliminar_historial(self, palabra):

    if palabra in self.historial:

        del self.historial[palabra]

        return True


    return False



# VARIANTE 10: Codificar varias palabras

def codificar_multiples(self, palabras, desplazamiento):

    resultado = {}


    for palabra in palabras:

        resultado[palabra] = self.codificar_palabra(
            palabra,
            desplazamiento
        )


    return resultado



# VARIANTE 11: Cambiar alfabeto para incluir números
# Caso ilustrativo combinando caracteres alfabéticos y dígitos.

def codificar_con_numeros(self, texto, desplazamiento):

    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"

    resultado = ""


    for letra in texto:

        if letra in caracteres:

            posicion = caracteres.index(letra)

            nueva_posicion = (
                posicion + desplazamiento
            ) % len(caracteres)

            resultado += caracteres[nueva_posicion]

        else:

            resultado += letra


    return resultado



# VARIANTE 12: Hacer desplazamiento negativo

def retroceder_letra(self, letra, desplazamiento):

    return self.codificar_letra(
        letra,
        -desplazamiento
    )



# VARIANTE 13: Validar desplazamiento

def validar_desplazamiento(self, desplazamiento):

    if desplazamiento >= 0:

        return True

    return False



# VARIANTE 14: Codificar usando while
# Empleando un bucle while en reemplazo de for.

def codificar_palabra_while(self, palabra, desplazamiento):

    resultado = ""

    i = 0


    while i < len(palabra):

        resultado += self.codificar_letra(
            palabra[i],
            desplazamiento
        )

        i += 1


    return resultado



# VARIANTE 15: Buscar frecuencia de letras codificadas

def frecuencia_letras(self, palabra):

    frecuencia = {}


    for letra in palabra:

        if letra in frecuencia:

            frecuencia[letra] += 1

        else:

            frecuencia[letra] = 1


    return frecuencia  

# PRÁCTICA 17: Clasificación de personas por rangos etarios

# Implementar la clase AgrupadorEdades de modo que:
# (1) disponga del método clasificar_edad(edad) que devuelva la categoría ("niño", "adolescente", "adulto", "mayor")
# (2) incorpore el método agrupar_por_categoria(*edades) que devuelva un diccionario con {categoría: [edades]}
# (3) cuente con el método edad_promedio_categoria(categoria).


class AgrupadorEdades:

    def __init__(self):

        self.grupos = {}



    def clasificar_edad(self, edad):

        if edad <= 12:

            return "niño"

        elif edad <= 17:

            return "adolescente"

        elif edad < 60:

            return "adulto"

        else:

            return "mayor"



    def agrupar_por_categoria(self, *edades):

        self.grupos = {

            "niño": [],

            "adolescente": [],

            "adulto": [],

            "mayor": []

        }


        for edad in edades:

            categoria = self.clasificar_edad(edad)

            self.grupos[categoria].append(edad)


        return self.grupos



    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:

            return 0


        if len(self.grupos[categoria]) == 0:

            return 0


        suma = 0


        for edad in self.grupos[categoria]:

            suma += edad


        return suma / len(self.grupos[categoria])

# VARIANTES Y EXTENSIONES POSIBLES DE MÉTODOS
# PRÁCTICA 17: Clasificación de personas por rangos etarios


# VARIANTE 1: Agregar más categorías

# Caso práctico:
# Rango primera infancia: entre 0 y 3 años
# Rango infantil: entre 4 y 12 años
# Rango adolescente: entre 13 y 17 años
# Rango adulto: entre 18 y 59 años
# Rango adulto mayor: a partir de los 60 años


def clasificar_edad_ampliada(self, edad):

    if edad <= 3:

        return "bebé"

    elif edad <= 12:

        return "niño"

    elif edad <= 17:

        return "adolescente"

    elif edad < 60:

        return "adulto"

    else:

        return "mayor"



# ----------------------------------------------------


# VARIANTE 2: Contar cantidad de personas por categoría


def cantidad_categoria(self, categoria):

    if categoria in self.grupos:

        return len(self.grupos[categoria])

    return 0



# Caso práctico:

# adulto = [25,30,40]

# valor devuelto:

# 3



# ----------------------------------------------------


# VARIANTE 3: Encontrar edad máxima de una categoría
# Mediante comparación manual sin max()


def mayor_edad_categoria(self, categoria):

    if categoria not in self.grupos:

        return None


    mayor = 0


    for edad in self.grupos[categoria]:

        if edad > mayor:

            mayor = edad


    return mayor



# ----------------------------------------------------


# VARIANTE 4: Encontrar edad mínima de una categoría
# Mediante comparación manual sin min()


def menor_edad_categoria(self, categoria):

    if categoria not in self.grupos:

        return None


    menor = self.grupos[categoria][0]


    for edad in self.grupos[categoria]:

        if edad < menor:

            menor = edad


    return menor



# ----------------------------------------------------


# VARIANTE 5: Promedio más manual
# Calculando el conteo sin recurrir a len()


def promedio_manual(self, categoria):

    suma = 0

    contador = 0


    for edad in self.grupos[categoria]:

        suma += edad

        contador += 1


    if contador == 0:

        return 0


    return suma / contador



# ----------------------------------------------------


# VARIANTE 6: Buscar personas de una categoría


def obtener_edades_categoria(self, categoria):

    if categoria in self.grupos:

        return self.grupos[categoria]


    return []



# ----------------------------------------------------


# VARIANTE 7: Agrupar desde una lista
# Recibiendo una lista explícita en vez de *edades


def agrupar_lista(self, edades):

    resultado = {}


    for edad in edades:

        categoria = self.clasificar_edad(edad)


        if categoria not in resultado:

            resultado[categoria] = []


        resultado[categoria].append(edad)


    return resultado



# ----------------------------------------------------


# VARIANTE 8: Encontrar categoría con más personas


def categoria_mas_grande(self):

    mayor = ""

    cantidad = 0


    for categoria, edades in self.grupos.items():

        if len(edades) > cantidad:

            cantidad = len(edades)

            mayor = categoria


    return mayor



# ----------------------------------------------------


# VARIANTE 9: Filtrar edades mayores a una edad dada


def mayores_a(self, edad_minima):

    resultado = []


    for categoria, edades in self.grupos.items():

        for edad in edades:

            if edad >= edad_minima:

                resultado.append(edad)


    return resultado



# ----------------------------------------------------


# VARIANTE 10: Guardar historial de agrupaciones


# Incorporar en el constructor __init__:

# self.historial = []



def guardar_historial(self):

    self.historial.append(self.grupos)



# ----------------------------------------------------


# VARIANTE 11: Mezclar con diccionario de personas


# Procesando diccionarios de personas en lugar de edades sueltas:

# [
# {"nombre":"Ana","edad":15},
# {"nombre":"Luis","edad":30}
# ]


def agrupar_personas(self, personas):

    resultado = {

        "niño": [],

        "adolescente": [],

        "adulto": [],

        "mayor": []

    }


    for persona in personas:

        categoria = self.clasificar_edad(persona["edad"])


        resultado[categoria].append(
            persona["nombre"]
        )


    return resultado



# ----------------------------------------------------


# VARIANTE 12: Verificar si una categoría existe


def existe_categoria(self, categoria):

    return categoria in self.grupos


# PRÁCTICA 18: Cálculo de distancias entre coordenadas

# Implementar la clase CalculadorDistancia de modo que:
# (1) disponga del método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia
# (2) incorpore el método punto_mas_cercano(referencia, *puntos) que devuelva el punto más cercano a referencia
# (3) mantenga un atributo tipo lista para almacenar todas las distancias calculadas.


class CalculadorDistancia:

    def __init__(self):

        self.distancias = []



    def distancia_euclidiana(self, p1, p2):

        x1, y1 = p1

        x2, y2 = p2


        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5


        self.distancias.append(distancia)


        return distancia



    def punto_mas_cercano(self, referencia, *puntos):

        if len(puntos) == 0:

            return None


        punto_cercano = puntos[0]


        menor_distancia = self.distancia_euclidiana(
            referencia,
            punto_cercano
        )


        for punto in puntos[1:]:


            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )


            if distancia < menor_distancia:

                menor_distancia = distancia

                punto_cercano = punto


        return punto_cercano

# POSIBLES VARIANTES, COMBINACIONES Y MÉTODOS COMPLEMENTARIOS
# PRÁCTICA 18: Cálculo de distancias entre coordenadas



# VARIANTE 1: Implementación de punto_mas_lejano()

# Análogo a punto_mas_cercano(),
# pero localizando la separación máxima.


def punto_mas_lejano(self, referencia, *puntos):

    if len(puntos) == 0:

        return None


    punto_lejano = puntos[0]


    mayor_distancia = self.distancia_euclidiana(
        referencia,
        punto_lejano
    )


    for punto in puntos[1:]:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia > mayor_distancia:

            mayor_distancia = distancia

            punto_lejano = punto


    return punto_lejano



# ----------------------------------------------------


# VARIANTE 2: Implementación de distancia_manhattan()

# Sustituye el cálculo euclidiano por la métrica Manhattan.


# Expresión matemática:

# |x2-x1| + |y2-y1|



def distancia_manhattan(self, p1, p2):

    x1, y1 = p1

    x2, y2 = p2


    distancia = abs(x2-x1) + abs(y2-y1)


    self.distancias.append(distancia)


    return distancia



# ----------------------------------------------------


# VARIANTE 3: Implementación de obtener_menor_distancia()

# Retorna el menor valor de distancia registrado.


def obtener_menor_distancia(self):

    if len(self.distancias) == 0:

        return None


    menor = self.distancias[0]


    for distancia in self.distancias:

        if distancia < menor:

            menor = distancia


    return menor



# ----------------------------------------------------


# VARIANTE 4: Implementación de obtener_mayor_distancia()

# Determina la mayor distancia mediante comparación iterativa.


def obtener_mayor_distancia(self):

    if len(self.distancias) == 0:

        return None


    mayor = self.distancias[0]


    for distancia in self.distancias:

        if distancia > mayor:

            mayor = distancia


    return mayor



# ----------------------------------------------------


# VARIANTE 5: Implementación de promedio_distancias()

# Obtiene la media aritmética de las distancias registradas.


def promedio_distancias(self):

    if len(self.distancias) == 0:

        return 0


    suma = 0


    for distancia in self.distancias:

        suma += distancia


    return suma / len(self.distancias)



# ----------------------------------------------------


# VARIANTE 6: Almacenar los pares de coordenadas asociados a su distancia.


# Modificación de propiedad:

# self.distancias = []


# Reemplazar por:


# self.distancias = {}



# Estructura almacenada:

# {
# ((0,0),(3,4)):5,
# ((1,1),(4,5)):5
# }



# ----------------------------------------------------


# VARIANTE 7: Implementación de historial_distancias()

# Desplegar el historial completo de distancias obtenidas.


def historial_distancias(self):

    return self.distancias



# ----------------------------------------------------


# VARIANTE 8: Implementación de cantidad_calculos()

# Consultar el total de distancias registradas.


def cantidad_calculos(self):

    return len(self.distancias)



# ----------------------------------------------------


# VARIANTE 9: Implementación de puntos_dentro_radio()

# Filtrar coordenadas ubicadas dentro de un radio límite.


def puntos_dentro_radio(self, referencia, radio, *puntos):

    resultado = []


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia <= radio:

            resultado.append(punto)


    return resultado



# ----------------------------------------------------


# VARIANTE 10: Implementación de ordenar_puntos_por_distancia()

# Retorna las coordenadas clasificadas desde el más cercano
# hasta el punto más distante.


def ordenar_puntos_por_distancia(self, referencia, *puntos):

    lista = []


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        lista.append(
            (punto, distancia)
        )


    lista.sort(
        key=lambda x: x[1]
    )


    return lista



# ----------------------------------------------------


# VARIANTE 11: Mezclar con lista de puntos.


# En sustitución de:

# *puntos


# Parámetros de entrada:

# puntos = [(1,2),(3,4),(5,6)]



def punto_mas_cercano_lista(self, referencia, puntos):

    cercano = None

    menor = None


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if menor is None or distancia < menor:

            menor = distancia

            cercano = punto


    return cercano



# ----------------------------------------------------


# VARIANTE 12: Validar puntos incorrectos.


def validar_punto(self, punto):

    if len(punto) != 2:

        return False


    return True



# ----------------------------------------------------


# VARIANTE 13: Guardar coordenadas separadas.


# Asignación de nueva propiedad:


# self.puntos = []



# Almacenar:

# [
# {"x":2,"y":3},
# {"x":5,"y":8}
# ]



# ----------------------------------------------------


# VARIANTE 14: Implementación de distancia_origen()

# Obtiene la distancia entre una coordenada y el origen (0,0).


def distancia_origen(self, punto):

    origen = (0,0)


    return self.distancia_euclidiana(
        origen,
        punto
    )



# ----------------------------------------------------


# VARIANTE 15: Implementación de cantidad_puntos_cercanos()

# Retorna el total de puntos están cerca de una referencia.


def cantidad_puntos_cercanos(self, referencia, limite, *puntos):

    contador = 0


    for punto in puntos:

        distancia = self.distancia_euclidiana(
            referencia,
            punto
        )


        if distancia <= limite:

            contador += 1


    return contador

# PRÁCTICA 19: Control de existencias en inventario
# Implementar la clase Inventario con: (1) un método agregar_stock(producto, cantidad) que almacene los datos en un diccionario
# (2) incorpore el método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente
# (3) cuente con el método productos_bajo_stock(minimo) que devuelva una lista de productos con cantidad < minimo.

class Inventario:

    def __init__(self):

        self.stock = {}



    def agregar_stock(self, producto, cantidad):

        if producto in self.stock:

            self.stock[producto] += cantidad

        else:

            self.stock[producto] = cantidad



    def restar_stock(self, producto, cantidad):

        if producto in self.stock:

            if self.stock[producto] >= cantidad:

                self.stock[producto] -= cantidad

                return True


        return False



    def productos_bajo_stock(self, minimo):

        productos = []


        for producto, cantidad in self.stock.items():

            if cantidad < minimo:

                productos.append(producto)


        return productos

# VARIANTES, COMBINACIONES Y MÉTODOS ADICIONALES
# PRÁCTICA 19: Control de existencias en inventario



# VARIANTE 1:
# Implementación de eliminar_producto(producto)

# Suprime íntegramente un artículo del registro.



def eliminar_producto(self, producto):

    if producto in self.stock:

        del self.stock[producto]

        return True

    return False



# VARIANTE 2:
# Implementación de consultar_stock(producto)

# Devuelve el stock actual disponible para un artículo.



def consultar_stock(self, producto):

    if producto in self.stock:

        return self.stock[producto]

    return 0



# VARIANTE 3:
# Implementación de producto_mayor_stock()

# Localiza el artículo con mayor existencia disponible.
# Se implementa mediante iteración sin recurrir a max().



def producto_mayor_stock(self):

    if len(self.stock) == 0:

        return None


    mayor = 0

    producto_mayor = None


    for producto, cantidad in self.stock.items():

        if cantidad > mayor:

            mayor = cantidad

            producto_mayor = producto


    return producto_mayor, mayor



# VARIANTE 4:
# Implementación de productos_agotados()

# Retorna los artículos cuya cantidad sea igual a cero.



def productos_agotados(self):

    agotados = []


    for producto, cantidad in self.stock.items():

        if cantidad == 0:

            agotados.append(producto)


    return agotados



# VARIANTE 5:
# Implementación de total_stock()

# Suma el total de existencias disponibles en inventario.



def total_stock(self):

    total = 0


    for cantidad in self.stock.values():

        total += cantidad


    return total



# VARIANTE 6:
# Implementación de actualizar_stock(producto, cantidad)

# Asigna un nuevo valor de existencias a un artículo.



def actualizar_stock(self, producto, cantidad):

    if producto in self.stock:

        self.stock[producto] = cantidad

        return True


    return False



# VARIANTE 7:
# Registrar un historial de entradas y salidas de inventario.

# Incorporar en el constructor __init__:

# self.historial = []


# Cada registro de operación puede almacenar:

# ("Mouse", "Agregado", 10)

# ("Mouse", "Retirado", 3)



# VARIANTE 8:
# Gestionar artículos almacenando múltiples atributos.

# En vez de almacenar únicamente el stock:

# {
# "Mouse": 10
# }


# Almacenar:

# {
# "Mouse": {
# "cantidad": 10,
# "precio": 15
# }
# }



# VARIANTE 9:
# Emplear una lista de pares ordenados en reemplazo de un diccionario.

# Caso práctico:

# [
# ("Mouse",10),
# ("Teclado",5)
# ]


# Posteriormente, iterar sobre:

# for producto, cantidad in lista:



# VARIANTE 10:
# Filtrar artículos según un intervalo de existencias.

# Caso práctico:

# Artículos cuyas existencias oscilan entre 5 y 20 unidades.



def productos_por_rango(self, minimo, maximo):

    resultado = []


    for producto, cantidad in self.stock.items():

        if cantidad >= minimo and cantidad <= maximo:

            resultado.append(producto)


    return resultado



# VARIANTE 11:
# Implementación de vender_producto()

# Análogo a restar_stock(),
# pero orientado al flujo de facturación.



def vender_producto(self, producto, cantidad):

    if producto in self.stock:

        if self.stock[producto] >= cantidad:

            self.stock[producto] -= cantidad

            return True


    return False



# VARIANTE 12:
# Implementación de agregar_stock_manual()

# Implementación explícita sin emplear "in".

# Se itera manualmente sobre las claves del diccionario
# verificando previamente la existencia del artículo.



def agregar_stock_manual(self, producto, cantidad):

    encontrado = False


    for clave in self.stock:

        if clave == producto:

            self.stock[clave] += cantidad

            encontrado = True


    if encontrado == False:

        self.stock[producto] = cantidad

# PRÁCTICA 20: Búsqueda y agrupación de patrones textuales
# Implementar la clase AnalizadorPatrones con: (1) un método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una listA
# (2) incorpore el método agrupar_por_longitud(texto) que devuelva un diccionario {longitud: [palabras]}
# (3) cuente con el método palabras_unicas() usando un conjunto.
class AnalizadorPatrones:

    def __init__(self):

        self.palabras = []



    def encontrar_palabras(self, texto, patron):

        palabras_encontradas = []


        palabras = texto.split()


        for palabra in palabras:

            if palabra.startswith(patron):

                palabras_encontradas.append(palabra)



        self.palabras = palabras


        return palabras_encontradas



    def agrupar_por_longitud(self, texto):

        agrupacion = {}


        palabras = texto.split()


        for palabra in palabras:

            longitud = len(palabra)


            if longitud not in agrupacion:

                agrupacion[longitud] = []


            agrupacion[longitud].append(palabra)



        return agrupacion



    def palabras_unicas(self):

        return set(self.palabras)


# VARIANTES, COMBINACIONES Y MÉTODOS ADICIONALES
# PRÁCTICA 20: Búsqueda y agrupación de patrones textuales



# VARIANTE 1:
# Implementación de encontrar_palabras_manual()

# Sustituye el método startswith() mediante comparación carácter por carácter.
# Evalúa el prefijo inicial del término
# con el prefijo indicado.



def encontrar_palabras_manual(self, texto, patron):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        coincide = True


        if len(palabra) < len(patron):

            coincide = False


        else:

            for i in range(len(patron)):

                if palabra[i] != patron[i]:

                    coincide = False


        if coincide:

            resultado.append(palabra)


    return resultado



# VARIANTE 2:
# Implementación de agrupar_por_longitud_manual()

# Construye el diccionario agrupado sin recurrir directamente a
# Operador not in para inicializar claves ausentes.



def agrupar_por_longitud_manual(self, texto):

    resultado = {}


    palabras = texto.split()


    for palabra in palabras:

        longitud = len(palabra)


        encontrado = False


        for clave in resultado:

            if clave == longitud:

                encontrado = True



        if encontrado:

            resultado[longitud].append(palabra)


        else:

            resultado[longitud] = [palabra]


    return resultado



# VARIANTE 3:
# Implementación de palabras_unicas_manual()

# Identifica términos duplicados sin recurrir a conjuntos.



def palabras_unicas_manual(self):

    unicas = []


    for palabra in self.palabras:

        repetida = False


        for elemento in unicas:

            if palabra == elemento:

                repetida = True



        if repetida == False:

            unicas.append(palabra)


    return unicas



# VARIANTE 4:
# Implementación de contar_palabras()

# Contabiliza el número de palabras tiene un texto.



def contar_palabras(self, texto):

    palabras = texto.split()


    contador = 0


    for palabra in palabras:

        contador += 1


    return contador



# VARIANTE 5:
# Implementación de palabra_mas_larga()

# Localiza el término con mayor cantidad de caracteres
# sin emplear la función max().



def palabra_mas_larga(self, texto):

    palabras = texto.split()


    if len(palabras) == 0:

        return None


    mayor = palabras[0]


    for palabra in palabras:

        if len(palabra) > len(mayor):

            mayor = palabra


    return mayor



# VARIANTE 6:
# Implementación de palabra_mas_corta()

# Localiza el término con menor cantidad de caracteres
# sin emplear la función min().



def palabra_mas_corta(self, texto):

    palabras = texto.split()


    if len(palabras) == 0:

        return None


    menor = palabras[0]


    for palabra in palabras:

        if len(palabra) < len(menor):

            menor = palabra


    return menor



# VARIANTE 7:
# Mantener un registro histórico de los textos procesados.


# Incorporar en el constructor __init__:


# self.historial = []



# Incluir dentro de cada método:


# self.historial.append(texto)



# Permite consultar la totalidad de cadenas analizadas.



# VARIANTE 8:
# Implementación de contar_repeticiones()

# Contabiliza la frecuencia de aparición de cada palabra
# apoyándose en un diccionario.



def contar_repeticiones(self, texto):

    frecuencia = {}


    palabras = texto.split()


    for palabra in palabras:

        if palabra in frecuencia:

            frecuencia[palabra] += 1


        else:

            frecuencia[palabra] = 1


    return frecuencia



# VARIANTE 9:
# Implementación de buscar_palabras_por_longitud()

# Retorna los términos que tengan una longitud específica.



def buscar_por_longitud(self, texto, longitud):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        if len(palabra) == longitud:

            resultado.append(palabra)


    return resultado



# VARIANTE 10:
# Implementación de convertir_mayusculas()

# Transforma los términos a mayúsculas iterando con upper().



def convertir_mayusculas(self, texto):

    palabras = texto.split()


    resultado = []


    for palabra in palabras:

        resultado.append(
            palabra.upper()
        )


    return resultado



# VARIANTE 11:
# Implementación de encontrar_patron_sin_distincion()

# Localiza coincidencias ignorando diferencias entre mayúsculas
# y minúsculas apoyándose en lower().



def encontrar_patron_sin_distincion(self, texto, patron):

    resultado = []


    palabras = texto.split()


    patron = patron.lower()


    for palabra in palabras:

        if palabra.lower().startswith(patron):

            resultado.append(palabra)


    return resultado



# VARIANTE 12:
# Depura términos duplicados preservando su secuencia inicial sin emplear conjuntos.
# Resulta útil en problemas de palabras únicas y eliminación de duplicados.


class AnalizadorPalabras:

    def __init__(self):

        self.palabras = []


    def cargar_texto(self, texto):

        self.palabras = texto.split()



    def palabras_unicas(self):

        resultado = []


        for palabra in self.palabras:

            if palabra not in resultado:

                resultado.append(palabra)


        return resultado



# Datos de prueba para ejecución


analizador = AnalizadorPalabras()


analizador.cargar_texto(
    "python casa python carro casa libro"
)


print(analizador.palabras_unicas())



# VARIANTE 13:
# Registra tanto las repeticiones como la extensión de cada término en un diccionario.
# Permite combinar contador de frecuencia con análisis de texto.


class AnalizadorFrecuencia:

    def __init__(self):

        self.datos = {}



    def analizar_texto(self, texto):

        palabras = texto.split()


        for palabra in palabras:

            if palabra in self.datos:

                self.datos[palabra]["cantidad"] += 1


            else:

                self.datos[palabra] = {

                    "cantidad": 1,

                    "longitud": len(palabra)

                }


        return self.datos



# Datos de prueba para ejecución


analizador = AnalizadorFrecuencia()


texto = "python casa python carro casa"


print(analizador.analizar_texto(texto))



# VARIANTE 14:
# Selecciona términos que cumplan con un largo mínimo establecido.
# Se utiliza para búsquedas y análisis de textos.


class FiltroPalabras:

    def eliminar_palabras_cortas(self, texto, minimo):

        resultado = []


        palabras = texto.split()


        for palabra in palabras:

            if len(palabra) >= minimo:

                resultado.append(palabra)


        return resultado



# Datos de prueba para ejecución


filtro = FiltroPalabras()


texto = "sol python casa computadora"


print(
    filtro.eliminar_palabras_cortas(texto, 5)
)


def eliminar_palabras_cortas(self, texto, minimo):

    resultado = []


    palabras = texto.split()


    for palabra in palabras:

        if len(palabra) >= minimo:

            resultado.append(palabra)


    return resultado



# VARIANTE 15:
# Implementación de invertir_palabras()

# Revierte la secuencia de palabras en el texto.



def invertir_palabras(self, texto):

    palabras = texto.split()


    resultado = []


    for i in range(len(palabras)-1, -1, -1):

        resultado.append(palabras[i])


    return resultado

# MODELO DE CLASE 1: Calculadora
# Permite reunir cálculos matemáticos tales como suma, promedio, conversiones y cálculos.
# Aplicable a ejercicios: 2, 3, 4, 13 y 14.


class Calculadora:

    def promedio(self, n1, n2, n3):

        return (n1 + n2 + n3) / 3


    def convertir_celsius_fahrenheit(self, celsius):

        return celsius * 1.8 + 32


    def calcular_imc(self, peso, estatura):

        return peso / (estatura ** 2)



# MODELO DE CLASE 2: ConversorTiempo
# Facilita la conversión de segundos, minutos y horas usando división entera y residuo.
# Aplicable a ejercicios: 5, 9 y 12.


class ConversorTiempo:

    def segundos_a_hora(self, segundos):

        horas = segundos // 3600

        resto = segundos % 3600

        minutos = resto // 60

        segundos_final = resto % 60

        return horas, minutos, segundos_final



    def minutos_a_horas(self, minutos):

        horas = minutos // 60

        minutos_restantes = minutos % 60

        return horas, minutos_restantes



# MODELO DE CLASE 3: AnalizadorNumeros
# Permite examinar números mediante condiciones y operadores matemáticos.
# Aplicable a ejercicios: 8, 11 y 15.


class AnalizadorNumeros:


    def es_par(self, numero):

        return numero % 2 == 0



    def suma_digitos(self, numero):

        suma = 0

        while numero > 0:

            digito = numero % 10

            suma += digito

            numero = numero // 10


        return suma



    def es_multiplo(self, numero, multiplo):

        return numero % multiplo == 0



# MODELO DE CLASE 4: Cajero
# Se emplea para determinar cantidades mínimas de billetes y monedas.
# Aplicable a ejercicio 10.


class Cajero:


    def calcular_billetes(self, monto):

        resultado = {}


        billetes = [50, 20, 10, 5, 1]


        for billete in billetes:

            cantidad = monto // billete

            resultado[billete] = cantidad

            monto = monto % billete


        return resultado



# MODELO DE CLASE 5: Producto
# Modela productos con precio, cantidad y descuentos.
# Aplicable a ejercicios 7 y 15.


class Producto:


    def __init__(self, nombre, precio, cantidad):

        self.nombre = nombre

        self.precio = precio

        self.cantidad = cantidad



    def calcular_total(self):

        return self.precio * self.cantidad



    def aplicar_descuento(self, porcentaje):

        descuento = self.precio * porcentaje

        return self.precio - descuento



# MODELO DE CLASE 6: Inventario
# Gestiona productos almacenados y cantidades disponibles.
# Aplicable a ejercicios 7, 10 y 15.


class Inventario:


    def __init__(self):

        self.productos = {}



    def agregar_producto(self, nombre, cantidad):

        if nombre in self.productos:

            self.productos[nombre] += cantidad

        else:

            self.productos[nombre] = cantidad



    def retirar_producto(self, nombre, cantidad):

        if nombre in self.productos:

            if self.productos[nombre] >= cantidad:

                self.productos[nombre] -= cantidad

                return True


        return False



# MODELO DE CLASE 7: RegistroEstudiante
# Permite registrar notas y calcular resultados académicos.
# Aplicable a ejercicio 2.


class RegistroEstudiante:


    def __init__(self):

        self.notas = []



    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        suma = 0

        for nota in self.notas:

            suma += nota


        return suma / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



# MODELO DE CLASE 8: ConversorGeometrico
# Ejecuta operaciones geométricas sobre figuras geométricas.
# Aplicable a ejercicio 3.


import math


class ConversorGeometrico:


    def area_rectangulo(self, base, altura):

        return base * altura



    def perimetro_rectangulo(self, base, altura):

        return 2 * (base + altura)



    def area_circulo(self, radio):

        return math.pi * radio ** 2



    def perimetro_circulo(self, radio):

        return 2 * math.pi * radio



# MODELO DE CLASE 9: SistemaCompra
# Modela el proceso de compras aplicando descuentos e impuestos.
# Aplicable a ejercicios 7 y 15.


class SistemaCompra:


    def calcular_total(self, precio, cantidad):

        subtotal = precio * cantidad


        if cantidad >= 10:

            descuento = subtotal * 0.15

        elif cantidad >= 5:

            descuento = subtotal * 0.05

        else:

            descuento = 0


        total = subtotal - descuento


        return total



# MODELO DE CLASE 10: ProcesadorTexto
# Permite examinar palabras, contar frecuencia y buscar patrones.
# Aplicable a ejercicios futuros de diccionarios y conjuntos.


class ProcesadorTexto:


    def contar_palabras(self, texto):

        palabras = texto.split()

        frecuencia = {}


        for palabra in palabras:

            if palabra in frecuencia:

                frecuencia[palabra] += 1

            else:

                frecuencia[palabra] = 1


        return frecuencia



    def buscar_palabra(self, texto, palabra):

        return palabra in texto.split()

# PRÁCTICA 1: Presentación personalizada con nombre y edad

# Definición de la clase Persona.
# Almacena los atributos de una persona e incluye un método de visualización.


class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad


    def saludar(self):

        return f"Hola {self.nombre}, tienes {self.edad} años"



# PRÁCTICA 2: Cálculo del promedio de calificaciones

# Definición de la clase Estudiante.
# Almacena calificaciones, obtiene la media y evalúa la aprobación.


class Estudiante:

    def __init__(self, nombre):

        self.nombre = nombre
        self.notas = []


    def agregar_nota(self, nota):

        self.notas.append(nota)


    def promedio(self):

        suma = 0

        for nota in self.notas:

            suma += nota

        return suma / len(self.notas)


    def estado(self):

        if self.promedio() >= 7:

            return "Aprobado"

        else:

            return "Reprobado"



# PRÁCTICA 3: Cálculos de área y perímetro en figuras

# Definición de la clase Figura.
# Reúne operaciones de superficie y contorno geométrico.


class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura


    def area(self):

        return self.base * self.altura


    def perimetro(self):

        return 2 * (self.base + self.altura)



# PRÁCTICA 4: Transformación de grados Celsius a Fahrenheit

# Definición de la clase Conversor.
# Agrupa diferentes conversiones.


class Conversor:

    def celsius_fahrenheit(self, celsius):

        return celsius * 1.8 + 32



# PRÁCTICA 5: Desglose de segundos en horas, minutos y segundos

# Definición de la clase Tiempo.
# Almacena una cantidad en segundos y la desglosa en horas, minutos y segundos.


class Tiempo:

    def __init__(self, segundos):

        self.segundos = segundos


    def convertir(self):

        horas = self.segundos // 3600

        resto = self.segundos % 3600

        minutos = resto // 60

        segundos = resto % 60

        return horas, minutos, segundos



# PRÁCTICA 6: Permutación de valores entre atributos

# Definición de la clase Intercambiador.
# Gestiona e intercambia datos internos.


class Intercambiador:

    def __init__(self, a, b):

        self.a = a
        self.b = b


    def intercambiar(self):

        self.a, self.b = self.b, self.a



# PRÁCTICA 7: Cálculo de impuestos y descuentos comerciales

# Definición de la clase Producto.
# Almacena el costo base y gestiona descuentos e impuestos.


class Producto:

    def __init__(self, precio):

        self.precio = precio


    def descuento(self, porcentaje):

        return self.precio * porcentaje


    def iva(self):

        return self.precio * 0.15


    def total(self):

        return self.precio + self.iva()



# PRÁCTICA 8: Evaluación de paridad y divisibilidad

# Definición de la clase Numero.
# Evalúa propiedades matemáticas de un valor numérico.


class Numero:

    def __init__(self, valor):

        self.valor = valor


    def es_par(self):

        return self.valor % 2 == 0


    def es_multiplo(self, numero):

        return self.valor % numero == 0



# PRÁCTICA 9: Conversión de formato horario a segundos totales

# Definición de la clase Tiempo.
# Clase reutilizable para transformar formatos horarios.


class TiempoFormato:

    def __init__(self, hora):

        self.hora = hora


    def segundos_totales(self):

        horas, minutos, segundos = self.hora.split(":")

        return int(horas)*3600 + int(minutos)*60 + int(segundos)



# PRÁCTICA 10: Desglose de efectivo en denominaciones mínimas

# Definición de la clase Cajero.
# Determina el desglose óptimo de billetes.


class Cajero:

    def __init__(self, monto):

        self.monto = monto


    def calcular_billetes(self):

        resultado = {}

        valores = [50,20,10,5,1]

        for valor in valores:

            resultado[valor] = self.monto // valor

            self.monto %= valor


        return resultado



# PRÁCTICA 11 y 23: Conteo y análisis de dígitos numéricos

# Definición de la clase AnalizadorNumero.
# Opera mediante divisiones enteras para examinar propiedades numéricas.


class AnalizadorNumero:

    def __init__(self, numero):

        self.numero = numero


    def cantidad_digitos(self):

        numero = abs(self.numero)

        contador = 0


        while numero > 0:

            contador += 1

            numero //= 10


        return contador



# PRÁCTICA 16 al 30: Operaciones iterativas: factorial, primalidad y serie Fibonacci

# Definición de la clase AnalizadorMatematico.
# Agrupa operaciones numéricas usando ciclos.


class AnalizadorMatematico:


    def factorial(self, n):

        resultado = 1

        for i in range(1, n + 1):

            resultado *= i

        return resultado



    def es_primo(self, n):

        for i in range(2, n):

            if n % i == 0:

                return False

        return True



    def fibonacci(self, cantidad):

        lista = []

        a = 0

        b = 1


        for i in range(cantidad):

            lista.append(a)

            a, b = b, a+b


        return lista



# PRÁCTICA 19 y 20: Registro de calificaciones y obtención de extremos

# Definición de la clase RegistroNotas.
# Almacena calificaciones y calcula indicadores estadísticos.


class RegistroNotas:

    def __init__(self):

        self.notas = []


    def agregar(self, nota):

        self.notas.append(nota)


    def nota_mayor(self):

        mayor = self.notas[0]

        for nota in self.notas:

            if nota > mayor:

                mayor = nota

        return mayor



# PRÁCTICA 26: Dinámica de adivinanza numérica con contador de intentos

# Definición de la clase Juego.
# Registra el número objetivo y el conteo de intentos realizados.


class JuegoNumero:

    def __init__(self, secreto):

        self.secreto = secreto
        self.intentos = 0


    def jugar(self, numero):

        self.intentos += 1

        return numero == self.secreto



# PRÁCTICA 28: Facturación con cálculo modular de impuestos

# Definición de la clase Factura.
# Combina métodos internos para obtener el importe final.


class Factura:

    def __init__(self, precio):

        self.precio = precio


    def calcular_iva(self):

        return self.precio * 0.15


    def total(self):

        return self.precio + self.calcular_iva()



# PRÁCTICA 29 y 30: Conteo y verificación de números primos

# Definición de la clase AnalizadorAvanzado.
# Integra funciones matemáticas modulares.


class AnalizadorAvanzado:


    def contar_primos(self, inicio, fin):

        contador = 0


        for numero in range(inicio, fin + 1):

            if self.es_primo(numero):

                contador += 1


        return contador



    def es_primo(self, numero):

        if numero <= 1:

            return False


        for i in range(2, numero):

            if numero % i == 0:

                return False


        return True

# PRÁCTICA 31
# Estructuración de un menú interactivo mediante programación orientada a objetos.
# Cada método encapsula una funcionalidad específica del menú.


class Menu:

    def __init__(self):
        pass

    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicación: {num1 * num2}")

        if num2 != 0:
            print(f"División: {num1 / num2}")
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):

        while True:

            print("\n--- MENÚ ---")
            print("1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                print("Programa finalizado")
                break

            else:
                print("Opción inválida")


menu = Menu()

menu.mostrar_menu()

# PRÁCTICA 31: Menú interactivo organizado en una clase

class Menu:
    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print("Suma:", a + b)
        print("Resta:", a - b)
        print("Multiplicación:", a * b)

        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir para cero")

    def iniciar(self):
        while True:
            print("\n1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.saludar()
            elif opcion == "2":
                self.despedir()
            elif opcion == "3":
                self.calcular()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")


# Menu().iniciar()



# PRÁCTICA 32

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = float(input("Base: "))
altura = float(input("Altura: "))

rect = Rectangulo(base, altura)

print("Área:", rect.area())



# PRÁCTICA 33

class Numeros:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maximo(self):
        return max(self.a, self.b, self.c)


n = Numeros(10, 25, 7)

print("Mayor:", n.maximo())



# PRÁCTICA 34

class Año:
    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):
        return (self.anio % 4 == 0 and self.anio % 100 != 0) or self.anio % 400 == 0


a = Año(2024)

print(a.es_bisiesto())



# PRÁCTICA 35

class Combinatoria:

    def factorial(self, n):
        resultado = 1

        for i in range(1, n + 1):
            resultado *= i

        return resultado


    def calcular(self, n, k):
        if k > n:
            return None

        return self.factorial(n) / (
            self.factorial(k) * self.factorial(n-k)
        )


c = Combinatoria()

print(c.calcular(5, 2))



# PRÁCTICA 36

class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return None

        return a / b


calc = Calculadora()

print(calc.sumar(5, 3))
print(calc.restar(5, 3))
print(calc.multiplicar(5, 3))
print(calc.dividir(5, 3))



# PRÁCTICA 37

class Texto:

    def __init__(self, frase):
        self.frase = frase

    def contar_vocales(self):
        contador = 0

        for letra in self.frase.lower():

            if letra in "aeiouáéíóú":
                contador += 1

        return contador


texto = Texto("Programación Python")

print("Vocales:", texto.contar_vocales())



# PRÁCTICA 38

class Notas:

    def __init__(self, lista):
        self.lista = lista

    def promedio(self):
        return sum(self.lista) / len(self.lista)

    def maxima(self):
        return max(self.lista)

    def minima(self):
        return min(self.lista)


notas = Notas([7, 8.5, 6, 9, 10, 5.5])

print("Promedio:", notas.promedio())
print("Máxima:", notas.maxima())
print("Mínima:", notas.minima())

# PRÁCTICA 31: Menú interactivo con acciones modularizadas

class Menu:
    
    def saludar(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print(f"Suma: {a + b}")
        print(f"Resta: {a - b}")
        print(f"Multiplicación: {a * b}")

        if b != 0:
            print(f"División: {a / b}")
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):
        print("\n--- MENU ---")
        print("1. Saludar")
        print("2. Despedir")
        print("3. Calcular")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()

            opcion = input("Seleccione: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                print("Programa finalizado")
                break

            else:
                print("Opción inválida")


# objeto = Menu()
# objeto.ejecutar()



# PRÁCTICA 32: Cálculo de superficie rectangular

class Rectangulo:

    def area(self, base, altura):
        return base * altura


rect = Rectangulo()

base = float(input("Base: "))
altura = float(input("Altura: "))

print(f"Área: {rect.area(base, altura)}")



# PRÁCTICA 33: Determinación del mayor entre tres valores

class Numeros:

    def maximo(self, a, b, c):

        if a >= b and a >= c:
            return a

        elif b >= a and b >= c:
            return b

        return c


n = Numeros()

a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

print(f"Mayor: {n.maximo(a,b,c)}")



# PRÁCTICA 34: Verificación de años bisiestos

class Fecha:

    def es_bisiesto(self, anio):

        return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


fecha = Fecha()

anio = int(input("Ingrese año: "))

print(fecha.es_bisiesto(anio))

# PRÁCTICA 3
# Modelo de clase orientado a calcular área y perímetro de figuras geométricas.

import math

class Figura:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0

    def rectangulo(self):
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

        area = self.base * self.altura
        perimetro = 2 * (self.base + self.altura)

        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")

    def circulo(self):
        self.radio = float(input("Radio: "))

        area = math.pi * self.radio ** 2
        perimetro = 2 * math.pi * self.radio

        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")


figura = Figura()

figura.rectangulo()
figura.circulo()

# PRÁCTICA 2
# Modelo de clase orientado a calcular promedio de notas y determinar si aprueba o reprueba.

class PromedioEstudiante:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.promedio = 0

    def ingresar_notas(self):
        self.n1 = float(input("Nota 1: "))
        self.n2 = float(input("Nota 2: "))
        self.n3 = float(input("Nota 3: "))

    def calcular_promedio(self):
        self.promedio = (self.n1 + self.n2 + self.n3) / 3

    def mostrar_resultado(self):
        if self.promedio >= 7:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"Promedio: {self.promedio:.2f}")
        print(f"Estado: {estado}")


estudiante = PromedioEstudiante()
estudiante.ingresar_notas()
estudiante.calcular_promedio()
estudiante.mostrar_resultado()

# PRÁCTICA 4
# Modelo de clase diseñado para transformar temperatura Celsius a Fahrenheit.

class ConversorTemperatura:
    def __init__(self):
        self.celsius = 0
        self.fahrenheit = 0

    def ingresar_temperatura(self):
        self.celsius = float(input("Temperatura en Celsius: "))

    def convertir(self):
        self.fahrenheit = self.celsius * 9 / 5 + 32

    def mostrar(self):
        print(f"{self.celsius}°C equivalen a {self.fahrenheit}°F")


temp = ConversorTemperatura()
temp.ingresar_temperatura()
temp.convertir()
temp.mostrar()

# PRÁCTICA 5
# Modelo de clase diseñado para transformar segundos totales a horas, minutos y segundos.

class Tiempo:
    def __init__(self):
        self.segundos_totales = 0

    def ingresar(self):
        self.segundos_totales = int(input("Segundos totales: "))

    def convertir(self):
        horas = self.segundos_totales // 3600

        resto = self.segundos_totales % 3600

        minutos = resto // 60

        segundos = resto % 60

        print(f"{horas}:{minutos:02d}:{segundos:02d}")


tiempo = Tiempo()
tiempo.ingresar()
tiempo.convertir()

# PRÁCTICA 31: Menú interactivo estructurado mediante métodos de clase

class Menu:

    def saludar(self):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}")

    def despedir(self):
        nombre = input("Nombre: ")
        print(f"Adiós {nombre}")

    def calcular(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))

        print("Suma:", a + b)
        print("Resta:", a - b)
        print("Multiplicación:", a * b)

        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir para cero")

    def mostrar_menu(self):

        while True:
            print("\n--- MENU ---")
            print("1. Saludar")
            print("2. Despedir")
            print("3. Calcular")
            print("4. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.saludar()

            elif opcion == "2":
                self.despedir()

            elif opcion == "3":
                self.calcular()

            elif opcion == "4":
                break

            else:
                print("Opción inválida")


menu = Menu()
# menu.mostrar_menu()



# PRÁCTICA 32: Cálculo de superficie rectangular

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input("Base: "))
altura = float(input("Altura: "))

rectangulo = Rectangulo(base, altura)

print("Área:", rectangulo.calcular_area())



# PRÁCTICA 33: Determinación del mayor entre tres valores

class Numeros:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maximo(self):

        if self.a >= self.b and self.a >= self.c:
            return self.a

        elif self.b >= self.a and self.b >= self.c:
            return self.b

        return self.c


a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

numeros = Numeros(a,b,c)

print("Mayor:", numeros.maximo())



# PRÁCTICA 34: Verificación de años bisiestos

class Anio:

    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):

        return (self.anio % 4 == 0 and self.anio % 100 != 0) or self.anio % 400 == 0


anio = int(input("Ingrese año: "))

objeto = Anio(anio)

print(objeto.es_bisiesto())



# PRÁCTICA 35: Cálculo de factorial y coeficientes combinatorios

class Matematicas:

    def factorial(self, n):

        resultado = 1

        for i in range(1,n+1):
            resultado *= i

        return resultado


    def combinatoria(self,n,k):

        if k > n or k < 0:
            return None

        return self.factorial(n) / (self.factorial(k) * self.factorial(n-k))


mat = Matematicas()

n = int(input("n: "))
k = int(input("k: "))

print("Combinatoria:", mat.combinatoria(n,k))



# PRÁCTICA 36: Operaciones aritméticas encapsuladas en una clase

class Calculadora:

    def sumar(self,a,b):
        return a+b

    def restar(self,a,b):
        return a-b

    def multiplicar(self,a,b):
        return a*b

    def dividir(self,a,b):

        if b == 0:
            return None

        return a/b



calc = Calculadora()

a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("Suma:", calc.sumar(a,b))
print("Resta:", calc.restar(a,b))
print("Multiplicación:", calc.multiplicar(a,b))
print("División:", calc.dividir(a,b))



# PRÁCTICA 37: Conteo de vocales en una cadena de texto

class Texto:

    def __init__(self, frase):
        self.frase = frase


    def contar_vocales(self):

        contador = 0

        for letra in self.frase.lower():

            if letra in "aeiouáéíóú":
                contador += 1

        return contador



frase = input("Ingrese frase: ")

texto = Texto(frase)

print("Vocales:", texto.contar_vocales())



# PRÁCTICA 38: Evaluación estadística de calificaciones

class Notas:

    def __init__(self, lista_notas):
        self.notas = lista_notas


    def promedio(self):

        return sum(self.notas) / len(self.notas)


    def maxima(self):

        return max(self.notas)


    def minima(self):

        return min(self.notas)



notas = [7,8.5,6,9,10,5.5]

objeto = Notas(notas)

print(f"Promedio: {objeto.promedio():.2f}")
print(f"Máxima: {objeto.maxima():.2f}")
print(f"Mínima: {objeto.minima():.2f}")


# PRÁCTICA 39
# Implementación de la clase ListaDatos encargada de suprimir duplicados respetando el orden.

class ListaDatos:

    def __init__(self, lista):
        self.lista = lista

    def eliminar_duplicados(self):

        resultado = []
        vistos = set()

        for elemento in self.lista:

            if elemento not in vistos:
                resultado.append(elemento)
                vistos.add(elemento)

        return resultado

    # MÉTODO ADICIONAL
    def cantidad_elementos(self):

        return len(self.lista)


lista = ListaDatos(["a", "b", "a", "c", "b", "d"])

print("Lista sin duplicados:", lista.eliminar_duplicados())
print("Cantidad de elementos:", lista.cantidad_elementos())



# PRÁCTICA 40
# Implementación de la clase Texto para contabilizar apariciones de palabras.

class Texto:

    def __init__(self, texto):

        self.texto = texto
        self.frecuencia = {}


    def contar_palabras(self):

        palabras = self.texto.lower().split()

        for palabra in palabras:

            self.frecuencia[palabra] = self.frecuencia.get(palabra, 0) + 1

        return self.frecuencia


    def palabra_mas_repetida(self):

        if not self.frecuencia:
            self.contar_palabras()

        return max(self.frecuencia, key=self.frecuencia.get)


    # MÉTODO ADICIONAL
    def cantidad_palabras(self):

        return len(self.texto.split())



texto = Texto("Python es fácil y Python es poderoso")

print(texto.contar_palabras())
print("Más repetida:", texto.palabra_mas_repetida())
print("Cantidad palabras:", texto.cantidad_palabras())



# PRÁCTICA 41
# Definición de la clase Pasajero

class Pasajero:


    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad


    def cumplir_anios(self):

        self.edad += 1


    def mostrar(self):

        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")


    # MÉTODO ADICIONAL
    def es_mayor_edad(self):

        return self.edad >= 18



pasajero1 = Pasajero("Ana", "123456", 20)
pasajero2 = Pasajero("Luis", "987654", 15)
pasajero3 = Pasajero("Maria", "456789", 30)


pasajero1.cumplir_anios()


pasajero1.mostrar()
print("Mayor de edad:", pasajero1.es_mayor_edad())

pasajero2.mostrar()
print("Mayor de edad:", pasajero2.es_mayor_edad())

pasajero3.mostrar()
print("Mayor de edad:", pasajero3.es_mayor_edad())



# PRÁCTICA 42
# Definición de la clase CuentaBancaria

class CuentaBancaria:


    def __init__(self):

        self.saldo_actual = 0
        self.historial = []


    def depositar(self, cantidad):

        self.saldo_actual += cantidad
        self.historial.append(f"+{cantidad}")


    def retirar(self, cantidad):

        if cantidad <= self.saldo_actual:

            self.saldo_actual -= cantidad
            self.historial.append(f"-{cantidad}")

        else:

            print("Fondos insuficientes")


    def saldo(self):

        return self.saldo_actual


    def ver_historial(self):

        return self.historial


    def __str__(self):

        return f"Saldo: ${self.saldo_actual}"


    # MÉTODO ADICIONAL
    def cantidad_operaciones(self):

        return len(self.historial)



cuenta = CuentaBancaria()

cuenta.depositar(100)
cuenta.depositar(50)
cuenta.retirar(30)

print(cuenta)
print("Historial:", cuenta.ver_historial())
print("Operaciones:", cuenta.cantidad_operaciones())



# PRÁCTICA 43
# Definición de la clase Producto

class Producto:


    productos_creados = []


    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        Producto.productos_creados.append(self)



    def vender(self, cantidad):

        if cantidad <= self.stock:

            self.stock -= cantidad
            print("Venta realizada")

        else:

            print("No hay stock")



    def reabastecer(self, cantidad):

        self.stock += cantidad



    def valor_inventario(self):

        return self.precio * self.stock



    @classmethod
    def total_inventario(cls):

        total = 0

        for producto in cls.productos_creados:

            total += producto.valor_inventario()

        return total



    # MÉTODO ADICIONAL
    def tiene_stock(self):

        return self.stock > 0



    def __str__(self):

        return f"{self.nombre} - Stock: {self.stock}"



p1 = Producto("Mouse",20,10)
p2 = Producto("Teclado",30,5)


p1.vender(2)
p2.reabastecer(3)


print(p1)
print("Tiene stock:",p1.tiene_stock())

print(p2)

print("Inventario total:",Producto.total_inventario())

# PRÁCTICA 39
# Implementación de la clase ListaDatos destinada a eliminar duplicados respetando orden

class ListaDatos:

    def __init__(self, lista):
        self.lista = lista

    def eliminar_duplicados(self):
        resultado = []
        vistos = set()

        for elemento in self.lista:
            if elemento not in vistos:
                resultado.append(elemento)
                vistos.add(elemento)

        return resultado

    def mostrar(self):
        print(self.lista)


datos = ListaDatos(["a", "b", "a", "c", "b", "d"])

print("Lista original:")
datos.mostrar()

print("Sin duplicados:")
print(datos.eliminar_duplicados())



# PRÁCTICA 40
# Implementación de la clase AnalizadorTexto destinada a contar palabras

class AnalizadorTexto:

    def __init__(self, texto):
        self.texto = texto.lower()
        self.frecuencia = {}

    def contar_palabras(self):

        palabras = self.texto.split()

        for palabra in palabras:

            if palabra in self.frecuencia:
                self.frecuencia[palabra] += 1

            else:
                self.frecuencia[palabra] = 1

        return self.frecuencia


    def palabra_mas_repetida(self):

        mayor = 0
        palabra_mayor = ""

        for palabra, cantidad in self.frecuencia.items():

            if cantidad > mayor:
                mayor = cantidad
                palabra_mayor = palabra

        return palabra_mayor


texto = input("Ingrese un texto: ")

analizador = AnalizadorTexto(texto)

print("Frecuencia:")
print(analizador.contar_palabras())

print("Palabra más repetida:")
print(analizador.palabra_mas_repetida())



# PRÁCTICA 41
# Definición de la clase Pasajero

class Pasajero:

    cantidad_pasajeros = 0

    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

        Pasajero.cantidad_pasajeros += 1


    def cumplir_anios(self):

        self.edad += 1


    def mostrar(self):

        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")


    @classmethod
    def mostrar_cantidad(cls):

        print(f"Cantidad pasajeros: {cls.cantidad_pasajeros}")



pasajero1 = Pasajero("Ana", "123", 20)
pasajero2 = Pasajero("Luis", "456", 25)
pasajero3 = Pasajero("Maria", "789", 30)


pasajero1.cumplir_anios()


pasajero1.mostrar()
print()

pasajero2.mostrar()
print()

pasajero3.mostrar()

Pasajero.mostrar_cantidad()



# PRÁCTICA 42
# Definición de la clase CuentaBancaria

class CuentaBancaria:

    def __init__(self, titular):

        self.titular = titular
        self._saldo = 0
        self.historial = []


    def depositar(self, cantidad):

        if cantidad > 0:

            self._saldo += cantidad
            self.historial.append(f"+{cantidad}")


    def retirar(self, cantidad):

        if cantidad <= self._saldo:

            self._saldo -= cantidad
            self.historial.append(f"-{cantidad}")

        else:

            print("Fondos insuficientes")


    def consultar_saldo(self):

        return self._saldo


    def ver_historial(self):

        return self.historial


    def cantidad_operaciones(self):

        return len(self.historial)


    def __str__(self):

        return f"Cuenta de {self.titular} - Saldo: ${self._saldo}"



cuenta = CuentaBancaria("Derick")


cuenta.depositar(500)
cuenta.depositar(200)
cuenta.retirar(100)


print(cuenta)

print("Saldo:", cuenta.consultar_saldo())

print("Historial:")
print(cuenta.ver_historial())

print("Operaciones realizadas:")
print(cuenta.cantidad_operaciones())

class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta realizada correctamente")
        else:
            print("Stock insuficiente")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print("Producto reabastecido")

    def valor_inventario(self):
        return self.precio * self.stock

    # Método adicional: cambiar precio
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método adicional: verificar disponibilidad
    def disponible(self):
        return self.stock > 0

    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:
            total += producto.valor_inventario()

        return total

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"


producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 180, 3)


producto1.vender(2)
producto2.reabastecer(5)

producto3.cambiar_precio(200)


print(producto1)
print("Valor inventario:", producto1.valor_inventario())

print(producto2)
print("Valor inventario:", producto2.valor_inventario())

print(producto3)
print("Valor inventario:", producto3.valor_inventario())


productos = [producto1, producto2, producto3]


print("Total inventario:",
      Producto.total_inventario(productos))


print("¿Mouse disponible?",
      producto1.disponible())

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura


    def perimetro(self):
        return 2 * (self.base + self.altura)


    # Método adicional: cambiar dimensiones
    def cambiar_dimensiones(self, base, altura):
        self.base = base
        self.altura = altura


    # Método adicional: verificar si es cuadrado
    def es_cuadrado(self):
        return self.base == self.altura


    def __str__(self):
        return f"Rectángulo Base: {self.base} Altura: {self.altura}"



rectangulo = Rectangulo(10, 5)


print(rectangulo)

print("Área:",
      rectangulo.area())

print("Perímetro:",
      rectangulo.perimetro())


print("¿Es cuadrado?",
      rectangulo.es_cuadrado())


rectangulo.cambiar_dimensiones(8,8)


print("\nDespués del cambio")

print(rectangulo)

print("Área:",
      rectangulo.area())

print("¿Es cuadrado?",
      rectangulo.es_cuadrado())

import math


class Circulo:


    def __init__(self, radio):
        self.radio = radio


    def area(self):
        return math.pi * self.radio ** 2


    def circunferencia(self):
        return 2 * math.pi * self.radio


    def diametro(self):
        return self.radio * 2


    # Método adicional: cambiar radio
    def cambiar_radio(self, nuevo_radio):
        self.radio = nuevo_radio


    # Método adicional: mostrar información
    def mostrar_datos(self):

        print("Radio:", self.radio)
        print("Área:", self.area())
        print("Circunferencia:",
              self.circunferencia())
        print("Diámetro:",
              self.diametro())



circulo = Circulo(5)


circulo.mostrar_datos()


circulo.cambiar_radio(10)


print("\nDespués del cambio")

circulo.mostrar_datos()

class Estudiante:


    def __init__(self, nombre):

        self.nombre = nombre
        self.notas = []


    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        return sum(self.notas) / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



    def cantidad_notas(self):

        return len(self.notas)



    # Método adicional: eliminar nota
    def eliminar_nota(self, posicion):

        if posicion < len(self.notas):

            self.notas.pop(posicion)



    # Método adicional: nota más alta
    def nota_maxima(self):

        return max(self.notas)



    # Método adicional: nota más baja
    def nota_minima(self):

        return min(self.notas)



    def mostrar(self):

        print("Nombre:",
              self.nombre)

        print("Notas:",
              self.notas)

        print("Promedio:",
              self.promedio())

        print("Aprobado:",
              self.aprobado())



estudiante = Estudiante("Derick")


estudiante.agregar_nota(8)
estudiante.agregar_nota(9)
estudiante.agregar_nota(7)


estudiante.mostrar()


print("Cantidad notas:",
      estudiante.cantidad_notas())


print("Nota máxima:",
      estudiante.nota_maxima())


print("Nota mínima:",
      estudiante.nota_minima())


estudiante.eliminar_nota(1)


print("\nDespués de eliminar")

estudiante.mostrar()


class Vehiculo:


    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.km = 0



    def recorrer(self, kilometros):

        self.km += kilometros



    def necesita_mantenimiento(self):

        return self.km >= 10000



    def reiniciar_mantenimiento(self):

        self.km = 0



    # Método adicional: calcular costo mantenimiento

    def costo_mantenimiento(self):

        return 150



    # Método adicional: obtener estado

    def estado(self):

        if self.necesita_mantenimiento():

            return "Necesita mantenimiento"

        else:

            return "Vehículo en buen estado"



    def __str__(self):

        return f"""
Marca: {self.marca}
Modelo: {self.modelo}
Kilómetros: {self.km}
"""



vehiculo = Vehiculo("Toyota",
                    "Corolla")


vehiculo.recorrer(12000)


print(vehiculo)


print(vehiculo.estado())


print("Costo mantenimiento:",
      vehiculo.costo_mantenimiento())


vehiculo.reiniciar_mantenimiento()


print("\nDespués del mantenimiento")


print(vehiculo)


print(vehiculo.estado())

# ==========================================
# PRÁCTICA 43
# Definición de la clase Producto equipada con los métodos:
# vender(), reabastecer(), valor_inventario()
# Método adicional: total_inventario()
# Extensiones incorporadas:
# - aplicar_descuento()
# - tiene_stock()
# - mostrar_estado()
# ==========================================


class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):

        if cantidad <= self.stock:
            self.stock -= cantidad
            print("Venta realizada")
        else:
            print("No existe suficiente stock")


    def reabastecer(self, cantidad):

        self.stock += cantidad


    def valor_inventario(self):

        return self.precio * self.stock


    def aplicar_descuento(self, porcentaje):

        descuento = self.precio * (porcentaje / 100)

        self.precio -= descuento


    def tiene_stock(self):

        return self.stock > 0


    def mostrar_estado(self):

        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")


    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:

            total += producto.valor_inventario()

        return total


    def __str__(self):

        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"



producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 200, 3)


producto1.vender(2)

producto2.reabastecer(10)

producto3.aplicar_descuento(10)


productos = [producto1, producto2, producto3]


print(producto1)
print(producto2)
print(producto3)


print("Valor total inventario:",
      Producto.total_inventario(productos))


print("Tiene stock:",
      producto1.tiene_stock())



# ==========================================
# PRÁCTICA 44
# Definición de la clase Rectangulo
# Operaciones disponibles:
# area()
# perimetro()
# __str__()
# Extensiones incorporadas:
# - cambiar_dimensiones()
# - es_cuadrado()
# ==========================================


class Rectangulo:


    def __init__(self, base, altura):

        self.base = base
        self.altura = altura



    def area(self):

        return self.base * self.altura



    def perimetro(self):

        return 2 * (self.base + self.altura)



    def cambiar_dimensiones(self, nueva_base, nueva_altura):

        self.base = nueva_base
        self.altura = nueva_altura



    def es_cuadrado(self):

        return self.base == self.altura



    def __str__(self):

        return f"Rectángulo Base:{self.base} Altura:{self.altura}"




rectangulo = Rectangulo(10,5)


print(rectangulo)

print("Área:", rectangulo.area())

print("Perímetro:", rectangulo.perimetro())


print("¿Es cuadrado?",
      rectangulo.es_cuadrado())


rectangulo.cambiar_dimensiones(8,8)


print(rectangulo)

print("¿Es cuadrado?",
      rectangulo.es_cuadrado())




# ==========================================
# PRÁCTICA 45
# Definición de la clase Circulo
# Operaciones disponibles:
# area()
# circunferencia()
# diametro()
# Extensiones incorporadas:
# - cambiar_radio()
# - es_mayor_que()
# ==========================================


import math



class Circulo:


    def __init__(self, radio):

        self.radio = radio



    def area(self):

        return math.pi * self.radio ** 2



    def circunferencia(self):

        return 2 * math.pi * self.radio



    def diametro(self):

        return self.radio * 2



    def cambiar_radio(self, nuevo_radio):

        self.radio = nuevo_radio



    def es_mayor_que(self, otro):

        return self.area() > otro.area()



    def __str__(self):

        return f"Círculo Radio: {self.radio}"




circulo1 = Circulo(5)

circulo2 = Circulo(3)



print(circulo1)

print("Área:", circulo1.area())

print("Circunferencia:",
      circulo1.circunferencia())

print("Diámetro:",
      circulo1.diametro())


print("¿Círculo 1 es mayor que círculo 2?",
      circulo1.es_mayor_que(circulo2))





# ==========================================
# PRÁCTICA 46
# Definición de la clase Estudiante
# Operaciones disponibles:
# agregar_nota()
# promedio()
# aprobado()
# cantidad_notas()
# Extensiones incorporadas:
# - nota_maxima()
# - nota_minima()
# - eliminar_nota()
# ==========================================



class Estudiante:


    def __init__(self, nombre):

        self.nombre = nombre

        self.notas = []



    def agregar_nota(self, nota):

        self.notas.append(nota)



    def promedio(self):

        return sum(self.notas) / len(self.notas)



    def aprobado(self):

        return self.promedio() >= 7



    def cantidad_notas(self):

        return len(self.notas)



    def nota_maxima(self):

        return max(self.notas)



    def nota_minima(self):

        return min(self.notas)



    def eliminar_nota(self, posicion):

        self.notas.pop(posicion)



    def mostrar(self):

        print("Nombre:", self.nombre)

        print("Notas:", self.notas)

        print("Promedio:", self.promedio())

        print("Aprobado:", self.aprobado())




estudiante = Estudiante("Derick")


estudiante.agregar_nota(8)

estudiante.agregar_nota(9)

estudiante.agregar_nota(7)


estudiante.mostrar()


print("Cantidad:",
      estudiante.cantidad_notas())


print("Nota mayor:",
      estudiante.nota_maxima())


print("Nota menor:",
      estudiante.nota_minima())




# ==========================================
# PRÁCTICA 47
# Definición de la clase Vehiculo
# Operaciones disponibles:
# recorrer()
# necesita_mantenimiento()
# reiniciar_mantenimiento()
# Extensiones incorporadas:
# - acelerar()
# - mostrar_km()
# - comparar_km()
# ==========================================



class Vehiculo:


    def __init__(self, marca, modelo):

        self.marca = marca

        self.modelo = modelo

        self.km = 0

        self.velocidad = 0



    def recorrer(self, kilometros):

        self.km += kilometros



    def necesita_mantenimiento(self):

        return self.km >= 10000



    def reiniciar_mantenimiento(self):

        self.km = 0



    def acelerar(self, aumento):

        self.velocidad += aumento



    def mostrar_km(self):

        return self.km



    def comparar_km(self, otro):

        if self.km > otro.km:

            return f"{self.marca} tiene más kilómetros"

        elif otro.km > self.km:

            return f"{otro.marca} tiene más kilómetros"

        else:

            return "Ambos tienen los mismos kilómetros"



    def __str__(self):

        return f"{self.marca} {self.modelo} - KM: {self.km} - Velocidad: {self.velocidad}"





vehiculo1 = Vehiculo("Toyota","Corolla")

vehiculo2 = Vehiculo("Mazda","3")



vehiculo1.recorrer(12000)

vehiculo2.recorrer(8000)


vehiculo1.acelerar(80)


print(vehiculo1)

print(vehiculo2)


print("Mantenimiento:",
      vehiculo1.necesita_mantenimiento())


print(vehiculo1.comparar_km(vehiculo2))


vehiculo1.reiniciar_mantenimiento()


print(vehiculo1)


# OPERACIONES CON LISTAS (list)

lista = [1, 2, 3]
tupla = (4, 5)
conjunto = {6, 7}
diccionario = {"a": 1}

# append(x)
# Añade un nuevo ítem al extremo final de la lista.
lista.append(5)

# extend(iterable)
# Anexa los ítems provenientes de otro iterable.
lista.extend([6, 7, 8])

# insert(pos, x)
# Ubica un nuevo ítem en el índice indicado.
lista.insert(1, 10)

# remove(x)
# Suprime la coincidencia inicial del valor especificado.
lista.remove(10)

# pop()
# Extrae y retorna el ítem situado al final.
lista.pop()

# pop(pos)
# Extrae y retorna el ítem ubicado en el índice indicado.
lista.pop(2)

# clear()
# Vacía por completo el contenido de la lista.
lista.clear()

# index(x)
# Retorna el índice correspondiente a la primera aparición del elemento.
lista.index(5)

# count(x)
# Contabiliza la frecuencia de aparición de un elemento.
lista.count(5)

# sort()
# Clasifica los elementos en sentido ascendente.
lista.sort()

# sort(reverse=True)
# Clasifica los elementos en sentido descendente.
lista.sort(reverse=True)

# reverse()
# Revierte la disposición actual de la lista.
lista.reverse()

# copy()
# Genera un duplicado independiente de la lista.
nueva_lista = lista.copy()

# len(lista)
# Retorna el total de elementos.
len(lista)

# sum(lista)
# Calcula la sumatoria de todos los números de la lista.
sum(lista)

# max(lista)
# Retorna el ítem de mayor valor.
max(lista)

# min(lista)
# Retorna el ítem de menor valor.
min(lista)

# sorted(lista)
# Retorna una copia ordenada sin alterar la colección inicial.
sorted(lista)

# enumerate(lista)
# Itera sobre la lista obteniendo posición y elemento.
for i, valor in enumerate(lista):
    print(i, valor)

# in
# Evalúa la existencia de un ítem.
if 5 in lista:
    print("Existe")

# not in
# Evalúa la ausencia de un ítem.
if 10 not in lista:
    print("No existe")



# =========================
# OPERACIONES CON TUPLAS (tuple)
# =========================

# count(x)
# Contabiliza la frecuencia de aparición de un elemento.
tupla.count(5)

# index(x)
# Retorna el índice correspondiente a un elemento.
tupla.index(5)

# len(tupla)
# Retorna el total de elementos.
len(tupla)

# max(tupla)
# Retorna el ítem de mayor valor.
max(tupla)

# min(tupla)
# Retorna el ítem de menor valor.
min(tupla)

# sum(tupla)
# Calcula la sumatoria de todos los elementos numéricos.
sum(tupla)

# sorted(tupla)
# Retorna una lista clasificada con los elementos.
sorted(tupla)

# in
# Evalúa la existencia de un ítem.
5 in tupla

# not in
# Evalúa la ausencia de un ítem.
10 not in tupla



# =========================
# OPERACIONES CON CONJUNTOS (set)
# =========================

# add(x)
# Incorpora un nuevo ítem.
conjunto.add(5)

# update(iterable)
# Incorpora múltiples ítems simultáneamente.
conjunto.update([6, 7])

# remove(x)
# Suprime un ítem; lanza excepción si no está presente.
conjunto.remove(5)

# discard(x)
# Suprime un ítem de forma segura sin lanzar error si falta.
conjunto.discard(5)

# pop()
# Extrae y elimina un ítem arbitrario.
conjunto.pop()

# clear()
# Suprime todos los elementos del set.
conjunto.clear()
conjunto2 = set()
# copy()
# Genera un duplicado independiente.
nuevo = conjunto.copy()

# union()
# Combina los elementos de ambos conjuntos.
conjunto.union(conjunto2)

# intersection()
# Retorna los ítems comunes.
conjunto.intersection(conjunto2)

# difference()
# Retorna los ítems que solo están en el primer conjunto.
conjunto.difference(conjunto2)

# symmetric_difference()
# Retorna los ítems diferentes entre ambos conjuntos.
conjunto.symmetric_difference(conjunto2)

# issubset()
# Comprueba si es subconjunto de otro set.
conjunto.issubset(conjunto2)

# issuperset()
# Comprueba si es superconjunto de otro set.
conjunto.issuperset(conjunto2)

# isdisjoint()
# Comprueba si ambos conjuntos son disjuntos.
conjunto.isdisjoint(conjunto2)

# len(conjunto)
# Total de ítems almacenados.
len(conjunto)

# in
# Comprueba la pertenencia de un ítem.
5 in conjunto

# not in
# Comprueba la ausencia de un ítem.
10 not in conjunto



# =========================
# OPERACIONES CON DICCIONARIOS (dict)
# =========================

# get(clave)
# Consulta el dato asociado a una llave o retorna None si está ausente.
diccionario.get("nombre")

# get(clave, valor)
# Retorna un valor predeterminado cuando la clave no se encuentra.
diccionario.get("edad", 0)

# keys()
# Retorna la colección de llaves del diccionario.
diccionario.keys()

# values()
# Retorna la colección de valores almacenados.
diccionario.values()

# items()
# Retorna pares de clave y valor.
diccionario.items()

# update()
# Incorpora o modifica múltiples entradas en el diccionario.
diccionario.update({"edad": 20})

# pop(clave)
# Suprime una llave y retorna el dato asociado.
diccionario.pop("edad")

# popitem()
# Extrae y suprime la última entrada del diccionario.
diccionario.popitem()

# clear()
# Suprime todas las entradas del diccionario.
diccionario.clear()

# copy()
# Genera un duplicado independiente.
nuevo = diccionario.copy()

# setdefault(clave, valor)
# Inserta la llave con el valor por defecto en caso de estar ausente.
diccionario.setdefault("pais", "Ecuador")

# len(diccionario)
# Total de entradas clave-valor registradas.
len(diccionario)

# in
# Comprueba si una llave está presente en el diccionario.
"nombre" in diccionario

# not in
# Comprueba la ausencia de una llave en el diccionario.
"apellido" not in diccionario



# =========================
# FUNCIONES FRECUENTES EN RESOLUCIÓN DE EJERCICIOS
# =========================

# range()
# Produce una progresión numérica.
range(5)

# enumerate()
# Itera sobre una secuencia obteniendo posición y elemento.
enumerate(lista)
lista1=[]
lista2=[]
# zip()
# Empareja ítems correspondientes de múltiples secuencias.
zip(lista1, lista2)

# sorted()
# Genera una nueva lista ordenada a partir de la colección.
sorted(lista)

# reversed()
# Itera sobre los elementos en orden inverso.
reversed(lista)

# any()
# Retorna True en caso de que al menos un elemento es True.
any(lista)

# all()
# Retorna True en caso de que todos los elementos son True.
all(lista)

# abs()
# Retorna la magnitud numérica sin signo.
abs(-5)

# round()
# Aproxima un valor decimal a la precisión indicada.
round(3.1416, 2)

# isinstance()
# Evalúa si una instancia corresponde a un tipo específico.
isinstance(lista, list)

# type()
# Retorna la clase o tipo de dato del elemento.
type(lista)



# =========================
# EXPRESIONES POR COMPRENSIÓN (USO FRECUENTE)
# =========================

# Generación de lista mediante comprensión
cuadrados = [x**2 for x in range(10)]

# Lista por comprensión con filtro condicional
pares = [x for x in range(20) if x % 2 == 0]

# Generación de diccionario mediante comprensión
dic = {x: x**2 for x in range(5)}

# Generación de conjunto mediante comprensión
conj = {x for x in range(10) if x % 2 == 0}



# =========================
# ITERACIONES MÁS HABITUALES
# =========================

# Iterar sobre una lista
for elemento in lista:
    print(elemento)

# Iterar sobre una lista con su índice
for i, elemento in enumerate(lista):
    print(i, elemento)

# Iterar sobre una tupla
for elemento in tupla:
    print(elemento)

# Iterar sobre un conjunto
for elemento in conjunto:
    print(elemento)

# Iterar sobre las llaves del diccionario
for clave in diccionario:
    print(clave)

# Iterar sobre los valores del diccionario
for valor in diccionario.values():
    print(valor)

# Iterar sobre llaves y valores simultáneamente
for clave, valor in diccionario.items():
    print(clave, valor)


# ==========================
# PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON
# ==========================

# class
# Define una nueva estructura de clase.

class Persona:
    pass


# __init__(self, ...)
# Método inicializador que se invoca de forma automática al instanciar.
# Se encarga de establecer los valores iniciales de las propiedades.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# self
# Hace referencia a la propia instancia en ejecución.
# Facilita el acceso a las propiedades y funciones internas del objeto.

        self.nombre
        self.edad


# ==========================
# TIPOS DE MÉTODOS MÁS FRECUENTES
# ==========================

# Implementación de normal
# Ejecuta una operación sobre la instancia.

def saludar(self):
    print("Hola")


# Implementación de que retorna un valor
# Retorna un resultado calculado.

def area(self):
    return self.base * self.altura


# Implementación de que modifica atributos

def cumplir_anios(self):
    self.edad += 1


# Método parametrizado

def depositar(self, cantidad):
    self.saldo += cantidad


# Implementación de que devuelve True o False

def aprobado(self):
    return self.promedio() >= 7


# ==========================
# MÉTODOS MÁGICOS O ESPECIALES
# ==========================

# __str__
# Establece la representación legible en texto de la instancia.

def __str__(self):
    return f"{self.nombre} - {self.edad}"


# __repr__
# Define la representación técnica de la instancia para depuración.

def __repr__(self):
    return f"Persona('{self.nombre}', {self.edad})"


# __len__
# Habilita el uso de la función integrada len() sobre la instancia.

def __len__(self):
    return len(self.notas)


# __eq__
# Define el comportamiento del operador de igualdad == entre instancias

def __eq__(self, otro):
    return self.nombre == otro.nombre


# __lt__
# Habilita la comparación mediante el operador <

def __lt__(self, otro):
    return self.edad < otro.edad


# __gt__
# Habilita la comparación mediante el operador >

def __gt__(self, otro):
    return self.edad > otro.edad


# ==========================
# USO DE DECORADORES
# ==========================

# @classmethod
# Opera a nivel de clase en lugar de sobre una instancia particular.
# Recibe cls como primer argumento de referencia.

@classmethod
def total(cls, lista):
    pass


# @staticmethod
# No requiere referencia a la instancia (self) ni a la clase (cls).
# Define una utilidad auxiliar vinculada conceptualmente a la clase.

@staticmethod
def convertir_dolares(valor):
    return valor * 3.8


# @property
# Habilita la consulta de un método utilizando sintaxis de atributo.

@property
def nombre_completo(self):
    return self.nombre + " " + self.apellido


# ==========================
# PROPIEDADES Y ATRIBUTOS
# ==========================

# Propiedad propia de cada instancia
# Cada instancia mantiene su propio valor independiente.

    self.nombre
    self.edad
    self.saldo


# Propiedad compartida a nivel de clase
# Es compartido por todas las instancias de la clase.

class Persona:

    especie = "Humano"


# ==========================
# FUNCIONES INTEGRADAS DE USO COMÚN
# ==========================
objeto={}
# isinstance()
# Comprueba si una instancia corresponde a cierta clase.

isinstance(objeto, Persona)


# type()
# Retorna la clase o tipo de dato del elemento.

type(objeto)

persona=""
# hasattr()
# Comprueba si el objeto posee determinada propiedad.

hasattr(persona, "edad")


# getattr()
# Recupera el valor de una propiedad del objeto.

getattr(persona, "edad")


# setattr()
# Modifica una propiedad existente o la define si no existe.

setattr(persona, "edad", 20)


# delattr()
# Suprime una propiedad del objeto.

delattr(persona, "edad")


# ==========================
# HERENCIA ENTRE CLASES
# ==========================

# Definir una subclase que hereda de otra.

class Animal:
    pass

class Perro(Animal):
    pass


# super()
# Invoca el inicializador o métodos definidos en la superclase.

super().__init__()


# ==========================
# INSTANCIACIÓN Y MANEJO DE OBJETOS
# ==========================

# Instanciar un objeto

persona = Persona("Juan", 20)


# Consultar propiedades de la instancia

persona.nombre
persona.edad


# Actualizar propiedades de la instancia

persona.edad = 25


# Invocar métodos de la instancia

persona.saludar()
persona.cumplir_anios()


# ==========================
# PATRONES DE CÓDIGO HABITUALES
# ==========================
class numero:
    def __init__(self,cantidad):
        pass
# Incrementar una propiedad numérica

# self.stock += cantidad


# Decrementar una propiedad numérica
# self.stock -= cantidad


# Restablecer una propiedad a su valor base

# self.saldo = 0


# Calcular producto entre propiedades
 # return self.precio * self.stock


# Comparar

     # if self.stock >= cantidad:
      # pass


# Validar

     # if cantidad > 0:
      # pass


# ==========================
# ITERACIÓN SOBRE COLECCIONES INTERNAS
# ==========================

# Iterar sobre una lista interna

# for nota in self.notas:
 # print(nota)


# Iterar sobre los pares de un diccionario

# for clave, valor in self.datos.items():
  # print(clave, valor)


# ==========================
# NOMBRES DE MÉTODOS FRECUENTES EN PRÁCTICAS
# ==========================

# agregar()
# agregar_nota()
# agregar_producto()
# agregar_estudiante()
# agregar_libro()

# eliminar()
# eliminar_producto()
# eliminar_cliente()

# buscar()

# actualizar()

# modificar()

# vender()

# comprar()

# depositar()

# retirar()

# transferir()

# recorrer()

# reabastecer()

# promedio()

# aprobado()

# area()

# perimetro()

# volumen()

# circunferencia()

# valor_inventario()

# total_inventario()

# calcular_total()

# calcular_promedio()

# mayor()

# menor()

# ordenar()

# contar()

# mostrar()

# listar()

# imprimir()

# resumen()

# ver_historial()

# limpiar()

# reiniciar()

# necesita_mantenimiento()

# cumplir_anios()

# es_mayor()

# cambiar_nombre()

# cambiar_precio()

# cambiar_stock()

# ==========================
# PALABRAS RESERVADAS Y ELEMENTOS CLAVE
# ==========================

# class
# def
# self
# cls
# return
# pass
# super
# @classmethod
# @staticmethod
# @property
# __init__
# __str__
# __repr__
# __len__
# __eq__
# __lt__
# __gt__

# ===============================
# CATÁLOGO DE MÉTODOS FRECUENTES EN CLASES
# ===============================


# -------------------------------
# Modificar una propiedad
# -------------------------------
def cambiar_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre


# -------------------------------
# Incrementar una cantidad
# -------------------------------
def aumentar(self, cantidad):
    self.valor += cantidad


# -------------------------------
# Reducir una cantidad
# -------------------------------
def disminuir(self, cantidad):
    self.valor -= cantidad


# -------------------------------
# Incrementar la edad en un año
# -------------------------------
def cumplir_anios(self):
    self.edad += 1


# -------------------------------
# Comprobar mayoría de edad
# -------------------------------
def es_mayor(self):
    return self.edad >= 18


# -------------------------------
# Añadir un ítem a la lista
# -------------------------------
def agregar(self, elemento):
    self.lista.append(elemento)


# -------------------------------
# Suprimir un ítem de la lista
# -------------------------------
def eliminar(self, elemento):
    if elemento in self.lista:
        self.lista.remove(elemento)


# -------------------------------
# Limpiar el contenido de la lista
# -------------------------------
def limpiar(self):
    self.lista.clear()


# -------------------------------
# Obtener el total de ítems
# -------------------------------
def cantidad(self):
    return len(self.lista)


# -------------------------------
# Comprobar pertenencia de un ítem
# -------------------------------
def existe(self, elemento):
    return elemento in self.lista


# -------------------------------
# Extraer el valor máximo
# -------------------------------
def mayor(self):
    return max(self.lista)


# -------------------------------
# Extraer el valor mínimo
# -------------------------------
def menor(self):
    return min(self.lista)


# -------------------------------
# Obtener la media aritmética
# -------------------------------
def promedio(self):
    if len(self.lista) == 0:
        return 0
    return sum(self.lista) / len(self.lista)


# -------------------------------
# Calcular la sumatoria total
# -------------------------------
def suma(self):
    return sum(self.lista)


# -------------------------------
# Consultar existencia de un ítem
# -------------------------------
def buscar(self, elemento):
    return elemento in self.lista


# -------------------------------
# Clasificar en orden ascendente
# -------------------------------
def ordenar(self):
    self.lista.sort()


# -------------------------------
# Clasificar en orden descendente
# -------------------------------
def ordenar_desc(self):
    self.lista.sort(reverse=True)


# -------------------------------
# Revertir el orden de la lista
# -------------------------------
def invertir(self):
    self.lista.reverse()


# -------------------------------
# Consultar el ítem final
# -------------------------------
def ultimo(self):
    if len(self.lista) > 0:
        return self.lista[-1]
    return None


# -------------------------------
# Consultar el ítem inicial
# -------------------------------
def primero(self):
    if len(self.lista) > 0:
        return self.lista[0]
    return None


# -------------------------------
# Limpiar el registro histórico
# -------------------------------
def borrar_historial(self):
    self.historial.clear()


# -------------------------------
# Registrar evento en el historial
# -------------------------------
def agregar_historial(self, texto):
    self.historial.append(texto)


# -------------------------------
# Desplegar el registro histórico
# -------------------------------
def ver_historial(self):
    for dato in self.historial:
        print(dato)


# -------------------------------
# Restablecer un valor a cero
# -------------------------------
def reiniciar(self):
    self.valor = 0


# -------------------------------
# Habilitar indicador de estado
# -------------------------------
def activar(self):
    self.activo = True


# -------------------------------
# Deshabilitar indicador de estado
# -------------------------------
def desactivar(self):
    self.activo = False


# -------------------------------
# Alternar indicador de estado
# -------------------------------
def cambiar_estado(self):
    self.activo = not self.activo


# -------------------------------
# Consultar indicador de estado
# -------------------------------
def esta_activo(self):
    return self.activo


# -------------------------------
# Abonar saldo a la cuenta
# -------------------------------
def depositar(self, cantidad):
    self.saldo += cantidad


# -------------------------------
# Debitar saldo de la cuenta
# -------------------------------
def retirar(self, cantidad):
    if cantidad <= self.saldo:
        self.saldo -= cantidad
        return True
    return False


# -------------------------------
# Consultar saldo disponible
# -------------------------------
def mostrar_saldo(self):
    return self.saldo


# -------------------------------
# Aplicar rebaja porcentual
# -------------------------------
def aplicar_descuento(self, porcentaje):
    self.precio -= self.precio * porcentaje / 100


# -------------------------------
# Aplicar aumento porcentual al precio
# -------------------------------
def aumentar_precio(self, porcentaje):
    self.precio += self.precio * porcentaje / 100


# -------------------------------
# Obtener precio con impuesto incluido
# -------------------------------
def precio_con_iva(self):
    return self.precio * 1.15


# -------------------------------
# Descontar unidades por venta
# -------------------------------
def vender(self, cantidad):
    if cantidad <= self.stock:
        self.stock -= cantidad
        return True
    return False


# -------------------------------
# Reabastecer
# -------------------------------
def reabastecer(self, cantidad):
    self.stock += cantidad


# -------------------------------
# Comprobar disponibilidad en inventario
# -------------------------------
def hay_stock(self):
    return self.stock > 0


# -------------------------------
# Calcular valoración total del stock
# -------------------------------
def valor_inventario(self):
    return self.precio * self.stock


# -------------------------------
# Sumar kilometraje recorrido
# -------------------------------
def recorrer(self, km):
    self.km += km


# -------------------------------
# Restablecer contador de kilómetros
# -------------------------------
def reiniciar_km(self):
    self.km = 0


# -------------------------------
# Evaluar requerimiento de mantenimiento
# -------------------------------
def necesita_mantenimiento(self):
    return self.km >= 10000


# -------------------------------
# Aprobar
# -------------------------------
def aprobado(self):
    return self.promedio() >= 7


# -------------------------------
# Registrar una calificación
# -------------------------------
def agregar_nota(self, nota):
    self.notas.append(nota)


# -------------------------------
# Consultar total de calificaciones
# -------------------------------
def cantidad_notas(self):
    return len(self.notas)


# -------------------------------
# Añadir un ítem al set
# -------------------------------
def agregar_conjunto(self, dato):
    self.conjunto.add(dato)


# -------------------------------
# Suprimir un ítem del set
# -------------------------------
def eliminar_conjunto(self, dato):
    self.conjunto.discard(dato)


# -------------------------------
# Asignar par clave-valor en el diccionario
# -------------------------------
def agregar_diccionario(self, clave, valor):
    self.diccionario[clave] = valor


# -------------------------------
# Consultar valor asociado a una clave
# -------------------------------
def obtener_diccionario(self, clave):
    return self.diccionario.get(clave)


# -------------------------------
# Suprimir entrada del diccionario
# -------------------------------
def eliminar_diccionario(self, clave):
    self.diccionario.pop(clave, None)


# -------------------------------
# Obtener total de entradas del diccionario
# -------------------------------
def cantidad_claves(self):
    return len(self.diccionario)


# -------------------------------
# Representación textual de la instancia
# -------------------------------
def __str__(self):
    return f"{self.nombre}"
