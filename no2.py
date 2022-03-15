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
    glVertex2f( 4.0, 3.0)
    glVertex2f( 5.0, 1.75)
    glVertex2f(6.0, 0.5)
    glVertex2f(7.0, - 0.75)
    glVertex2f(8.0, -2)
    glEnd() 
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(800,800)
    glutInitWindowPosition(100,100)
    glutCreateWindow("no 2")
    glutDisplayFunc(ploting)

    init()
    glutMainLoop()
    
main()
