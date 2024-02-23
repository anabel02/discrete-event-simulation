from .inventory import ShopProductEvent, RefillEvent, InventoryState, InventoryConfig, ActionByTimeInventory
from heapq import heappush, heapify
from typing import List, Callable
from simulation.core import Event, State
from simulation.simulator import simulation


def generate_events(index: int, time: float, time_dist: Callable[[], None], cant_dist: Callable[[], None], config: InventoryConfig) -> List[Event]:
    current = 0
    events = []

    def post_action(state: State, events: List[Event]):
        if state.cants[index] < config.parameter_s:
            heappush(events, RefillEvent(current, config.refill_interval, index, config.parameter_S -
                     state.cants[index], config.cost_refill(config.parameter_S - state.cants[index])))

    while current < time:
        interval = time_dist()
        current += interval
        events.append(ShopProductEvent(current, interval, index,
                      cant_dist(), config.price, post_action))


def configure(time: float, time_dist: Callable[[], None], configs: List[InventoryConfig], cant_dists: List[Callable[[], None]]) -> List[Event]:
    events = []

    for i in range(len(configs)):
        events += generate_events(i, time, time_dist,
                                  cant_dists[i], configs[i])

    heapify(events)

    return events


def inventory_simulation(time: float, time_dist: Callable[[], None], configs: List[InventoryConfig], cant_dists: List[Callable[[], None]], initial_cants: List[int], initial_money: float):
    state = InventoryState(initial_cants, initial_money)
    events = configure(time, time_dist, configs, cant_dists)
    action_by_time = ActionByTimeInventory(configs)

    simulation(events, action_by_time, state, time)
