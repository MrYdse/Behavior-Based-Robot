from Behavior import *


class FindDuck(Behavior):
    def sense_and_act(self):
        duck_direction = self.sensobs["duckfinder"].get_interpretation()
        if duck_direction != 2.0:
            match_degree = abs(duck_direction)**(1/2)
            if duck_direction < 0:
                self.motor_recommendation = ("L", abs(duck_direction)*45)
            else:
                self.motor_recommendation = ("R", duck_direction*45)
        else:
            match_degree = 0.8
            self.motor_recommendation = ("L", 45)
        return match_degree


    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False