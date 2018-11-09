from Sensob import Sensob
from reflectance_sensors import ReflectanceSensors
from camera import Camera
import imager2 as IMR
import time


class FallingOut(Sensob):
    def __init__(self):
        super(FallingOut, self).__init__()
        self.sensor = ReflectanceSensors()
        self.value = []

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value()

    def calibrate(self):
        self.sensor = ReflectanceSensors(auto_calibrate=True)

    def interpret(self):
        danger = 0
        if self.value[0] < 0.1:
            danger = -1
        elif self.value[5] < 0.1:
            danger = 1
        return danger

# class ButtonFeeler(Sensob):


class DuckFinder(Sensob):
    def __init__(self):
        super(DuckFinder, self).__init__()
        self.sensor = Camera(img_width=32, img_height=24)
        self.value = None
        self.K = 12
        self.imager = IMR.Imager(width=32, height=24)

    def update(self):
        self.value = self.sensor.update()  # Image object

    def interpret(self):
        self.imager.set_image(self.value)
        image = self.imager
        rgb_table = [[image.get_pixel(x, y) for y in range(0, 24)] for x in range(0, 32)]
        lines = [0 for x in range(0, 8)]
        index = 0
        for i in range(0, 8):
            for j in range(0, 4):
                for k in range(0, 24):
                    if rgb_table[index][k][0] in range(140, 200) and \
                            rgb_table[index][k][1] in range(160, 180) and \
                            rgb_table[index][k][2] in range(80, 100):
                        lines[i] += 1
                index += 1
        if sum(lines) < self.K:  # If there are not enough duckpixels
            return 2.0
        maximum = (-1, 0)
        position = 0.0  # Value between -1.0 and 1.0 in steps of .25
        for i in range(0, 8):
            if lines[i] > maximum[1]:
                maximum = (i, lines[i])
        if maximum[0] < 4:
            position = (4 - maximum[0]) * -0.25
        else:
            position = (3 - maximum[0]) * 0.25
        return position



if __name__ == '__main__':
    mmmducks = DuckFinder()
    while True:
        mmmducks.update()
        time.sleep(1)
        print(mmmducks.interpret())
