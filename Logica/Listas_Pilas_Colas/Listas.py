import math

# EJERCICIO: Gestión integral para registrar, listar, consultar por cédula, actualizar, eliminar y ordenar alfabéticamente pasajeros empleando la clase Pasajero junto con una lista.

# 1. Análisis del problema
# Datos de entrada: Opción seleccionada del menú e información del pasajero (nombre, cédula o nombre actualizado) conforme a la acción elegida.
# Procesamiento: Administrar una colección de instancias Pasajero habilitando el registro (evitando cédulas repetidas), visualización, búsqueda por cédula, edición de nombre, borrado, ordenamiento alfabético por nombre y salida.
# Resultado esperado: Notificaciones de confirmación, reportes de pasajeros, resultados de consulta o alertas de error/inexistencia en consola.

# 2. Diseño en pseudocódigo
# Declarar clase Pasajero con nombre, cedula y representación __str__
# Codificar función auxiliar buscar_por_cedula(lista, ced)
# Inicializar lista vacía para almacenar los pasajeros
# Dentro de un bucle while True, desplegar el menú con las acciones disponibles
# Incorporar la opción 6 para ordenar la colección por nombre mediante lista.sort(key=lambda p: p.nombre) y desplazar Salir a la opción 7
# Ejecutar la operación seleccionada hasta que el usuario decida finalizar

# 3. Identificación de la lógica
# Cada pasajero se modela como una instancia de Pasajero almacenada dentro de una lista dinámica.
# Reutilizar buscar_por_cedula evita código repetido en las operaciones de consulta, edición y borrado.
# El ordenamiento en sitio mediante sort() con una expresión lambda permite clasificar objetos según su atributo nombre.

# 4. Implementación en Python

class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Devuelve la instancia encontrada o None si no existe."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Flujo principal del programa ---
lista = []

while True:
    print("\n--- MENÚ ---")
    # Incorporación de la opción 6.Ordenar por nombre y reubicación de Salir en la opción 7
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar por nombre 7.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado")
        else:
            print("No existe")

    # Funcionalidad añadida para ordenar alfabéticamente los pasajeros por nombre empleando sort y lambda
    elif op == "6":
        if not lista:
            print("No hay pasajeros para ordenar")
        else:
            lista.sort(key=lambda p: p.nombre.lower())
            print("Lista ordenada por nombre")

    # Reasignación de la salida a la opción "7" tras incluir el ordenamiento
    elif op == "7":
        break

    # Control de errores para entradas no contempladas en el menú
    else:
        print("Opción inválida")



# EJERCICIO: A partir de una lista de N calificaciones y una lista paralela de nombres, obtener promedio, calificación máxima, mínima, total de aprobados, alumno destacado y desviación estándar poblacional.

# 1. Análisis del problema
# Datos de entrada: Lista de nombres de alumnos y lista paralela de N calificaciones numéricas.
# Procesamiento: Determinar promedio, nota máxima, nota mínima, conteo de notas iguales o superiores a 7, alumno con mayor calificación y desviación estándar mediante sqrt(sum((n - prom)**2 for n in notas) / len(notas)), comparando funciones nativas con el cálculo iterativo manual.
# Resultado esperado: Indicadores estadísticos de promedio, extremos, aprobados, mejor alumno y dispersión estándar impresos en consola.

# 2. Diseño en pseudocódigo
# Declarar listas paralelas nombres y notas
# Obtener promedio, max, min, aprobados y alumno destacado aprovechando utilidades y comprensiones de Python
# Incorporar el cálculo de desviación estándar mediante math.sqrt y el promedio obtenido
# Ejecutar un recorrido manual con bucle for para acumular sumas, hallar extremos, contar aprobados y sumar desviaciones cuadráticas
# Obtener la raíz cuadrada de la varianza manual e imprimir los resultados

# 3. Identificación de la lógica
# Las listas paralelas se vinculan mediante posiciones de índice o expresiones generadoras para asociar cada nota con su estudiante.
# El promedio calculado previamente se reutiliza para cuantificar la desviación cuadrática de cada elemento respecto a la media.
# Se comparan las herramientas nativas de Python frente a una implementación manual basada en acumuladores.

# 4. Implementación en Python

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Utilidades integradas de Python:
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Conteo de aprobados mediante comprensión de listas y len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Identificación del mejor alumno localizando el índice de la nota máxima
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# Cálculo agregado de la desviación estándar poblacional según la ecuación establecida
desviacion_std = math.sqrt(sum((n - promedio) ** 2 for n in notas) / len(notas))
print(f"Desviación estándar: {desviacion_std:.2f}")

# --- Implementación manual (para comprender el funcionamiento interno) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

