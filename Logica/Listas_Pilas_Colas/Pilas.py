from collections import deque

# EJERCICIO: Emplear una estructura de pila para invertir una cadena de caracteres y extender la lógica para invertir únicamente el orden de las palabras sin modificar sus letras mediante split(" ").

# 1. Análisis del problema
# Datos de entrada: Una cadena de texto (como "Python", "Hola" o "Hola Mundo").
# Procesamiento: Apilar letras o palabras completas en una deque empleada como pila (LIFO) y extraerlas para recomponer el texto en sentido inverso, incorporando una función adicional que invierta la secuencia de palabras manteniendo intacta cada una.
# Resultado esperado: El texto invertido letra por letra, su contraste con el atajo nativo y la oración con sus palabras en orden inverso.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Codificar invertir_con_pila(s) apilando cada carácter y desapilando para construir la cadena invertida
# Incorporar invertir_palabras_con_pila(frase) fragmentando con split(" ") y utilizando deque como pila
# Apilar cada palabra secuencialmente y extraerlas uniéndolas mediante espacios
# Ejecutar pruebas para ambas funciones e imprimir los resultados en pantalla

# 3. Identificación de la lógica
# Una pila opera bajo el esquema LIFO (último en entrar, primero en salir), lo cual resulta óptimo para revertir secuencias.
# Al segmentar mediante split(" "), cada elemento almacenado en la pila corresponde a una palabra entera en lugar de un carácter aislado.
# Reutilizar la mecánica de inserción y extracción en la pila permite resolver tanto la inversión de caracteres como la de palabras.

# 4. Implementación en Python

def invertir_con_pila(s):
    pila = deque()
    # Etapa 1: insertar todos los caracteres en la pila
    for letra in s:
        pila.append(letra)
    # Etapa 2: extraer elementos para ensamblar la cadena resultante
    resultado = ""
    while pila:
        resultado += pila.pop()
    return resultado


# Función adicional para revertir la secuencia de palabras conservando intacta la escritura de cada una
def invertir_palabras_con_pila(frase):
    pila = deque()
    palabras = frase.split(" ")

    # Etapa de inserción de cada palabra completa en la pila
    for palabra in palabras:
        pila.append(palabra)

    # Etapa de extracción de las palabras para reconstruir la oración en orden inverso
    invertidas = []
    while pila:
        invertidas.append(pila.pop())

    return " ".join(invertidas)


# --- Ejemplos de ejecución ---
print(invertir_con_pila("Python"))    # nohtyP
print(invertir_con_pila("Hola"))      # aloH

# Caso de prueba para revertir únicamente las palabras empleando pila y split(" ")
print(invertir_palabras_con_pila("Hola Mundo"))  # Mundo Hola

# Contraste con la técnica idiomática de Python (slicing)
print("Python"[::-1])                 # nohtyP (en una sola instrucción)

# Contraste equivalente abreviado para invertir el orden de las palabras
print(" ".join("Hola Mundo".split(" ")[::-1]))



# EJERCICIO: Analizar una expresión con paréntesis, corchetes y llaves para comprobar si están debidamente balanceados y anidados, informando el índice exacto del fallo en caso contrario.

# 1. Análisis del problema
# Datos de entrada: Una cadena de texto que puede contener paréntesis, corchetes y llaves.
# Procesamiento: Iterar sobre la cadena apoyándose en una pila (deque) para confirmar que cada delimitador de cierre corresponda con el último de apertura y que no existan bloques abiertos sin cerrar al concluir, registrando además el índice donde surge el primer error.
# Resultado esperado: Diagnóstico de validez de la expresión junto con la posición exacta del fallo cuando no esté balanceada.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Mapear los símbolos de cierre hacia sus respectivas aperturas y utilizar una pila que almacene tuplas (símbolo, índice)
# Iterar carácter por carácter con enumerate para rastrear la posición exacta
# Ante una apertura, apilar (ch, idx); ante un cierre, comprobar que la pila no esté vacía y que coincida con el tope
# Reportar el índice del cierre erróneo o, si quedan aperturas pendientes al finalizar, la posición de la primera sin cerrar
# Validar con diversas expresiones e imprimir el diagnóstico detallado

