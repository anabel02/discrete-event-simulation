from .core import Event, State, ActionByTime
from heapq import heappop
from typing import List, Callable


def simulation(events: List[Event], action_by_time: ActionByTime, state: State, max_time: float, stop_case: Callable[[State], bool]) -> (List[Event], State):
    """
    Simulate the system. It stops when the stop_case returns True or when the time is over.
    :param events: List of events
    :param action_by_time: Change the state simulating the time between events
    :param state: Initial state of the system
    :param max_time: Max time to simulate
    :param stop_case: Function that returns True if the simulation should stop
    :return: List of events that happened and the final state of the system
    """
    history = []
    last_time = 0
    interrupted = False

    while events:
        event = heappop(events)

        if event.time > max_time:
            break

        last_time = event.time
        history.append(event)

        action_by_time.action(event.time - last_time, state)
        # Check if the action by time triggered the stop_case
        if stop_case(state):
            interrupted = True
            break

        event.action(state, events)
        # Check if the action of the event triggered the stop_case
        if stop_case(state):
            interrupted = True
            break

    # If the simulation stops because the time is over, simulate an action between the last event and the max_time
    if not interrupted:
        action_by_time.action(max_time - last_time, state)

    return history, state
