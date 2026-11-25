# EJERCICIO: Incorporar en ListaEnlazada el método insertar_ordenado_desc(data) para colecciones ordenadas de forma descendente, añadiendo una verificación complementaria.

# 1. Análisis del problema
# Datos de entrada: Un nuevo valor para alojar en una lista enlazada ordenada de mayor a menor.
# Procesamiento: Instanciar el nodo y posicionarlo en la cabecera si supera a head, o recorrer hasta el último nodo cuyo sucesor sea mayor o igual al valor para enlazarlo preservando el orden descendente; incluir también un método que valide si la secuencia descendente se mantiene íntegra.
# Resultado esperado: Lista enlazada actualizada en orden descendente y confirmación booleana de su ordenamiento.

# 2. Diseño en pseudocódigo
# Declarar las clases Nodo y ListaEnlazada con los atributos head y cantidad
# En insertar_ordenado_desc(data), verificar si la lista está vacía o si data > self.head.data para insertarlo en la cabeza
# Caso contrario, avanzar con anterior mientras anterior.next exista y anterior.next.data >= data
# Enlazar nuevo.next = anterior.next y seguidamente anterior.next = nuevo, incrementando cantidad en 1
# Incorporar el método esta_ordenada_desc() para evaluar cada par adyacente de nodos
# Ejecutar pruebas insertando múltiples datos y desplegando la lista junto con su validación

# 3. Identificación de la lógica
# Cambiar el criterio de ordenamiento de ascendente a descendente invierte el sentido de las desigualdades al localizar el punto de inserción.
# Emplear >= durante el recorrido preserva el orden relativo de llegada ante valores repetidos.
# Asignar primero nuevo.next antes de reasignar anterior.next previene la pérdida de referencia hacia el resto de la cadena.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_ordenado(self, data):
        nuevo = Nodo(data)
        # Escenario A: lista vacía o el valor nuevo es menor que la cabecera -> insertar al principio
        if self.head is None or data < self.head.data:
            nuevo.next = self.head
            self.head = nuevo
        else:
            # Escenario B: localizar el nodo PREDECESOR (el último cuyo valor sea <= data)
            anterior = self.head
            while anterior.next is not None and anterior.next.data <= data:
                anterior = anterior.next
            nuevo.next = anterior.next      # paso 1: el nuevo nodo enlaza con el tramo restante
            anterior.next = nuevo           # paso 2: el nodo predecesor apunta al nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de insertar_ordenado_desc invirtiendo los operadores relacionales para ordenar de mayor a menor
    def insertar_ordenado_desc(self, data):
        nuevo = Nodo(data)
        # Ajuste 1: si la lista carece de nodos o el nuevo dato supera a la cabeza, se ubica al inicio
        if self.head is None or data > self.head.data:
            nuevo.next = self.head
            self.head = nuevo
        else:
            # Localizar el nodo PREDECESOR (el último con valor >= data)
            anterior = self.head
            # Ajuste 2: desplazarse mientras el nodo siguiente sea mayor o igual al dato por insertar
            while anterior.next is not None and anterior.next.data >= data:
                anterior = anterior.next
            nuevo.next = anterior.next      # paso 1: el nuevo nodo enlaza con el tramo restante
            anterior.next = nuevo           # paso 2: el nodo predecesor apunta al nuevo
        self.cantidad = self.cantidad + 1

    # Método complementario para validar que toda la secuencia respete el criterio descendente
    def esta_ordenada_desc(self):
        actual = self.head
        while actual is not None and actual.next is not None:
            if actual.data < actual.next.data:
                return False
            actual = actual.next
        return True

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista_desc = ListaEnlazada()
valores = [15, 40, 25, 40, 5, 30]

for v in valores:
    lista_desc.insertar_ordenado_desc(v)

# Desplegar los valores almacenados, el total de nodos y la verificación del orden descendente
print("Lista descendente:", lista_desc.a_lista())
print("Cantidad de nodos:", lista_desc.cantidad)
print("¿Está ordenada de mayor a menor?:", lista_desc.esta_ordenada_desc())

# EJERCICIO: Incorporar el método eliminar_todos(data) en ListaEnlazada y desarrollar quitar_duplicados() para colecciones ordenadas, incluyendo una métrica de eliminación.

