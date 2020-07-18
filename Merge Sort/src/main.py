from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


class Cube:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, number):
        self.value = int(number)
        self.x = Cube.x + 12.0
        self.y = Cube.y + 12.0
        self.z = Cube.z + 12.0
        self.image = "img_" + number + "_.jpg"  # image path


def main():
    arr_list = []
    print("\tEnter the values to sort:\n")
    for i in range(0, 8):
        arr_list.append(Cube(input()))

