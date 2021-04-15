import pygame
pygame.init()

pygame.joystick.init()
screen = pygame.display.set_mode((500, 700))

joy = pygame.joystick.Joystick(0)
joy.init()
done = True
while(done):
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = False # Flag that we are done so we exit this loop.
    J = []
    for i in range(joy.get_numaxes()):
        J.append(joy.get_axis(i))

    print(J)