# 3. Identificación de la lógica
# Almacenar el índice junto con cada símbolo de apertura permite localizar con exactitud dónde quedó un delimitador sin cerrar.
# Al detectar un cierre huérfano o incompatible, el índice actual de iteración señala el punto preciso del error.
# Devolver el estado booleano acompañado del índice de fallo simplifica la depuración y la explicación del error.

# 4. Implementación en Python

def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}   # mapeo cierre -> apertura

    # Almacenar tuplas (simbolo, indice) en la pila para rastrear aperturas sin cierre
    for idx, ch in enumerate(s):
        if ch in "([{":
            # Símbolo de apertura: se apila junto con su índice
            pila.append((ch, idx))
        elif ch in ")]}":
            # Símbolo de cierre: el tope de la pila debe corresponder a su pareja
            if not pila or pila[-1][0] != parejas[ch]:
                # Devolver False junto con el índice exacto del delimitador de cierre inválido
                return False, idx
            pila.pop()

    # Comprobar si quedaron símbolos de apertura pendientes e informar el índice del primero
    if pila:
        _, idx_pendiente = pila[0]
        return False, idx_pendiente

    return True, None


# Función auxiliar para dar formato legible al diagnóstico de cada expresión evaluada
def describir_resultado(expresion):
    valido, pos_error = paren_balanceado(expresion)
    if valido:
        return "Balanceado"
    return f"No balanceado (error en posición {pos_error})"


# --- Casos de prueba ---
tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]
for t in tests:
    # Desplegar el diagnóstico y el índice del fallo cuando la expresión no sea válida
    print(f"{t!r:15} -> {describir_resultado(t)}")



# EJERCICIO: Transformar un entero decimal a binario mediante divisiones sucesivas entre 2 apoyándose en una pila, e incorporar la conversión inversa binario_a_decimal(s).

# 1. Análisis del problema
# Datos de entrada: Un entero decimal no negativo para pasar a base 2 y una cadena binaria (ej. "1101") para pasar a base 10.
# Procesamiento: Dividir iterativamente el decimal entre 2 apilando los residuos en una deque y desapilándolos para ensamblar el número binario; incorporar asimismo una función que traduzca una cadena binaria a su equivalente decimal.
# Resultado esperado: Representación en base 2 de los valores de prueba, contraste con bin() y conversión de cadenas binarias a base 10.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Codificar decimal_a_binario(n) contemplando el caso n == 0, apilando los restos n % 2 y desapilándolos al concluir
# Incorporar binario_a_decimal(s) iterando sobre los bits y sumando el peso posicional en base 2
# Validar decimal_a_binario con distintos valores contrastando contra bin()
# Ejecutar casos de prueba para binario_a_decimal verificando con int(s, 2)

# 3. Identificación de la lógica
# El método de divisiones sucesivas genera primero los bits menos significativos y la pila revierte su orden al extraerlos (LIFO).
# En binario_a_decimal, cada dígito binario multiplica una potencia creciente de 2 según su posición de derecha a izquierda.
# Contrastar los resultados contra las funciones nativas de Python garantiza la exactitud de ambos algoritmos.

# 4. Implementación en Python

def decimal_a_binario(n):
    if n == 0:
        return "0"

    pila = deque()
    while n > 0:
        residuo = n % 2
        pila.append(residuo)
        n = n // 2

    # Extraer elementos de la pila para construir la cadena binaria
    binario = ""
    while pila:
        binario += str(pila.pop())
    return binario


# Función complementaria para transformar una cadena binaria como "1101" en su equivalente decimal (13)
def binario_a_decimal(s):
    decimal = 0
    potencia = 1
    for bit in reversed(s):
        if bit == "1":
            decimal += potencia
        potencia *= 2
    return decimal


