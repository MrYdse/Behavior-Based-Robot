from abc import ABC, abstractmethod
from random import randint


class Behavior(ABC):
    def __init__(self, BBCON, priority):
        self.BBCON = BBCON
        self.motor_recommendation = ("B", 50)  # Tuple of string and int
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


class Wander(Behavior):
    def __init__(self, BBCON, priority):
        super(Wander, self).__init__(BBCON, priority)

    def sense_and_act(self):
        match_degree = 1.0
        direction = randint(0, 3)
        directions = ["L", "R", "F", "S"]
        self.motor_recommendation = (directions[direction], 25)
        return match_degree

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True


class DontFall(Behavior):
    def __init__(self, BBCON, priority):
        super(DontFall, self).__init__(BBCON, priority)

    def sense_and_act(self):
        danger = self.BBCON.sensobs["fallingout"].interpret()
        match_degree = 0.0
        if danger != 0:
            match_degree = 1.0
            if danger == -1:
                self.motor_recommendation = ("B", 30)
            else:
                self.motor_recommendation = ("B", 30)
        return match_degree

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True


class Stop(Behavior):
    def __init__(self, BBCON, priority):
        super(Stop, self).__init__(BBCON, priority)

    def sense_and_act(self):
        match_degree = 0.0
        if self.BBCON.sensobs["buttonfeeler"].interpret():
            self.halt_request = True
            match_degree = 1.0
            self.motor_recommendation = ("S", 0)
        else:
            self.halt_request = False
        return match_degree

    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False


class ViolateDuck(Behavior):
    def __init__(self, BBCON, priority):
        super().__init__(BBCON, priority)

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True

    def sense_and_act(self):
        duckfinder_value = self.BBCON.sensobs["duckfinder"].get_interpretation()
        distance = self.BBCON.sensobs["peeper"].get_interpretation()
        match_degree = 1-abs(duckfinder_value)

        if distance > 0.1:
            self.motor_recommendation = ("F", 25)
        else:
            self.motor_recommendation = ("F", 30)

        return match_degree


class FindDuck(Behavior):
    def __init__(self, BBCON, priority):
        super(FindDuck, self).__init__(BBCON, priority)

    def sense_and_act(self):
        duck_direction = self.BBCON.sensobs["duckfinder"].get_interpretation()
        print(duck_direction)
        if duck_direction != 2.0:
            match_degree = abs(duck_direction)
            if duck_direction < 0:
                self.motor_recommendation = ("L", abs(duck_direction)*50)
            else:
                self.motor_recommendation = ("R", duck_direction*50)
        else:
            match_degree = 0.1
            self.motor_recommendation = ("L", 30)
        return match_degree

    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False
