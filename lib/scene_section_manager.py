from .scene_section import SceneSection
from typing import List, Tuple, TYPE_CHECKING
from .collision_manager import CollisionManager

if TYPE_CHECKING:
    from .scene import Scene
    from .component import Component

class SceneSectionManager:

    def __init__(self, scene: 'Scene', rows: int, columns: int):
        self.__scene = scene
        self.__rows = rows
        self.__columns = columns
        self.__section_width = self.__scene.width() / self.__columns
        self.__section_height = self.__scene.height() / self.__rows
        self.__init_section_matrix()
        self.__collision_manager = CollisionManager()

    def __init_section_matrix(self):
        col_index = 0
        row_index = 0
        self.__section_matrix: List[List[SceneSection]] = []
        while row_index * self.__section_height < self.__scene.height():
            self.__section_matrix.append([])
            while col_index * self.__section_width < self.__scene.width():
                self.__section_matrix[-1].append(SceneSection(
                    self.__scene,
                    (row_index, col_index),
                    (self.__section_width * col_index, self.__section_height * row_index),
                    self.__section_width,
                    self.__section_height
                ))
                col_index += 1
            col_index = 0
            row_index += 1
    
    def classify_component(self, component: 'Component'):
        pos_x, pos_y = component.pos.array
        col_index = min( max(0, int(pos_x // self.__section_width)), self.__columns - 1)
        row_index = min( max(0, int(pos_y // self.__section_height)), self.__rows - 1)
        seed_section = self.__section_matrix[row_index][col_index]
        self.__classify_component_into_section(component, seed_section)

    
    def __classify_component_into_section(self, component: 'Component', section: SceneSection):
        if section.includes_component(component):
            return
        if not section.is_collision(component):
            return
        section.add_component(component)
        for neighboring_section in self.__get_section_neighbors(section):
            self.__classify_component_into_section(component, neighboring_section)
    
    def reset(self):
        for scene_section_list in self.__section_matrix:
            for scene_section in scene_section_list:
                scene_section.reset_components()

    def handle_collisions(self):
        collisions: List[Tuple[Component, Component]] = []
        for scene_section_list in self.__section_matrix:
            for scene_section in scene_section_list:
                collisions += scene_section.get_possible_collisions()
        self.__collision_manager.handle_all(collisions)
    
    def draw_sections(self):
        for scene_section_list in self.__section_matrix:
            for scene_section in scene_section_list:
                scene_section.draw()
    
    def __get_section_neighbors(self, section: SceneSection):
        row_index, col_index = section.index()
        neighbors: List[SceneSection] = []
        if row_index > 0:
            neighbors.append(self.__section_matrix[row_index - 1][col_index])
        if row_index < self.__rows - 1:
            neighbors.append(self.__section_matrix[row_index + 1][col_index])
        if col_index > 0:
            neighbors.append(self.__section_matrix[row_index][col_index - 1])
        if col_index < self.__columns - 1:
            neighbors.append(self.__section_matrix[row_index][col_index + 1])
        return neighbors