from typing import Callable, List, Tuple, Dict

from .component import Component

class CollisionManager:
    registered_handlers = {}
    def __init__(self):
        pass

    @staticmethod
    def register_collision_type(constructor1: callable, constructor2: callable, handler: Callable[[Component, Component], None]) -> None:
        CollisionManager.registered_handlers[(constructor1, constructor2)] = handler

    def handle_all(self, collisions: List[Tuple[Component, Component]]):
        handled_collisions = {}
        for handler in self.registered_handlers.values():
            handled_collisions[handler] = set()
        collisions = {(c1, c2) for c1, c2 in collisions if c1.is_collision(c2) or c2.is_collision(c1)}
        for collision in collisions:
            self.__handle(*collision, handled_collisions)

    def __handle(self, comp1: Component, comp2: Component, handled_collisions: Dict[callable, set]):
        collision_id = comp1.id * comp2.id
        for collision_type, handler in self.registered_handlers.items():
            c1, c2 = collision_type
            if isinstance(comp1, c1) and isinstance(comp2, c2):
                if collision_id in handled_collisions[handler]:
                    print("skipping:", comp1, comp2)
                    continue
                handler(comp1, comp2)
                handled_collisions[handler].add(collision_id)

    
    def __get_collision_type(self, comp1: Component, comp2: Component):
        return tuple([comp1.__class__, comp2.__class__].sorted(key=lambda cls: cls.__name__))