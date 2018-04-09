import pygame
from OpenGL.GL import glBegin, GL_LINES, glVertex3fv, glEnd, glTranslatef, glRotatef, glClear, GL_COLOR_BUFFER_BIT, \
    GL_DEPTH_BUFFER_BIT, GL_LINE, glVertex2fv, glVertex2d
from OpenGL.raw.GLU import gluPerspective


vertices=(
    (1,-1),
    (1,1),
    (-1,1),
    (-1,-1)
)

edges=(
    (0,1),
    (0,3),
    (2,1),
    (2,3)
)
def square():
    glBegin(GL_LINE)
    for edge in edges:
        for vertice in edge:
            glVertex2fv(vertices[vertice])

    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        square()
        pygame.display.flip()
        pygame.time.wait(10)


main()