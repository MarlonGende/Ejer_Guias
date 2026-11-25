# MATERIA: ESTRUCTURA DE DATOS
# ALUMNO: Marlon Elias Gende Cedeño
# PROFESOR: ING. DANIEL VERA

# TABLA DE CONTENIDOS:
# Líneas 8 a 258: COMPARATIVA JS VS PYTHON
# Líneas 268 a 574: VARIABLES Y OPERADORES
# Líneas 576 a 812: ESTRUCTURAS DE CONTROL
# Líneas 815 a 1605: FUNCIONES
# Líneas 1608 a 1904: COLECCIONES BÁSICAS
# Líneas 1906 a 2463: PROGRAMACIÓN ORIENTADA A OBJETOS

# EJERCICIO 1: Solicitar el nombre y la edad del usuario para mostrar un saludo personalizado.

# 1. Análisis del problema
# Datos de entrada: nombre (texto) y edad (entero)
# Procesamiento: Unir el nombre y la edad dentro de una cadena de texto
# Resultado esperado: Mostrar en consola "Hola {nombre}, tienes {edad} años"

# 2. Diseño en pseudocódigo
# nombre = input("Mensaje")
# edad = int(input("Mensaje"))
# print(f"Hola, {nombre}, tienes {edad} años")

# 3. Identificación de la lógica
# Solo se requiere imprimir en pantalla los datos capturados mediante print()

# 4. Implementación en Python
def saludar_edad():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    print(f"Hola {nombre}, tienes {edad} años")

# saludar_edad()

# 5. Validación y pruebas

# EJERCICIO 2: Capturar tres calificaciones, calcular su promedio e indicar si «Aprueba» (≥ 7) o «Reprueba».

# 1. Análisis del problema
# Datos de entrada: tres notas decimales (n1, n2, n3)
# Procesamiento: Obtener la media aritmética sumando las notas y dividiendo entre 3.
# Evaluar mediante condicionales (if/else) si alcanza la nota mínima aprobatoria.
# Resultado esperado: Imprimir el promedio calculado junto con el estado académico.

# 2. Diseño en pseudocódigo
# n1 = float(input("Mensaje"))
# n2 = float(input("Mensaje"))
# n3 = float(input("Mensaje"))
# promedio = (n1 + n2 + n3) / 3
# estado = ""
# si promedio >= 7 entonces estado = "Aprobado" sino estado = "Reprobado"
# imprimir("Tu promedio final es {promedio} y tu estado es {estado}")

# 3. Identificación de la lógica
# Se capturan tres valores numéricos, se promedian y se aplica una estructura condicional para asignar el estado.

# 4. Implementación en Python
def promedio_estado():
    n1 = float(input("Ingrese la nota #1: "))
    n2 = float(input("Ingrese la nota #2: "))
    n3 = float(input("Ingrese la nota #3: "))
    promedio = (n1 + n2 + n3) / 3
    estado = ""

    if promedio >= 7:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    print(f"Tu promedio final es {promedio:.2f}, y tu estado es {estado}")

# promedio_estado()

# 5. Validación y pruebas

# EJERCICIO 3: Calcular área y perímetro de un rectángulo (base y altura) y de un círculo (radio) usando math.pi.

# 1. Análisis del problema
# Al tratarse de dos figuras distintas, conviene separar la lógica en dos funciones independientes.
# Se requiere importar el módulo math para acceder a la constante pi.

# Función rectangulo():
# Datos de entrada: base y altura (decimales)
# Procesamiento: Calcular área (base * altura) y perímetro (2 * (base + altura)).
# Resultado esperado: Imprimir ambos valores calculados.

# Función circulo():
# Datos de entrada: radio (decimal)
# Procesamiento: Calcular área (π * r²) y perímetro (2 * π * r) utilizando math.pi.
# Resultado esperado: Imprimir el área y la circunferencia.

# 2. Diseño en pseudocódigo
# importar math
# definir rectangulo():
#     base = float(input("Mensaje"))
#     altura = float(input("Mensaje"))
#     area = base * altura
#     perimetro = 2 * (base + altura)
#     imprimir("El area es {area} y el perimetro es {perimetro}")

# definir circulo():
#     radio = float(input("Mensaje"))
#     area = math.pi * radio ** 2
#     perimetro = 2 * math.pi * radio
#     imprimir("El area es {area} y el perimetro es {perimetro}")

# 3. Identificación de la lógica
# En ambas funciones se piden dimensiones al usuario y se aplican las fórmulas geométricas correspondientes.

# 4. Implementación en Python
import math

def rectangulo():
    base = float(input("Ingrese la base de su rectangulo: "))
    altura = float(input("Ingrese la altura de su rectangulo: "))

    area = base * altura
    perimetro = 2 * (base + altura)

    print(f"Para un rectangulo de base: {base:.2f} y altura: {altura:.2f}; su area es: {area:.2f} y su perimetro es: {perimetro:.2f}")

# rectangulo()

def circulo():
    radio = float(input("Ingrese el radio del circulo: "))

    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio

    print(f"Para un circulo de radio: {radio:.2f}, su area es: {area:.2f} y su perimnetro es: {perimetro:.2f}")

# circulo()

# EJERCICIO 4: Convertir una temperatura ingresada en grados Celsius a Fahrenheit (F = C × 9/5 + 32).
# 1. Análisis del problema
# Datos de entrada: temperatura en Celsius (decimal)
# Procesamiento: Aplicar la fórmula de conversión a Fahrenheit.
# Resultado esperado: Mostrar la equivalencia en grados Fahrenheit.

# 2. Diseño en pseudocódigo
# Celsius = float(input("Mensaje"))
# Fahrenheit = Celsius × 9/5 + 32
# imprimir({Fahrenheit})

# 3. Identificación de la lógica
# Se aplica directamente la ecuación matemática de conversión térmica sobre el dato ingresado.

# 4. Implementación en Python
def convertir_grados_CF():
    celsius = float(input("Ingrese la temperatura en °Celsius: "))
    fahrenheit = celsius * 1.8 + 32

    print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")

# convertir_grados_CF()

# 5. Validación y pruebas

# EJERCICIO 5: Transformar una cantidad total de segundos al formato hh:mm:ss (ej. 3725 → 1:02:05).

# 1. Análisis del problema
# Datos de entrada: cantidad total de segundos (entero)
# Procesamiento: Emplear división entera (//) y módulo (%) para extraer horas, minutos y segundos.
# Formatear con {n:02d} para asegurar dos dígitos con cero a la izquierda.
# Resultado esperado: Imprimir el tiempo desglosado en formato reloj.

# 2. Diseño en pseudocódigo
# total_segundos = int(input("Mensaje"))
# horas = total_segundos // 3600
# resto = total_segundos % 3600
# minutos = resto // 60
# segundos = resto % 60
# imprimir("mensaje")

# 3. Identificación de la lógica
# Se divide el total entre 3600 para hallar las horas exactas.
# El residuo obtenido (% 3600) representa los segundos restantes.
# Ese residuo se divide entre 60 para sacar los minutos, y el nuevo residuo (% 60) son los segundos finales.

# 4. Implementación en Python
def trans_seg():
    total_segundos = int(input("Ingrese los segundos totales: "))
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60

    print(f"{total_segundos} equivale a: {horas}:{minutos:02d}:{segundos:02d}")

# trans_seg()

# 5. Validación y pruebas

# EJERCICIO 6: Intercambiar el valor de dos variables numéricas en una sola instrucción.

# 1. Análisis del problema
# Datos de entrada: dos números enteros
# Procesamiento: Asignación múltiple de Python (a, b = b, a)
# Resultado esperado: Mostrar ambas variables con sus valores invertidos.

# 2. Diseño en pseudocódigo
# a = int(input("Mensaje"))
# b = int(input("Mensaje"))
# a, b = b, a
# imprimir({a} {b})

# 3. Identificación de la lógica
# Se leen dos datos y se permutan simultáneamente aprovechando el desempaquetado de tuplas de Python.

# 4. Implementación en Python
def intercam_valores():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))

    a, b = b, a

    print(f"a: {a}, b: {b}")

# intercam_valores()

# 5. Validación y pruebas

# EJERCICIO 7: Calcular un descuento del 10% sobre un precio base, sumar el 15% de IVA y mostrar el desglose.

# 1. Análisis del problema
# Datos de entrada: precio base del artículo (decimal)
# Procesamiento: Restar el 10% de descuento y luego calcular el 15% de IVA sobre el monto rebajado.
# Resultado esperado: Imprimir el descuento aplicado, el impuesto y el total final.

# 2. Diseño en pseudocódigo
# precio = float(input("mensaje"))
# descuento = precio * 0.10
# precio_des = precio - descuento
# iva = precio_des * 0.15
# total = precio_des + iva
# imprimir resultados

# 3. Identificación de la lógica
# Se aplica primero la rebaja porcentual al precio original y sobre ese subtotal se grava el impuesto.

# 4. Implementación en Python
def iva_descuento():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = precio * 0.10
    precio_des = precio - descuento
    iva = precio_des * 0.15
    total = precio_des + iva

    print(f"Valor inicial: ${precio:.2f}")
    print(f"Descuento del 10% aplicado: ${descuento:.2f}, por lo que el nuevo valor seria ${precio_des:.2f}")
    print(f"IVA del 15% aplicado: ${iva:.2f} ")
    print(f"Total a pagar ${total:.2f}")

