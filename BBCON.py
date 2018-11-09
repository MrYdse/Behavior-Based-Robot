from Arbitrator import *
from Behavior import *
import time


class BBCON:
    def __init__(self, behaviors, sensobs, motobs):
        self.behaviors = behaviors
        self.active_behaviors = []
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = Arbitrator(self)
        self.halt = False

    def add_behavior(self, behavior): self.behaviors.append(behavior)

    def add_sensob(self, sensob): self.sensobs.append(sensob)

    def activate_behavior(self, behavior): self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior): self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            self.sensobs[sensob].update()
        for behavior in self.behaviors:
            behavior.update()
        action = self.arbitrator.choose_action()
        if action[1]:
            self.motobs[0].update(("S", 0))
            self.halt = True
        else:
            self.motobs[0].update(action[0])
        time.sleep(0.3)
        for sensob in self.sensobs:
            self.sensobs[sensob].reset()


