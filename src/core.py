from abc import ABC
from typing import List


class State(ABC):
    pass

class ActionByTime(ABC):
    def action(self, interval: float, state: State):
        pass


class Event(ABC):
    def __init__(self, time: float, interval: float) -> None:
        self.time: float = time
        self.interval: float = interval

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

    def action(self, state: State, events: List['Event']):
        pass