# Computar manualmente la media aritmética y la desviación estándar a partir de los acumuladores
prom_manual = suma / len(notas)
suma_cuadrados = 0
for n in notas:
    suma_cuadrados += (n - prom_manual) ** 2
desv_manual = math.sqrt(suma_cuadrados / len(notas))

print(f"\nManual -> prom: {prom_manual:.2f}, máx: {maxima}, mín: {minima}, aprob: {aprob_manual}, mejor: {nombres[idx_max_manual]}, desv_std: {desv_manual:.2f}")

# EJERCICIO: Codificar el ordenamiento burbuja sobre una lista, contrastar su salida con list.sort() e implementar selection sort ubicando en cada pasada el menor valor del tramo restante al principio.

# 1. Análisis del problema
# Datos de entrada: Lista de valores numéricos sin ordenar.
# Procesamiento: Ordenar duplicados de la lista aplicando el método de burbuja, validar la equivalencia frente a list.sort() y ordenar otra copia mediante selection sort localizando en cada iteración el elemento mínimo del segmento pendiente para intercambiarlo con el inicio de dicho segmento.
# Resultado esperado: Listas resultantes de burbuja, verificación de coincidencia contra list.sort() y resultado de selection sort impresos en pantalla.

# 2. Diseño en pseudocódigo
# Declarar una lista inicial desordenada
# Duplicar la lista y aplicar ordenamiento burbuja intercambiando elementos adyacentes desordenados
# Duplicar la lista base y ordenarla con list.sort() como referencia
# Añadir la lógica de selection sort iterando el índice actual i desde 0 hasta n - 1
# En cada iteración de selection sort, hallar la posición del mínimo entre i y n - 1 e intercambiarlo con la posición i
# Mostrar y contrastar las salidas obtenidas por cada enfoque

# 3. Identificación de la lógica
# Ambos algoritmos ordenan en sitio particionando gradualmente la colección en una sublista ordenada y otra pendiente.
# Burbuja desplaza los valores mayores hacia el extremo derecho mediante permutaciones contiguas, mientras selection sort elige el mínimo restante efectuando un único intercambio por ciclo.
# Trabajar sobre copias preserva intacta la lista original para realizar comparaciones justas entre algoritmos.

# 4. Implementación en Python

def ordenamiento_burbuja(datos):
    lista = datos.copy()
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista


# Implementación adicional de selection sort localizando el mínimo restante para situarlo al inicio
def selection_sort(datos):
    lista = datos.copy()
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        if indice_min != i:
            lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


# --- Ejecución y contraste ---
original = [38, 12, 45, 7, 23, 12]

burbuja_res = ordenamiento_burbuja(original)

referencia_sort = original.copy()
referencia_sort.sort()

# Aplicar selection sort sobre un duplicado de la lista base
seleccion_res = selection_sort(original)

print(f"Original: {original}")
print(f"Burbuja: {burbuja_res}")
print(f"list.sort(): {referencia_sort}")
print(f"Coincide burbuja con list.sort(): {burbuja_res == referencia_sort}")

# Mostrar el resultado de selection sort junto con su verificación frente a list.sort()
print(f"Selection sort: {seleccion_res}")
print(f"Coincide selection sort con list.sort(): {seleccion_res == referencia_sort}")

# EJERCICIO: Dada una colección numérica y un valor objetivo, contabilizar sus apariciones e incorporar la extracción de los índices donde se ubica.

# 1. Análisis del problema
# Datos de entrada: Lista de valores numéricos y elemento objetivo a localizar.
# Procesamiento: Iterar sobre la lista o emplear count() para calcular la frecuencia del número buscado, añadiendo una función complementaria que recopile los índices exactos de cada coincidencia.
# Resultado esperado: Total de apariciones del elemento y listado de posiciones en consola.

# 2. Diseño en pseudocódigo
# Declarar la lista numérica y el valor a rastrear
# Contabilizar coincidencias mediante un acumulador en un ciclo for y contrastar con lista.count(valor)
# Incorporar la recolección de las posiciones donde aparece el elemento buscado
# Desplegar el total de ocurrencias junto con los índices encontrados

# 3. Identificación de la lógica
# Se itera secuencialmente sobre la lista cotejando cada ítem contra el valor objetivo para incrementar un contador.
# La función enumerate facilita acceder al índice y al valor simultáneamente de forma clara.
# Cotejar el resultado manual frente a lista.count() confirma la exactitud del algoritmo.

# 4. Implementación en Python

def contar_ocurrencias(numeros, objetivo):
    contador = 0
    for numero in numeros:
        if numero == objetivo:
            contador += 1
    return contador


# Función complementaria obtener_indices para almacenar las posiciones de cada aparición
def obtener_indices(numeros, objetivo):
    indices = []
    for indice, numero in enumerate(numeros):
        if numero == objetivo:
            indices.append(indice)
    return indices


