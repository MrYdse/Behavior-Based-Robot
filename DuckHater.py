from BBCON import *
from Motob import *
from FindAndFall import *
from Stop import Stop
from DontFall import DontFall
from ViolateDuck import ViolateDuck
from FindDuck import FindDuck

if __name__ == '__main__':
    BBCON = BBCON()
    behaviors = [Stop(BBCON, 1.0), DontFall(BBCON, 1.0),
                 ViolateDuck(BBCON, 0.8), FindDuck(BBCON, 0.8)]
    sensobs = {"fallingout": FallingOut(), "duckfinder": DuckFinder(),
               "buttonfeeler": ButtonFeeler(), "peeper": Peeper()}
    BBCON.add_motob(Motob())
    for behavior in behaviors:
        BBCON.add_behavior(behavior)
    for sensob in sensobs:
        BBCON.add_sensob(sensobs[sensob])
    while not BBCON.halt:
        BBCON.run_one_timestep()
