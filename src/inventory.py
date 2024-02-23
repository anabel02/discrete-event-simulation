from abc import ABC
from typing import List, Callable
from .core import Event, State


class InventoryState(State):
    def __init__(self, initial: List[int], initial_money: float) -> None:
        self.cants: List[int] = initial
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
    def __init__(self, current_time: float, interval: float, index: int, cant: int, post_action: Callable[[InventoryState, Event]]) -> None:
        super().__init__(interval+current_time, interval)
        self.index: int = index
        self.cant: int = cant
        self.post_action: Callable[[InventoryState, Event]] = post_action

    def action(self, state: InventoryState, events: List[Event]):
        if state.cants[self.index] >= self.cant:
            state.remove_cant(self.index, self.cant)
            state.add_money(self.price)

        self.post_action(state, events)


class InventoryConfig(ABC):
    def __init__(self, parameter_s: int, parameter_S: int, refill_interval: float) -> None:
        self.parameter_s: int = parameter_s
        self.parameter_S: int = parameter_S
        self.refill_interval: float = refill_interval

    def cost_refill(self, cant: int) -> float:
        pass

    def cost_inventory(state: InventoryState) -> float:
        pass


class InventoryConfigImpl(InventoryConfig):
    def cost_refill(self, cant: int) -> float:
        return cant * 10

    def cost_inventory(self, state: InventoryState) -> float:
        return 10 * sum(state.cants)
