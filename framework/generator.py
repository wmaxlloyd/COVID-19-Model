from numpy.random import choice, randint
from math import sin, cos, pi
from typing import Tuple, TYPE_CHECKING, List, Callable, Union, Dict

if TYPE_CHECKING:
    from .scene import Scene
    from .component import Component

RandomValueConfig = Union[List, Callable, int, str]

class ComponentGenerator:
    def __init__(self, scene: 'Scene', ComponentConstructor: 'Component'):
        self.__scene = scene
        self.__Constructor = ComponentConstructor
        self.__constructor_kwargs: Dict[str, RandomValueConfig] = {}
        self.__constructor_args: List[RandomValueConfig] = []

    def random_position_in_scene(self):
        return (
            randint(0, self.__scene.width()),
            randint(0, self.__scene.height())
        )
    
    def __get_random_value_from_config(self, config: RandomValueConfig):
        if isinstance(config, list):
            return choice(config)
        if callable(config):
            return config()
        return config

    def __generate_args(self):
        return map(self.__get_random_value_from_config, self.__constructor_args)

    def __generate_kwargs(self):
        kwargs = {}
        for (key, value) in self.__constructor_kwargs.items():
            kwargs[key] = self.__get_random_value_from_config(value)
        return kwargs
    
    def __generate_component(self):
        return self.__Constructor(*self.__generate_args(), **self.__generate_kwargs())

    def generate(self, collision_check = True):
        component = self.__generate_component()
        while collision_check and self.__scene.contains_collision_with(component):
            component = self.__generate_component()
        self.__scene.add_componenet(component)
        return self

    def use_arg(self, arg: RandomValueConfig):
        self.__constructor_args.append(arg)
        return self

    def use_kwarg(self, argName: str, possible_values: RandomValueConfig):
        self.__constructor_kwargs[argName] = possible_values
        return self

    def random_velocity_with_magnitude_range(self, min_vel, max_vel):
        if not min_vel:
            min_vel = 0
        if not max_vel:
            max_vel = min_vel
        return lambda: self.__generate_velocity(min_vel, max_vel)
    
    def __generate_velocity(self, min_vel, max_vel):
        velocity = randint(min_vel, max_vel)
        angle_rad = randint(0, 360) / 360 * 2 * pi
        return (velocity * cos(angle_rad), velocity * sin(angle_rad))


