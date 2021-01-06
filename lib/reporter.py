from abc import abstractmethod

class Reporter:

    @abstractmethod
    def time_step_finished(self, time_step: int):
        pass