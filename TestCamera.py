from camera import Camera
import imager2 as IMR
from zumo_button import *


def duck_color():
    camera = Camera(img_width=32, img_height=24)
    button = ZumoButton()
    while True:
        button.wait_for_press()
        image = IMR.Imager(image=camera.update())
        rgb_table = [[image.get_pixel(x, y) for y in range(0, 24)] for x in range(0, 32)]
        for i in range(0, 32):
            for j in range(0, 24):
                print(rgb_table[i][j], end=" ")
            print()
            print()


if __name__ == '__main__':
    duck_color()
