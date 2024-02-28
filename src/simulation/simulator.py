from .core import Event, State, ActionByTime
from heapq import heappop
from typing import List


def simulation(events: List[Event], actionByTime: ActionByTime, state: State, time: float) -> List[Event]:
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

        actionByTime.action(event.time - last_time, state)
        event.action(state, events)

    actionByTime.action(time-last_time, state)

    return history
