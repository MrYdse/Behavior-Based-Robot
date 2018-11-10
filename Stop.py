from FindAndFall import *
from Behavior import *


class Stop(Behavior):
    def __init__(self, BBCON, priority):
        super(Stop, self).__init__(BBCON, priority)
        self.sensob = BBCON.sensobs["buttonfeeler"]

    def sense_and_act(self):
        match_degree = 0.0
        if self.sensob.interpret():
            self.halt_request = True
            match_degree = 1.0
            self.motor_recommendation = ("S", 0)
        else:
            self.halt_request = False
            match_degree = 0.0
        return  match_degree

    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False
