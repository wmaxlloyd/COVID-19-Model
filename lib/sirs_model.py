# from typing import List, Generator
# from .person import Person, HealthStatus
# from enum import Enum
# from .event_emitter import EventEmitter
# from random import random

# @dataclass
# class AgentStatusBase:
#     name: str
#     color: Tuple[int, int, int]

#     def __str__(self):
#         return self.name

# class HealthStatus(Enum):
#     HEALTHY = NewHealthStatus(name = 'Healthy', color = (1,1,1))
#     INFECTED = NewHealthStatus(name = 'Infected', color = (1,1,0))
#     RECOVERED = NewHealthStatus(name = 'Recovered', color = (1,0,1))
#     DEAD = NewHealthStatus(name = 'Dead', color = (0,1,1)) 

# class SirsDisease:
#     pass

# class SirsAgent(Person):
#     def __init__(
#         self,
#         host: Person,
#         stages_with_symptoms: List[InfectionStage] = [
#             InfectionStage.PERIOD_OF_ILLNESS,
#             InfectionStage.PERIOD_OF_DECLINE,
#         ],
#         stages_when_contagious: List[InfectionStage] = [
#             InfectionStage.PRODROMAL_PERIOD,
#             InfectionStage.PERIOD_OF_ILLNESS,
#             InfectionStage.PERIOD_OF_DECLINE,
#             InfectionStage.PERIOD_OF_CONVALESCENCE,
#         ],
#         initial_pathogens: int = 10,
#         pathogen_evolut
        
#         ion: Generator[int, 'Infection', None] = mock_generator,
#         mortality_rate: float = .01

#     ):
#         self.host = host
#         self.stage: InfectionStage = InfectionStage.INCUBATION_PERIOD
#         self.stages_with_symptoms = stages_with_symptoms
#         self.stages_when_contagious = stages_when_contagious
#         self.host.update_health_status(HealthStatus.INFECTED)
#         self.pathogens = initial_pathogens
#         self.pathogen_evolution = pathogen_evolution()
#         self.mortality_rate = mortality_rate
#         self.infection_done: bool = False
    
#     def is_contagious(self):
#         return self.stage in self.stages_when_contagious
    
#     def is_symptomatic(self):
#         return (self.stage in self.stages_with_symptoms)

#     def finish(self):
#         self.host.update_health_status(HealthStatus.RECOVERED)
    
#     def kill_host(self):
#         self.host.update_health_status(HealthStatus.DEAD)
#         return self
    
#     def update_state(self):
#         try:
#             self.pathogens = self.pathogen_evolution.__next__()
#         except StopIteration:
#             if self.host.health_status() != HealthStatus.INFECTED:
#                 return
#             if random() <= self.mortality_rate:
#                 self.kill_host()
#             else:
#                 self.finish()
#         return self
    
#     def infect_person(self, person: Person):
#         if person.infection:
#             return
#         infection = self.__class__(person)
#         person.infect_with(infection)  
    




