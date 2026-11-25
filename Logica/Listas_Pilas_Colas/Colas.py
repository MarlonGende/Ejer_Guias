from collections import deque
import random
# EJERCICIO: Modelar la atención en una sucursal bancaria en la que los usuarios ingresan (encolar) y pasan a ventanilla secuencialmente (desencolar), incorporando acceso preferencial al inicio para usuarios VIP mediante cola.appendleft().

# 1. Análisis del problema
# Datos de entrada: Opción elegida en el menú, nombre del usuario y confirmación de categoría VIP al incorporarse a la fila.
# Procesamiento: Emplear una estructura de cola (deque) bajo política FIFO (primero en entrar, primero en salir) con popleft(), insertar usuarios regulares al final mediante append() y posicionar a los VIP al comienzo con appendleft(), llevando además un conteo acumulado de atenciones realizadas.
# Resultado esperado: Avisos de registro, atención en caja, consulta del próximo turno, visualización íntegra de la fila y total de usuarios atendidos impresos en pantalla.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Inicializar la cola vacía y el acumulador de personas atendidas
# Dentro de un bucle while True, desplegar el menú y capturar la opción seleccionada
# Al registrar un usuario, consultar si posee estatus VIP para aplicar appendleft() o append() según corresponda
# Conservar las funcionalidades para despachar turno, consultar el frente, listar toda la fila y reportar el total de atendidos
# Finalizar la ejecución cuando se seleccione la opción de salida

# 3. Identificación de la lógica
# El uso de deque optimiza tanto la inserción por el extremo final como la extracción por el frente en tiempo constante.
# Ubicar a los clientes VIP en la cabecera mediante appendleft() les otorga prioridad inmediata sin alterar la secuencia relativa de los demás.
# Distinguir entre ingresos regulares y preferenciales evidencia claramente cómo se modifica el flujo de atención.

# 4. Implementación en Python

cola = deque()
# Variable acumuladora para contabilizar el total de usuarios ya despachados
atendidos_total = 0

while True:
    print("\n1.Llega cliente 2.Atender 3.Ver frente 4.Ver toda la cola 5.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        # Verificar si el usuario cuenta con prioridad VIP para ubicarlo al inicio o al final
        es_vip = input("¿Es cliente VIP? (s/n): ").strip().lower()
        if es_vip == "s":
            cola.appendleft(f"{nom} [VIP]")
            print(f"{nom} (VIP) entró al frente de la fila. {len(cola)} clientes en espera.")
        else:
            cola.append(nom)
            print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            # Incrementar en una unidad el registro global de personas atendidas
            atendidos_total += 1
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}. (Atendidos hoy: {atendidos_total})")

    elif op == "3":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "4":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " <- siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")

    elif op == "5":
        # Desplegar el resumen de usuarios atendidos antes de concluir la ejecución
        print(f"Total de clientes atendidos: {atendidos_total}")
        break

    # Validación para gestionar entradas que no correspondan a ninguna opción válida
    else:
        print("Opción inválida")



# EJERCICIO: Gestor de cola de impresión que despacha archivos según su orden de recepción, tomando 2 segundos por cada página e incorporando la posibilidad de anular un documento por su nombre.

# 1. Análisis del problema
# Datos de entrada: Colección de documentos pendientes representados como tuplas (nombre, paginas) y, de forma opcional, el identificador de un archivo a descartar antes de iniciar.
# Procesamiento: Encolar los archivos en una deque siguiendo el esquema FIFO, habilitar la búsqueda por nombre para suprimir el elemento con cola.remove((nombre, paginas)) y ejecutar los trabajos activos calculando 2 segundos por página junto con el tiempo transcurrido.
# Resultado esperado: Notificaciones de anulación cuando proceda, detalle de cada documento procesado con su duración individual y acumulada, y tiempo total invertido en consola.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Implementar cancelar_trabajo(cola, nombre_objetivo) para localizar la tupla dentro de la deque y suprimirla mediante cola.remove()
# Crear procesar_impresora(trabajos, cancelar=None) inicializando la estructura con deque(trabajos)
# Ejecutar la anulación del documento especificado antes de comenzar el ciclo si se recibe un nombre
# Extraer elementos con popleft(), acumular paginas * 2 en el tiempo global y reportar cada avance
# Validar ambos escenarios (con y sin cancelación) mostrando la duración total

