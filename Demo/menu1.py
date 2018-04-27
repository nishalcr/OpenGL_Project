from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)


VOID, CLEAR, COLOR, QUIT = list(range(4))

def clear():
    return


def color():
    glClearColor(1.0,0.0,0.0,1.0)
    return


def doquit():
    sys.exit(0)
    return


menudict = {CLEAR: clear,
            COLOR: color,
            QUIT: doquit}


def dmenu(item):
    menudict[item]()
    return 0

def reshape(w,h):
    if(h==0):
        h=1
    aspect=w/h
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,aspect,0.1,100.0)

if __name__=="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow(b'Menu')
    glutInitWindowPosition(0,0)
    glutInitWindowSize(5000,5000)
    glutReshapeFunc(reshape)
    glutCreateMenu(dmenu)
    glutAddMenuEntry("Add plane", CLEAR)
    glutAddMenuEntry("Remove plane", COLOR)
    glutAddMenuEntry("Quit", QUIT)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutDisplayFunc(display)
    glutMainLoop()