import sys

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    draw_text(1, 1, 'HELLO \n This is the start page.')
    glFlush()
    glutSwapBuffers()


def my_reshape(w, h):
    glViewport(0, 0, int(w), int(h))
    glColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if w <= h:
        glOrtho(-100.0, 100.0, -100.0 * h / w, 100.0 * h / w, -10.0, 10.0)
    else:
        glOrtho(-100.0 * w / h, 100.0 * w / h, -100.0, 100.0, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b'Start Page')
    glutDisplayFunc(display)
    glutReshapeFunc(my_reshape)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


main()
