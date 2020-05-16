from framework.ball import Ball
from enum import Enum
from math import inf
from numpy.random import choice

class HealthStatus(Enum):
    HEALTHY = 0
    INCUBATING = 1
    ASYMPTOMATIC = 2
    SYMPTOMATIC = 3
    RECOVERED = 4
    DEAD = 5

health_status_flow = {
    HealthStatus.HEALTHY: {
        "duration": inf
    },
    HealthStatus.INCUBATING: {
        "duration": 10,
        "next": {
            HealthStatus.ASYMPTOMATIC: .5,
            HealthStatus.SYMPTOMATIC: .5
        }
    },
    HealthStatus.SYMPTOMATIC: {
        "duration": 500,
        "next": {
            HealthStatus.RECOVERED: .99,
            HealthStatus.DEAD: .01
        }
    },
    HealthStatus.ASYMPTOMATIC: {
        "duration": 100,
        "next": {
            HealthStatus.RECOVERED: .99,
            HealthStatus.DEAD: .01
        }
    },
    HealthStatus.RECOVERED: {
        "duration": inf
    },
    HealthStatus.DEAD: {
        "duration": inf
    }
}

health_status_color_map = {
    HealthStatus.HEALTHY: (1,1,1),
    HealthStatus.INCUBATING: (1,1,0),
    HealthStatus.ASYMPTOMATIC: (1,1,0),
    HealthStatus.SYMPTOMATIC: (0,1,1),
    HealthStatus.RECOVERED: (1,.5,.5),
    HealthStatus.DEAD: (0,0,1)
}

class Person(Ball):
    def __init__(self, *args, health_status: HealthStatus = HealthStatus.HEALTHY, **kwargs):
        super().__init__(*args, **kwargs, radius = 5)
        self.set_new_health_status(health_status)
    
    def update_state(self):
        self.update_health_status()
        return super().update_state()
    
    def health_status(self):
        return self.__health_status
    
    def is_contagious(self):
        return self.__health_status == HealthStatus.ASYMPTOMATIC or \
            self.__health_status == HealthStatus.SYMPTOMATIC

    def is_immune(self):
        return self.__health_status == HealthStatus.RECOVERED or \
            self.__health_status == HealthStatus.DEAD

    def set_new_health_status(self, new_status: HealthStatus):
        self.__health_status = new_status
        self.__generations_in_status = 0
        self.color = health_status_color_map[new_status]
    
    def update_health_status(self):
        current_status_flow = health_status_flow[self.__health_status]
        self.__generations_in_status += 1
        if current_status_flow["duration"] >= self.__generations_in_status:
            return
        next_status = choice(
            list(current_status_flow["next"].keys()),
            p=list(current_status_flow["next"].values()),
        )
        self.set_new_health_status(next_status)