# --- Casos de prueba ---
for n in [0, 1, 5, 13, 100, 255]:
    print(f"{n:4d} -> {decimal_a_binario(n)}")

# Contraste con la función incorporada de Python
print(bin(13))          # 0b1101

# Casos de prueba para binario_a_decimal contrastados con int(..., 2)
for bin_str in ["0", "1", "101", "1101", "1100100", "11111111"]:
    print(f"{bin_str:>8s} -> {binario_a_decimal(bin_str)} (int: {int(bin_str, 2)})")



# EJERCICIO: Implementar un gestor de historial de acciones basado en pilas con opciones para registrar, deshacer, consultar y rehacer operaciones.

# 1. Análisis del problema
# Datos de entrada: Opción seleccionada del menú y descripción textual al registrar una nueva operación.
# Procesamiento: Emplear una pila (deque) para apilar cada operación ejecutada, extraer la más reciente al deshacer, desplegar el registro actual e incorporar la funcionalidad de rehacer la última acción revertida.
# Resultado esperado: Mensajes de confirmación al ejecutar, deshacer o rehacer tareas, visualización del historial y notificaciones cuando no existan operaciones pendientes.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Inicializar la pila historial mediante deque()
# Incorporar una pila auxiliar rehechos mediante deque() para almacenar acciones revertidas
# En un bucle while True, desplegar el menú con Ejecutar acción, Deshacer, Ver historial, Rehacer y Salir
# Apilar con append al registrar, extraer con pop al deshacer y listar desde el tope al consultar el historial
# Gestionar la opción Rehacer transfiriendo el elemento desde rehechos nuevamente hacia historial

# 3. Identificación de la lógica
# El registro de operaciones responde a la lógica LIFO: la acción más reciente es la primera en revertirse.
# Mantener una segunda pila para elementos deshechos habilita la función de rehacer preservando el comportamiento de pila.
# Vaciar la pila de rehechos al ejecutar una acción nueva evita incoherencias en la línea temporal del historial.

# 4. Implementación en Python

def mostrar_menu():
    print("\n--- HISTORIAL DE ACCIONES ---")
    print("1. Hacer acción")
    print("2. Deshacer")
    print("3. Ver historial")
    # Opción 4 añadida para restaurar la última operación revertida
    print("4. Rehacer")
    # Desplazar la salida a la opción 5 para dar cabida a la funcionalidad de rehacer
    print("5. Salir")


historial = deque()
# Pila auxiliar destinada a almacenar temporalmente las operaciones deshechas
rehechos = deque()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        accion = input("Escriba la acción: ").strip()
        if accion:
            historial.append(accion)
            # Vaciar la pila de rehechos al generarse una nueva secuencia de acciones
            rehechos.clear()
            print(f"Acción registrada: '{accion}'")
        else:
            print("La acción no puede estar vacía.")

    elif opcion == "2":
        if historial:
            ultima = historial.pop()
            # Almacenar la operación revertida para permitir su posterior restauración
            rehechos.append(ultima)
            print(f"Se deshizo la acción: '{ultima}'")
        else:
            print("No hay acciones para deshacer.")

    elif opcion == "3":
        if historial:
            print("\nHistorial (de la más reciente a la más antigua):")
            for idx, act in enumerate(reversed(historial), start=1):
                print(f"  {idx}. {act}")
        else:
            print("El historial está vacío.")

    # Bloque encargado de restaurar una operación previamente revertida
    elif opcion == "4":
        if rehechos:
            recuperada = rehechos.pop()
            historial.append(recuperada)
            print(f"Se rehízo la acción: '{recuperada}'")
        else:
            print("No hay acciones para rehacer.")

    # Salida controlada en la opción 5 y validación ante entradas no reconocidas
    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")



# EJERCICIO: Emplear una pila para revertir la SECUENCIA de palabras en una oración manteniendo intacta la ortografía de cada palabra, e incorporar métricas complementarias.

