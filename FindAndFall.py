from Sensob import Sensob
import os
from reflectance_sensors import ReflectanceSensors
from camera import Camera
import imager2 as IMR
# import time
from zumo_button import *
from ultrasonic import Ultrasonic


class FallingOut(Sensob):
    def __init__(self):
        super(FallingOut, self).__init__()
        self.sensor = ReflectanceSensors(max_reading=3000, min_reading=1000)
        self.value = []

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()

    def calibrate(self):
        self.sensor = ReflectanceSensors(auto_calibrate=True)

    def interpret(self):
        danger = 0
        if self.value[0] < 0.8:
            danger = -1
        elif self.value[5] < 0.8:
            danger = 1
        return danger


class ButtonFeeler(Sensob):
    def __init__(self):
        super(ButtonFeeler, self).__init__()
        self.sensor = ZumoButton()
        self.button_pressed = False
        self.value = 0

    def update(self):
        if self.sensor.update():
            self.value = 1
        else:
            self.value = 0

    def interpret(self):
        return self.value == 1


class DuckFinder(Sensob):
    def __init__(self):
        super(DuckFinder, self).__init__()
        self.width = 48
        self.height = 36
        self.sensor = Camera(img_width=self.width, img_height=self.height)
        # os.system('rm -f image.png')
        self.value = None
        self.K = 12
        self.imager = IMR.Imager(width=self.width, height=self.height)
        self.interpretation = 2.0

    def reset(self):
        self.value = None
        # os.system('rm -f image.png')
        self.sensor.reset()

    def update(self):
        self.value = self.sensor.update()  # Image object
        self.interpret()

    def interpret(self):
        self.imager.set_image(self.value)
        image = self.imager
        rgb_table = [[image.get_pixel(x, y) for y in range(0, self.height)] for x in range(0, self.width)]
        lines = [0 for x in range(0, 8)]
        index = 0
        for i in range(0, len(lines)):
            for j in range(0, int(self.width/len(lines))):
                for k in range(0, self.height):
                    if rgb_table[index][k][0] > 150 and \
                            rgb_table[index][k][1] > 130 and \
                            rgb_table[index][k][2] < 60:
                        if rgb_table[index][k][0] < 190 and \
                            rgb_table[index][k][1] < 190 and \
                                rgb_table[index][k][2] > 100:
                            lines[i] += 1
                index += 1
        if sum(lines) < self.K:  # If there are not enough duck-pixels
            return 2.0
        maximum = (-1, 0)
        position = 0.0  # Value between -1.0 and 1.0 in steps of .25
        for i in range(0, len(lines)):
            if lines[i] > maximum[1]:
                maximum = (i, lines[i])
        if maximum[0] < 4:
            position = (4 - maximum[0]) * -0.25
        else:
            position = (maximum[0] - 3) * 0.25
        self.interpretation = position
        return position


class Peeper(Sensob):
    def __init__(self):
        super(Peeper, self).__init__()
        self.sensor = Ultrasonic()
        self.value = -1.0
        self.interpretation = 1.0

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()
        self.interpret()

    def interpret(self):
        if self.value > 90:
            self.interpretation = 1.0
        else:
            self.interpretation = self.value/90
        return self.interpretation

    def get_interpretation(self): return self.interpretation


if __name__ == '__main__':
    mmmducks = DuckFinder()
    button = ZumoButton()
    while True:
        mmmducks.update()
        print(mmmducks.interpret())
        button.wait_for_press()
        mmmducks.reset()
