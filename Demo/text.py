from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

name = ('Pratheek T')


def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-50, 500, -50, 500)


def drawText():
    glRasterPos2f(0, 450)
    for c in name:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    drawText()
    glFlush()
    return


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'text')
    myInit()
    glutDisplayFunc(display)
    glutMainLoop()
