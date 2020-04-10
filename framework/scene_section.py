from .component import Component
from .hitbox import Hitbox
from .collison import Collision
from typing import Set, Tuple, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .scene import Scene

class SceneSection(Component):
    def __init__(
        self,
        scene: 'Scene',
        matrix_index: Tuple[int, int],
        location: Tuple[float, float],
        width: float,
        height: float
    ):
        super().__init__(init_pos=location, init_vel=(0,0))
        self.__width = width
        self.__height = height
        self.__scene = scene
        self.__index = matrix_index
        self.__next_to_border = self.__is_next_to_border()
        self.reset_components()
    
    def reset_components(self):
        self.__components_set: Set[Component] = set()
        self.__components_list: List[Component] = []

    def get_hitbox(self):
        return Hitbox(self, (0, self.__width), (0, self.__height))
        
    def draw(self):
        self.get_hitbox().draw()

    def index(self):
        return self.__index

    def __is_next_to_border(self) -> bool:
        hitbox = self.get_hitbox()
        return (
            hitbox.bottom() <= 0 or
            hitbox.top() >= self.__scene.height() or
            hitbox.left() <= 0 or 
            hitbox.right() >= self.__scene.width()
        )
    
    def add_component(self, component: Component):
        self.__components_list.append(component)
        self.__components_set.add(component)

    def includes_component(self, component: Component):
        return component in self.__components_set
    
    def handle_collisions(self):
        for i in range(len(self.__components_list)):
            component1 = self.__components_list[i]
            self.__scene.border().handle_component_collision(component1)
            for j in range(i + 1, len(self.__components_list)):
                component2 = self.__components_list[j]
                Collision.handle(component1, component2)