from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
import math
import sys

def LS():   
    global xrot       
    global yrot        
    global ambient  
    global lightpos     

    xrot = 170.0                          
    yrot = 170.0                          
    zrot = -90.0                          

    glClearColor(0.5, 0.65, 0.5, 1.0)               
    lightpos = (0.0, 0.0, -30.0)                 
    
    glEnable(GL_LIGHTING)                       
    glEnable(GL_LIGHT0)      
    glClearDepth ( 1.0 )                    
    glDepthFunc ( GL_LEQUAL )              
    glEnable ( GL_DEPTH_TEST )   
    quadric = None
    greencolor = (0.4, 0.8, 0.0, 0.2) 
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                
    glPushMatrix()                                              
    glRotatef(xrot, 1.0, 0.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)
def Tex():
    image = pygame.image.load('photo.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)    
def Flower():
    quadric=gluNewQuadric(); 
    gluQuadricNormals(quadric, GLU_SMOOTH); 
    gluQuadricTexture(quadric, GL_TRUE);
    glTexCoord1f (1)
    glTranslatef(0.0,0.0,0.0)
    gluSphere(quadric,0.150,150,150)
    glTranslatef(0.1,0.0,0.0)
    gluSphere(quadric,0.120,100,100)
    glTranslatef(-0.1,0.1,0.0)
    gluSphere(quadric,0.120,100,100)
    glTranslatef(0.0,-0.2,0.0)
    gluSphere(quadric,0.120,100,100)
    glTranslatef(0.0,0.2,0.0)
    gluSphere(quadric,0.120,100,100)
    glTranslatef(-0.1,-0.1,0.0)
    gluSphere(quadric,0.120,100,100)
    return
pygame.init()
dp = (800,600)
pygame.display.set_mode(dp,DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    glRotatef(0, 0, 0, 0)        
    LS()
    Tex()
    Flower()
    clock.tick(1)
    pygame.display.flip()