# 3. Identificación de la lógica
# La estructura FIFO garantiza que los archivos no anulados se impriman respetando estrictamente su turno de llegada.
# Localizar la tupla exacta dentro de la deque permite invocar cola.remove((nombre, paginas)) sin complicaciones.
# Modularizar la lógica de cancelación en una función independiente mejora la legibilidad y facilita las pruebas.

# 4. Implementación en Python

# Función auxiliar para localizar un documento por su nombre en la deque y removerlo con cola.remove()
def cancelar_trabajo(cola, nombre_objetivo):
    for trabajo in list(cola):
        nombre, _ = trabajo
        if nombre == nombre_objetivo:
            cola.remove(trabajo)
            print(f"Trabajo cancelado: {nombre}")
            return True
    print(f"No se encontró el trabajo '{nombre_objetivo}' en la cola")
    return False


def procesar_impresora(trabajos, cancelar=None):
    cola = deque(trabajos)
    tiempo_total = 0

    # Verificar si se solicitó anular algún archivo antes de arrancar el proceso de impresión
    if cancelar is not None:
        cancelar_trabajo(cola, cancelar)

    while cola:
        nombre, paginas = cola.popleft()      # Esquema FIFO: se procesa primero el más antiguo
        tiempo = paginas * 2
        tiempo_total += tiempo
        print(f"Imprimiendo {nombre}: {paginas} páginas -> {tiempo}s "
              f"(acumulado {tiempo_total}s)")

    return tiempo_total


# --- Ejemplos de ejecución ---
trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10),
]

total = procesar_impresora(trabajos)
print(f"\nTiempo total: {total}s")

# Caso de prueba anulando un documento específico antes de comenzar la impresión
print("\n--- Prueba cancelando 'Recibo.pdf' ---")
total_cancelado = procesar_impresora(trabajos, cancelar="Recibo.pdf")
print(f"\nTiempo total tras cancelar: {total_cancelado}s")


# EJERCICIO: Ampliar la estructura de cola para gestionar niveles de urgencia, despachando primero los de mayor jerarquía y desempatando por orden de llegada, con soporte para reasignar la prioridad de un elemento ya registrado.

# 1. Análisis del problema
# Datos de entrada: Ítems acompañados de un grado de prioridad al insertarse, así como un elemento existente junto con su nuevo nivel de urgencia cuando se requiera reubicarlo.
# Procesamiento: Administrar un deque independiente por cada nivel en ColaPrioridad para extraer de mayor a menor jerarquía respetando FIFO en cada nivel, incorporando un método que localice el ítem, lo extraiga de su cola actual y lo inserte en el nivel destino.
# Resultado esperado: Visualización de los niveles activos, notificación del cambio de jerarquía y secuencia resultante al despachar los elementos.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Conservar ColaPrioridad con un arreglo de deques en self.colas, además de encolar() y desencolar()
# Añadir cambiar_prioridad(valor, nueva_prioridad) para encontrar el ítem, removerlo de su deque actual y reubicarlo en el nivel indicado
# Comprobar que la nueva jerarquía sea válida y que el elemento exista previamente
# Validar reasignando la prioridad de un elemento en espera y comprobando el nuevo orden de salida

# 3. Identificación de la lógica
# Asignar una cola FIFO dedicada por nivel asegura que elementos con idéntica urgencia salgan en estricto orden de ingreso.
# Reasignar prioridad implica simplemente extraer el dato de su cola actual y añadirlo al final de la cola correspondiente al nuevo nivel.
# Las comprobaciones de rango y existencia previenen fallos silenciosos al manipular elementos ya almacenados.

# 4. Implementación en Python

class ColaPrioridad:
    def __init__(self, niveles=3):
        # Arreglo de deques indexado por nivel (a mayor índice, mayor urgencia)
        self.niveles = niveles
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, valor, prioridad):
        if not 0 < prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")
        self.colas[prioridad].append(valor)

    def desencolar(self):
        """Extrae el ítem más urgente; ante igualdad de nivel, despacha el primero en llegar."""
        # Iterar de forma descendente desde el nivel máximo hasta el mínimo
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                return self.colas[i].popleft()
        raise IndexError("Cola vacía")

    # Método para localizar un elemento en espera y reasignarlo a un nivel diferente
    def cambiar_prioridad(self, valor, nueva_prioridad):
        if not 0 < nueva_prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")

        # Explorar todos los niveles en busca del elemento especificado
        for nivel in range(1, self.niveles + 1):
            if valor in self.colas[nivel]:
                # Extraer del nivel anterior e insertar al final del nuevo nivel asignado
                self.colas[nivel].remove(valor)
                self.colas[nueva_prioridad].append(valor)
                return True
        return False

    def __str__(self):
        s = []
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                s.append(f"  P{i}: {list(self.colas[i])}")
        return "\n".join(s) if s else "(vacía)"


