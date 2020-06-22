from dataclasses import dataclass
from enum import Enum
from typing import Tuple

@dataclass
class AgentStatus:
    name: str
    color: Tuple[int, int, int]

    def __str__(self):
        return self.name

    def __hash__(self):
        return self.name.__hash__()

susceptible = AgentStatus(name = 'Susceptible', color = (1,1,1))
latent = AgentStatus(name = 'Latent', color = (1,1,.5))
infected = AgentStatus(name = 'Infected', color = (1,1,0))
asymptomatic = AgentStatus(name = 'Asymptomatic', color = (1,.5,0))
recovered = AgentStatus(name = 'Recovered', color = (1,0,1))
dead = AgentStatus(name = 'Dead', color = (0,1,1)) 