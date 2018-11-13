from Arbitrator import *
from Behavior import *
import time


class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = {}
        self.motob = None
        self.arbitrator = Arbitrator(self)
        self.halt = False

    def add_behavior(self, behavior): self.behaviors.append(behavior)

    def add_sensob(self, name, sensob): self.sensobs[name] = sensob

    def add_motob(self, motob): self.motob = motob

    def activate_behavior(self, behavior): self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior): self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            self.sensobs[sensob].update()
        for behavior in self.behaviors:
            behavior.update()
        action = self.arbitrator.choose_action()
        if action[1]:
            self.motob.update(("S", 0))
            self.halt = True
        else:
            print(action[0], " was used")
            self.motob.update(action[0])
        # time.sleep(0.1)
        for sensob in self.sensobs:
            self.sensobs[sensob].reset()