# --- Ejemplos de ejecución ---
cp = ColaPrioridad(3)
cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

print(cp)
# P3: ['Luis']
# P2: ['Beto']
# P1: ['Ana', 'Diana']

# Validación de cambio de jerarquía sobre un ítem previamente encolado
print("\nCambiando prioridad de 'Ana' de 1 a 3...")
if cp.cambiar_prioridad("Ana", 3):
    print("Prioridad actualizada.")
print(cp)

# Despacho secuencial según prioridad
print("\nAtendiendo en orden:")
while True:
    try:
        print("Atendiendo:", cp.desencolar())
    except IndexError:
        break


# EJERCICIO: Sistema de gestión de turnos con emisión automática de tickets secuenciales (1, 2, 3...) que llama a los usuarios siguiendo su orden de llegada.

# 1. Análisis del problema
# Datos de entrada: Opción seleccionada del menú y nombre del usuario al solicitar un turno.
# Procesamiento: Emplear una cola (deque) bajo política FIFO junto con un contador incremental para generar números de turno correlativos (1, 2, 3...), incluyendo además una consulta del total de personas pendientes en fila.
# Resultado esperado: Confirmación del ticket generado con número y titular, llamado al próximo turno al despachar, listado de la fila vigente y conteo de usuarios en espera en consola.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Inicializar la cola vacía y la variable siguiente_ticket = 1
# En un bucle while True, presentar el menú con opciones de llegada, atención, consulta y salida
# Al registrar un usuario, vincularle siguiente_ticket, almacenar (ticket, nombre) e incrementar el contador
# Al despachar, extraer el primer elemento mediante popleft() y anunciar su número y nombre
# Incorporar una opción para reportar la cantidad de personas aún pendientes de atención

# 3. Identificación de la lógica
# Empaquetar cada registro como una tupla (ticket, nombre) mantiene asociados el identificador numérico y el usuario.
# Un contador monótono creciente garantiza tickets únicos y consecutivos sin importar cuántas atenciones ocurran entre medias.
# La estructura FIFO asegura llamar siempre al turno más antiguo pendiente en la fila.

# 4. Implementación en Python

cola = deque()
siguiente_ticket = 1

while True:
    print("\n1.Llega cliente 2.Atender siguiente 3.Ver cola 4.Clientes en espera 5.Salir")
    op = input("Opción: ").strip()

    if op == "1":
        nombre = input("Nombre del cliente: ").strip()
        if nombre:
            ticket = siguiente_ticket
            siguiente_ticket += 1
            cola.append((ticket, nombre))
            print(f"Ticket #{ticket} asignado a {nombre}.")
        else:
            print("El nombre no puede estar vacío.")

    elif op == "2":
        if not cola:
            print("No hay clientes en espera.")
        else:
            ticket, nombre = cola.popleft()
            print(f"Llamando al Ticket #{ticket} - {nombre}. Quedan {len(cola)} en espera.")

    elif op == "3":
        if not cola:
            print("La cola está vacía.")
        else:
            print("Fila actual:")
            for i, (ticket, nombre) in enumerate(cola):
                marca = " <- siguiente" if i == 0 else ""
                print(f"  {i+1}. Ticket #{ticket} - {nombre}{marca}")

    # Consulta rápida del número total de usuarios que permanecen en la fila
    elif op == "4":
        print(f"Clientes en espera: {len(cola)}")

    elif op == "5":
        print("Simulador finalizado.")
        break

    # Manejo de entradas numéricas o textuales no contempladas en el menú
    else:
        print("Opción inválida.")


# EJERCICIO: Simular la rotación cíclica de turnos entre participantes donde, tras jugar, cada integrante regresa al final de la fila durante 10 jugadas consecutivas.

