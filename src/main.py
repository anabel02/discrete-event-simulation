from inventory.inventory_simulation import InventoryConfig, inventory_simulation
import numpy as np

config1 = InventoryConfig(10, 10, 100, 10, lambda x: 10*x, lambda x, y: 10*x*y)
config2 = InventoryConfig(20, 10, 100, 10, lambda x: 10*x, lambda x, y: 4*x*y)


def dist1(): return np.random.randint(1, 10)
def dist2(): return np.random.randint(2, 24)


def time_dist(): return np.random.poisson(10)


initial_cants = [100, 100]
initial_money = 10

time = 1000

inventory_simulation(time, time_dist, [config1, config2], [
                     dist1, dist2], initial_cants, initial_money)

# print(np.random.normal(10))
