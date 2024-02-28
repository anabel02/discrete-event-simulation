# Proyecto: Simulación de Eventos Discretos

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos
fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar
y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

## Introducción

- Breve descripción del proyecto

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos
fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar
y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

- Objetivos y metas

- El sistema específico a simular. ¿Qué es lo que se está simulando?

Para satisfacer las demandas, el tendero debe mantener una cantidad del producto a mano, y siempre que el inventario a
mano se vuelve bajo, se ordenan unidades adicionales al distribuidor. El tendero utiliza una política de pedido
llamada (s, S); es decir, siempre que el inventario a mano es menor que s y no hay un pedido pendiente, entonces se
ordena una cantidad para llevarlo hasta S, donde $s<S$. Es decir, si el nivel de inventario actual es x y no hay un
pedido pendiente, entonces si $x<s$ se ordena la cantidad S−x.
El costo de pedir y unidades del producto es una función especificada c(y), y toma L unidades de tiempo hasta que se
entrega el pedido, con el pago realizado a la entrega. Además, la tienda paga un costo de mantenimiento de inventario de
h por unidad de artículo por unidad de tiempo.
Supongamos además que siempre que un cliente demanda más del producto de lo que está disponible actualmente, entonces se
vende la cantidad a mano y el resto del pedido se pierde para la tienda.

El tendero está interesado en determinar el costo total esperado por unidad de tiempo para satisfacer la demanda del
producto.

- Parámetros del sistema
    - Tiempo máximo de la simulación (tmax)
    - Distribución del tiempo entre llegadas de los clientes (T)
    - Distribución de la demanda de los clientes para cada producto (D)
    - s, S, L, h, c(y) para cada producto,
      s_i es el nivel mínimo que debe alcanzar el producto i,
      S_i es el nivel máximo que debe alcanzar el producto i,
      L_i es el tiempo que toma en llegar el pedido del producto i,
      h_i es el costo de mantenimiento de inventario por unidad de artículo por unidad de tiempo,
      c_i(y) es el costo de pedir y unidades del producto i.
    - Cantidad inicial de inventario (I0)
    - Cantidad inicial de dinero (M0)

- Variables de interés
    - Tiempo esperado en el que la ganancia supera una cantidad  (esta cantidad pudiera ser la inversión inicial)
    - Tiempo esperado en que el negocio quiebra (se queda sin dinero)
    - Costo total esperado por unidad de tiempo para satisfacer la demanda del producto

## Detalles de Implementación

En el directorio source se encuentran los archivos que contienen el código fuente de la simulación. El archivo `main.py`
es el punto de entrada de la simulación.
El módulo `simulation` contiene una abstractación de la simulación, y el módulo `inventory` contiene la implementación
para nuestro problema específico.

### simulation

En `core.py` encontramos:

- La clase `Event` que representa un evento en la simulación. Cada evento tiene un tiempo asociado y una
  función `action` que ejecuta el evento.
- La clase `State` que representa el estado de la simulación.
- La clase `ActionByTime` que representa una acción que se ejecutará antes de cada evento programado.

En `simulator.py` encontramos:

- La función `simulation` que recibe como parámetros una cola con prioridad de eventos, una instancia de ActionByTime,
  el estado
  inicial de la simulación, el tiempo máximo de la simulación y una función que determina si la simulación debe
  detenerse. La función ejecuta la simulación de la siguiente manera:
  Mientras haya eventos en la cola, se extrae el primer evento, si el tiempo del evento es menor o igual al tiempo
  máximo de la simulación, se ejecuta la acción de ActionByTime, luego se revisa si se cumple el caso de parada, en caso
  negativo se ejecuta el evento y se actualiza el estado de la simulación, y se vuelve a revisar si se cumple el caso de
  parada con este nuevo estado.
  La simulación se detiene por alguno de los siguientes 3 motivos:
- Se alcanza el tiempo máximo de la simulación.
- Se cumple el caso de parada definido en stop_case
- Se terminan los eventos programados.

### inventory

Contiene la implementación específica de `simulation` para el problema de inventario.

En `inventory.py` se definen:

- La clase `InventoryState` que representa el estado del inventario.
- La clase `RefillEvent` que representa el evento de reabastecimiento del inventario.
- La clase `SaleEvent` que representa el evento de venta de un producto.
- La clase `InventoryConfig` que representa la configuración del inventario.
- La clase `ActionByTimeInventory` que representa la característica de nuestro problema de pagar el costo de
  mantenimiento de inventario por unidad de artículo por unidad de tiempo.

En `inventory_simulation.py` se define:

- La función `inventory_simulation` que recibe como parámetros el tiempo máximo de la simulación, la distribución del
  tiempo entre llegadas de los clientes, la lista con configuraciones del inventario, la distribución de la demanda de
  los clientes
  para cada producto, la cantidad inicial de cada producto en el inventario, la cantidad inicial de dinero y una función
  que determina si
  la simulación debe detenerse.
  La función primeramente verifica la consistencia de los parámetros (revisa que las listas que describen los productos
  tengan igual tamaño), luego inicializa el estado de la simulación, crea la cola con prioridad de eventos y ejecuta la
  simulación descrita en el módulo anterior.

- ¿Cómo se crea la cola de eventos?
  Se inicializa una lista vacía.
  Por cada producto en la lista de configuraciones del inventario, se agregan eventos de venta hasta que el tiempo del
  evento sea mayor al tiempo máximo de la simulación.
  Se ordena la lista de eventos por tiempo y se devuelve.

## Resultados y Experimentos

- Hallazgos de la simulación
- Interpretación de los resultados
- Necesidad de realizar el análisis estadístico de la simulación (Variables de interés)
- Análisis de parada de la simulación

## Modelo Matemático

- Descripción del modelo de simulación
- Supuestos y restricciones
