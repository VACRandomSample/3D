import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def LineSegment():
    global xrot         
    global yrot         
    global ambient     
    global treecolor    
    global lightpos     

    xrot = 150.0                          
    yrot = 150.0                          
    zrot = 0.0                          

    glClearColor(0.5, 0.65, 0.5, 1.0)           
    lightpos = (-150.0,80.0, 10.0)        

    glEnable(GL_LIGHTING)                         
    glEnable(GL_LIGHT0)                 
    glClearDepth ( 1.0 )                
    glDepthFunc ( GL_LEQUAL )          
    glEnable ( GL_DEPTH_TEST )            
    quadric = None 
    greencolor = (0.4, 0.8, 0.0, 0.0) 
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                
    glPushMatrix()
    #Camera
    glRotatef(xrot, 1.0, 0.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)
    
def Tab(x1, x2, y1, y2, z1, z2):
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
    glBegin ( GL_POLYGON )#Правая стена
    glNormal3f ( -1.0, 0.0, 0 )
    glVertex3f ( x1, y1, z1 )
    glVertex3f ( x1, y1, z2 )
    glVertex3f ( x1, y2, z2 )
    glVertex3f ( x1, y2, z1 )
    glEnd ()
    glBegin ( GL_POLYGON )#Левая стена
    glNormal3f ( 1.0, 0.0, 0 )
    glVertex3f ( x2, y1, z2 )
    glVertex3f ( x2, y1, z1 )
    glVertex3f ( x2, y2, z1 )
    glVertex3f ( x2, y2, z2 )
    glEnd ()
    glBegin ( GL_POLYGON )#Пол
    glNormal3f ( 0.0, 1.0, 0 )
    glVertex3f ( x1, y2, z2 )
    glVertex3f ( x2, y2, z2 )
    glVertex3f ( x2, y2, z1 )
    glVertex3f ( x1, y2, z1 )
    glEnd ()
    glBegin ( GL_POLYGON )#Потолок
    glNormal3f ( 0.0, -1.0, 0 )
    glVertex3f ( x2, y1, z2 )
    glVertex3f ( x1, y1, z2 )
    glVertex3f ( x1, y1, z1 )
    glVertex3f ( x2, y1, z1 )
    glEnd()
    Polka(0.0,0.2,0.3,0.4,0.3,0.0)
    Polka(0.0,0.1,0.3,0.4,0.3,0.0)
    Polka(0.0,-0.1,0.3,0.4,0.3,0.0)
    Polka(0.0,-0.2,0.3,0.4,0.3,0.0)
def Polka(x1,y1,z1,x2,y2,z2):
    glBegin ( GL_POLYGON )#Потолок
    glNormal3f ( 0.0, -1.0, 0 )
    glVertex3f ( x2, y1, z2 )
    glVertex3f ( x1, y1, z2 )
    glVertex3f ( x1, y1, z1 )
    glVertex3f ( x2, y1, z1 )
    glEnd()
def Tex():
    image = pygame.image.load('wood.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)
    
pygame.init()
display = (1000, 670)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    glRotatef(1, 1, 1, 1)  
    LineSegment()
    Tex()
    Tab(0.0,0.4,-0.4,0.4,0.3,0.0)
    clock.tick(1)
    pygame.display.flip()

