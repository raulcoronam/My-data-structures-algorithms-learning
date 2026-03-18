# 📂 Arrays (Arreglos) y la Memoria

Para entender cómo funcionan las estructuras de datos, primero debemos entender dónde viven: la memoria de la computadora.

---

## 1. La Base Física: Memoria RAM

**RAM** significa *Random Access Memory* (Memoria de Acceso Aleatorio). El término "aleatorio" es clave aquí: significa que podemos acceder a cualquier parte (una locación "random") de la memoria en tiempo constante, es decir, de forma instantánea.

### ¿Qué es una estructura de datos?
Es, fundamentalmente, una forma de estructurar, organizar y gestionar datos. Estos datos estarán siendo estructurados dentro de la RAM. La RAM es donde todas nuestras variables de nuestros programas serán almacenadas. Inclusive si no sabemos qué tipo de datos o qué tipo de estructura utilizaremos, hay una certeza absoluta: **vivirán en la RAM**.

### Unidades de Medida en la RAM
La RAM está medida en **Bytes**. Para entender su escala:

* **1 Bit**: Puede ser pensado como una posición que puede almacenar un solo dígito, pero con una restricción estricta: dicho dígito solo puede ser 0 o 1. Los ceros y unos son el lenguaje máquina.
* **1 Byte** = 8 bits. Bits individuales conforman bytes, que a su vez conforman la memoria RAM.
* **Gigabyte (GB)**: $1 \text{ GB} = 10^9 \text{ Bytes}$ (aproximadamente mil millones de bytes).

### Almacenamiento de Datos
Usualmente, para almacenar un número entero (**Integer**) en la RAM, la computadora destina **4 bytes** (es decir, 32 bits). Si se quiere almacenar el número 1, en lenguaje binario serían 31 ceros seguidos de un uno (`00000000 00000000 00000000 00000001`).

En la RAM se almacenarán estos valores y cada valor tendrá una locación distinta llamada **"Address"** (Dirección de memoria). Es decir, cada valor tiene su propia "dirección de casa" única dentro de la enorme ciudad que es la RAM.

---

## 2. Estructuras Contiguas: Arrays (Arreglos)

Un arreglo es una estructura de datos ordenada que permite almacenar distintos valores en la RAM, pero con una regla de oro: **de manera contigua** (uno exactamente al lado del otro, sin espacios vacíos entre ellos).

| Tipo de Dato | Tamaño | Ejemplo de Índices/Address |
| :--- | :--- | :--- |
| **Enteros (Integer)** | 4 bytes | Address: 0, 4, 8... |
| **Caracteres (ASCII)** | 1 byte | Address: 0, 1, 2... |

> **Ejemplo con Enteros:** Si almacenaras un arreglo con los números `[1, 3, 5]`, los valores de sus address iniciales serían 0, 4 y 8 respectivamente.

---

## 3. Static Arrays (Arreglos Estáticos)

Definiendo a un array como un bloque contiguo de datos, los arreglos estáticos tienen una característica principal: tienen un **tamaño fijo (Fixed Size)**. Tienes que decirle a la computadora desde el principio cuántos espacios vas a necesitar.

*(Nota: Lenguajes como Python o JavaScript utilizan Dynamic Arrays de forma nativa).*

### Operaciones Comunes
1.  **Lectura de datos**: La computadora accede mediante índices. El primer índice siempre es el **índice 0**. Eficiencia: **$O(1)$** (Tiempo Constante).
2.  **Escritura y Modificación**: Sobrescribir un dato existente es **$O(1)$**.
3.  **Insertar desplazando elementos**: Si queremos insertar al inicio, debemos mover todos los elementos una posición a la derecha. Eficiencia: **$O(n)$** (Tiempo Lineal).

### Diferencia clave: Length vs Size
* **Length (Largo)**: Número de elementos reales que nos importan.
* **Size/Capacity (Tamaño)**: Número total de espacios reservados en memoria (incluyendo los vacíos o "0").

---

## 4. Dynamic Arrays (Arreglos Dinámicos)

Solucionan el problema del tamaño fijo (ej. `list` en Python). No requieren especificar el tamaño al crearlos.

### ¿Cómo crecen?
Cuando el array se llena (**Length == Size**):
1.  Crea un nuevo arreglo en otra parte de la RAM.
2.  **Duplica su tamaño** (Capacidad).
3.  Copia los elementos del arreglo viejo al nuevo.
4.  Libera la memoria del arreglo anterior.

### Complejidad Amortizada
Relocalizar el array es una operación **$O(n)$**. Sin embargo, al duplicar el tamaño, evitamos hacer esta operación costosa en cada inserción. En promedio, la adición de un elemento al final se considera **$O(1)$ amortizado**.

---

## 5. Stack (Pila)

Los Dynamic Arrays son ideales para construir un **Stack**. Es una estructura conceptual que restringe la interacción mediante la regla **LIFO (Last In, First Out)**.

### Operaciones Principales
* **Push**: Agrega un elemento a la cima (top). Complejidad: **$O(1)$**.
* **Pop**: Elimina y retorna el último elemento de la cima. Complejidad: **$O(1)$**.
* **Peek (o Top)**: Observa el elemento de la cima sin removerlo. Complejidad: **$O(1)$**.

> **Analogía:** Una pila de platos para lavar. Solo puedes interactuar con el plato que está arriba de todo sin arriesgarte a que los demás se caigan.
