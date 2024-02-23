from .core import Event, State, ActionByTime
from heapq import heappop
from typing import List


def simulation(events: List[Event], actionByTime: ActionByTime, state: State, time: float):
    while events:
        event = heappop(events)

        if event.time > time:
            break

        event.action(state, events)
        actionByTime.action(event.interval, state)
