# Proyecto: Simulación de Eventos Discretos

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

## Introducción

- Breve descripción del proyecto

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

- Objetivos y metas

- El sistema específico a simular. ¿Qué es lo que se está simulando?

Para satisfacer las demandas, el tendero debe mantener una cantidad del producto a mano, y siempre que el inventario a mano se vuelve bajo, se ordenan unidades adicionales al distribuidor. El tendero utiliza una política de pedido llamada (s, S); es decir, siempre que el inventario a mano es menor que s y no hay un pedido pendiente, entonces se ordena una cantidad para llevarlo hasta S, donde $s<S$. Es decir, si el nivel de inventario actual es x y no hay un pedido pendiente, entonces si $x<s$ se ordena la cantidad S−x.
El costo de pedir y unidades del producto es una función especificada c(y), y toma L unidades de tiempo hasta que se entrega el pedido, con el pago realizado a la entrega. Además, la tienda paga un costo de mantenimiento de inventario de h por unidad de artículo por unidad de tiempo.
Supongamos además que siempre que un cliente demanda más del producto de lo que está disponible actualmente, entonces se vende la cantidad a mano y el resto del pedido se pierde para la tienda. 

El tendero está interesado en determinar el costo total esperado por unidad de tiempo para satisfacer la demanda del producto.

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

## S2 Detalles de Implementación

- Pasos seguidos para la implementación

## S3 Resultados y Experimentos

- Hallazgos de la simulación
- Interpretación de los resultados
- Necesidad de realizar el análisis estadístico de la simulación (Variables de interés)
- Análisis de parada de la simulación

## S4 Modelo Matemático

- Descripción del modelo de simulación
- Supuestos y restricciones
