from .ball import Ball

class Person(Ball):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, radius = 5)
