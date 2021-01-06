from lib.reporter import Reporter
from .status_aggrogator import AggrograteHealthStatus

class NewInfectionCount(Reporter):

    def __init__(self):
        # prep viz
        pass

    def time_step_finished(self, time_step: int):
        snapshot = self.get_snapshot(time_step)
        self.write_to_graph(snapshot)

    def get_snapshot(self, time):
        return AggrograteHealthStatus.get()
    
    def write_to_graph(self, data):
        print(data)
    