# iva_descuento()

# 5. Validación y pruebas

# EJERCICIO 8: Evaluar si un entero es par o impar, y verificar si es múltiplo de 3, de 5 o de ambos.

# 1. Análisis del problema
# Datos de entrada: número entero
# Procesamiento: Evaluar divisibilidad exacta mediante el operador residuo (%)
# Resultado esperado: Indicar paridad y divisibilidad entre 3 y 5.

# 2. Diseño en pseudocódigo
# numero = int(input("Mensaje"))
# si numero % 2 == 0: es par sino: es impar
# si numero % 3 == 0 y numero % 5 == 0: múltiplo de ambos
# sino si numero % 3 == 0: múltiplo de 3
# sino si numero % 5 == 0: múltiplo de 5
# sino: no es múltiplo de ninguno

# 3. Identificación de la lógica
# Se emplean estructuras condicionales comprobando que el residuo de la división sea igual a cero.

# 4. Implementación en Python
def par_impar_muti():
    numero = int(input("Ingrese un numero para saber si es par, impar, mutiplo de 3, de 5 o de ambos: "))

    if numero % 2 == 0:
        print("El numero es par.")
    else:
        print("El numerp es impar.")

    if numero % 3 == 0 and numero % 5 == 0:
        print("El mutiplo de 3 y de 5 a la vez.")
    elif numero % 3 == 0:
        print("Es multiplo de 3")
    elif numero % 5 == 0:
        print("Es mutiplo de 5")
    else:
        print("No es multiplo ni de 3 ni de 5. ")

# par_impar_muti()

# 5. Validación y pruebas

# EJERCICIO 9: Convertir una cadena de tiempo en formato hh:mm:ss a su equivalente total en segundos.

# 1. Análisis del problema
# Datos de entrada: texto con formato de hora (ej. 1:02:04)
# Procesamiento: Dividir la cadena usando split(":") para extraer horas, minutos y segundos por separado.
# Resultado esperado: Mostrar la suma total en segundos.

# 2. Diseño en pseudocódigo
# tiempo = input("Mensaje")
# horas, minutos, segundos = tiempo.split(":")
# total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)
# imprimir resultado

# 3. Identificación de la lógica
# Se captura la hora como una sola cadena, se fragmenta por los dos puntos con split() y cada parte se convierte a entero para multiplicarla por su factor en segundos.

# 4. Implementación en Python
def tiempot_seg():
    tiempo = input("Ingrese la hora (hh:mm:ss): ")
    horas, minutos, segundos = tiempo.split(":")
    total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)

    print(f"Total de segundos: {total_segundos}")

# tiempot_seg()

# 5. Validación y pruebas

# EJERCICIO 10: Desglosar un monto en la menor cantidad de billetes ($50, $20, $10, $5, $1) y luego en monedas ($0.25, $0.10, $0.05, $0.01).

# 1. Análisis del problema
# Datos de entrada: monto numérico
# Procesamiento: Aplicar divisiones enteras (//) y residuos (%) sucesivos de mayor a menor denominación.
# Resultado esperado: Cantidad exacta de billetes o monedas necesarios de cada valor.

# 2. Diseño en pseudocódigo
# monto = int(input("Mensaje"))
# b50 = monto // 50; monto = monto % 50
# b20 = monto // 20; monto = monto % 20
# b10 = monto // 10; monto = monto % 10
# b5 = monto // 5; monto = monto % 5
# b1 = monto // 1

# 3. Identificación de la lógica
# Se asigna la máxima cantidad posible de la denominación más alta y se actualiza el monto con el sobrante para el siguiente nivel.

# 4. Implementación en Python
def billetes():
    monto = int(input("Ingrese el monto total: "))

    b50 = monto // 50
    monto = monto % 50

    b20 = monto // 20
    monto = monto % 20

    b10 = monto // 10
    monto = monto % 10

    b5 = monto // 5
    monto = monto % 5

    b1 = monto // 1

    print(f"$50 × {b50}")
    print(f"$20 × {b20}")
    print(f"$10 × {b10}")
    print(f"$5  × {b5}")
    print(f"$1  × {b1}")

# billetes()

# 5. Validación y pruebas

# Para monedas se aplica el mismo principio, convirtiendo primero el monto a centavos enteros con round(monto * 100) para evitar errores de punto flotante.
# Implementación en Python:

def monedas():
    monto = float(input("Ingrese el monto total en dolares: "))
    centavos = round(monto * 100)

    m25 = centavos // 25
    centavos = centavos % 25

    m10 = centavos // 10
    centavos = centavos % 10

    m5 = centavos // 5
    centavos = centavos % 5

    m1 = centavos

    print("\nCantidad de monedas:")
    print(f"25¢: {m25}")
    print(f"10¢: {m10}")
    print(f"5¢ : {m5}")
    print(f"1¢ : {m1}")

# monedas()
# Validación y pruebas

# EJERCICIO 11: Calcular la suma de los dígitos de un número entero de tres cifras (ej. 435 → 12).
# 1. Análisis del problema
# Se emplea la misma técnica de división entera y módulo para descomponer el número en centenas, decenas y unidades, y luego sumarlas.

# 2. Diseño en pseudocódigo
# Descomponer el número usando // 100, // 10 y % 10, y sumar los tres dígitos extraídos.

# 3. Identificación de la lógica
# Aislamiento posicional de cada cifra mediante aritmética entera y acumulación en una variable suma.

# 4. Implementación en Python
def suma_digitos():
    numero = int(input("Ingrese un numero de 3 cifras: "))

    centenas = numero // 100
    numero = numero % 100

    decenas = numero // 10
    numero = numero % 10

    unidades = numero

    suma = centenas + decenas + unidades

    print(f"Suma: {suma}")

# suma_digitos()

# 5. Validación y pruebas

# EJERCICIO 12: Convertir un total de minutos al formato «X horas Y minutos» (ej. 135 → «2 horas 15 minutos»).
# 1. Análisis del problema
# Se aplica el mismo patrón de división entera y residuo tomando 60 como base.

# 2. Diseño en pseudocódigo
# Dividir entre 60 para obtener horas y calcular el módulo 60 para los minutos sobrantes.

# 3. Identificación de la lógica
# Conversión de unidades de tiempo usando // 60 y % 60.

# 4. Implementación en Python
def minutos_horasm():
    minutos_totales = int(input("Ingrese el tiempo total en minutos: "))

    horas = minutos_totales // 60
    minutos = minutos_totales % 60

    print(f"{horas} horas {minutos} minutos")

# minutos_horasm()

# 5. Validación y pruebas

# EJERCICIO 13: Calcular el Índice de Masa Corporal (IMC = peso / estatura²) con dos decimales.

# 1. Análisis del problema
# Datos de entrada: peso en kilogramos y estatura en metros (decimales)
# Procesamiento: Dividir el peso entre el cuadrado de la estatura.
# Resultado esperado: Mostrar el IMC formateado a dos decimales.

# 2. Diseño en pseudocódigo
# peso = float()
# estatura = float()
# imc = peso / estatura ** 2
# imprimir({imc})

# 3. Identificación de la lógica
# Captura de dos datos flotantes y evaluación directa de la fórmula antropométrica.

# 4. Implementación en Python
def imc():
    peso = float(input("Ingrese su peso (kg): "))
    estatura = float(input("Ingrese su estatura (m): "))

    imc_v = peso / (estatura ** 2)

    print(f"Su Indice de Masa Corporal es: {imc_v:.2f}")

# imc()
# 5. Validación y pruebas

# EJERCICIO 14: Redondear un número decimal a la cantidad de cifras decimales indicada por el usuario.
# 1. Análisis del problema
# Datos de entrada: número flotante y cantidad de decimales deseada (entero)
# Procesamiento: Aplicar la función nativa round(decimal, redondeo)
# Resultado esperado: Imprimir el valor ya redondeado.

# 2. Diseño en pseudocódigo
# decimal = float(), redondeo = int()
# resultado = round(decimal, redondeo)
# imprimir({resultado})

# 3. Identificación de la lógica
# Uso directo de la función incorporada round() pasando el número y la precisión requerida.

# 4. Implementación en Python
def decimal_redondeo():
    decimal = float(input("Ingrese el numero decimal: "))
    redondeo = int(input("¿A cuantas cifras desea redondearlo?: "))

    resultado = round(decimal, redondeo)

    print(resultado)

# redondeo()

# 5. Validación y pruebas

# EJERCICIO 15: Calcular el total a pagar por un producto de $12 aplicando 15% de descuento si se llevan 10 o más, y 5% si se llevan entre 5 y 9.

# 1. Análisis del problema
# Datos de entrada: cantidad de unidades compradas (entero), dado un precio fijo de $12.
# Procesamiento: Evaluar tramos de cantidad mediante condicionales (if/elif/else) para determinar el porcentaje de rebaja.
# Resultado esperado: Desglose de compra y monto final a pagar.

