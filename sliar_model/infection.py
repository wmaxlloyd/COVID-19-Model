from dataclasses import dataclass
from typing import Tuple, Dict, TYPE_CHECKING
from .statuses import latent, asymptomatic, infected, recovered, dead, AgentStatus
from random import random, randint

if TYPE_CHECKING:
    from .basic_agent import BasicAgent

@dataclass
class Infection:
    transmission_rate: Dict[AgentStatus, float]
    mortality_rate: float
    incubation_period_range: Tuple[int, int]
    infection_period_range: Tuple[int, int]
    asymptomatic_proportion: float

    def __init__(self, host: 'BasicAgent'):
        self.host = host
        self.host.update_health_status(latent)
        self.infection_time = 0
        self.incubation_period = randint(*self.incubation_period_range)
        self.infection_period = self.incubation_period + randint(*self.infection_period_range)
        self.will_show_symptoms = random() >= self.asymptomatic_proportion
        self.will_die = random() < self.mortality_rate
    
    def update_infection(self):
        self.infection_time += 1
        if (
            self.host.health_status() == latent and
            self.infection_time >= self.incubation_period
        ):
            self.host.update_health_status(infected if self.will_show_symptoms else asymptomatic)
        if (
            (self.host.health_status() == infected or self.host.health_status() == asymptomatic) and
            self.infection_time >= self.infection_period
        ):
            self.host.update_health_status(dead if self.will_die else recovered)
        
    def is_contagious(self):
        return self.host.health_status() in self.transmission_rate
    
    def will_transmit(self):
        host_health = self.host.health_status()
        if host_health not in self.transmission_rate:
            return False
        return random() < self.transmission_rate[host_health]