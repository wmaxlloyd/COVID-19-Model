from .basic_agent import BasicAgent, Events
from .statuses import AgentStatus

aggrograte_health_status = {}

class AggrograteHealthStatus:

    @staticmethod
    def update(agent: BasicAgent, new_status: AgentStatus, old_status: AgentStatus):
        if new_status not in aggrograte_health_status:
            aggrograte_health_status[new_status] = 0
        aggrograte_health_status[new_status] += 1
        if old_status:
            aggrograte_health_status[old_status] -= 1

    @staticmethod
    def get():
        return aggrograte_health_status

BasicAgent.on(Events.HEALTH_STATUS_CHANGE, AggrograteHealthStatus.update)
