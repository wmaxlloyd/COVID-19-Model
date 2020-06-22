from lib.person import Person
from lib.event_emitter import EventEmitter
from .infection import Infection
from enum import Enum
from .statuses import susceptible, latent, infected, asymptomatic, AgentStatus

class Events(Enum):
    HEALTH_STATUS_CHANGE="HealthStatusChange"

class BasicAgent(Person, EventEmitter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.infection: Infection = None
        self.__health_status: AgentStatus = None
        self.update_health_status(susceptible)
    
    def update_state(self):
        if self.infection:
            self.infection.update_infection()
        return super().update_state()

    def health_status(self):
        return self.__health_status
    
    def update_health_status(self, status: AgentStatus):
        if status != self.__health_status:
            self.emit(Events.HEALTH_STATUS_CHANGE, status, self.__health_status)
            self.__health_status = status
            self.color = self.__health_status.color
        return self
    
    def infect_with(self, infection: Infection):
        if self.can_be_infected():
            self.infection = infection(self)
    
    def is_contagious(self):
        return self.infection and self.infection.is_contagious()
    
    def can_be_infected(self):
        return self.__health_status == susceptible
        
    def infect_agent(self, agent: 'Agent'):
        if (
            self.is_contagious() and
            self.infection.will_transmit()
        ):
            agent.infect_with(self.infection.__class__)