# 1. Análisis del problema
# Datos de entrada: Una lista enlazada, un valor objetivo a suprimir en su totalidad y una lista ordenada con posibles repeticiones contiguas.
# Procesamiento: Suprimir todas las apariciones de un valor (incluyendo consecutivas o ubicadas en la cabeza) retornando el total eliminado, y depurar duplicados adyacentes en una lista ordenada cotejando cada nodo con su sucesor sin avanzar el puntero tras borrar; añadir también el conteo de nodos suprimidos.
# Resultado esperado: Total de nodos eliminados por eliminar_todos, lista depurada sin repetidos y cantidad de duplicados descartados en consola.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con eliminar_todos(data)
# Incorporar quitar_duplicados() iterando la lista ordenada desde head
# Cotejar actual.data frente a actual.next.data; ante igualdad, puentear actual.next sin desplazar actual
# Ante desigualdad, avanzar actual = actual.next y actualizar self.cantidad al finalizar
# Validar ambos métodos con casos de prueba e imprimir los resultados

# 3. Identificación de la lógica
# En una estructura ordenada, los elementos idénticos permanecen agrupados de forma contigua.
# Mantener fijo el puntero tras suprimir un nodo permite inspeccionar inmediatamente el nuevo sucesor en caso de múltiples repeticiones seguidas.
# Sincronizar self.cantidad garantiza que la longitud registrada refleje siempre el estado real de la lista.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    def eliminar_todos(self, data):
        borrados = 0
        # Etapa 1: mientras la CABECERA contenga el valor objetivo, desplazarla
        while self.head is not None and self.head.data == data:
            self.head = self.head.next
            borrados = borrados + 1
        # Etapa 2: inspeccionar el tramo restante observando UN nodo por delante
        anterior = self.head
        while anterior is not None and anterior.next is not None:
            if anterior.next.data == data:
                anterior.next = anterior.next.next    # puentear el nodo coincidente...
                borrados = borrados + 1               # ...y mantener fijo el puntero
            else:
                anterior = anterior.next              # avanzar únicamente cuando no hubo borrado
        self.cantidad = self.cantidad - borrados
        return borrados

    # Implementación de quitar_duplicados() para listas ordenadas aplicando la regla de mantener el puntero al eliminar
    def quitar_duplicados(self):
        eliminados = 0
        actual = self.head

        while actual is not None and actual.next is not None:
            if actual.data == actual.next.data:
                actual.next = actual.next.next
                eliminados = eliminados + 1
            else:
                actual = actual.next

        self.cantidad = self.cantidad - eliminados
        # Retornar la cantidad de elementos repetidos suprimidos como dato informativo
        return eliminados

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista_dup = ListaEnlazada()
for x in [1, 1, 2, 3, 3, 3]:
    lista_dup.insertar_final(x)

print("Lista ordenada original:", lista_dup.a_lista())
quitados = lista_dup.quitar_duplicados()
print("Sin duplicados:", lista_dup.a_lista())
print("Duplicados quitados:", quitados)
print("Cantidad actual:", lista_dup.cantidad)

# Caso de prueba para eliminar_todos con ocurrencias repetidas al comienzo y contiguas
lista_borrar = ListaEnlazada()
for x in [5, 5, 8, 5, 9, 5, 5]:
    lista_borrar.insertar_final(x)

print("\nLista para eliminar_todos:", lista_borrar.a_lista())
borrados_5 = lista_borrar.eliminar_todos(5)
print(f"Borrados del valor 5: {borrados_5} -> Lista restante: {lista_borrar.a_lista()}")

# EJERCICIO: Implementar el método contar() en ListaEnlazada para recorrer secuencialmente los nodos sin depender de self.cantidad, añadiendo una auditoría de integridad.

# 1. Análisis del problema
# Datos de entrada: Una lista enlazada con cero, uno o múltiples nodos enlazados a partir de self.head.
# Procesamiento: Iterar por toda la cadena de enlaces desde la cabecera hasta None incrementando un contador por cada nodo visitado sin leer self.cantidad, e incorporar un método que contraste este conteo real contra self.cantidad.
# Resultado esperado: Número efectivo de nodos obtenidos por recorrido y diagnóstico de consistencia de self.cantidad.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En contar(), inicializar contador = 0 y actual = self.head
# Mientras actual exista, incrementar contador y avanzar a actual.next
# Incorporar verificar_cantidad() para cotejar contar() frente a self.cantidad
# Validar tras inserciones y borrados que ambas cifras concuerden

