import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # making a window (x,y)

    def run(self):
        while True:  # keeping the window open
            menu = Menu(self.window)
            menu.run()
            pass