# 1. Análisis del problema
# Datos de entrada: Lista de participantes inscritos y número total de turnos a ejecutar (10 jugadas).
# Procesamiento: Inicializar una deque con los participantes, extraer al primero con popleft() para ejecutar su jugada y reinsertarlo al fondo mediante append() durante 10 ciclos, rastreando simultáneamente el avance de rondas completas.
# Resultado esperado: Detalle de cada uno de los 10 turnos con su número, participante activo y configuración actualizada de la fila, más un balance de participaciones.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Inicializar la estructura con deque(jugadores) y definir total_turnos = 10
# Incorporar un diccionario contador de jugadas por participante para estadísticas finales
# Iterar 10 veces: extraer el frente con popleft(), anunciar su turno y reencolarlo al final con append()
# Reportar la cantidad total de turnos disputados por cada integrante al concluir

# 3. Identificación de la lógica
# Encadenar popleft() con append() transforma una cola lineal en una estructura circular sin alterar la secuencia relativa.
# En cada paso, el participante en cabecera actúa y pasa al final para permitir el avance del siguiente.
# Contabilizar las intervenciones permite comprobar el equilibrio del reparto tras una cantidad fija de turnos.

# 4. Implementación en Python

jugadores = ["Ana", "Luis", "Diana", "Beto"]
cola = deque(jugadores)
total_turnos = 10

# Diccionario auxiliar para registrar cuántas intervenciones acumula cada participante
conteo_turnos = {jugador: 0 for jugador in jugadores}

for turno in range(1, total_turnos + 1):
    jugador_actual = cola.popleft()
    # Incrementar el registro de participaciones del jugador activo
    conteo_turnos[jugador_actual] += 1
    cola.append(jugador_actual)

    # Determinar el número de ronda completa en curso según el total de participantes
    ronda = (turno - 1) // len(jugadores) + 1
    print(f"Turno {turno:2d} (Ronda {ronda}): juega {jugador_actual} -> Siguiente orden: {list(cola)}")

# Despliegue estadístico final con el total de turnos disputados por cada integrante
print("\nResumen de participaciones en 10 turnos:")
for jugador, veces in conteo_turnos.items():
    print(f"  {jugador}: {veces} turnos")



# EJERCICIO: Implementar una cola FIFO que incorpore el método maximo_visto(), capaz de devolver el valor más alto que haya ingresado en algún momento, incluso si ya fue desencolado.

# 1. Análisis del problema
# Datos de entrada: Elementos numéricos o comparables insertados y extraídos bajo orden FIFO, junto con peticiones del récord histórico máximo.
# Procesamiento: Gestionar una deque estándar para inserciones y extracciones, manteniendo un atributo auxiliar con el mayor valor ingresado hasta el momento para retornarlo en maximo_visto() sin importar si sigue presente, además de permitir consultar el máximo vigente en fila.
# Resultado esperado: Registro de inserciones y salidas, consultas de maximo_visto() en diversas etapas y contraste frente al mayor valor activo en la cola.

# 2. Diseño en pseudocódigo
# Importar deque del módulo collections
# Definir ColaConMaximoHistorico con self.cola = deque() y self._max_visto = None
# En encolar(valor), insertar el dato y actualizar self._max_visto si es el inicial o supera el récord previo
# En desencolar(), extraer el frente con popleft() preservando intacto self._max_visto
# Codificar maximo_visto() devolviendo self._max_visto
# Añadir maximo_actual() para obtener el mayor elemento que aún permanece dentro de la cola

# 3. Identificación de la lógica
# Dado que el máximo histórico persiste tras las extracciones, solo se requiere actualizar una variable de control durante cada inserción.
# Preservar intacta la mecánica FIFO garantiza que el comportamiento estándar de la cola no se vea alterado.
# Contrastar el récord histórico con el máximo vigente evidencia por qué el valor máximo no se pierde al desencolarlo.

# 4. Implementación en Python

class ColaConMaximoHistorico:
    def __init__(self):
        self.cola = deque()
        self._max_visto = None

    def encolar(self, valor):
        self.cola.append(valor)
        if self._max_visto is None or valor > self._max_visto:
            self._max_visto = valor

    def desencolar(self):
        if not self.cola:
            raise IndexError("La cola está vacía")
        return self.cola.popleft()

    def maximo_visto(self):
        return self._max_visto

    # Método auxiliar para obtener el valor más alto presente actualmente dentro de la fila
    def maximo_actual(self):
        if not self.cola:
            return None
        return max(self.cola)

    def __str__(self):
        return f"Cola: {list(self.cola)}"


# --- Ejemplos de ejecución ---
cola = ColaConMaximoHistorico()

for num in [10, 45, 22, 8]:
    cola.encolar(num)
    print(f"Encolado {num} -> {cola} | Máximo visto: {cola.maximo_visto()}")

