# 📚 **Linked Lists y Queues**

## 1. ***Introducción a las Linked Lists (Listas Enlazadas o encadenadas)***

A diferencia de los Arrays, donde los elementos se guardan en bloques de memoria contiguos (uno al lado del otro), una Linked List es una colección lineal de elementos llamados Nodos, los cuales pueden estar dispersos en diferentes partes de la memoria.

### El Nodo: La unidad básica

Un nodo es un objeto que actúa como un contenedor con dos compartimentos:

1. **Value** (Dato): El valor que queremos guardar (int, str, bool, etc.).
2. **Next** (Puntero/Referencia): Una flecha que apunta a la ubicación del siguiente nodo en la secuencia. Si no hay más nodos, apunta a *None (null)*.

### Implementación en Python

```Python

class ListNode:
    def __init__(self, val):
        self.val = val     # Almacena el valor
        self.next = None   # Referencia al siguiente nodo (inicialmente vacía)

# Conexión manual de nodos
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3
# node3.next sigue siendo None, marcando el fin de la lista.

```

## 2. ***Singly Linked Lists (Listas Simplemente Enlazadas)***
En esta variante, la navegación es unidireccional (solo hacia adelante).

En una *Singly List* tenemos un **head pointer** que apunta hacia un nodo (la cabeza de la fila), el cuál a su vez apunta hacia el siguiente nodo, 
el cuál apunta hacia el siguiente nodo, hasta llegar a aquel nodo que no apunta hacia nada (es decir, su *next es = null*)

### Recorrido (Traversal)
Para leer una lista, empezamos desde la "Cabeza" (Head) y saltamos de nodo en nodo usando el puntero next hasta llegar a None.

```Python

cur = node1
while cur:
    print(cur.val)
    cur = cur.next # Movemos el puntero al siguiente nodo
```

### Operaciones Principales

- ***Inserción*** *(O(1)*): Si ya tenemos la referencia al nodo previo, insertar es tan simple como cambiar a dónde apuntan las "flechas". No hay que mover el resto de los elementos (como ocurriría en un array).
- ***Eliminación*** *(O(1)*): Para borrar el node2, hacemos que node1.next apunte directamente a node3.Comando: node1.next = node1.next.next

- ***Casos Especiales***:
	- **Circular Linked List**: Ocurre cuando el next del último nodo apunta de regreso al primer nodo (Head) en lugar de a None.

## 3. ***Doubly Linked Lists (Listas Doblemente Enlazadas)***

Aquí, cada nodo es más "inteligente" porque conoce quién está adelante y quién está atrás.

### Estructura del Nodo Doble
Tiene tres atributos: *val, next (siguiente) y prev (anterior).*

### Ventajas y Desventajas

- **Pro**: Puedes recorrer la lista en ambas direcciones (hacia adelante y hacia atrás).
- **Pro**: Eliminar un nodo es más fácil porque el nodo sabe quién es su antecesor sin tener que buscarlo desde el inicio.
- **Con**: Consume más memoria (un puntero extra por cada nodo).

### Operaciones de Inserción y Eliminación

Para mantener la integridad, siempre debemos actualizar ambos punteros:

|Operación|Lógica Clave|
|---------|------------|
|Insertar al Final|```tail.next = newNode, newNode.prev = tail, tail = newNode```|
|Borrar al Final|```newTail = tail.prev, newTail.next = None, tail = newTail```|
|Acceso/Búsqueda|Sigue siendo *O(n)* porque no hay índices directos.|

## 4. ***Queues (Colas)***

Una Queue es una estructura de datos que sigue el principio FIFO (First In, First Out): El primero en llegar es el primero en salir.

### Operaciones Fundamentales

***Enqueue (Encolar)***: Agregar un elemento al final (Rear/Right).

***Dequeue (Desencolar)***: Eliminar y retornar el elemento del frente (Front/Left).

### Implementación Óptima con Linked List

Usar una Linked List para una Queue permite que ambas operaciones sean $O(1)$, manteniendo una referencia al inicio (head o left) y al final (tail o right).

```Python

class Queue:
    def __init__(self):
        self.left = None   # Frente de la cola
        self.right = None  # Final de la cola

    def enqueue(self, val):
        newNode = ListNode(val)
        if self.right: # Si la cola no está vacía
            self.right.next = newNode
            self.right = newNode
        else: # Si la cola está vacía
            self.left = self.right = newNode

    def dequeue(self):
        if not self.left: # Caso: Cola vacía
            return None
        
        val = self.left.val
        self.left = self.left.next # El frente ahora es el siguiente
        if not self.left: # Si al quitarlo la cola quedó vacía
            self.right = None
        return val

```

### ***Variación: Deque (Double-ended Queue)***

Se pronuncia "deck". Es una cola híbrida que permite push y pop tanto por el frente como por el final, todo en tiempo constante $O(1)$. Es ideal para algoritmos de grafos como BFS (Breadth-First Search).

### 📊 ***Tabla Comparativa de Complejidad (Big O)***

|Operación|Array (Dinámico)|Singly Linked List|Doubly Linked List|
|:--------|:---------------|:-----------------|:-----------------|
|Acceso|O(1)|O(n)|O(n)|
|Búsqueda|O(n)|O(n)|O(n)|
|Insertar Inicio|O(n)|O(1)|O(1)|
|Insertar Final|O(1) amortizado|O(1) (con puntero tail)|O(1)|
|Eliminar Inicio |O(n)|O(1)|O(1)|

**Nota Crítica**: Las Linked Lists son superiores en inserciones y eliminaciones frecuentes, pero fallan en acceso aleatorio. Si necesitas leer el elemento en la posición 500 rápidamente, usa un Array. Si necesitas estar metiendo y sacando gente de una fila constantemente, usa una Queue/Linked List.