# 2. Diseño en pseudocódigo
# Datos de entrada:
# cantidad = int(input("Mensaje"))
#
# Procesamiento:
# Si cantidad >= 10 -> descuento = 15%
# Si cantidad >= 5 -> descuento = 5%
# Caso contrario -> descuento = 0%
# Calcular subtotal, descuento y total neto
# Salida: Imprimir el resumen de la compra

# 3. Identificación de la lógica
# Estructura condicional escalonada para asignar tasas de descuento según el volumen de compra.

# 4. Implementación en Python
def descuento():
    PRECIO = 12
    cantidad = int(input("Cantidad: "))

    if cantidad >= 10:
        descuento = 0.15
    elif cantidad >= 5:
        descuento = 0.05
    else:
        descuento = 0

    precio_inicial = PRECIO * cantidad
    valor_descueto = precio_inicial * descuento
    total = precio_inicial - valor_descueto

    print(f"Precio unitario: {PRECIO}")
    print(f"Cantidad a comprar: {cantidad}")
    print(f"Total inicial a pagar: {precio_inicial:.2f}")
    print(f"Descuento aplicado en %: {int(descuento * 100)}%")
    print(f"Descuento aplicado en $: {valor_descueto:.2f}")
    print(f"Total final a pagar: {total:.2f}")

# descuento()
# 5. Validación y pruebas

# EJERCICIO 16: Imprimir la secuencia numérica desde 1 hasta N.
# 1. Análisis del problema
# Datos de entrada: límite superior N (entero)
# Procesamiento: Iterar desde 1 hasta N usando un bucle for.
# Resultado esperado: Mostrar cada número en consola dentro del ciclo.

# 2. Diseño en pseudocódigo
# Se emplea un ciclo for con range(1, n + 1) para automatizar la impresión secuencial sin escribir múltiples print() manuales.

# 3. Identificación de la lógica
# Iteración controlada por contador mediante range(1, n + 1).

# 4. Implementación en Python
def primerfor(n):
    for i in range(1, n + 1):
        print(i)
# primerfor(10)

# Variante descendente (de N hasta 1) utilizando paso negativo: range(n, 0, -1)
def primerfor_reves(n):
    for i in range(n, 0, -1):
        print(i)
# primerfor_reves(10)

# 5. Validación y pruebas

# EJERCICIO 17: Obtener la sumatoria de los enteros consecutivos desde 1 hasta N.
# 1. Análisis del problema
# Datos de entrada: número límite N
# Procesamiento: Acumular cada valor de la secuencia en una variable mediante un ciclo for.
# Resultado esperado: Retornar e imprimir la suma total fuera del bucle.

# 2. Diseño en pseudocódigo
# Leer N
# suma = 0
# Para cada número desde 1 hasta N:
#     suma = suma + número
# Retornar suma

# 3. Identificación de la lógica
# Patrón de acumulador dentro de un bucle for con range(1, n + 1).

# 4. Implementación en Python
def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
# print(suma_numeros(10))

# Variante para sumar únicamente los números pares entre 2 y 100 usando paso de 2 en range().
def suma_pares(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma
# print(suma_pares(100))

# 5. Validación y pruebas

# EJERCICIO 18: Calcular el factorial de un número N (N! = 1 × 2 × ... × N).
# 1. Análisis del problema
# Datos de entrada: entero N
# Procesamiento: Multiplicar sucesivamente los enteros desde 1 hasta N en un acumulador iniciado en 1.
# Resultado esperado: Retornar el producto factorial resultante.

# 2. Diseño en pseudocódigo
# Leer N
# factorial = 1
# Para cada número desde 1 hasta N:
#     factorial = factorial * número
# Retornar factorial

# 3. Identificación de la lógica
# Acumulador multiplicativo dentro de un ciclo for con range(1, n + 1).

# 4. Implementación en Python
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
# print(factorial(5))

# Prueba con valores grandes (100!): Python soporta enteros de precisión arbitraria sin desbordamiento, a diferencia de los enteros estándar en JS.
# print(factorial(100))

# 5. Validación y pruebas

# EJERCICIO 19: Registrar las notas de N alumnos y contabilizar cuántos obtuvieron nota aprobatoria (≥ 70).
# 1. Análisis del problema
# Datos de entrada: cantidad N de estudiantes y cada una de sus calificaciones.
# Procesamiento: Iterar N veces, evaluando cada nota con un condicional e incrementando un contador si es ≥ 70.
# Resultado esperado: Número total de aprobados.

# 2. Diseño en pseudocódigo
# Leer N
# contador_aprobados = 0
# Repetir N veces:
#     Leer nota
#     Si nota >= 70 entonces contador_aprobados += 1
# Retornar contador_aprobados

# 3. Identificación de la lógica
# Uso de un contador condicional dentro de un ciclo definido por N iteraciones.

# 4. Implementación en Python
def contar_aprobados(n):
    contador_aprobados = 0
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota >= 70:
            contador_aprobados += 1
    return contador_aprobados
# print(f"Cantidad de estudiantes aprobados: {contar_aprobados(5)}")

# Ampliación: incluir conteo de reprobados y calcular los porcentajes de ambos grupos.

def contar_aprobados_reprobados(n):
    contador_aprobados = 0
    contador_reprobados = 0
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota >= 70:
            contador_aprobados += 1
        else:
            contador_reprobados += 1
    porcentaje_aprobados = (contador_aprobados / n) * 100
    porcentaje_reprobados = (contador_reprobados / n) * 100
    return contador_aprobados, contador_reprobados, porcentaje_aprobados, porcentaje_reprobados
# resultado = contar_aprobados_reprobados(5)

# print(f"Cantidad de estudiantes aprobados: {resultado[0]}")
# print(f"Cantidad de estudiantes reprobados: {resultado[1]}")
# print(f"Porcentaje de estudiantes aprobados: {resultado[2]}%")
# print(f"Porcentaje de estudiantes reprobados: {resultado[3]}%")

# 5. Validación y pruebas

# EJERCICIO 20: Leer N calificaciones y determinar cuál es la más alta.
# 1. Análisis del problema
# Datos de entrada: cantidad N de alumnos y sus respectivas notas.
# Procesamiento: Comparar cada nota ingresada contra una variable auxiliar iniciada en menos infinito (-inf).
# Resultado esperado: Retornar la calificación máxima registrada.

# 2. Diseño en pseudocódigo
# Leer N, inicializar nota_maxima = -infinito, iterar N veces actualizando el máximo si la nota actual lo supera.

# 4. Implementación en Python
def nota_mas_alta(n):
    nota_maxima = float('-inf')
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota > nota_maxima:
            nota_maxima = nota
    return nota_maxima

# Variante para hallar la calificación mínima inicializando en infinito positivo ('inf') e invirtiendo la comparación.
def nota_mas_baja(n):
    nota_minima = float('inf')
    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota < nota_minima:
            nota_minima = nota
    return nota_minima

# 5. Validación y pruebas

# EJERCICIO 21: Comprobar si un número es primo utilizando una variable bandera (flag) y break.
# 1. Análisis del problema
# Datos de entrada: número entero N
# Procesamiento: Buscar divisores exactos en el rango de 2 hasta N-1 mediante un ciclo for.
# Resultado esperado: Indicar si el número es primo o compuesto.

# 2. Diseño en pseudocódigo
# Leer N
# bandera = False
# Para i desde 2 hasta N - 1:
#     Si N % i == 0:
#         bandera = True
#         romper ciclo (break)
# Si no bandera: es primo, sino: no es primo

# 3. Identificación de la lógica
# Si se detecta al menos un divisor exacto, se activa la bandera y se interrumpe la búsqueda inmediatamente con break.

# 4. Implementación en Python
def es_primo(n):
    if n <= 1:
        return False
    divisor_extra = False
    for i in range(2, n):
        if n % i == 0:
            divisor_extra = True
            break
    return not divisor_extra

# Ejemplo de comprensión de listas para filtrar los números primos entre 2 y 100:
# primos = [i for i in range(2, 101) if es_primo(i)]
# print("Números primos entre 2 y 100:", primos)

# 5. Validación y pruebas

# EJERCICIO 22: Imprimir la tabla de multiplicar de un número N desde el 1 hasta el 12.

# 1. Análisis del problema
# Datos de entrada: número entero N.
# Procesamiento: Iterar del 1 al 12 multiplicando N por cada índice del ciclo.
# Resultado esperado: Desplegar en pantalla cada línea de la tabla.

# 2. Diseño en pseudocódigo
# Leer N
# Para i desde 1 hasta 12:
#     Calcular producto = N * i
#     Mostrar "N × i = producto"

# 3. Identificación de la lógica
# Bucle for sobre range(1, 13) que imprime el producto formateado en cada iteración.

# 4. Implementación en Python
def tabla_multiplicar(n):
    for i in range(1, 13):
        print(f"{n} × {i} = {n * i}")

# tabla_multiplicar(9)

# 5. Validación y pruebas

# EJERCICIO 23: Contar la cantidad de dígitos de un número entero sin transformarlo a cadena de texto.

# 1. Análisis del problema
# Datos de entrada: número entero (positivo, negativo o cero).
# Procesamiento: Tomar el valor absoluto y dividir sucesivamente entre 10 (división entera) hasta llegar a cero, contando los pasos.
# Resultado esperado: Cantidad total de cifras del número.

# 2. Diseño en pseudocódigo
# Leer número y obtener su valor absoluto
# Si es igual a 0 -> dígitos = 1
# Caso contrario:
#     Mientras número != 0:
#         Incrementar contador
#         número = número // 10
# Retornar contador

# 3. Identificación de la lógica
# Cada división entera entre 10 descarta el dígito de las unidades; el bucle while cuenta cuántas veces es posible hacerlo.

# 4. Implementación en Python
def digitos(num):
    n = abs(num)
    contador = 0

    if n == 0:
        contador = 1
    else:
        while n != 0:
            contador += 1
            n = n // 10

    return contador

# print(digitos(108972))

# 5. Validación y pruebas

# EJERCICIO 24: Capturar N números enteros y calcular por separado la suma de los pares y la de los impares.

# 1. Análisis del problema
# Datos de entrada: cantidad N de valores y cada uno de los números enteros.
# Procesamiento: Evaluar cada entrada con módulo 2 y sumarla al acumulador correspondiente.
# Resultado esperado: Total acumulado de pares y total acumulado de impares.

# 2. Diseño en pseudocódigo
# Leer N
# suma_pares = 0, suma_impares = 0
# Para i desde 1 hasta N:
#     Leer número
#     Si número % 2 == 0 -> sumar a suma_pares
#     Sino -> sumar a suma_impares
# Retornar ambos acumuladores

# 3. Identificación de la lógica
# Clasificación de paridad mediante (%) dentro de un bucle for con dos acumuladores independientes.

# 4. Implementación en Python
def suma_pares_impares(n):
    suma_pares = 0
    suma_impares = 0

    for i in range(1, n + 1):
        numero = int(input(f"Ingrese el valor #{i}: "))

        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero

    return suma_pares, suma_impares

# resultado = suma_pares_impares(4)

# print(f"La suma de los pares es: {resultado[0]}")
# print(f"La suma de los impares es: {resultado[1]}")

# 5. Validación y pruebas

# EJERCICIO 25: Solicitar una edad y repetir la petición hasta que se ingrese un valor válido entre 0 y 120.

# 1. Análisis del problema
# Datos de entrada: edad entera.
# Procesamiento: Validar el rango [0, 120] mediante una función booleana dentro de un bucle infinito while True.
# Resultado esperado: Confirmar e imprimir la edad una vez que sea válida.

# 2. Diseño en pseudocódigo
# Definir validar_edad(edad): retornar 0 <= edad <= 120
# Bucle infinito:
#     Pedir edad
#     Si validar_edad(edad) es True -> salir con break
#     Sino -> mostrar aviso de error
# Imprimir edad válida

# 3. Identificación de la lógica
# Bucle de validación de entrada controlado por una función predicado y salida mediante break.

# 4. Implementación en Python
def validar_edad(edad):
    return 0 <= edad <= 120

def principal():
    while True:
        edad = int(input("Edad (0-120): "))

        if validar_edad(edad):
            break

        print("Inválida, intenta de nuevo")

    print(f"Edad válida: {edad}")

# principal()

# 5. Validación y pruebas

# EJERCICIO 26: Implementar un juego para adivinar un número secreto generado al azar entre 1 y 100.

# 1. Análisis del problema
# Datos de entrada: números enteros propuestos por el usuario.
# Procesamiento: Comparar cada intento con el número aleatorio e indicar si el objetivo es mayor o menor, llevando la cuenta de intentos.
# Resultado esperado: Felicitar al jugador al acertar e informar el número de intentos empleados.

# 2. Diseño en pseudocódigo
# Generar número secreto aleatorio
# intentos = 0
# Repetir indefinidamente:
#     Leer intento e incrementar contador
#     Si intento == secreto -> felicitar y salir (break)
#     Si intento < secreto -> indicar "Es mayor"
#     Sino -> indicar "Es menor"

# 3. Identificación de la lógica
# Bucle while True con retroalimentación condicional (búsqueda guiada) hasta lograr la coincidencia exacta.

# 4. Implementación en Python
import random

def adivinar_numero(secreto):

    intentos = 0

    while True:
        intento = int(input("Adivina el numero del 1 al 100: "))
        intentos += 1

        if intento == secreto:
            print(f"Felicidades lo adivinaste en {intentos} intentos")
            break

        elif intento < secreto:
            print("Es mayor")

        else:
            print("Es menor")

numero = random.randint(1, 100)

# adivinar_numero(numero)

# 5. Validación y pruebas

# EJERCICIO 27: Generar e imprimir los primeros N términos de la sucesión de Fibonacci.

# 1. Análisis del problema
# Datos de entrada: cantidad N de términos deseados.
# Procesamiento: Partir de (0, 1) e ir desplazando los valores mediante suma simultánea en un bucle for.
# Resultado esperado: Secuencia de los N primeros números de Fibonacci en una misma línea.

# 2. Diseño en pseudocódigo
# Leer N
# a = 0, b = 1
# Repetir N veces:
#     Imprimir a
#     a, b = b, a + b

# 3. Identificación de la lógica
# Actualización simultánea de dos variables de estado para avanzar en la serie sin variables temporales adicionales.

# 4. Implementación en Python
def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):

        print(a, end=" ")

        a, b = b, a + b

    print()