# 1. Análisis del problema
# Datos de entrada: Una oración o cadena textual compuesta por múltiples palabras separadas por espacios.
# Procesamiento: Fragmentar la oración en palabras, insertar cada una en una pila (deque) y desapilarlas para reconstruir el texto con el orden de palabras invertido, añadiendo una función auxiliar para contabilizar palabras y depurar espacios redundantes.
# Resultado esperado: La cadena inicial junto con su versión invertida por palabras y el conteo total en consola.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Codificar invertir_orden_palabras(frase) fragmentando los términos y empleando una pila LIFO
# Apilar cada término con append y desapilar con pop para ensamblar la oración resultante
# Depurar espacios extra usando split() sin argumentos para descartar cadenas vacías por espacios múltiples o extremos
# Validar la solución con distintas oraciones de prueba e imprimir los resultados

# 3. Identificación de la lógica
# Dado que una pila extrae primero el último elemento insertado (LIFO), apilar palabras enteras revierte su secuencia sin alterar sus letras.
# Invocar split() sin parámetros divide por espacios y filtra automáticamente espacios duplicados o en los bordes.
# Reconstruir mediante " ".join(...) genera una cadena limpia separada por un único espacio entre términos.

# 4. Implementación en Python

def invertir_orden_palabras(frase):
    pila = deque()
    # Emplear split() sin argumentos para tokenizar palabras descartando espacios vacíos adicionales
    palabras = frase.split()

    for palabra in palabras:
        pila.append(palabra)

    invertidas = []
    while pila:
        invertidas.append(pila.pop())

    return " ".join(invertidas)


# Función complementaria para calcular la cantidad total de palabras en la oración original
def contar_palabras(frase):
    return len(frase.split())


# --- Ejemplos de ejecución ---
frases = [
    "Hola Mundo",
    "Aprender Python es muy útil",
    "  una   dos   tres  "
]

for f in frases:
    resultado = invertir_orden_palabras(f)
    # Obtener el número de palabras como métrica informativa adicional para cada ejemplo
    total = contar_palabras(f)
    print(f"Original: {f!r} ({total} palabras) -> Invertida: {resultado!r}")

# EJERCICIO: Determinar si una palabra es un palíndromo (se lee igual en ambos sentidos) y extender la verificación a oraciones completas ignorando espacios.

# 1. Análisis del problema
# Datos de entrada: Una palabra o cadena textual (como "reconocer" o "ana").
# Procesamiento: Convertir el texto a minúsculas y cotejar los caracteres desde ambos extremos hacia el centro para comprobar si es palíndromo, añadiendo una función que elimine espacios para evaluar frases completas.
# Resultado esperado: Confirmación booleana de si cada palabra u oración es palíndromo impresa en consola.

# 2. Diseño en pseudocódigo
# Normalizar la palabra a minúsculas para evitar diferencias por capitalización
# Emplear dos punteros (izquierda y derecha) desplazándose hacia el centro mientras los caracteres coincidan
# Retornar False si algún par difiere; devolver True si ambos punteros logran cruzarse
# Incorporar es_frase_palindromo(texto) suprimiendo espacios antes de evaluar
# Ejecutar pruebas con términos como "reconocer", "ana" y oraciones palíndromas

# 3. Identificación de la lógica
# Cotejar caracteres desde los extremos hacia el interior permite descartar rápidamente cadenas no palíndromas ante la primera discrepancia.
# Convertir a minúsculas previene falsos negativos derivados de mayúsculas.
# Reutilizar la validación base sobre una cadena sin espacios amplía la solución a frases enteras.

# 4. Implementación en Python

