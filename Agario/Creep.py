import random

import pygame
from pygame.math import Vector3, Vector2

from p5 import core


class Creep():

    def __init__(self):
        self.size = 2
        self.color = Vector3(0,255,0)
        self.position = Vector2(random.randint(0,400),random.randint(0,400))

    def afficher(self,core):

        pygame.draw.circle(core.screen, (int(self.color.x), int(self.color.y), int(self.color.z)),
                            (int(self.position.x), int(self.position.y)), self.size)

    def mourir(self):

        self.size = 0

    pass