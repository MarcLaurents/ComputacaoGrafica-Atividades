import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Set up the display
pygame.init()
width, height = 800, 600
display = (width, height)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# Set up the perspective
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

# Set up the cube
vertices = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1, -1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1, -1,  1),
    (-1,  1,  1)
)
edges = (
    (0,1),
    (0,3),
    (0,4),
    (1,2),
    (1,5),
    (2,3),
    (2,7),
    (3,6),
    (4,5),
    (4,6),
    (5,7),
    (6,7)
)

# Set up the rotation
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5.0)
glRotatef(0, 0, 1, 0)

# Start the animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen and set the background color
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glClearColor(0.5, 0.5, 0.5, 1.0)

    # Draw the cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Rotate the cube
    glRotatef(1, 0, 1, 0)

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)