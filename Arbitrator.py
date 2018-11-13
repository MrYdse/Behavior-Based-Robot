from BBCON import *
from utils import take_first


class Arbitrator:
    def __init__(self, BBCON):
        self.BBCON = BBCON

    def choose_action(self):
        behaviors = self.BBCON.active_behaviors
        recommendations = []
        for behavior in behaviors:
            if behavior.active_flag:
                recommendations.append((behavior.weight, behavior))
        recommendations.sort(key=take_first)
        pick = recommendations[-1][1]
        print(pick.__class__, " got chosen with weight ", recommendations[-1][0])
        choice = (pick.motor_recommendation, pick.halt_request)
        return choice

#if __name__ == '__main__':
#    test = BBCON()


