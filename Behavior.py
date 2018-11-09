from abc import ABC, abstractmethod
from BBCON import BBCON


class Behavior(ABC):
    def __init__(self, BBCON, priority):
        self.BBCON = BBCON
        self.sensobs = BBCON.sensobs
        self.motor_recommendation = None  # Tuple of string and int
        self.active_flag = True
        self.halt_request = False  # This stops the program completely
        self.priority = priority  # Float 0-1 which is given at creation and never changed
        self.weight = 0.0  # Motivation due to current conditions

    def update(self):
        self.weight = self.sense_and_act()*self.priority
        self.consider_activation()
        self.consider_deactivation()

    @abstractmethod
    def consider_deactivation(self):
        pass

    @abstractmethod
    def consider_activation(self):
        pass

    @abstractmethod
    def sense_and_act(self):
        pass
