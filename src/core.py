from abc import ABC
from typing import List
from heapq import heappush, heappop


class State:
    def __init__(self, initial: List[int], initial_money: int) -> None:
        self.cants = initial
        self.money = initial_money
        self.money_history = [initial_money]

    def add_cant(self, index: int, cant: int):
        self.cants[index] += cant

    def remove_cant(self, index: int, cant: int):
        self.cants[index] -= cant

    def add_money(self, money: int):
        self.money += money
        self.money_history.append(self.money)

    def remove_money(self, money: int):
        self.money -= money
        self.money_history.append(self.money)


class ActionByTime(ABC):
    def action(self, interval: float, state: State):
        pass


class Event(ABC):
    def __init__(self, time: float, interval: float) -> None:
        self.time = time
        self.interval = interval

    def action(self, state: State, events: List['Event']):
        pass
