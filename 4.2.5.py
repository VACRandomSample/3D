import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def LS():
    global xrot         # Величина вращения по оси x
    global yrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    global treecolor    
    global lightpos     # Положение источника освещения

    xrot = -29.0                          
    yrot = 50.0                          
    zrot = 0.0                          

    glClearColor(0.5, 0.65, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    lightpos = (100.0, 80.0, 30.0)          # Положение источника освещения по осям xyz

    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glClearDepth ( 1.0 )                            # Задает значение для очистки буфера глубины
    glDepthFunc ( GL_LEQUAL )                       # Задает алгоритм очистки буфера глубины. Удаляет все, что меньше или равно
    glEnable ( GL_DEPTH_TEST )                      # Собственно задание проверки по глубине
    quadric = None # Задание квадрики для использования в модлировании окружности
    greencolor = (0.4, 0.8, 0.0, 0.0) # Зеленый цвет
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos) # Источник света вращаем вместе со сценой (если есть вращение)
# Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                
# Очищаем экран и заливаем серым цветом
    glPushMatrix()                                              
# Сохраняем текущее положение "камеры"
    glRotatef(xrot, 1.0, 0.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glRotatef(zrot, 0.0, 0.0, 1.0)                              
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, greencolor)
def Horse():
    Cylinder(0.10,0.40)

    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslatef(0.04,0.3,0.02)
    Cylinder(0.02,0.20)
    glTranslatef(-0.08,0,0)
    Cylinder(0.02,0.20)

    glTranslatef(0.0,-0.25,0)
    Cylinder(0.02,0.20)
    glTranslatef(0.08,0,0.0)
    Cylinder(0.02,0.20)

    glTranslatef(-0.04,0,0.0)
    glRotatef(135, 1.0, 0.0, 0.0)
    Cylinder(0.01,0.30)

    quadric=gluNewQuadric(); # Create A Pointer To The Quadric Object
    gluQuadricNormals(quadric, GLU_SMOOTH); # Create Smooth Normals
    gluQuadricTexture(quadric, GL_TRUE);
    glTexCoord1f (1)
    glTranslatef(0.0,-0.4,-0.1)
    gluSphere(quadric,0.12,10,10)
    glTranslatef(0, 0, -0.3)
    Cylinder (0.07,0.2)
    return
def Circle(center,radius):
    nvert=50 # Количество вершин аппроксимации (чем боьше, тем точнее окружность)
    pi=3.1415
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center[0],center[1],center[2]) # вершина в центре круга
    for i in range (0,nvert+1):
        a = i/nvert*pi*2.0
        glVertex3f(math.cos(a)*radius+center[0],math.sin(a)*radius+center[1],center[2])
    glEnd()
    return
def Cylinder(radius,height):
    nvert=100 # Количество вершин аппроксимации
    pi=3.1415
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    a = 0
    for i in range (1,nvert+1):
        glBegin(GL_POLYGON)
        b = i/nvert*pi*2.0
        glNormal3f(math.cos((a+b)/2), math.sin((a+b)/2), 0.0 )
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,0)
        glVertex3f(math.cos(b)*radius,math.sin(b)*radius,height)
        glVertex3f(math.cos(a)*radius,math.sin(a)*radius,height)
        a=b
        glEnd()
    glNormal3f(0,0,-1)
    Circle((0,0,0),radius)
    glNormal3f(0,0,1)
    Circle((0,0,height),radius)
    glColor(0.5, 0.25, 0.25, 1.0)
    return
def Tex():
    image = pygame.image.load('skin.jpg')
    datas = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture (GL_TEXTURE_2D, texID)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(),
                  0, GL_RGBA, GL_UNSIGNED_BYTE, datas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)    

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
clock = pygame.time.Clock() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    LS()
    Tex()
    Horse()
    clock.tick(1)
    pygame.display.flip()

