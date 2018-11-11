from BBCON import *
from Motob import *
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton

if __name__ == '__main__':
    button = ZumoButton()
    button.wait_for_press()
    BBCON = BBCON()
    behaviors = [Stop(BBCON, 1.0), DontFall(BBCON, 1.0),
                 ViolateDuck(BBCON, 0.8), FindDuck(BBCON, 0.8)]
    BBCON.active_behaviors = BBCON.behaviors()
    sensobs = {"fallingout": FallingOut(), "duckfinder": DuckFinder(),
               "buttonfeeler": ButtonFeeler(), "peeper": Peeper()}
    BBCON.add_motob(Motob())
    for behavior in behaviors:
        BBCON.add_behavior(behavior)
    for sensob in sensobs:
        BBCON.add_sensob(sensob, sensobs[sensob])
    while not BBCON.halt:
        BBCON.run_one_timestep()
