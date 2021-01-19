import numpy
from numpy import cos, sin, sqrt
from math import pi, acos
from typing import Tuple
from enum import Enum

class VectorDirection(Enum):
    POSITIVE = 0
    NEGATIVE = 1

class Vector:
    def __init__(self, x: float, y: float):
        self.array = (numpy.array((x, y)))

    def x(self):
        return self.array[0]
    
    def reflect_x(self):
        self.array[0] = -1 * self.array[0]
        return self
    
    def set_x_direction(self, direction: VectorDirection):
        if direction == VectorDirection.POSITIVE and self.x() < 0:
            self.reflect_x()
        if direction == VectorDirection.NEGATIVE and self.x() > 0:
            self.reflect_x()
        return self
    
    def set_y_direction(self, direction: VectorDirection):
        if direction == VectorDirection.POSITIVE and self.y() < 0:
            self.reflect_y()
        if direction == VectorDirection.NEGATIVE and self.y() > 0:
            self.reflect_y()
        return self
    
    def y(self):
        return self.array[1]
    
    def reflect_y(self):
        self.array[1] = -1 * self.array[1]
        return self
    
    def magnitude(self) -> float:
        return sqrt(self.x() ** 2 + self.y() ** 2)

    def unit_vector(self) -> 'Vector':
        unit_vector_array = self.array / self.magnitude()
        return Vector(*unit_vector_array)

    def dot(self, v: 'Vector') -> float:
        return numpy.dot(self.array, v.array)

    def get_angle_between(self, v: 'Vector') -> float:
        dot_product = self.dot(v)
        approx_clipped_product = numpy.clip(dot_product, -1.0, 1.0)
        return acos(approx_clipped_product)

    def get_acute_angle_between(self, v: 'Vector') -> float:
        angle = self.get_angle_between(v)
        return angle if angle <= pi / 2 else pi - angle

    def rotate(self, angle: float) -> Tuple[float, float]:
        transformation = numpy.array([
            [cos(angle), -sin(angle)],
            [sin(angle), cos(angle)]
        ])
        new_vector = numpy.matmul(transformation, numpy.vstack(self.array)).flatten()
        self.array = new_vector

    def set_magnitude(self, length = 1):
        new_vector = self.unit_vector().array * length
        self.array = new_vector

    def transform(self , angle = 0.0, magnitude = 1):
        self.rotate(angle)
        self.set_length(magnitude)

    
    def isParallelWith(self, v: 'Vector') -> bool:
        threshold = .01
        return -threshold <= self.get_acute_angle_between(v) <= threshold
        
    def distanceFrom(self, v: 'Vector') -> float:
        return Vector.difference(self, v).magnitude()

    @staticmethod
    def difference(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector(*(v1.array - v2.array))
    
    @staticmethod
    def add(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector(*(v1.array + v2.array))

    @staticmethod
    def perpendicular(v: 'Vector') -> 'Vector':
        return Vector(v.y(), -v.x())
    
    @staticmethod
    def opposite(v: 'Vector') -> 'Vector':
        return Vector(-v.x, -v.y)
    
    @staticmethod
    def scale(v: 'Vector', magnitude: float) -> 'Vector':
        v_f = Vector(v.x(), v.y())
        v_f.set_magnitude(magnitude)
        return v_f
