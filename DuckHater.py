from BBCON import *
from Motob import *
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton
import time

if __name__ == '__main__':
    button = ZumoButton()
    BBCON = BBCON()
    fall = FallingOut()
    duck = DuckFinder()
    butt = ButtonFeeler()
    peep = Peeper()
    sensobs = {"fallingout": fall, "duckfinder": duck,
               "buttonfeeler": butt, "peeper": peep}
    print("Sensobs made")
    for sensob in sensobs:
        BBCON.add_sensob(sensob, sensobs[sensob])
    print("Sensobs added")
    stop = Stop(BBCON, 1.0)
    fall = DontFall(BBCON, 1.0)
    violate = ViolateDuck(BBCON, 0.8)
    find = FindDuck(BBCON, 0.8)
    # wander = Wander(BBCON, 0.1)
    behaviors = [stop, fall, violate, find]
    for behavior in behaviors:
        BBCON.add_behavior(behavior)
    print("Added behaviors to BBCON")
    BBCON.active_behaviors = BBCON.behaviors
    lil_pump = Motob()
    lil_pump.motors.stop()
    BBCON.add_motob(lil_pump)
    print("Duck hater initialized")
    button.wait_for_press()
    time.sleep(1)
    while not BBCON.halt:
        BBCON.run_one_timestep()
