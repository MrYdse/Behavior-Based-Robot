from Behavior import *


class DontFall(Behavior):
    def __init__(self, BBCON, priority):
        super(DontFall, self).__init__(BBCON, priority)

    def sense_and_act(self):
        danger = self.BBCON.sensobs["fallingout"].interpret()
        match_degree = 0.0
        if danger != 0:
            match_degree = 1.0
            if danger == -1:
                self.motor_recommendation = ("R", 45)
            else:
                self.motor_recommendation = ("L", 45)
        return match_degree

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True
