from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
from random import *
from math import *

M_PI = pi
M_PI_2 = pi / 2.0
MAX_CUBE=10
moving= GL_FALSE
s=("Top of the stack")
name=('Pratheek T')
VOID, CLEAR,ADD_PLANE, REMOVE_PLANE,COLOR, MOTION_ON, MOTION_OFF, QUIT = list(range(8))
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
    c = cube(0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0,0.0, 0.0)
    cubes.append(c)


def drawText():
    glRasterPos2f(2,0)
    for c in s:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

def ccube():

    for n in range(MAX_CUBE):

        if(cubes[n].speed !=0):
            glPushMatrix()

            glTranslate(cubes[n].x,cubes[n].y,cubes[n].z)

            glTranslate(0.0, (n * 2.5) + (-9.0), -15.0)
            glRotatef(cubes[n].theta, 1.0, 0.0, 0.0)
            glRotatef(cubes[n].theta, 0.0, 1.0, 0.0)
            glRotatef(cubes[n].theta, 1.0, 0.0, 1.0)
            glColor3f(1.0, 1.0, 1.0)
            drawText()

            glScalef(2.0 , 2.0 , 2.0 )
            glBegin(GL_QUADS)
            red=cubes[n].red
            green=cubes[n].green
            blue=cubes[n].blue

            glColor3f(red, green, blue)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)

            glColor3f(red, 0, blue)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)

            glColor3f(red, green, 0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)

            glColor3f(0, green, blue)
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


def display():
    glClear(GL_DEPTH_BUFFER_BIT)
    # paint black to blue smooth shaded polygon for background
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-20.0, 20.0, -19.0)
    glVertex3f(20.0, 20.0, -19.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(20.0, -20.0, -19.0)
    glVertex3f(-20.0, -20.0, -19.0)
    glEnd()
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)

    ccube()
    glFlush()
    glutSwapBuffers()

def tick_per_plane(i):
    cubes[i].theta += cubes[i].speed
    theta = cubes[i].theta
    cubes[i].z = -15.0
    cubes[i].x = 0.0
    cubes[i].y = (i * 2.5) + (-9.0)
    cubes[i].angle = ((atan(2.0) + M_PI_2) * sin(theta) - M_PI_2) * 180 / M_PI
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


def remove_cube():
    for i in range(MAX_CUBE - 1, -1, -1):
        if (cubes[i].speed != 0):
            cubes[i].speed = 0
            if (not moving):
                glutPostRedisplay()
            return
    return

def tick():

    for i in range(MAX_CUBE):
        cubes[i].theta+=0.5
        while cubes[i].theta>360.0:
            cubes[i].theta -= 0.5

        print(cubes[i].z,cubes[i].x, cubes[i].y)
    return

def animate():
    tick()
    glutPostRedisplay()
    return

def visible(state):
    if (state == GLUT_VISIBLE):
        if (moving):
            glutIdleFunc(animate)
    else:
        if (moving):
            glutIdleFunc(None)
    return

def motion_on():
    moving = GL_TRUE
    glutChangeToMenuEntry(4, "Motion off", MOTION_OFF)
    glutIdleFunc(animate)
    return


def motion_off():
    moving = GL_FALSE
    glutChangeToMenuEntry(4, "Motion", MOTION_ON)
    glutIdleFunc(None)
    return

def clear():
    return




def color(item):
    colordict[item]()
    return 0

def doquit():
    sys.exit(0)












menudict = {CLEAR:clear,
            ADD_PLANE: add_cube,
            REMOVE_PLANE: remove_cube,
            MOTION_ON:motion_on,
            MOTION_OFF:motion_off,
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
    glutAddMenuEntry("Push", ADD_PLANE)
    glutAddMenuEntry("Pop", REMOVE_PLANE)
    glutAddMenuEntry("Motion", MOTION_ON)
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
    glutVisibilityFunc(visible)
    glClearDepth(2.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 30)
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()