# Extracción secuencial de elementos, incluyendo el 45 que marcó el máximo histórico
for _ in range(3):
    sacado = cola.desencolar()
    # Comparar el récord histórico frente al máximo vigente tras cada extracción
    print(f"Desencolado {sacado} -> {cola} | Máximo visto: {cola.maximo_visto()} | Máximo actual: {cola.maximo_actual()}")

# Inserción de un valor inferior para verificar que maximo_visto() mantiene el máximo anterior
cola.encolar(30)
print(f"Encolado 30 -> {cola} | Máximo visto: {cola.maximo_visto()} | Máximo actual: {cola.maximo_actual()}")


# EJERCICIO: Modelar una fila única de 10 usuarios atendidos por 2 ventanillas en paralelo, donde cada ventanilla toma al siguiente al desocuparse y cada trámite dura entre 30 y 90 segundos, incluyendo métricas adicionales.

# 1. Análisis del problema
# Datos de entrada: 10 usuarios en una fila compartida y tiempos de servicio aleatorios comprendidos entre 30 y 90 segundos.
# Procesamiento: Gestionar una cola FIFO (deque) y monitorear el instante de disponibilidad de cada ventanilla; asignar cada usuario a la caja que quede libre primero y actualizar su reloj de salida, calculando además el tiempo que cada persona aguardó en fila.
# Resultado esperado: Ventanilla asignada a cada usuario, marcas de inicio y fin, tiempo de espera individual y duración total hasta desocupar ambas cajas.

# 2. Diseño en pseudocódigo
# Importar deque de collections y el módulo random
# Inicializar la fila con 10 usuarios y definir tiempo_libre_cajas = [0, 0] para ambas ventanillas
# Mientras existan usuarios en espera, seleccionar la ventanilla con menor tiempo de liberación
# Determinar inicio = tiempo_libre_cajas[idx_caja], duracion = random.randint(30, 90) y fin = inicio + duracion
# Registrar el tiempo de espera en fila y actualizar tiempo_libre_cajas[idx_caja] = fin
# Imprimir la traza de atención por usuario y el tiempo global de operación

# 3. Identificación de la lógica
# Una fila única FIFO regula la prioridad de paso, mientras que comparar los relojes de liberación determina qué ventanilla atiende de inmediato.
# Asignar siempre la caja que se desocupa antes modela con precisión el procesamiento concurrente en dos puntos de atención.
# Registrar el instante de inicio permite cuantificar exactamente cuánto tiempo aguardó cada usuario antes de ser atendido.

# 4. Implementación en Python

def simular_cajas(cantidad_clientes=10, semilla=42):
    random.seed(semilla)
    cola = deque(f"Cliente {i}" for i in range(1, cantidad_clientes + 1))

    # Almacena el instante exacto en segundos en que se desocupa cada una de las 2 ventanillas
    tiempo_libre_cajas = [0, 0]
    # Contador auxiliar para registrar el volumen de usuarios despachados por cada caja
    atendidos_por_caja = [0, 0]

    print(f"Simulando {cantidad_clientes} clientes con 2 cajas (30s a 90s por cliente):\n")

    while cola:
        cliente = cola.popleft()

        # Seleccionar la ventanilla que se libere más pronto (en caso de empate, se asigna la Caja 1)
        idx_caja = 0 if tiempo_libre_cajas[0] <= tiempo_libre_cajas[1] else 1
        inicio = tiempo_libre_cajas[idx_caja]
        duracion = random.randint(30, 90)
        fin = inicio + duracion

        # Determinar el tiempo aguardado en fila hasta que la ventanilla queda disponible
        espera = inicio
        tiempo_libre_cajas[idx_caja] = fin
        atendidos_por_caja[idx_caja] += 1

        print(f"{cliente} -> Caja {idx_caja + 1} | Inicia: {inicio}s | Tarda: {duracion}s | "
              f"Termina: {fin}s | Espera: {espera}s")

    tiempo_total = max(tiempo_libre_cajas)
    print(f"\nTiempo total para atender a todos: {tiempo_total}s")
    # Reporte comparativo de carga de trabajo atendida por cada ventanilla
    print(f"Clientes atendidos -> Caja 1: {atendidos_por_caja[0]}, Caja 2: {atendidos_por_caja[1]}")
    return tiempo_total


# --- Ejemplos de ejecución ---
simular_cajas(10)

