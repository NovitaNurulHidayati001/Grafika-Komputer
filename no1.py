from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glOrtho(-6, 6, -6, 6, -1, 1)

def ploting():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-5.0, 5.0)
    glVertex2f(-4.0, 4.5)
    glVertex2f(-3.0, 4.0)
    glVertex2f(-2.0, 3.5)
    glVertex2f(-1.0,3.0)
    glVertex2f(0.0,2.5)
    glVertex2f(1.0,2.0)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(100,100)
    glutCreateWindow("no 1")
    glutDisplayFunc(ploting)

    init()
    glutMainLoop()
    
main()
