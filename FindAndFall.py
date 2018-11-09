from Sensob import Sensob
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from PIL import Image, ImageFilter, ImageEnhance


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
        self.sensor = Camera()
        self.value = None

    def update(self):
        self.sensor.update()
        self.value = self.sensor.get_value() # Image object

    def interpret(self):
        pass

