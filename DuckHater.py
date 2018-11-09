from BBCON import *
from Motob import *
from FindAndFall import *

if __name__ == '__main__':
    behaviors = []
    sensobs = {"fallingout": FallingOut(), "duckfinder": DuckFinder()}
    motobs = [Motob()]
    BBCON = BBCON(behaviors, sensobs, motobs)
    while not BBCON.halt:
        BBCON.run_one_timestep()
