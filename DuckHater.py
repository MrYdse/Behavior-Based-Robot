from BBCON import *
from Motob import *
from Behavior import *
from Sensob import *
from zumo_button import ZumoButton

if __name__ == '__main__':
    button = ZumoButton()
    BBCON = BBCON()
    fall = FallingOut()
    time.sleep(1)
    duck = DuckFinder()
    time.sleep(1)
    butt = ButtonFeeler()
    peep = Peeper()
    time.sleep(1)
    sensobs = {"fallingout": fall, "duckfinder": duck,
               "buttonfeeler": butt, "peeper": peep}
    for sensob in sensobs:
        BBCON.add_sensob(sensob, sensobs[sensob])
    behaviors = [Stop(BBCON, 1.0), DontFall(BBCON, 1.0),
                 ViolateDuck(BBCON, 0.8), FindDuck(BBCON, 0.8), Wander(BBCON, 0.1)]
    for behavior in behaviors:
        BBCON.add_behavior(behavior)
    BBCON.active_behaviors = BBCON.behaviors
    BBCON.add_motob(Motob())
    print("Duck hater initialized")
    button.wait_for_press()
    while not BBCON.halt:
        BBCON.run_one_timestep()
