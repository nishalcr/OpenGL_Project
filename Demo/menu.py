from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

value=0

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500.0,500.0,-500.0,500.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if value == 1:
         glClearColor(1,1,1,1)
         return 0
    elif value == 2:
        glClearColor(1.0, 0.0, 0.0,1.0)
    elif value == 3:
        glClearColor(0.0, 1.0, 0.0, 1.0)
    elif value == 4:
        glClearColor(0.0, 0.0, 1.0, 1.0)


def menu(num):
    if num==0:
        sys.exit(0)
    else:
        value=num


def createmenu():
    submenu=glutCreateMenu(menu)
    glutAddMenuEntry("Red",2)
    glutAddMenuEntry("Green",3)
    glutAddMenuEntry("Blue",4)

    menuid=glutCreateMenu(menu)
    glutAddMenuEntry("Clear",1)
    glutAddSubMenu("Color",submenu)
    glutAddMenuEntry("Quit",0)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


if __name__=="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow(b'Menu')
    glutInitWindowPosition(0,0)
    glutInitWindowSize(5000,5000)
    createmenu()
    glutDisplayFunc(display)
    myInit()
    glutMainLoop()
