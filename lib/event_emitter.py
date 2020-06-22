from typing import Callable, Dict, List

subscribers: Dict[str, List[Callable]] = {}

class EventEmitter:
    @staticmethod
    def on(event_name: str, action: Callable):
        if event_name not in subscribers:
            subscribers[event_name] = []
        subscribers[event_name].append(action)
    
    def emit(self, event_name, *args, **kwargs):
        if event_name not in subscribers:
            return
        for action in subscribers[event_name]:
            action(self, *args, **kwargs)