# --- Ejemplos de ejecución ---
numeros = [4, 7, 2, 4, 9, 4, 1, 7]
valor_buscado = 4

total_manual = contar_ocurrencias(numeros, valor_buscado)
total_count = numeros.count(valor_buscado)

# Obtener y mostrar las posiciones exactas donde se encuentra el número buscado
posiciones = obtener_indices(numeros, valor_buscado)

print(f"Lista: {numeros}")
print(f"Valor buscado: {valor_buscado}")
print(f"Apariciones (manual): {total_manual}")
print(f"Apariciones (count): {total_count}")
print(f"Posiciones (índices): {posiciones}")

# EJERCICIO: Revertir la secuencia de una lista sin recurrir a lista.reverse(), incorporando una validación de equivalencia.

# 1. Análisis del problema
# Datos de entrada: Lista de elementos en su disposición original.
# Procesamiento: Permutar los elementos desde los extremos hacia el centro mediante dos punteros sin usar lista.reverse(), añadiendo una verificación que contraste el resultado contra list(reversed()).
# Resultado esperado: Lista inicial, lista invertida y confirmación booleana de validez en consola.

# 2. Diseño en pseudocódigo
# Declarar una lista inicial con datos
# Generar una copia para invertirla en sitio empleando dos índices (izquierda y derecha)
# Permutar valores opuestos avanzando hacia el centro mientras izquierda < derecha
# Incorporar la validación comparando contra list(reversed(original))
# Imprimir la lista original, la invertida y el resultado de la comprobación

# 3. Identificación de la lógica
# Emplear dos punteros convergentes permite revertir una colección in-place en una sola pasada sin estructuras auxiliares completas.
# La asignación múltiple de Python realiza el intercambio sin requerir variables temporales.
# Contrastar contra list(reversed(lista)) valida el resultado manteniendo intacta la lista de entrada.

# 4. Implementación en Python

def invertir_lista(elementos):
    lista = elementos.copy()
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda < derecha:
        lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
        izquierda += 1
        derecha -= 1

    return lista


# Función auxiliar verificar_inversion para validar la salida frente a reversed()
def verificar_inversion(original, invertida):
    return invertida == list(reversed(original))


# --- Ejemplos de ejecución ---
original = [10, 20, 30, 40, 50]
invertida = invertir_lista(original)

# Confirmar que el orden invertido sea correcto empleando reversed()
es_valida = verificar_inversion(original, invertida)

print(f"Original: {original}")
print(f"Invertida: {invertida}")
print(f"Inversión válida: {es_valida}")

# EJERCICIO: Dada una lista con elementos repetidos, devolver una nueva colección sin duplicados respetando el orden de aparición.

# 1. Análisis del problema
# Datos de entrada: Colección de elementos que puede contener valores duplicados.
# Procesamiento: Iterar sobre la lista conservando únicamente la primera ocurrencia de cada valor y contabilizar cuántos duplicados fueron descartados.
# Resultado esperado: Lista depurada sin repeticiones en su orden original y cantidad de elementos eliminados.

# 2. Diseño en pseudocódigo
# Definir una lista con valores repetidos
# Inicializar una lista vacía para elementos únicos y un conjunto (set) para registrar los ya procesados
# Iterar sobre cada elemento: si no figura en el conjunto, añadirlo a ambas estructuras
# Contabilizar cuántos elementos duplicados quedaron excluidos
# Imprimir la lista inicial, la depurada y el total de duplicados descartados

# 3. Identificación de la lógica
# Registrar los elementos visitados en un set permite verificar pertenencia en tiempo constante O(1).
# Recorrer secuencialmente de izquierda a derecha preserva la posición de primera aparición de cada elemento.
# Encapsular la depuración en una función facilita su reutilización sobre cualquier lista.

# 4. Implementación en Python

def eliminar_duplicados(elementos):
    sin_duplicados = []
    vistos = set()

    for elemento in elementos:
        if elemento not in vistos:
            vistos.add(elemento)
            sin_duplicados.append(elemento)

    return sin_duplicados


# Función complementaria para calcular el total de elementos duplicados descartados
def contar_duplicados_eliminados(original, limpia):
    return len(original) - len(limpia)


# --- Ejemplos de ejecución ---
entrada = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "María"]
resultado = eliminar_duplicados(entrada)

# Obtener la cantidad de repeticiones eliminadas como métrica informativa adicional
eliminados = contar_duplicados_eliminados(entrada, resultado)

print(f"Lista original: {entrada}")
print(f"Sin duplicados (en orden): {resultado}")
print(f"Duplicados eliminados: {eliminados}")

# EJERCICIO: Determinar el segundo valor máximo de una lista sin ordenarla por completo.

