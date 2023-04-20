import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Define the vertices of the square
vertices = (
    (1, -1, 0),
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0)
)

def draw_square():
    # Begin rendering
    glBegin(GL_QUADS)

    # Set color to green
    glColor3f(0.0, 1.0, 0.0)

    # Draw the square
    for vertex in vertices:
        glVertex3fv(vertex)

    # End rendering
    glEnd()

def main():
    # Initialize Pygame
    pygame.init()

    # Set the display mode and size
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Set up the OpenGL viewport
    glViewport(0, 0, 800, 600)

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Set up the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

    # Enable depth testing
    glEnable(GL_DEPTH_TEST)

    # Loop until the user closes the window
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the square
        draw_square()

        # Swap the buffers
        pygame.display.flip()

if __name__ == "__main__":
    main()