# 3. Identificación de la lógica
# Contabilizar mediante recorrido de enlaces audita la estructura efectiva en memoria al margen del atributo cantidad.
# Una discrepancia entre contar() y self.cantidad evidencia que alguna operación modificadora omitió actualizar el contador.
# Finalizar la iteración cuando actual is None gestiona limpiamente tanto colecciones vacías como extensas.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Método contar() que recorre secuencialmente los enlaces desde la cabecera sin consultar self.cantidad
    def contar(self):
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    # Método verificar_cantidad() para auditar si el recorrido coincide con el atributo self.cantidad
    def verificar_cantidad(self):
        real = self.contar()
        return real == self.cantidad, real, self.cantidad

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista = ListaEnlazada()
print("Lista vacía -> contar():", lista.contar(), "| verificar:", lista.verificar_cantidad())

for valor in [10, 20, 30, 40]:
    lista.insertar_final(valor)

print("Lista:", lista.a_lista())
print("Total contando nodos:", lista.contar())

# Validar que el atributo self.cantidad concuerde con el conteo efectivo de nodos
coincide, real, guardada = lista.verificar_cantidad()
print(f"¿Coincide con self.cantidad? {coincide} (real: {real}, guardada: {guardada})")

# EJERCICIO: Incorporar en ListaEnlazada el método mayor() para devolver el elemento máximo de la colección o None si carece de nodos, añadiendo la búsqueda del mínimo.

# 1. Análisis del problema
# Datos de entrada: Una lista enlazada con datos comparables (o vacía).
# Procesamiento: Iterar desde la cabecera rastreando el valor máximo hallado y retornar None ante una lista vacía, incorporando además el método menor() para extraer también el valor mínimo.
# Resultado esperado: El elemento máximo de la lista (o None si está vacía) junto con el elemento mínimo como métrica adicional en pantalla.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En mayor(), retornar None si self.head es None
# Asignar maximo = self.head.data e iterar sobre los nodos sucesivos con actual = self.head.next
# Si actual.data > maximo, actualizar maximo y desplazarse mediante actual.next
# Incorporar el método menor() bajo la misma lógica para hallar el valor mínimo
# Validar con una instancia vacía y otra poblada con enteros positivos y negativos

# 3. Identificación de la lógica
# Inicializar la referencia con el dato de la cabecera evita recurrir a cotas artificiales y soporta correctamente valores negativos.
# Avanzar nodo a nodo mediante actual.next permite determinar los extremos en una sola pasada lineal sin transformar la estructura.
# Retornar None cuando self.head es None expresa de forma inequívoca la ausencia de elementos.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de mayor() iterando sobre los nodos para retornar el valor máximo o None si está vacía
    def mayor(self):
        if self.head is None:
            return None

        maximo = self.head.data
        actual = self.head.next

        while actual is not None:
            if actual.data > maximo:
                maximo = actual.data
            actual = actual.next

        return maximo

    # Implementación complementaria de menor() para extraer el valor mínimo de la colección o None si está vacía
    def menor(self):
        if self.head is None:
            return None

        minimo = self.head.data
        actual = self.head.next

        while actual is not None:
            if actual.data < minimo:
                minimo = actual.data
            actual = actual.next

        return minimo

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista_vacia = ListaEnlazada()
print("Lista vacía -> mayor():", lista_vacia.mayor())

lista = ListaEnlazada()
for valor in [12, -5, 48, 27, 48, 9]:
    lista.insertar_final(valor)

print("Lista:", lista.a_lista())
print("Dato más grande (mayor()):", lista.mayor())

# Desplegar también el valor mínimo obtenido mediante menor()
print("Dato más pequeño (menor()):", lista.menor())

# EJERCICIO: Desarrollar el método eliminar_final() en ListaEnlazada para extraer el último nodo y devolver su valor, cubriendo listas vacías y de un único elemento, más una función de vaciado.

# 1. Análisis del problema
# Datos de entrada: Una lista enlazada (vacía, unitaria o con múltiples nodos).
# Procesamiento: Retornar None si está vacía; si posee un único nodo, extraer su dato, anular self.head y decrementar cantidad; si tiene varios, desplazarse hasta el penúltimo nodo, rescatar el valor del último, cortar el enlace con penultimo.next = None y restar 1 a cantidad; incluir además un método para vaciar toda la colección devolviendo el total purgado.
# Resultado esperado: Dato extraído del último nodo (o None si estaba vacía), estado resultante de la lista y conteo al vaciarla.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En eliminar_final(), comprobar si self.head es None para retornar None
# Comprobar si self.head.next es None: rescatar dato, anular self.head, restar cantidad y devolver dato
# Si existen múltiples nodos, avanzar actual hasta que actual.next.next sea None, rescatar actual.next.data, anular actual.next y restar cantidad
# Incorporar vaciar() para descartar todos los nodos simultáneamente y retornar la cantidad previa
# Validar con lista vacía, unitaria, múltiple y ejecución de vaciar()

