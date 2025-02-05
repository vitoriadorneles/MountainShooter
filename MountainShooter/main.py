import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))  # making a window (x,y)
print('Setup End')

print('Loop Start')
while True:  # keeping the window open
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame
