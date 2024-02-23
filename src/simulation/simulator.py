from .core import Event, State, ActionByTime
from heapq import heappop
from typing import List


def simulation(events: List[Event], actionByTime: ActionByTime, state: State, time: float) -> List[Event]:
    history = []

    while events:
        event = heappop(events)

        if event.time > time:
            break

        history.append(event)

        event.action(state, events)
        actionByTime.action(event.interval, state)

    return history