# 3. Identificación de la lógica
# Suprimir el nodo terminal en una lista simplemente enlazada requiere posicionarse en el nodo predecesor para anular su puntero next.
# Manejar por separado los casos de lista vacía y unitaria previene accesos a atributos nulos o referencias colgantes en self.head.
# Decrementar self.cantidad en cada extracción mantiene sincronizado el tamaño de la estructura.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de eliminar_final() cubriendo lista vacía, lista unitaria y lista con múltiples nodos
    def eliminar_final(self):
        if self.head is None:
            return None

        if self.head.next is None:
            dato = self.head.data
            self.head = None
            self.cantidad = self.cantidad - 1
            return dato

        actual = self.head
        while actual.next.next is not None:
            actual = actual.next

        dato = actual.next.data
        actual.next = None
        self.cantidad = self.cantidad - 1
        return dato

    # Método complementario para purgar todos los nodos de la colección y devolver cuántos se descartaron
    def vaciar(self):
        eliminados = self.cantidad
        self.head = None
        self.cantidad = 0
        return eliminados

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista_vacia = ListaEnlazada()
print("Lista vacía -> eliminar_final():", lista_vacia.eliminar_final())

lista_uno = ListaEnlazada()
lista_uno.insertar_final("Solo")
print("Un solo nodo antes:", lista_uno.a_lista(), "| eliminado:", lista_uno.eliminar_final(),
      "| después:", lista_uno.a_lista(), "| cantidad:", lista_uno.cantidad)

lista = ListaEnlazada()
for valor in [10, 20, 30, 40]:
    lista.insertar_final(valor)

print("\nLista inicial:", lista.a_lista())
print("Eliminado al final:", lista.eliminar_final())
print("Lista tras eliminar_final():", lista.a_lista(), "| cantidad:", lista.cantidad)

# Validar vaciar() para purgar los elementos restantes y verificar el conteo eliminado
quitados = lista.vaciar()
print(f"Vaciando lista: se eliminaron {quitados} nodos -> Lista: {lista.a_lista()}, cantidad: {lista.cantidad}")

# EJERCICIO: Incorporar en ListaEnlazada el método insertar_despues(referencia, data) para localizar la primera coincidencia de referencia y enlazar un nuevo nodo a continuación, notificando si no existe y añadiendo insertar_antes().

# 1. Análisis del problema
# Datos de entrada: Un valor objetivo de referencia y el nuevo dato a insertar inmediatamente después de su primera aparición.
# Procesamiento: Recorrer desde la cabeza hasta hallar el primer nodo con valor igual a referencia; al ubicarlo, instanciar el nodo, apuntar su next al sucesor actual, enlazar el nodo referencia hacia el nuevo nodo e incrementar cantidad; si no se encuentra, emitir aviso sin alterar la lista; añadir también insertar_antes() para inserción previa.
# Resultado esperado: Lista actualizada tras la inserción posterior (o anterior), notificación si la referencia no existe y retorno booleano de estado.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En insertar_despues(referencia, data), iniciar actual = self.head e iterar mientras actual exista
# Si actual.data == referencia, crear nuevo = Nodo(data), enlazar nuevo.next = actual.next y actual.next = nuevo, incrementar cantidad y devolver True
# Si finaliza el recorrido sin coincidencias, imprimir notificación y devolver False
# Incorporar insertar_antes(referencia, data) para enlazar un nodo justo antes de la primera aparición
# Validar insertando tras nodos intermedios, tras el nodo final y ante una referencia inexistente

