# import numpy as np

# def simular_eventos_poisson(T, lambda_):
#     num_eventos = np.random.poisson(lambda_ * T)
#     tiempos_eventos = np.random.uniform(0, T, num_eventos)
#     tiempos_eventos.sort()

    
#     for tiempo in tiempos_eventos:
#         print(f"Evento ocurre en el tiempo: {tiempo}")

#     print(len(tiempos_eventos))

# # Ejemplo de uso
# T =  10  # Período de tiempo en unidades de tiempo
# lambda_ =  2  # Tasa de eventos por unidad de tiempo
# simular_eventos_poisson(T, lambda_)


from heapq import heapify,heappop,heappush

l=[2,23,-2,2,3,5,6,7]

print('a')
heapify(l)
print(l)
while l:
    print(heappop(l))