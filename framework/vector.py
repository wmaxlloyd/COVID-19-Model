import numpy
from numpy import cos, sin, sqrt
from math import pi
from typing import Tuple

class Vector:
    def __init__(self, x: float, y: float):
        self.__set(numpy.array((x, y)))

    def __set(self, a: numpy.array) -> None:
        self.array = a
        self.x = a[0]
        self.y = a[1]
        self.magnitude = sqrt(self.x ** 2 + self.y ** 2)
        self.unit_vector = self.array / self.magnitude        

    def get_angle_between(self, v: 'Vector') -> float:
        dot_product = numpy.dot(self.unit_vector, v.unit_vector)
        approx_clipped_product = numpy.clip(dot_product, -1.0, 1.0)
        return numpy.arccos(approx_clipped_product)

    def get_acute_angle_between(self, v: 'Vector') -> float:
        angle = self.get_angle_between(v)
        return angle if angle <= pi / 2 else pi - angle

    def rotate(self, angle: float) -> Tuple[float, float]:
        transformation = numpy.array([
            [cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]
        ])
        new_vector = numpy.matmul(transformation, numpy.vstack(self.array)).flatten()
        self.__set(new_vector)

    def set_magnitude(self, length = 1):
        new_vector = self.unit_vector * length
        self.__set(new_vector)

    def transform(self , angle = 0.0, magnitude = 1):
        self.rotate(angle)
        self.set_length(magnitude)
    
    def set_x(self, x: float):
        new_vector = numpy.array((x, self.y))
        self.__set(new_vector)
    
    def set_y(self, y: float):
        new_vector = numpy.array((self.x, y))
        self.__set(new_vector)
    
    def isParallelWith(self, v: 'Vector') -> bool:
        threshold = .01
        return -threshold <= self.get_acute_angle_between(v) <= threshold
        
    def distanceFrom(self, v: 'Vector') -> float:
        return Vector.difference(self, v).magnitude

    @staticmethod
    def difference(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector(*(v1.array - v2.array))
    
    @staticmethod
    def add(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector(*(v1.array + v2.array))

    @staticmethod
    def perpendicular(v: 'Vector') -> 'Vector':
        return Vector(-v.y, v.x)
    
    @staticmethod
    def opposite(v: 'Vector') -> 'Vector':
        return Vector(-v.x, -v.y)
    
    @staticmethod
    def scale(v: 'Vector', magnitude: float) -> 'Vector':
        v_f = Vector(v.x, v.y)
        v_f.set_magnitude(magnitude)
        return v_f
