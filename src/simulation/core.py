from abc import ABC
from typing import List


class State(ABC):
    pass


class ActionByTime(ABC):
    def action(self, interval: float, state: State):
        """
        This method should be called before each event action. It should be used to update the state of the system.
        """
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
        """
        This method should be called when the event is popped from the heap. It should be used to update the state of the system and to generate new events.
        :param state: The state of the system
        :param events: The list of events
        :return: None
        """
        pass