fibonacci(10)

# 5. Validación y pruebas

# EJERCICIO: Modularizar el cálculo de IVA (15%) y total a pagar creando dos funciones que colaboren entre sí.

# 1. Análisis del problema
# Datos de entrada: precio base (decimal).
# Procesamiento: Una función calcula el 15% de impuesto y la segunda invoca a la primera para sumarlo al precio original.
# Resultado esperado: Mostrar el valor del IVA y el monto total.

# 2. Diseño en pseudocódigo
# Definir calcular_iva(precio): retornar precio * 0.15
# Definir calcular_total(precio): retornar precio + calcular_iva(precio)
# Leer precio e imprimir ambos resultados

# 3. Identificación de la lógica
# Composición de funciones: descomposición de tareas y reutilización de código invocando una función dentro de otra.

# 4. Implementación en Python
def calcular_iva(precio):

    iva = precio * 0.15

    return iva


def calcular_total(precio):

    total = precio + calcular_iva(precio)

    return total


# precio = float(input("Ingrese el precio: "))

# print(f"IVA: ${calcular_iva(precio):.2f}")
# print(f"Total: ${calcular_total(precio):.2f}")

# 5. Validación y pruebas

# EJERCICIO 29: Reutilizar una función booleana es_primo() para contabilizar cuántos números primos existen en un rango [a, b].

# 1. Análisis del problema
# Datos de entrada: límites inferior (a) y superior (b) del intervalo.
# Procesamiento: Recorrer el rango [a, b] y sumar 1 por cada número que devuelva True al pasar por es_primo().
# Resultado esperado: Total de números primos encontrados en el intervalo.

# 2. Diseño en pseudocódigo
# Definir contar_primos(a, b):
#     contador = 0
#     Para i desde a hasta b:
#         Si es_primo(i) es True -> contador += 1
#     Retornar contador

# 3. Identificación de la lógica
# Invocación de una función auxiliar de validación dentro de un ciclo de conteo sobre un rango dado.

# 4. Implementación en Python
# Se reutiliza directamente la función es_primo() definida previamente en el Ejercicio 21
def contar_primos(a, b):

    contador = 0

    for i in range(a, b + 1):

        if es_primo(i):
            contador += 1

    return contador


print(contar_primos(1, 20))

# 5. Validación y pruebas

# EJERCICIO 30: Determinar si un número es narcisista (igual a la suma de sus dígitos elevados a la cantidad total de cifras, ej. 153).
# 1. Análisis del problema
# Datos de entrada: número entero.
# Procesamiento: Obtener el total de cifras con digitos(), extraer cada dígito mediante % 10 y // 10, elevarlo a esa potencia y acumularlo.
# Resultado esperado: True si la suma coincide con el valor absoluto original, False en caso contrario.

# 2. Diseño en pseudocódigo
# Obtener cantidad de cifras usando digitos(n)
# Mientras el número sea distinto de 0:
#     Extraer último dígito (% 10)
#     Sumar dígito ** cantidad
#     Reducir número (// 10)
# Comparar suma == abs(n)

# 3. Traza de ejecución manual
# Ejemplo con n = 153 (3 dígitos):
# Paso 1: dígito = 3 -> suma = 27 -> resto = 15
# Paso 2: dígito = 5 -> suma = 27 + 125 = 152 -> resto = 1
# Paso 3: dígito = 1 -> suma = 152 + 1 = 153 -> resto = 0
# Resultado: 153 == 153 -> True

# 4. Implementación en Python
# Se invoca la función digitos() implementada en el Ejercicio 23

def es_narcisista(n):

    cantidad = digitos(n)
    numero = abs(n)
    suma = 0

    while numero != 0:

        digito = numero % 10
        suma += digito ** cantidad
        numero = numero // 10

    return suma == abs(n)


print(es_narcisista(153))

# 5. Validación y pruebas

# EJERCICIO 31: Implementar un menú interactivo modularizado en funciones separadas para saludar, despedir y realizar operaciones aritméticas básicas.

