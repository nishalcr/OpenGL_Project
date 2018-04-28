from OpenGL.GL import *
# from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw_text(x, y, z, text, r, g, b):
    glColor3f(r, g, b)
    glRasterPos3f(x, y, z)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))


def my_display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glLoadIdentity()
    draw_text(10.0, 10.0, 0.0, "HELLO WORLD", 0.0, 0.0, 0.0)


def my_reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-100.0, 100.0, -100.0 * (h / w), 100.0 * (h / w), -100.0, 100.0)
    else:
        glOrtho(-100.0 * (h / w), 100.0 * (h / w), -100.0, 100.0, -100.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b'START PAGE')
    glutDisplayFunc(my_display)
    glutReshapeFunc(my_reshape)
    glutMainLoop()