# 3. Identificación de la lógica
# Enlazar un nodo tras otro localizado exige asignar primero nuevo.next = actual.next para no perder la conexión con el resto de la lista.
# Retornar inmediatamente tras hallar la primera coincidencia garantiza que la inserción afecte solo a la primera ocurrencia.
# Devolver un valor booleano junto con el mensaje informativo facilita tanto la retroalimentación al usuario como las aserciones de prueba.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de insertar_despues(referencia, data) ubicando la primera ocurrencia y notificando si no existe
    def insertar_despues(self, referencia, data):
        actual = self.head

        while actual is not None:
            if actual.data == referencia:
                nuevo = Nodo(data)
                nuevo.next = actual.next
                actual.next = nuevo
                self.cantidad = self.cantidad + 1
                return True
            actual = actual.next

        print(f"Aviso: la referencia '{referencia}' no existe en la lista.")
        return False

    # Método complementario para enlazar un nuevo nodo inmediatamente antes de la primera aparición de referencia
    def insertar_antes(self, referencia, data):
        if self.head is None:
            print(f"Aviso: la referencia '{referencia}' no existe en la lista.")
            return False

        if self.head.data == referencia:
            nuevo = Nodo(data)
            nuevo.next = self.head
            self.head = nuevo
            self.cantidad = self.cantidad + 1
            return True

        actual = self.head
        while actual.next is not None:
            if actual.next.data == referencia:
                nuevo = Nodo(data)
                nuevo.next = actual.next
                actual.next = nuevo
                self.cantidad = self.cantidad + 1
                return True
            actual = actual.next

        print(f"Aviso: la referencia '{referencia}' no existe en la lista.")
        return False

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista = ListaEnlazada()
for valor in ["A", "B", "C", "B", "D"]:
    lista.insertar_final(valor)

print("Lista inicial:", lista.a_lista(), "| cantidad:", lista.cantidad)

# Insertar a continuación de la primera ocurrencia de "B"
lista.insertar_despues("B", "X")
print("Tras insertar_despues('B', 'X'):", lista.a_lista(), "| cantidad:", lista.cantidad)

# Insertar a continuación del nodo terminal "D"
lista.insertar_despues("D", "Z")
print("Tras insertar_despues('D', 'Z'):", lista.a_lista(), "| cantidad:", lista.cantidad)

# Validar el comportamiento y aviso ante una referencia ausente
lista.insertar_despues("NO_EXISTE", "Y")

# Caso de prueba para insertar_antes ubicando un nodo previo a una referencia válida
lista.insertar_antes("C", "W")
print("Tras insertar_antes('C', 'W'):", lista.a_lista(), "| cantidad:", lista.cantidad)

# EJERCICIO: Desarrollar el método desde_final(k) en ListaEnlazada para obtener el dato en la k-ésima posición desde el extremo final (k=1 corresponde al último) sin usar cantidad, más acceso desde el inicio.

# 1. Análisis del problema
# Datos de entrada: Un entero positivo k (donde k=1 designa al último nodo, k=2 al penúltimo, etc.) sobre una lista enlazada.
# Procesamiento: Emplear la técnica de dos punteros (rapido y lento) distanciados por k posiciones sin consultar self.cantidad para localizar el nodo objetivo y devolver su dato, retornando None si k está fuera de rango; incorporar también desde_inicio(k) para acceso directo desde la cabecera.
# Resultado esperado: Valor almacenado a k posiciones desde el final (o None si es inválido) y contraste con la consulta desde el inicio.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En desde_final(k), comprobar k >= 1 y que self.head exista
# Adelantar el puntero rapido k posiciones; si alcanza None prematuramente, retornar None
# Desplazar rapido y lento simultáneamente hasta que rapido sea None; lento apuntará al nodo buscado
# Incorporar desde_inicio(k) para obtener el k-ésimo elemento partiendo desde la cabecera (k=1 es el primero)
# Validar con diversos valores de k e imprimir los resultados

# 3. Identificación de la lógica
# Conservar una brecha constante de k nodos entre dos punteros resuelve la búsqueda inversa en una sola pasada lineal sin conocer la longitud total.
# Al alcanzar el puntero adelantado el extremo final (None), el puntero rezagado queda posicionado exactamente a k nodos del final.
# Validar índices no positivos o mayores que la longitud evita accesos nulos por desbordamiento.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de desde_final(k) mediante dos punteros sin consultar self.cantidad (k=1 es el último)
    def desde_final(self, k):
        if k <= 0 or self.head is None:
            return None

        rapido = self.head
        for _ in range(k):
            if rapido is None:
                return None
            rapido = rapido.next

        lento = self.head
        while rapido is not None:
            rapido = rapido.next
            lento = lento.next

        return lento.data

    # Método complementario para consultar el k-ésimo nodo partiendo desde la cabecera (k=1 es el primero)
    def desde_inicio(self, k):
        if k <= 0 or self.head is None:
            return None

        actual = self.head
        pasos = 1
        while actual is not None and pasos < k:
            actual = actual.next
            pasos += 1

        if actual is None:
            return None
        return actual.data

    def a_lista(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.data)
            actual = actual.next
        return elementos


