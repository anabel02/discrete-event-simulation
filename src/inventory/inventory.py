from typing import List, Callable
from simulation.core import Event, State, ActionByTime


class InventoryState(State):
    def __init__(self, initial_cants: List[int], initial_money: float) -> None:
        self.cants: List[int] = initial_cants
        self.money: float = initial_money
        self.money_history: List[float] = [initial_money]

    def add_cant(self, index: int, cant: int):
        self.cants[index] += cant

    def remove_cant(self, index: int, cant: int):
        self.cants[index] -= cant

    def add_money(self, money: float):
        self.money += money
        self.money_history.append(self.money)

    def remove_money(self, money: float):
        self.money -= money
        self.money_history.append(self.money)


class RefillEvent(Event):
    def __init__(self, current_time: float, interval: float, index: int, cant: int, cost: int) -> None:
        super().__init__(current_time+interval, interval)
        self.index: int = index
        self.cant: int = cant
        self.cost: float = cost

    def action(self, state: State, _: List[Event]):
        state.add_cant(self.index, self.cant)
        state.remove_money(self.cost)


class ShopProductEvent(Event):
    def __init__(self, current_time: float, interval: float, index: int, cant: int, price: float, post_action: Callable[[float, InventoryState, List[Event]], None]) -> None:
        super().__init__(interval+current_time, interval)
        self.index: int = index
        self.cant: int = cant
        self.price: float = price
        self.post_action: Callable[[InventoryState, Event]] = post_action

    def action(self, state: InventoryState, events: List[Event]):
        if state.cants[self.index] >= self.cant:
            state.remove_cant(self.index, self.cant)
            state.add_money(self.price*self.cant)

        self.post_action(self.time, state, events)


class InventoryConfig:
    def __init__(self, price: float, parameter_s: int, parameter_S: int, refill_interval: float, cost_refill: Callable[[int], float], cost_inventory: Callable[[int, float], float]) -> None:
        self.parameter_s: int = parameter_s
        self.parameter_S: int = parameter_S
        self.price = price
        self.refill_interval: float = refill_interval
        self.cost_refill: Callable[[int], float] = cost_refill
        self.cost_inventory: Callable[[int, float], float] = cost_inventory


class ActionByTimeInventory(ActionByTime):
    def __init__(self, configs: List[InventoryConfig]) -> None:
        self.configs: List[InventoryConfig] = configs

    def action(self, interval: float, state: InventoryState):
        for config in self.configs:
            state.remove_money(config.cost_inventory(
                state.cants[self.configs.index(config)], interval))