# 1. Análisis del problema
# Datos de entrada: opción seleccionada del menú y, para la opción de cálculo, dos operandos numéricos.
# Procesamiento: Encapsular cada acción en su propia función (saludar, despedir, calcular, mostrar_menu) y gestionar el flujo mediante un bucle while True.
# Resultado esperado: Ejecución de la acción elegida hasta que el usuario opte por salir.

# 2. Diseño en pseudocódigo
# Definir funciones saludar(), despedir(), calcular() (validando división por cero) y mostrar_menu()
# En un ciclo infinito:
#     Mostrar menú y leer opción
#     Ejecutar la función asociada o romper el ciclo si elige salir

# 3. Identificación de la lógica
# Arquitectura modular donde el bucle principal actúa únicamente como despachador de opciones.

# 4. Implementación en Python
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def calcular():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")

    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("No se puede dividir para cero.")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Calcular")
    print("4. Salir")

while True:
    mostrar_menu()

    opcion = input("Opción: ")

    if opcion == "1":
        saludar()

    elif opcion == "2":
        despedir()

    elif opcion == "3":
        calcular()

    elif opcion == "4":
        print("Adiós")
        break

    else:
        print("Opción inválida")

# 5. Validación y pruebas

# EJERCICIO 32: Crear la función area_rectangulo(base, altura) que devuelva el área calculada.

# 1. Análisis del problema
# Datos de entrada: base y altura (decimales).
# Procesamiento: Multiplicar ambos parámetros dentro de la función y retornar el producto.
# Resultado esperado: Mostrar el área devuelta por la función.

# 2. Diseño en pseudocódigo
# Definir area_rectangulo(base, altura): retornar base * altura
# Capturar base y altura, invocar la función e imprimir el retorno

# 3. Identificación de la lógica
# Separación entre entrada/salida de datos y lógica de cálculo mediante paso de parámetros y retorno de valor.

# 4. Implementación en Python
def area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

resultado = area_rectangulo(base, altura)

print(f"El área del rectángulo es: {resultado}")

def area_rectangulo_validacion(base, altura):

    if base <= 0 or altura <= 0:
        return None

    return base * altura


base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

resultado = area_rectangulo_validacion(base, altura)

if resultado is None:
    print("La base y la altura deben ser mayores que cero.")
else:
    print(f"El área del rectángulo es: {resultado}")

print(f"El área del rectángulo es: {resultado}")

# 5. Validación y pruebas

# EJERCICIO 33: Implementar la función maximo(a, b, c) para hallar el mayor de tres valores numéricos.

# 1. Análisis del problema
# Datos de entrada: tres números reales.
# Procesamiento: Comparar los tres parámetros mediante condicionales encadenados para identificar el mayor.
# Resultado esperado: Retornar e imprimir el valor máximo.

# 2. Diseño en pseudocódigo
# Definir maximo(a, b, c):
#     Si a >= b y a >= c -> retornar a
#     Sino si b >= a y b >= c -> retornar b
#     Sino -> retornar c

# 3. Identificación de la lógica
# Evaluación relacional múltiple dentro de una función pura que devuelve el mayor argumento.

# 4. Implementación en Python
def maximo(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = maximo(num1, num2, num3)

print(f"El número mayor es: {resultado}")

def maximo_iguales(a, b, c):

    if a == b == c:
        return "Los tres números son iguales"

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c

# 5. Validación y pruebas

# EJERCICIO 34: Crear la función es_bisiesto(anio) que evalúe si un año calendario es bisiesto.

# 1. Análisis del problema
# Datos de entrada: año (entero).
# Procesamiento: Comprobar divisibilidad entre 4 (excluyendo múltiplos de 100) o divisibilidad entre 400.
# Resultado esperado: Valor booleano (True o False).

# 2. Diseño en pseudocódigo
# Definir es_bisiesto(anio):
#     Retornar (anio % 4 == 0 y anio % 100 != 0) o (anio % 400 == 0)

# 3. Identificación de la lógica
# Expresión booleana compuesta con operadores lógicos and y or para validar las reglas del calendario gregoriano.

# 4. Implementación en Python
def es_bisiesto(anio):

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True

    return False


anio = int(input("Ingrese un año: "))

print(es_bisiesto(anio))

def bisiesto(anio):

    if anio <= 0:
        return None

    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


anio = int(input("Ingrese un año: "))

resultado = bisiesto(anio)

if resultado is None:
    print("Ingrese un año válido.")
else:
    print(resultado)
# 5. Validación y pruebas

# EJERCICIO 35: Calcular el coeficiente binomial combinatoria(n, k) = n! / (k! · (n-k)!) reutilizando factorial(n).

# 1. Análisis del problema
# Datos de entrada: enteros n y k.
# Procesamiento: Definir factorial(n) e invocarla tres veces dentro de combinatoria(n, k), validando previamente que 0 <= k <= n.
# Resultado esperado: Número de combinaciones posibles.

# 2. Diseño en pseudocódigo
# Definir factorial(n) mediante bucle multiplicativo
# Definir combinatoria(n, k):
#     Validar rango de k
#     Calcular factorial(n) / (factorial(k) * factorial(n - k))

# 3. Identificación de la lógica
# Reutilización modular: una función matemática básica sirve como bloque de construcción para una fórmula más compleja.

# 4. Implementación en Python
def factorial(n):

    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def combinatoria(n, k):

    # MEJORA: Se comprueba que k esté dentro del rango válido [0, n].
    # Si no se cumple, la operación no está definida y devuelve None.

    if k < 0 or k > n:
        return None

    return factorial(n) / (factorial(k) * factorial(n - k))


n = int(input("Ingrese n: "))
k = int(input("Ingrese k: "))

resultado = combinatoria(n, k)

if resultado is None:
    print("Valores inválidos. Debe cumplirse 0 ≤ k ≤ n.")
else:
    print(f"La combinatoria es: {resultado}")

# 5. Validación y pruebas

# EJERCICIO 36: Calculadora interactiva con funciones independientes para sumar, restar, multiplicar y dividir.

# 1. Análisis del problema
# Datos de entrada: opción del menú y dos números reales.
# Procesamiento: Delegar cada operación aritmética a su respectiva función con retorno de resultado.
# Resultado esperado: Imprimir el resultado de la operación elegida hasta seleccionar salir.

# 2. Diseño en pseudocódigo
# Definir sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b) y mostrar_menu()
# En un ciclo while True: leer opción, solicitar operandos si aplica, invocar función y mostrar salida.

# 3. Identificación de la lógica
# Desacoplamiento de operaciones matemáticas en funciones puras coordinadas por un menú iterativo.

# 4. Implementación en Python
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):

    # MEJORA: Se previene el error de división entre cero retornando None.

    if b == 0:
        return None

    return a / b


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Programa finalizado.")
        break

    if opcion in ("1", "2", "3", "4"):

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")

        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")

        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")

        elif opcion == "4":

            resultado = dividir(num1, num2)

            if resultado is None:
                print("No es posible dividir para cero.")
            else:
                print(f"Resultado: {resultado}")

    else:
        print("Opción inválida.")

# 5. Validación y pruebas

# EJERCICIO 37: Contabilizar el total de vocales en una cadena ingresada sin distinguir mayúsculas o minúsculas.

# 1. Análisis del problema
# Datos de entrada: cadena de texto.
# Procesamiento: Normalizar la frase con .lower() e iterar carácter por carácter verificando pertenencia al conjunto de vocales.
# MEJORA: Se incluyen también las vocales acentuadas (á, é, í, ó, ú).
# Resultado esperado: Total de vocales encontradas.

# 2. Diseño en pseudocódigo
# Leer frase, convertir a minúsculas, recorrer caracteres e incrementar contador si pertenece a "aeiouáéíóú".

# 3. Identificación de la lógica
# Iteración directa sobre un objeto iterable (str) con verificación de pertenencia mediante el operador in.

# 4. Implementación en Python
def contar_vocales(frase):

    contador = 0

    for letra in frase.lower():

        if letra in "aeiouáéíóú":
            contador += 1

    return contador


frase = input("Ingrese una frase: ")

print(f"La frase tiene {contar_vocales(frase)} vocales.")

def contar_vocales_bandera(frase):

    contador = 0

    for letra in frase.lower():

        es_vocal = False

        if letra in "aeiou":
            es_vocal = True

        if es_vocal:
            contador += 1

    return contador


frase = input("Ingrese una frase: ")

print(f"La frase tiene {contar_vocales(frase)} vocales.")

# 5. Validación y pruebas

# EJERCICIO 38: Obtener promedio, calificación máxima y mínima de la lista [7, 8.5, 6, 9, 10, 5.5] con dos decimales.

# 1. Análisis del problema
# Datos de entrada: lista predefinida de calificaciones.
# Procesamiento: Calcular media aritmética y extremos (máximo y mínimo).
# MEJORA: Encapsular el procesamiento en una función que devuelva los tres indicadores como tupla.
# Resultado esperado: Imprimir los tres estadísticos formateados a dos decimales.

# 2. Diseño en pseudocódigo
# Definir analizar_notas(notas): calcular suma/longitud, máximo y mínimo, y retornarlos.

# 3. Identificación de la lógica
# Uso de funciones incorporadas de agregación (sum, len, max, min) y desempaquetado de tuplas.

