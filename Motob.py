from motors import *


class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = ("L", 45)

    def update(self, value):
        self.value = value
        self.operationalize()

    def operationalize(self):
        if self.value[0] == "L":
            self.motors.stop()
            self.motors.left(self.value[1]/100)
        elif self.value[0] == "R":
            self.motors.stop()
            self.motors.right(self.value[1]/100)
        elif self.value[0] == "F":
            # Drive forwards with speed self.value[1]
            self.motors.forward(self.value[1]/100)
        elif self.value[0] == "B":
            # Drive backwards with speed self.value[1]
            self.motors.backward(self.value[1]/100)
        elif self.value[0] == "BL":
            s = int(self.motors.max * self.value[1]/100)
            self.motors.set_left_dir(1)
            self.motors.set_left_speed(0)
            self.motors.set_right_dir(0)
            self.motors.set_right_speed(s)
        elif self.value[0] == "BR":
            s = int(self.motors.max * self.value[1] / 100)
            self.motors.set_left_dir(0)
            self.motors.set_left_speed(s)
            self.motors.set_right_dir(1)
            self.motors.set_right_speed(0)
        elif self.value[0] == "S":
            self.motors.stop()
