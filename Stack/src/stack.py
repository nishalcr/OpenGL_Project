from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
from random import *
from math import *

M_PI = pi
M_PI_2 = pi / 2.0
MAX_CUBE=8
moving= False


VOID, CLEAR,PUSH,POP,COLOR, QUIT = list(range(6))
VOID, RED, GREEN,BLUE =list(range(4))
class cube(object):
    def __init__(self, speed, red, green, blue, theta, x, y, z, angle):
        self.speed = speed
        self.red = red
        self.green = green
        self.blue = blue
        self.theta = theta
        self.angle = angle
        self.x = x
        self.y = y
        self.z = z


cubes=[]
rgblist = [(1.0, 0.0, 0.0),  # red
           (1.0, 1.0, 1.0),  # white
           (0.0, 1.0, 0.0),  # green
           (1.0, 0.0, 1.0),  # magenta
           (1.0, 1.0, 0.0),  # yellow
           (0.0, 1.0, 1.0)  # cyan
           ]


colordict={}

for n in range(MAX_CUBE):
    c = cube(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -7.0, -30.0, 0.0)
    cubes.append(c)

def display():
    glClear(GL_DEPTH_BUFFER_BIT)
    # paint black to blue smooth shaded polygon for background
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-20.0, 20.0, -19.0)
    glVertex3f(20.0, 20.0, -19.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(20.0, -20.0, -19.0)
    glVertex3f(-20.0, -20.0, -19.0)
    glEnd()
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    for n in range(MAX_CUBE):
        if(cubes[n].speed !=0):
            glPushMatrix()
            #glTranslate(0.0,-7.0,-15.0)
            glTranslate(0.0,(n*2.5)+(-9.0),-15.0)
            #glRotatef(90,1.0,0.0,0.0)
            #glScalef(1.0 , 1.5 , 1.0 )
            glBegin(GL_QUADS)
            red=cubes[n].red
            green=cubes[n].green
            blue=cubes[n].blue

            glColor3f(red, green, blue)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)

            glColor3f(red, green, blue)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)

            glColor3f(red, green, blue)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)

            glColor3f(red, green, blue)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)

            glColor3f(red, green, blue)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, 1.0)

            glColor3f(0, 0, blue)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, -1.0)

            glEnd()
            glPopMatrix()
    glutSwapBuffers()


def tick_per_plane(i):

    if (cubes[i].speed < 0.0):
        cubes[i].angle += 45.0
    return

def add_cube():
    for i in range(MAX_CUBE):
        if (cubes[i].speed == 0.0):
            cubes[i].red, cubes[i].green, cubes[i].blue = choice(rgblist)
            cubes[i].speed = -0.001
            if (getrandbits(32) & 0x1):
                cubes[i].speed *= -1
                cubes[i].theta = float(randint(0, 256)) * 0.1111
            tick_per_plane(i)
            if (not moving):
                glutPostRedisplay()
            return
    return


def clear():
    glutSwapBuffers()
    glutPostRedisplay()
    glClear(GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-20.0, 20.0, -19.0)
    glVertex3f(20.0, 20.0, -19.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(20.0, -20.0, -19.0)
    glVertex3f(-20.0, -20.0, -19.0)
    glEnd()
    return

def remove_cube():
    for i in range(MAX_CUBE - 1, -1, -1):
        if (cubes[i].speed != 0):
            cubes[i].speed = 0
            if (not moving):
                glutPostRedisplay()
            return
    return


def color(item):
    colordict[item]()
    return 0

def doquit():
    sys.exit(0)



menudict = {CLEAR:clear,
            PUSH: add_cube,
            POP: remove_cube,
            COLOR:color,
            QUIT: doquit}

def menu(item):
    menudict[item]()
    return 0

def createmenu():
    submenuid = glutCreateMenu(color)
    glutAddMenuEntry("Red", RED)
    glutAddMenuEntry("Blue", BLUE)
    glutAddMenuEntry("Green", GREEN)

    menu_id = glutCreateMenu(menu)
    glutAddMenuEntry("Clear",CLEAR)
    glutAddMenuEntry("Push", PUSH)
    glutAddMenuEntry("Pop", POP)
    glutAddMenuEntry("Quit", QUIT)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

if __name__=="__main__":
    glutInit(sys.argv)
    glutInitWindowSize(800,600)
    glutInitWindowPosition(110,80)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE|GLUT_DEPTH|GLUT_MULTISAMPLE)
    glutCreateWindow(b'Stack')
    glutDisplayFunc(display)
    createmenu()
   # glutReshapeFunc(reshape)

#    glClearDepth(1.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 30)
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()

