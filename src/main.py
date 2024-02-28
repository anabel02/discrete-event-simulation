from inventory.inventory_simulation import InventoryConfig, inventory_simulation
import numpy as np

price_product1 = 10
price_product2 = 4

s_product1 = 7
s_product2 = 5

S_product1 = 100
S_product2 = 70

refill_interval_product1 = 10
refill_interval_product2 = 7

refill_cost_product1 = lambda x: 10*x
refill_cost_product2 = lambda x: 6*x

inventory_cost_product1 = lambda x, y: 10*x*y
inventory_cost_product2 = lambda x, y: 4*x*y

config_product1 = InventoryConfig(price_product1, s_product1, S_product1, refill_interval_product1, refill_cost_product1, inventory_cost_product1)
config_product2 = InventoryConfig(price_product2, s_product2, S_product2, refill_interval_product2, refill_cost_product2, inventory_cost_product2)
configs = [config_product1, config_product2]

demand_dist_product1 = lambda: np.random.randint(1, 10)
demand_dist_product2 = lambda: np.random.randint(2, 24)
demand_dists = [demand_dist_product1, demand_dist_product2]

initial_cant_product1 = 100
initial_cant_product2 = 70
initial_cants = [initial_cant_product1, initial_cant_product2]

max_time = 24 * 7 * 4

time_dist = lambda: np.random.exponential(8)

initial_money = 300


inventory_simulation(max_time, time_dist, configs, demand_dists, initial_cants, initial_money)

