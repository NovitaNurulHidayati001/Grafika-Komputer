from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgDDA():
    #tentukan titik awal dan akhir
    x1 = 1
    y1 = 1
    x2 = 500
    y2 = 400
    x = x1
    y = y1

    #hitung dx dan dy
    dx = x2 - x1
    dy = y2 - y1

    #hitung steps
    if (dx > dy):
        steps = dx
    else:
        steps = dy

    #hitung perubahan nilai x (x_inc) dan y (y_inc)
    x_inc = dx / steps
    y_inc = dy / steps

    #gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y) #gambar titik awal

    #perulangan untuk menggambar titik-titik
    
    while x < x2:
        x += x_inc
        y += y_inc
        glVertex2f(x,y) #gambar titik

    glEnd()
    glFlush()

if _name_ == '_main_':
    glutInit()
    glutInitWindowSize(640,480)
    glutInitWindowPosition(700,100)
    glutCreateWindow("Algoritma DDA")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()
    glutMainLoop()