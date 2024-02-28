from .core import Event, State, ActionByTime
from heapq import heappop
from typing import List, Callable


def simulation(events: List[Event], action_by_time: ActionByTime, state: State, time: float, stop_case: Callable[[State], bool]) -> List[Event]:
    """
    Simulate the system. It stops when the stop_case returns True or when the time is over.
    :param events: List of events
    :param action_by_time: Change the state simulating the time between events
    :param state: Initial state of the system
    :param time: Max time to simulate
    :param stop_case: Function that returns True if the simulation should stop
    :return: List of events that happened
    """
    history = []
    last_time = 0

    while events:
        event = heappop(events)

        if stop_case(state):
            break

        if event.time > time:
            break

        last_time = event.time
        history.append(event)

        action_by_time.action(event.time - last_time, state)
        event.action(state, events)

    action_by_time.action(time - last_time, state)

    return history
