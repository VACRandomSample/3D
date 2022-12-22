from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
import math
import sys

global xrot         # Величина вращения по оси x
global yrot         # Величина вращения по оси y
global ambient      # Рассеянное освещение  
global lightpos     # Положение источника освещения

xrot = 150.0                          
yrot = 150.0
zrot = 0.0

def LS():                      
    glClearColor(1.0, 1.0, 1.0, 1.0)            
    lightpos = (-80.0, 80.0, 30.0)               
    
    glEnable(GL_LIGHTING)                       
    glEnable(GL_LIGHT0)                 
    glClearDepth ( 1.0 )   
    glEnable ( GL_DEPTH_TEST )              
    greencolor = (1.0, 1.0, 1.0, 1.0) 
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                
    glPushMatrix()                                              
    glRotatef(xrot, 1.0, 0.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)

def Tex():
    image = pygame.image.load('brick.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

def Home():
    #Основание
    glBegin(GL_POLYGON)
    glNormal3f ( 0.0, 0.0, 1 )#Задняя стенка
    glTexCoord2f (0,0)
    glVertex3f ( x1, y1, z2 )
    glTexCoord2f (1,0)
    glVertex3f ( x2, y1, z2 )
    glTexCoord2f (1,1)
    glVertex3f ( x2, y2, z2 )
    glTexCoord2f (0,1)
    glVertex3f ( x1, y2, z2 )
    glEnd ()
    glBegin ( GL_POLYGON )#Передняя стенка
    glNormal3f ( 0.0, 0.0, -1 )
    glTexCoord2f (1,0)
    glVertex3f ( x2, y1, z1 )
    glTexCoord2f (0,0)
    glVertex3f ( x1, y1, z1 )
    glTexCoord2f (0,1)
    glVertex3f ( x1, y2, z1 )
    glTexCoord2f (1,1)
    glVertex3f ( x2, y2, z1 )
    glEnd ()
    glBegin ( GL_POLYGON )#Правая стена
    glNormal3f ( -1.0, 0.0, 0 )
    glTexCoord2f (0,0)
    glVertex3f ( x1, y1, z1 )
    glTexCoord2f (0,1)
    glVertex3f ( x1, y1, z2 )
    glTexCoord2f (1,1)
    glVertex3f ( x1, y2, z2 )
    glTexCoord2f (1,0)
    glVertex3f ( x1, y2, z1 )
    glEnd ()
    glBegin ( GL_POLYGON )#Левая стена
    glNormal3f ( 1.0, 0.0, 0 )
    glTexCoord2f (0,1)
    glVertex3f ( x2, y1, z2)
    glTexCoord2f (0,0)
    glVertex3f ( x2, y1, z1 )
    glTexCoord2f (1,0)
    glVertex3f ( x2, y2, z1 )
    glTexCoord2f (1,1)
    glVertex3f ( x2, y2, z2 )
    glEnd ()
    glBegin ( GL_POLYGON )#Пол
    glNormal3f ( 0.0, 1.0, 0 )
    glTexCoord2f (0,1)
    glVertex3f ( x1, y2, z2 )
    glTexCoord2f (1,1)
    glVertex3f ( x2, y2, z2 )
    glTexCoord2f (1,0)
    glVertex3f ( x2, y2, z1 )
    glTexCoord2f (0,0)
    glVertex3f ( x1, y2, z1 )
    glEnd ()
    glBegin ( GL_POLYGON )#Потолок
    glNormal3f ( 0.0, -1.0, 0 )
    glTexCoord2f (1,1)
    glVertex3f ( x2, y1, z2 )
    glTexCoord2f (0,1)
    glVertex3f ( x1, y1, z2 )
    glTexCoord2f (0,0)
    glVertex3f ( x1, y1, z1 )
    glTexCoord2f (1,0)
    glVertex3f ( x2, y1, z1 )
    glEnd()
    Krisha()
def Krisha():
    #Крыша
    glBegin (GL_POLYGON)
    glNormal3f(0.0,1.0,-1.0)
    glTexCoord2f (0,1)
    glVertex3f(x1, y1, z2)
    glTexCoord2f (1,0)
    glVertex3f(x2, y1, z2)
    glTexCoord3f (1,1,1)
    glVertex3f((x2/2), (-y2/2), ((z1+z2)/2))
    glEnd()
    glBegin (GL_POLYGON)
    glNormal3f(1.0,1.0,0.0)
    glTexCoord2f (0,0)
    glVertex3f(x1,y1,z1)
    glTexCoord2f (0,1)
    glVertex3f(x1, y1, z2)
    glTexCoord3f (1,1,1)
    glVertex3f((x2/2), (-y2/2), ((z1+z2)/2))
    glEnd()
    glBegin (GL_POLYGON)
    glNormal3f(-1.0,-1.0,0.0)
    glTexCoord2f (1,1)
    glVertex3f(x2, y1, z2)
    glTexCoord2f (1,0)
    glVertex3f(x2, y1, z1)
    glTexCoord3f (1,1,1)
    glVertex3f((x2/2), (-y2/2), ((z1+z2)/2))
    glEnd()
    glBegin (GL_POLYGON)
    glNormal3f(0.0,-1.0,1.0)
    glTexCoord2f (1,0)
    glVertex3f ( x2, y1, z1 )
    glTexCoord2f (0,0)
    glVertex3f ( x1, y1, z1 )
    glTexCoord3f (1,1,1)
    glVertex3f ((x2/2), (-y2/2), ((z1+z2)/2))
    glEnd()
    return
pygame.init()
dp = (800,600)
pygame.display.set_mode(dp,DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()
#==========
x1 = 0.0
x2 = 0.7
y1 = 0.1
y2 = 0.7
z1 = -0.3
z2 = 0.4
#==========

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    glRotatef(0, 0, 0, 0)  
    LS()
    Tex()
    Home()
    clock.tick(1)
    pygame.display.flip()
    