# 4. Implementación en Python
def analizar_notas(notas):

    promedio = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)

    return promedio, maxima, minima


notas = [7, 8.5, 6, 9, 10, 5.5]

promedio, maxima, minima = analizar_notas(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {maxima:.2f}")
print(f"Nota mínima: {minima:.2f}")

def analizar_notas(notas):

    suma = 0
    maxima = notas[0]
    minima = notas[0]

    for nota in notas:

        suma += nota

        if nota > maxima:
            maxima = nota

        if nota < minima:
            minima = nota

    promedio = suma / len(notas)

    return promedio, maxima, minima


notas = [7, 8.5, 6, 9, 10, 5.5]

promedio, maxima, minima = analizar_notas(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {maxima:.2f}")
print(f"Nota mínima: {minima:.2f}")

# 5. Validación y pruebas

# EJERCICIO 39: Eliminar elementos repetidos de ["a", "b", "a", "c", "b", "d"] preservando el orden original.

# 1. Análisis del problema
# Datos de entrada: lista con elementos duplicados.
# Procesamiento: Recorrer la lista apoyándose en un conjunto (set) auxiliar para registrar los elementos ya vistos en tiempo O(1).
# MEJORA: Generalizar la solución en una función reutilizable para cualquier lista.
# Resultado esperado: Nueva lista con elementos únicos en su orden de primera aparición.

# 2. Diseño en pseudocódigo
# Definir eliminar_duplicados(lista):
#     resultado = [], vistos = set()
#     Para cada elemento en lista:
#         Si no está en vistos -> añadir a resultado y a vistos
#     Retornar resultado

# 3. Identificación de la lógica
# Combinación de estructuras de datos: la lista mantiene la secuencia ordenada mientras el conjunto garantiza búsquedas rápidas de unicidad.

# 4. Implementación en Python
def eliminar_duplicados(lista):

    resultado = []
    vistos = set()

    for elemento in lista:

        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)

    return resultado


lista = ["a", "b", "a", "c", "b", "d"]

nueva_lista = eliminar_duplicados(lista)

print(nueva_lista)

def eliminar_duplicados2(lista):

    resultado = []
    vistos = {}

    for elemento in lista:

        if elemento not in vistos:
            resultado.append(elemento)
            vistos[elemento] = True

    return resultado


lista = ["a", "b", "a", "c", "b", "d"]

nueva_lista = eliminar_duplicados(lista)

print(nueva_lista)

# 5. Validación y pruebas

# EJERCICIO 40: Contar la frecuencia de aparición de cada palabra en un texto (insensible a mayúsculas) e identificar la más frecuente.

# 1. Análisis del problema
# Datos de entrada: cadena de texto.
# Procesamiento: Convertir a minúsculas, tokenizar por espacios con .split() y contabilizar ocurrencias usando un diccionario.
# MEJORA: Aislar en otra función la búsqueda de la clave con mayor valor dentro del diccionario.
# Resultado esperado: Diccionario de frecuencias y la palabra con mayor número de apariciones.

# 2. Diseño en pseudocódigo
# Definir contar_palabras(texto) -> diccionario {palabra: conteo}
# Definir palabra_mas_repetida(frecuencia) -> clave con valor máximo

# 3. Identificación de la lógica
# Mapeo clave-valor mediante diccionarios para indexar cada palabra única con su contador de frecuencia.

# 4. Implementación en Python
def contar_palabras(texto):

    palabras = texto.lower().split()

    frecuencia = {}

    for palabra in palabras:

        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


def palabra_mas_repetida(frecuencia):

    mayor = 0
    palabra = ""

    for clave, valor in frecuencia.items():

        if valor > mayor:
            mayor = valor
            palabra = clave

    return palabra


texto = input("Ingrese un texto: ")

resultado = contar_palabras(texto)

print(resultado)

print(f"La palabra que más se repite es: {palabra_mas_repetida(resultado)}")

def contar_palabras(texto):

    frecuencia = {}

    for palabra in texto.lower().split():

        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


def palabra_mas_repetida(frecuencia):

    palabra = max(frecuencia, key=frecuencia.get)

    return palabra


texto = input("Ingrese un texto: ")

resultado = contar_palabras(texto)

print(resultado)

print(f"La palabra que más se repite es: {palabra_mas_repetida(resultado)}")

# 5. Validación y pruebas

# EJERCICIO 41: Definir la clase Pasajero (nombre, cédula, edad) con el método cumplir_anios() e instanciar tres objetos.

# 1. Análisis del problema
# Datos de entrada: atributos de identidad y edad para tres pasajeros.
# Procesamiento: Modelar la clase Pasajero con su constructor __init__, un método modificador de edad y un método de visualización.
# Resultado esperado: Despliegue en consola de los datos de cada instancia.

# 2. Diseño en pseudocódigo
# Clase Pasajero: constructor(nombre, cedula, edad), método cumplir_anios() (+1 edad), método mostrar().
# Instanciar tres pasajeros, incrementar edad del primero y mostrar todos.

# 3. Identificación de la lógica
# Encapsulamiento de estado y comportamiento en una clase plantilla para generar múltiples objetos independientes.

# 4. Implementación en Python
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


pasajero1 = Pasajero("Ana", "1234567890", 20)
pasajero2 = Pasajero("Luis", "0987654321", 25)
pasajero3 = Pasajero("María", "1122334455", 30)

pasajero1.cumplir_anios()

pasajero1.mostrar()
pasajero2.mostrar()
pasajero3.mostrar()

# 5. Validación y pruebas

# EJERCICIO 42: Modelar CuentaBancaria con métodos depositar, retirar, saldo, __str__ y registro de movimientos en historial.

# 1. Análisis del problema
# Datos de entrada: montos de depósito y retiro.
# Procesamiento: Gestionar un saldo privado iniciado en 0, impidiendo retiros superiores al saldo disponible.
# MEJORA: Incorporar una lista historial para auditar transacciones ('+monto' / '-monto') y el método ver_historial().
# Resultado esperado: Saldo actualizado y listado cronológico de movimientos.

# 2. Diseño en pseudocódigo
# Clase CuentaBancaria: _saldo = 0, historial = []
# Métodos: depositar(), retirar() (con validación de fondos), saldo(), __str__() y ver_historial().

# 3. Identificación de la lógica
# Protección de invariantes de estado (saldo no negativo) y registro secuencial de eventos en una lista interna.

# 4. Implementación en Python
class CuentaBancaria:

    def __init__(self):

        self._saldo = 0

        # MEJORA
        self.historial = []

    def depositar(self, cantidad):

        self._saldo += cantidad

        # MEJORA
        self.historial.append(f"+{cantidad}")

    def retirar(self, cantidad):

        if cantidad <= self._saldo:

            self._saldo -= cantidad

            # MEJORA
            self.historial.append(f"-{cantidad}")

        else:

            print("Fondos insuficientes.")

    def saldo(self):

        return self._saldo

    def __str__(self):

        return f"Saldo actual: ${self._saldo}"

    # MEJORA
    def ver_historial(self):

        return self.historial


cuenta = CuentaBancaria()

cuenta.depositar(100)

cuenta.depositar(50)

cuenta.retirar(30)

cuenta.retirar(200)

print(cuenta)

print("Historial:", cuenta.ver_historial())

# 5. Validación y pruebas

# EJERCICIO 43: Implementar la clase Producto (nombre, precio, stock) con gestión de ventas, reposición y valorización total de inventario.

# 1. Análisis del problema
# Datos de entrada: datos de productos y unidades a vender o reponer.
# Procesamiento: Controlar existencias mediante vender() y reabastecer(), y calcular el capital por producto con valor_inventario().
# MEJORA: Añadir el método de clase @classmethod total_inventario(productos) para consolidar el valor de una colección de productos.
# Resultado esperado: Detalle individual por artículo y valoración global del almacén.

# 2. Diseño en pseudocódigo
# Clase Producto: atributos(nombre, precio, stock), métodos de instancia y @classmethod total_inventario(cls, productos).

# 3. Identificación de la lógica
# Uso de métodos de instancia para mutar el estado individual y un método de clase para operar sobre agregaciones de objetos.

# 4. Implementación en Python
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

            print("No hay suficiente stock")

    def reabastecer(self, cantidad):

        self.stock += cantidad

    def valor_inventario(self):

        return self.precio * self.stock

    # MEJORA
    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:

            total += producto.valor_inventario()

        return total

    def __str__(self):

        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"


producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 180, 3)

producto1.vender(2)
producto2.reabastecer(4)

print(producto1)
print("Valor inventario:", producto1.valor_inventario())

print(producto2)
print("Valor inventario:", producto2.valor_inventario())

print(producto3)
print("Valor inventario:", producto3.valor_inventario())

productos = [producto1, producto2, producto3]

print("Valor total del inventario:", Producto.total_inventario(productos))

# 5. Validación y pruebas

# EJERCICIO 44: Modelar la gestión de inventario de productos con operaciones de venta, reabastecimiento y cálculo de valor total.