# --- Ejemplos de ejecución ---
lista = ListaEnlazada()
for valor in [10, 20, 30, 40, 50]:
    lista.insertar_final(valor)

print("Lista:", lista.a_lista())
print("k=1 desde el final (último):", lista.desde_final(1))
print("k=2 desde el final (penúltimo):", lista.desde_final(2))
print("k=5 desde el final (primero):", lista.desde_final(5))
print("k=6 desde el final (fuera de rango):", lista.desde_final(6))
print("k=0 desde el final (inválido):", lista.desde_final(0))

# Caso de prueba con desde_inicio(k) para contrastar la indexación desde la cabecera
print("\nk=2 desde el inicio:", lista.desde_inicio(2))

# EJERCICIO: Incorporar en ListaEnlazada el método tiene_ciclo() aplicando el algoritmo de detección de ciclos de Floyd (tortuga y liebre), más la localización del nodo inicial del bucle.

# 1. Análisis del problema
# Datos de entrada: Una lista enlazada lineal (terminada en None) o circularizada mediante un enlace hacia un nodo previo.
# Procesamiento: Desplazar desde la cabeza un puntero lento de un paso y uno rápido de dos pasos; si llegan a coincidir existe ciclo (True), mientras que si el rápido alcanza None no hay ciclo (False); añadir además inicio_ciclo() para identificar el nodo donde comienza el bucle.
# Resultado esperado: Confirmación booleana de existencia de ciclo y, en caso afirmativo, el dato del nodo de entrada al ciclo.

# 2. Diseño en pseudocódigo
# Declarar Nodo y ListaEnlazada con head y cantidad
# En tiene_ciclo(), inicializar lento = self.head y rapido = self.head
# Mientras rapido y rapido.next existan, avanzar lento un nodo y rapido dos nodos
# Si lento is rapido, retornar True; al concluir el bucle sin colisión, retornar False
# Incorporar inicio_ciclo() para determinar el primer nodo perteneciente al bucle cuando exista
# Validar sobre una lista acíclica y otra con un enlace circular forzado

# 3. Identificación de la lógica
# En ausencia de ciclos, el puntero rápido alcanza el final (None) de forma determinista.
# Si existe un bucle, ambos punteros quedan atrapados en él y la diferencia de velocidad garantiza que el rápido alcance al lento.
# Detectar ciclos previene iteraciones infinitas en recorridos de lectura o conteo.

# 4. Implementación en Python

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad = self.cantidad + 1

    # Implementación de tiene_ciclo() mediante el algoritmo de Floyd (punteros lento y rápido)
    def tiene_ciclo(self):
        lento = self.head
        rapido = self.head

        while rapido is not None and rapido.next is not None:
            lento = lento.next
            rapido = rapido.next.next
            if lento is rapido:
                return True

        return False

    # Método complementario para localizar el dato del nodo donde se origina el ciclo si existe
    def inicio_ciclo(self):
        lento = self.head
        rapido = self.head
        hay_ciclo = False

        while rapido is not None and rapido.next is not None:
            lento = lento.next
            rapido = rapido.next.next
            if lento is rapido:
                hay_ciclo = True
                break

        if not hay_ciclo:
            return None

        lento = self.head
        while lento is not rapido:
            lento = lento.next
            rapido = rapido.next

        return lento.data


# --- Ejemplos de ejecución ---
lista_normal = ListaEnlazada()
for x in [10, 20, 30, 40]:
    lista_normal.insertar_final(x)

print("Lista normal -> tiene_ciclo():", lista_normal.tiene_ciclo())
print("Lista normal -> inicio_ciclo():", lista_normal.inicio_ciclo())

# Construir una lista cíclica conectando el último nodo de vuelta hacia el nodo con valor 20
lista_ciclo = ListaEnlazada()
for x in [10, 20, 30, 40]:
    lista_ciclo.insertar_final(x)

nodo_20 = lista_ciclo.head.next
ultimo = lista_ciclo.head
while ultimo.next is not None:
    ultimo = ultimo.next
ultimo.next = nodo_20  # Enlace circular generado manualmente para efectos de prueba

print("\nLista con ciclo -> tiene_ciclo():", lista_ciclo.tiene_ciclo())
# Desplegar el valor del nodo donde comienza el bucle detectado
print("Lista con ciclo -> inicio_ciclo():", lista_ciclo.inicio_ciclo())
