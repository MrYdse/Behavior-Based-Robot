from motors import Motors


class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = ("L", 45)

    def update(self, value):
        self.value = value
        self.operationalize()

    def operationalize(self):
        if self.value[0] == "L":
            # Try to swing self.value[1] degrees to the left
            self.motors.left(self.value[1]/90)
        elif self.value[0] == "R":
            # Try to swing self.value[1] degrees to the right
            self.motors.right(self.value[1]/90)
        elif self.value[0] == "F":
            # Drive forwards with speed self.value[1]
            self.motors.forward(self.value[1]/100)
        elif self.value[0] == "B":
            # Drive backwards with speed self.value[1]
            self.motors.backward(self.value[1]/100)
        elif self.value[0] == "S":
            self.motors.stop()
