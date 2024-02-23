from inventory.inventory_simulation import InventoryConfig, inventory_simulation
import numpy as np

config1=InventoryConfig(10, 10, 100, 10, lambda x: 10*x, lambda x: 10*x)
config2=InventoryConfig(20, 10, 100, 10, lambda x: 10*x, lambda x: 4*x)

# dist1=np.random.normal(10, 1)

# initial_cants=[100, 100]
# initial_money=10

# time=1000

# inventory_simulation(time, lambda: , [config1, config2], [lambda: 10, lambda: 10], initial_cants, initial_money)

# print(np.random.normal(10))