# 1. Análisis del problema
# Datos de entrada: Lista numérica (con valores positivos, negativos o repetidos).
# Procesamiento: Iterar sobre la lista rastreando simultáneamente el máximo y el segundo máximo sin ordenar toda la colección, añadiendo una función que contabilice cuántas veces se repite dicho segundo mayor.
# Resultado esperado: El segundo valor más alto encontrado y su frecuencia de aparición en la lista.

# 2. Diseño en pseudocódigo
# Contemplar la existencia de al menos dos valores distintos para determinar un segundo máximo
# Inicializar mayor y segundo como None
# Iterar sobre cada número: si supera a mayor, desplazar mayor hacia segundo y actualizar mayor
# Si es distinto de mayor y supera a segundo, actualizar segundo
# Contabilizar la frecuencia del segundo valor máximo dentro de la colección
# Desplegar ambos resultados en consola

# 3. Identificación de la lógica
# Mantener dos variables de estado en un único recorrido lineal evita el costo de ordenar la lista completa.
# Excluir los valores iguales al máximo principal impide que un número repetido ocupe ambos puestos.
# Aislar el conteo de frecuencia en una función separada mejora la claridad estructural del código.

# 4. Implementación en Python

def segundo_mayor(numeros):
    mayor = None
    segundo = None

    for n in numeros:
        if mayor is None or n > mayor:
            segundo = mayor
            mayor = n
        elif n != mayor and (segundo is None or n > segundo):
            segundo = n

    return segundo


# Función complementaria para contabilizar las apariciones del segundo valor máximo
def contar_apariciones(numeros, valor):
    if valor is None:
        return 0
    return sum(1 for n in numeros if n == valor)


# --- Ejemplos de ejecución ---
datos = [14, 5, 28, 28, 19, 3, 28]
resultado = segundo_mayor(datos)

# Calcular cuántas veces figura el segundo máximo dentro de la colección original
veces = contar_apariciones(datos, resultado)

print(f"Lista: {datos}")
print(f"Segundo número más grande: {resultado}")
print(f"Veces que aparece en la lista: {veces}")

# EJERCICIO: Combinar dos listas previamente ordenadas en una tercera lista ordenada sin emplear sort().

# 1. Análisis del problema
# Datos de entrada: Dos listas que ya se encuentran ordenadas (ej. de forma ascendente).
# Procesamiento: Cotejar los elementos actuales de ambas listas mediante dos índices para construir una nueva lista ordenada sin recurrir a sort(), incorporando un resumen con el total de elementos integrados.
# Resultado esperado: La colección resultante fusionada y ordenada, acompañada del conteo global de elementos.

# 2. Diseño en pseudocódigo
# Recibir dos colecciones ordenadas lista1 y lista2
# Inicializar punteros i = 0 y j = 0, junto con una lista vacía fusionada
# Mientras queden elementos en ambas listas, comparar lista1[i] y lista2[j] e insertar el menor en fusionada
# Al agotarse una lista, anexar los elementos restantes de la otra
# Generar un resumen con la longitud total de la lista combinada
# Imprimir las listas iniciales, la lista fusionada y el resumen

# 3. Identificación de la lógica
# Dado que ambas listas mantienen un orden previo, basta comparar únicamente sus elementos frontales en cada iteración.
# Incrementar solo el índice de la lista de donde se extrae el elemento garantiza el orden global en tiempo lineal.
# Los elementos remanentes al finalizar el ciclo principal ya están ordenados y pueden añadirse directamente.

# 4. Implementación en Python

def fusionar_listas_ordenadas(lista1, lista2):
    fusionada = []
    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            fusionada.append(lista1[i])
            i += 1
        else:
            fusionada.append(lista2[j])
            j += 1

    # Anexar los elementos pendientes de lista1 en caso de que aún queden por procesar
    while i < len(lista1):
        fusionada.append(lista1[i])
        i += 1

    # Anexar los elementos pendientes de lista2 en caso de que aún queden por procesar
    while j < len(lista2):
        fusionada.append(lista2[j])
        j += 1

    return fusionada


# Función auxiliar para generar un mensaje resumen de la combinación efectuada
def resumen_fusion(lista1, lista2, fusionada):
    return f"Total combinados: {len(fusionada)} (de {len(lista1)} + {len(lista2)} elementos)"


# --- Ejemplos de ejecución ---
a = [1, 4, 7, 10]
b = [2, 3, 7, 12, 15]

resultado = fusionar_listas_ordenadas(a, b)

# Desplegar el resumen informativo para complementar la salida de la colección fusionada
resumen = resumen_fusion(a, b, resultado)

print(f"Lista 1: {a}")
print(f"Lista 2: {b}")
print(f"Lista fusionada ordenada: {resultado}")
print(resumen)
