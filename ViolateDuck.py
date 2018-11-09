from Behavior import Behavior


class ViolateDuck(Behavior):
    def __init__(self, bbcon, priority):
        super().__init__(bbcon, priority)

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True

    def sense_and_act(self):
        duckfinder_value = self.BBCON["duckfinder"].interpret()
        peeper_value = self.BBCON["peeper"].interpret()
        match_degree = 1-abs(duckfinder_value)**(1/2)

        if peeper_value > 0.1:
            self.motor_recommendation = ("F", 10)
        else:
            self.motor_recommendation = ("F", 100)

        return match_degree
