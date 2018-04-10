from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Creating the view type
def init():
    glClearColor(1.0,0.0,1.0,1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,200.0,0.0,150.0)

#displaying the square
def square():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.4,0.2)
    glBegin(GL_POLYGON)
    glVertex2i(50,50)
    glVertex2i(80,50)
    glVertex2i(80,80)
    glVertex2i(50,80)
    glEnd()
    glFlush()

#main function
if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,100)
    glutInitWindowSize(400,300)
    glutCreateWindow(b'Square')
    init()
    glutDisplayFunc(square)
    glutMainLoop()