def es_palindromo(palabra):
    limpia = palabra.lower()
    izquierda = 0
    derecha = len(limpia) - 1

    while izquierda < derecha:
        if limpia[izquierda] != limpia[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True


# Función complementaria para evaluar palíndromos en oraciones omitiendo los espacios en blanco
def es_frase_palindromo(frase):
    sin_espacios = "".join(frase.lower().split())
    return es_palindromo(sin_espacios)


# --- Ejemplos de ejecución ---
palabras = ["reconocer", "ana", "python", "radar", "oso"]

for p in palabras:
    print(f"{p:12s} -> es palíndromo: {es_palindromo(p)}")

# Caso de prueba para oración palíndroma empleando la función extendida
frase_prueba = "Anita lava la tina"
print(f"\nFrase: '{frase_prueba}' -> es palíndromo: {es_frase_palindromo(frase_prueba)}")



# EJERCICIO: Evaluar expresiones aritméticas en notación postfija (polaca inversa), como "3 4 + 5 *" = 35, mediante una pila e incorporando el operador potencia y validaciones.

# 1. Análisis del problema
# Datos de entrada: Una cadena con operandos y operadores delimitados por espacios en formato postfijo (ej. "3 4 + 5 *").
# Procesamiento: Iterar sobre cada token; apilar los valores numéricos en una deque y, ante un operador (+, -, *, /), desapilar los dos últimos operandos, ejecutar el cálculo en el orden adecuado y apilar el resultado, añadiendo soporte para potenciación (^) y control de errores.
# Resultado esperado: El valor numérico resultante de evaluar cada expresión postfija mostrado en pantalla.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Codificar evaluar_postfija(expresion) tokenizando por espacios y empleando una pila vacía
# Si el token es numérico, convertirlo a int o float e insertarlo en la pila
# Si es operador, extraer el segundo operando (b = pila.pop()) y el primero (a = pila.pop()), operar y apilar el resultado
# Incorporar el operador de potencia "^" junto con validaciones para entradas vacías o sintaxis incorrecta
# Al finalizar, el único elemento restante en la pila constituye el resultado final

# 3. Identificación de la lógica
# La notación postfija prescinde de paréntesis y reglas de precedencia, ya que cada operador actúa directamente sobre los dos valores previos en la pila.
# Respetar el orden de extracción resulta fundamental en operaciones no conmutativas (resta y división): el primer pop corresponde al operando derecho y el segundo al izquierdo.
# Apilar cada resultado parcial permite encadenar cálculos sucesivos de manera natural.

# 4. Implementación en Python

def evaluar_postfija(expresion):
    pila = deque()
    tokens = expresion.strip().split()

    if not tokens:
        raise ValueError("La expresión está vacía")

    for token in tokens:
        if token in {"+", "-", "*", "/", "^"}:
            if len(pila) < 2:
                raise ValueError(f"Operandos insuficientes para el operador '{token}'")

            # Extraer primero el operando derecho y posteriormente el izquierdo
            b = pila.pop()
            a = pila.pop()

            if token == "+":
                res = a + b
            elif token == "-":
                res = a - b
            elif token == "*":
                res = a * b
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero")
                res = a / b
            # Soporte adicional para el operador de potenciación "^" en la evaluación postfija
            elif token == "^":
                res = a ** b

            pila.append(res)
        else:
            try:
                numero = int(token)
            except ValueError:
                numero = float(token)
            pila.append(numero)

    # Comprobación final para verificar que quede exactamente un único resultado en la pila
    if len(pila) != 1:
        raise ValueError("Expresión postfija inválida: sobran o faltan operadores")

    return pila.pop()


# Función auxiliar para presentar el resultado como entero sin punto decimal cuando sea exacto
def formatear_resultado(valor):
    if isinstance(valor, float) and valor.is_integer():
        return int(valor)
    return valor


# --- Casos de prueba ---
expresiones = [
    "3 4 +",
    "3 4 + 5 *",
    "10 2 - 4 /",
    # Caso de prueba adicional empleando el operador de potenciación "^"
    "2 3 ^ 4 +"
]

for expr in expresiones:
    resultado = evaluar_postfija(expr)
    # Aplicar formatear_resultado para imprimir 35 en vez de 35.0 ante resultados enteros exactos
    print(f"{expr} = {formatear_resultado(resultado)}")
