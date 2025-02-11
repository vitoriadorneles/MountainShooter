import pygame

from code.menu import Menu


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # making a window (x,y)

    def run(self, ):
        while True:  # keeping the window open
            menu = Menu(self.window)
            menu.run()
            pass


            # check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # close window
            #        quit()  # end pygame
