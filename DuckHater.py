from BBCON import *
from Motob import *
from FindAndFall import *
from Stop import Stop
from DontFall import DontFall

if __name__ == '__main__':
    BBCON = BBCON()
    behaviors = [Stop(BBCON, 1.0), DontFall(BBCON, 1.0)]
    sensobs = {"fallingout": FallingOut(), "duckfinder": DuckFinder(),
               "buttonfeeler": ButtonFeeler()}
    BBCON.add_motob(Motob())
    for behavior in behaviors:
        BBCON.add_behavior(behavior)
    for sensob in sensobs:
        BBCON.add_sensob(sensobs[sensob])
    while not BBCON.halt:
        BBCON.run_one_timestep()