# 1. Análisis del problema
# Datos de entrada: atributos de los productos (nombre, precio, existencias) y movimientos de inventario.
# Procesamiento: Gestionar el stock mediante métodos de instancia y calcular el valor monetario por ítem.
# MEJORA: Incorporar el método de clase total_inventario(productos) para obtener el monto acumulado de todo el catálogo.
# Resultado esperado: Estado de cada artículo y suma total del inventario.

# 2. Diseño en pseudocódigo
# Definir clase Producto con constructor, vender(), reabastecer(), valor_inventario() y método de clase total_inventario().

# 3. Identificación de la lógica
# Encapsulamiento de reglas de negocio de stock por instancia y agregación colectiva mediante @classmethod.

# 4. Implementación en Python
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

            print("No hay suficiente stock")

    def reabastecer(self, cantidad):

        self.stock += cantidad

    def valor_inventario(self):

        return self.precio * self.stock

    # MEJORA
    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:

            total += producto.valor_inventario()

        return total

    def __str__(self):

        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"


producto1 = Producto("Mouse", 20, 10)
producto2 = Producto("Teclado", 35, 5)
producto3 = Producto("Monitor", 180, 3)

producto1.vender(2)
producto2.reabastecer(4)

print(producto1)
print("Valor inventario:", producto1.valor_inventario())

print(producto2)
print("Valor inventario:", producto2.valor_inventario())

print(producto3)
print("Valor inventario:", producto3.valor_inventario())

productos = [producto1, producto2, producto3]

print("Valor total del inventario:", Producto.total_inventario(productos))

# 5. Validación y pruebas

# EJERCICIO 45: Definir la clase Circulo con atributo radio y métodos para área, circunferencia y diámetro.
# MEJORA: Se agrega el método diametro() que retorna el doble del radio.

# 1. Análisis del problema
# Datos de entrada: longitud del radio (decimal).
# Procesamiento: Instanciar Circulo y computar sus propiedades geométricas usando math.pi.
# MEJORA: Incorporar el cálculo del diámetro (2 * r).
# Resultado esperado: Área, perímetro y diámetro del círculo.

# 2. Diseño en pseudocódigo
# Importar math, definir clase Circulo(radio) con métodos area(), circunferencia() y diametro().

# 3. Identificación de la lógica
# Agrupación de fórmulas geométricas dependientes de un único atributo de estado (radio).

# 4. Implementación en Python
import math

class Circulo:

    def __init__(self, radio):

        self.radio = radio

    def area(self):

        return math.pi * self.radio ** 2

    def circunferencia(self):

        return 2 * math.pi * self.radio

    # MEJORA
    def diametro(self):

        return self.radio * 2


radio = float(input("Ingrese el radio: "))

circulo = Circulo(radio)

print(f"Área: {circulo.area()}")

print(f"Circunferencia: {circulo.circunferencia()}")

print(f"Diámetro: {circulo.diametro()}")

# 5. Validación y pruebas

# EJERCICIO 46: Modelar la clase Estudiante con registro dinámico de notas, cálculo de promedio, estado de aprobación y conteo.
# MEJORA: Se incorpora cantidad_notas() para consultar el total de calificaciones registradas.

# 1. Análisis del problema
# Datos de entrada: nombre del alumno y sus calificaciones.
# Procesamiento: Almacenar notas en una lista interna, calcular su media y evaluar si alcanza la nota mínima de 7.
# MEJORA: Exponer la longitud de la lista de notas mediante un método dedicado.
# Resultado esperado: Nombre, promedio, condición de aprobado y número de evaluaciones.

# 2. Diseño en pseudocódigo
# Clase Estudiante(nombre): lista notas = [], métodos agregar_nota(), promedio(), aprobado() y cantidad_notas().

# 3. Identificación de la lógica
# Composición de una lista dentro de un objeto para gestionar colecciones dinámicas propias de cada instancia.

# 4. Implementación en Python
class Estudiante:

    def __init__(self, nombre):

        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, n):

        self.notas.append(n)

    def promedio(self):

        return sum(self.notas) / len(self.notas)

    def aprobado(self):

        return self.promedio() >= 7

    # MEJORA
    def cantidad_notas(self):

        return len(self.notas)


estudiante = Estudiante("Derick")

estudiante.agregar_nota(8)
estudiante.agregar_nota(9)
estudiante.agregar_nota(7)

print(f"Nombre: {estudiante.nombre}")
print(f"Promedio: {estudiante.promedio()}")
print(f"Aprobado: {estudiante.aprobado()}")
print(f"Cantidad de notas: {estudiante.cantidad_notas()}")

# 5. Validación y pruebas

# EJERCICIO 47: Crear la clase Vehiculo con control de odómetro, alerta de mantenimiento cada 10 000 km y reinicio de servicio.
# MEJORA: Se añade reiniciar_mantenimiento() para poner el kilometraje nuevamente en 0 tras el servicio.

# 1. Análisis del problema
# Datos de entrada: marca, modelo y distancias recorridas.
# Procesamiento: Acumular kilómetros en el atributo km y evaluar si alcanza el umbral de 10 000 km.
# MEJORA: Permitir restablecer el contador a cero mediante un método específico.
# Resultado esperado: Estado del vehículo antes y después de realizar el mantenimiento.

# 2. Diseño en pseudocódigo
# Clase Vehiculo(marca, modelo): km = 0, recorrer(km), necesita_mantenimiento(), reiniciar_mantenimiento() y __str__().

# 3. Identificación de la lógica
# Gestión del ciclo de vida y mantenimiento de estado numérico mediante métodos modificadores y de consulta.

# 4. Implementación en Python
class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0

    def recorrer(self, km):
        self.km += km

    def necesita_mantenimiento(self):
        return self.km >= 10000

    # MEJORA
    def reiniciar_mantenimiento(self):
        self.km = 0

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Km: {self.km}"


vehiculo = Vehiculo("Toyota", "Corolla")

vehiculo.recorrer(12000)

print(vehiculo)

print("¿Necesita mantenimiento?", vehiculo.necesita_mantenimiento())

# MEJORA
vehiculo.reiniciar_mantenimiento()

print("Después del mantenimiento:")
print(vehiculo)

# 5. Validación y pruebas

# 1. Análisis del problema
# Datos de entrada: datos personales (nombre, cédula), laborales (código, salario) y de tripulación (rol, horas de vuelo).
# Procesamiento: Construir una jerarquía de herencia multinivel (Persona -> Empleado -> Tripulante),
# incorporando en el último nivel el rol y el registro acumulado de horas de vuelo.
# Resultado esperado: Salida polimórfica en consola y formateo personalizado mediante __str__().

# 2. Diseño en pseudocódigo
# Conservar clases Persona, Pasajero(Persona) y Empleado(Persona)
# MEJORA: Definir Tripulante(Empleado) invocando super().__init__() y añadiendo rol y horas_vuelo
# MEJORA: Implementar registrar_horas(h) y sobrescribir __str__()
# Crear instancias y verificar la herencia en cadena

# 3. Identificación de la lógica
# Herencia multinivel: Tripulante extiende a Empleado, que a su vez hereda de Persona.
# super().__init__() delega la inicialización hacia las superclases, permitiendo reutilizar presentarse() y aumentar_salario().

# 4. Implementación en Python
class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cedula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)
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


# MEJORA: Subclase con herencia multinivel
class Tripulante(Empleado):
    def __init__(self, nombre, cedula, codigo_emp, salario, rol):
        super().__init__(nombre, cedula, codigo_emp, salario)
        self.rol = rol
        self.horas_vuelo = 0

    def registrar_horas(self, horas):
        self.horas_vuelo += horas

    def __str__(self):
        return (f"Tripulante {self.nombre} [{self.codigo_emp}] · Rol: {self.rol} "
                f"· {self.horas_vuelo} hrs vuelo · ${self.salario:.2f}")


# 5. Validación y pruebas

p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)
t = Tripulante("Carlos", "0923456781", "TRP-05", 2500, "Piloto")

p.sumar_millas(500)
e.aumentar_salario(10)

# Tripulante combina métodos propios y heredados de sus ancestros:
t.registrar_horas(85)          # Método propio de Tripulante
t.aumentar_salario(5)          # Método heredado de Empleado

# Todas las instancias heredan presentarse() desde Persona:
p.presentarse()
e.presentarse()
t.presentarse()

# Cada objeto ejecuta su propia implementación de __str__():
print(p)
print(e)
print(t)

# EJERCICIO 49: Jerarquía polimórfica de figuras geométricas (Figura -> Rectangulo, Circulo, Triangulo y Cuadrado).
# MEJORA: Se incorpora la interfaz perimetro() en la clase base y sus subclases, además de crear Cuadrado heredando de Rectangulo mediante super().

# 1. Análisis del problema
# Datos de entrada: medidas geométricas (base, altura, radio, lados).
# Procesamiento: Definir contratos abstractos area() y perimetro() en Figura, implementarlos en las subclases y especializar Cuadrado(Rectangulo).
# Resultado esperado: Cálculo polimórfico individual y sumatoria total de áreas y perímetros.

# 2. Diseño en pseudocódigo
# Declarar perimetro() abstracto en Figura e implementarlo en Rectangulo, Circulo y Triangulo
# MEJORA: Definir Cuadrado(Rectangulo) llamando a super().__init__(lado, lado)
# Iterar sobre una lista mixta de figuras sumando áreas y perímetros

