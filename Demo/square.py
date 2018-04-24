from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Creating the view type

def init():
    glClearColor(0.0,0.0,0.0,0.0) #Set background color to black and opaque
    glClearDepth(1.0)             #Set background depth to farthest
    glEnable(GL_DEPTH_TEST)       #Enable depth testing for z-culling
    glDepthFunc(GL_LEQUAL)        # Set the type of depth-test
    glShadeModel(GL_SMOOTH)       #Enable Smooth shading
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) #Nice perspective corrections


#displaying the cube
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-8.0,5.0,-25.0)#View changes of the cube can be done here
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)# Green
    glVertex3f(1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,1.0)
    glVertex3f(1.0,1.0,1.0)

    glColor3f(1.0, 0.0, 0.0)  # RED
    glVertex3f(1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(1.0,-1.0,-1.0)

    glColor3f(0.0, 0.0, 1.0)  # BLUE
    glVertex3f(1.0, 1.0,1.0)
    glVertex3f(-1.0, 1.0,1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(1.0,-1.0,1.0)

    glColor3f(1.0,0.5, 0.0)  # ORANGE
    glVertex3f(1.0,-1.0, -1.0)
    glVertex3f(-1.0,-1.0, -1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(1.0, 1.0,-1.0)

    glColor3f(1.0, 1.0, 0.0)  #YELLOW
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)  # Green
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0,-1.0, 1.0)
    glVertex3f(1.0,-1.0,-1.0)

    glEnd()
    glutSwapBuffers()

def reshape(w,h):
    if(h==0):
        h=1
    aspect=w/h
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,aspect,0.1,100.0)

#main functionw
if __name__ ==   "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowPosition(50,100)
    glutInitWindowSize(640,480)
    glutCreateWindow(b'Square')
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutMainLoop()

