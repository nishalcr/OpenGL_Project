from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGL.GL import *
import time
try:
    from PIL.Image import open
except :
    from Image import open
class TestContext( BaseContext ):

    initialPosition = (0,0,0) # set initial camera position, tutorial does the re-positioning

    def OnInit(self):
        """Load the image on initial load of the application"""
        self.imageID = self.loadImage()

    def loadImage(self, imageName="nehe_wall.bmp"):
        """Load an image file as a 2D texture using PIL"""
        im = open(imageName)
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)

        ID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0,GL_RGBA, GL_UNSIGNED_BYTE, image)
        return ID

    def Render(self, mode):
            """Render scene geometry"""
            BaseContext.Render(self, mode)
            glDisable(GL_LIGHTING)  # context lights by default
            glTranslatef(1.5, 0.0, -6.0);
            glRotated(time.time() % (8.0) / 8 * -360, 1, 0, 0)
            self.setupTexture()
            self.drawCube()

    def setupTexture(self):
        """Render-time texture environment setup"""
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.imageID)

    def drawCube(self):
        """Draw a cube with texture coordinates"""
        glBegin(GL_QUADS);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, 1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, 1.0, 1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0);
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0);
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, 1.0, 1.0);
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0);
        glEnd()

    def OnIdle(self, ):
        """Request refresh of the context whenever idle"""
        self.triggerRedraw(1)
        return 1

if __name__ == "__main__":
        TestContext.ContextMainLoop()