# 3. Identificación de la lógica
# Polimorfismo y especialización: cualquier figura responde uniformemente a .area() y .perimetro(), mientras Cuadrado reutiliza la lógica de Rectangulo sin duplicar código.

# 4. Implementación en Python
import math


class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

    # MEJORA
    def perimetro(self):
        raise NotImplementedError("Cada figura debe implementar perimetro()")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    # MEJORA
    def perimetro(self):
        return 2 * (self.base + self.altura)


# MEJORA: Especialización heredando de Rectangulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    # MEJORA
    def perimetro(self):
        return 2 * math.pi * self.radio


class Triangulo(Figura):
    def __init__(self, base, altura, lado1=None, lado2=None):
        self.base = base
        self.altura = altura
        # Si se omiten los lados laterales, se calculan asumiendo un triángulo rectángulo
        self.lado1 = lado1 if lado1 is not None else math.sqrt(base**2 + altura**2)
        self.lado2 = lado2 if lado2 is not None else altura

    def area(self):
        return (self.base * self.altura) / 2

    # MEJORA
    def perimetro(self):
        return self.base + self.lado1 + self.lado2


# 5. Validación y pruebas

figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3, lado1=5, lado2=3),
    Cuadrado(4)  # MEJORA
]

for f in figuras:
    nombre = type(f).__name__
    print(f"{nombre:<12} | Area: {f.area():.2f} | Perimetro: {f.perimetro():.2f}")

total_area = sum(f.area() for f in figuras)
total_perimetro = sum(f.perimetro() for f in figuras)

print("-" * 45)
print(f"Area total     : {total_area:.2f}")
print(f"Perimetro total: {total_perimetro:.2f}")

# EJERCICIO 50: Jerarquía Vehiculo -> Auto / Moto con evaluación de antigüedad clásica.
# MEJORA: Se añade el atributo anio y el método es_clasico() (≥ 25 años) en Vehiculo para ser heredado por Auto y Moto.

# 1. Análisis del problema
# Datos de entrada: marca, modelo, año de fabricación y atributos propios (puertas o cilindraje).
# Procesamiento: Centralizar en Vehiculo el cálculo de antigüedad respecto a 2026 y delegar la inicialización común desde las subclases con super().
# Resultado esperado: Descripción de cada vehículo e indicación de si califica como clásico.

# 2. Diseño en pseudocódigo
# Ampliar Vehiculo con anio y método es_clasico()
# Actualizar constructores y __str__ de Auto y Moto pasando anio a super()
# Recorrer colección de vehículos evaluando es_clasico()

# 3. Identificación de la lógica
# Herencia simple con factorización de comportamiento común en la superclase para evitar redundancia en las clases derivadas.

# 4. Implementación en Python
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # Método compartido mediante herencia con todas las subclases
    def es_clasico(self):
        anio_actual = 2026
        return (anio_actual - self.anio) >= 25

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo} ({self.anio}), {self.puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindraje):
        super().__init__(marca, modelo, anio)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo} ({self.anio}), {self.cilindraje}cc"


# 5. Validación y pruebas

auto1 = Auto("Toyota", "Corolla", 2018, 4)
auto2 = Auto("Volkswagen", "Escarabajo", 1985, 2)
moto1 = Moto("Honda", "CBR", 2022, 600)

garaje = [auto1, auto2, moto1]

for v in garaje:
    clasico_txt = "Si" if v.es_clasico() else "No"
    print(f"{v} | Clasico: {clasico_txt}")

# EJERCICIO 51: Polimorfismo en la jerarquía Animal (Perro, Gato, Ave) con sistema de gestión de energía.
# MEJORA: Se incorpora energia = 100 en Animal, el método dormir() para recuperarla y consumo de 10 puntos al ejecutar hablar().

# 1. Análisis del problema
# Datos de entrada: nombre del animal y secuencia de acciones (hablar o dormir).
# Procesamiento: Controlar el gasto energético en la clase base antes de permitir que cada subclase emita su sonido característico.
# Resultado esperado: Sonido del animal y energía restante, o aviso de cansancio si la energía es insuficiente.

# 2. Diseño en pseudocódigo
# Inicializar energia = 100 en Animal.__init__
# Implementar puede_actuar(costo) y dormir() en Animal
# Sobrescribir hablar() en Perro, Gato y Ave condicionándolo a puede_actuar()

# 3. Identificación de la lógica
# Polimorfismo combinado con gestión centralizada de recursos: la superclase regula el estado energético mientras las subclases especializan la acción.

# 4. Implementación en Python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100

    def puede_actuar(self, costo=10):
        if self.energia >= costo:
            self.energia -= costo
            return True
        print(f"{self.nombre} no tiene energia para hablar (Energia: {self.energia}). Necesita dormir.")
        return False

    def dormir(self):
        self.energia = min(100, self.energia + 30)
        print(f"{self.nombre} durmio una siesta. Energia actual: {self.energia}")

    def hablar(self):
        if self.puede_actuar():
            print(f"{self.nombre}: (sonido genérico)")


class Perro(Animal):
    def hablar(self):
        if self.puede_actuar():
            print(f"{self.nombre}: Guau guau! (Energia restante: {self.energia})")


class Gato(Animal):
    def hablar(self):
        if self.puede_actuar():
            print(f"{self.nombre}: Miau miau (Energia restante: {self.energia})")


class Ave(Animal):
    def hablar(self):
        if self.puede_actuar():
            print(f"{self.nombre}: Pio pio (Energia restante: {self.energia})")


# 5. Validación y pruebas

perro = Perro("Rex")
gato = Gato("Felix")
ave = Ave("Piolin")

animales = [perro, gato, ave]

# Primera ronda de vocalizaciones
for a in animales:
    a.hablar()

# Agotamos la energía de Felix para comprobar el límite
for _ in range(9):
    gato.hablar()

# Intento de hablar sin energía disponible
gato.hablar()

# Recuperación mediante descanso y nueva vocalización
gato.dormir()
gato.hablar()

# EJERCICIO 52: Sistema de nómina polimórfica con Empleado (sueldo_mensual abstracto), EmpleadoPorHoras, EmpleadoFijo y EmpleadoComision.
# MEJORA: Se incorpora calcular_bono() en Empleado (15% por desempeño sobresaliente) y se crea la subclase EmpleadoComision.

# 1. Análisis del problema
# Datos de entrada: nombre, parámetros contractuales (horas/tarifa, salario fijo o base/ventas/comisión) e indicador de desempeño.
# Procesamiento: Cada subclase implementa su fórmula de sueldo_mensual(), mientras la clase base calcula bonificaciones sobre dicho monto.
# Resultado esperado: Desglose salarial individual, bonos asignados y costo total de la nómina.

# 2. Diseño en pseudocódigo
# Definir Empleado con sueldo_mensual() abstracto y método concreto calcular_bono()
# Implementar EmpleadoPorHoras, EmpleadoFijo y EmpleadoComision
# Iterar sobre la plantilla consolidando sueldos base y bonificaciones

# 3. Identificación de la lógica
# Patrón Método Plantilla (Template Method): calcular_bono() en la superclase invoca polimórficamente a self.sueldo_mensual(), delegando el cálculo específico a cada subclase.

# 4. Implementación en Python
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def sueldo_mensual(self):
        raise NotImplementedError("La subclase debe definir sueldo_mensual()")

    # Método plantilla que invoca polimórficamente a sueldo_mensual()
    def calcular_bono(self, es_sobresaliente=False):
        if es_sobresaliente:
            return round(self.sueldo_mensual() * 0.15, 2)
        return 0.0

    def __str__(self):
        return f"{self.nombre}: ${self.sueldo_mensual():.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def sueldo_mensual(self):
        return self.horas * self.tarifa


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def sueldo_mensual(self):
        return self.sueldo


# Nueva subclase para personal con esquema de comisiones por ventas
class EmpleadoComision(Empleado):
    def __init__(self, nombre, sueldo_base, total_ventas, porcentaje_comision):
        super().__init__(nombre)
        self.sueldo_base = sueldo_base
        self.total_ventas = total_ventas
        self.porcentaje_comision = porcentaje_comision

    def sueldo_mensual(self):
        comision = self.total_ventas * (self.porcentaje_comision / 100)
        return self.sueldo_base + comision


# 5. Validación y pruebas

empleados = [
    EmpleadoPorHoras("Ana", 160, 8),
    EmpleadoFijo("Luis", 1500),
    EmpleadoComision("Marcos", 600, 8000, 5)
]

total_nomina = 0
total_bonos = 0

for emp in empleados:
    sueldo = emp.sueldo_mensual()
    # Asignación de bono por mérito (aplica a Ana y Marcos)
    destacado = emp.nombre in ["Ana", "Marcos"]
    bono = emp.calcular_bono(destacado)
    
    total_nomina += sueldo
    total_bonos += bono
    
    print(f"{emp} | Bono por desempeno: ${bono:.2f} | Total a cobrar: ${sueldo + bono:.2f}")

print("-" * 55)
print(f"Nomina base total: ${total_nomina:.2f}")
print(f"Bonos acumulados : ${total_bonos:.2f}")
print(f"Gasto final      : ${total_nomina + total_bonos:.2f}")