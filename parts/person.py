from framework.ball import Ball
from enum import Enum

class HealthStatus(Enum):
    HEALTHY = 0
    INCUBATING = 1
    ASYMPTOMATIC = 2
    SYMPTOMATIC = 3
    RECOVERED = 4
    DEAD = 5

class Person(Ball):
    def __init__(self, status: HealthStatus, **kwargs):
        super().__init__(**kwargs)
        self.status = status
    
    def update
    
