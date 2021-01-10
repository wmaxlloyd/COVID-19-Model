from matplotlib import pyplot as plt
import numpy as np

from lib.reporter import Reporter
from .status_aggrogator import AggrograteHealthStatus
from .statuses import infected

class NewInfectionCount(Reporter):

    def __init__(self):
        self.y_values = []
        self.figure = plt.figure()

    def time_step_finished(self, time_step: int):
        snapshot = self.get_snapshot()
        self.write_to_graph(snapshot, time_step)

    def get_snapshot(self):
        return AggrograteHealthStatus.get()
    
    def write_to_graph(self, data: dict, time_step: int):  
        self.y_values.append(data[infected] if infected in data else 0)
        if not time_step % 100:
            plt.plot(self.y_values)
            plt.draw()
            plt.pause(0.0001)
            plt.clf()
        