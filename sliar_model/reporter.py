from matplotlib import pyplot as plt
import numpy as np
import pyglet

from lib.reporter import Reporter
from .status_aggrogator import AggrograteHealthStatus
from .statuses import infected, susceptible

class NewInfectionCount(Reporter):

    def __init__(self):
        self.infections = []
        self.susceptible = []

    def time_step_finished(self, time_step: int):
        snapshot = self.get_snapshot()
        self.write_to_graph(snapshot, time_step)

    def get_snapshot(self):
        return AggrograteHealthStatus.get()
    
    def write_to_graph(self, data: dict, time_step: int):  
        self.infections.append(data[infected] if infected in data else 0)
        self.susceptible.append(data[susceptible] if susceptible in data else 0)
        if not time_step % 100:
            plt.plot(self.infections)
            plt.plot(self.susceptible)
            plt.draw()
            plt.pause(0.0001)
            plt.clf()

class EndWhenNoInfected(Reporter):

    def time_step_finished(self, time_step):
        if not time_step % 100:
            return
        if AggrograteHealthStatus.get()[infected] == 0:
            print(AggrograteHealthStatus.get())
            pyglet.app.exit()
            plt.show()
        