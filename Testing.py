from camera import Camera
import imager2 as IMR
from zumo_button import *
from reflectance_sensors import ReflectanceSensors
import time
from ultrasonic import Ultrasonic


def duck_color():
    width = 48
    height = 36
    camera = Camera(img_width=width, img_height=height)
    button = ZumoButton()
    while True:
        button.wait_for_press()
        image = IMR.Imager(image=camera.update())
        rgb_table = [[image.get_pixel(x, y) for y in range(0, height)] for x in range(0, width)]
        for i in range(0, width):
            for j in range(0, height):
                print(rgb_table[i][j], end=" ")
            print()
            print()


def edge_detection():
    ir = ReflectanceSensors(max_reading=3000, min_reading=1000)
    button = ZumoButton()
    while True:
        button.wait_for_press()
        reading = ir.update()
        print(reading)
        time.sleep(0.6)


def distance():
    us = Ultrasonic()
    button = ZumoButton()
    while True:
        button.wait_for_press()
        us.update()
        reading = us.get_value()
        print(reading)
        time.sleep(0.6)

if __name__ == '__main__':
    # duck_color()
    # edge_detection()
    distance()
