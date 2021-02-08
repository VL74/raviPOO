from random import random
import core
import pygame
from pygame import Vector2

class drop:
        def __init__(self):
            self.gravity = random.randint(0,10)
            self.size = random.randint(0,25)
            self.R = random.randint(0,255)
            self.V = random.randint(0,255)
            self.B = random.randint(0,255)
            self.position = Vector2(50, 50)

        def tomber(self,tailleFenetre):
            self.position.y = self.position.y+self.gravity
            if(self.position.y > tailleFenetre):
                self.raz()

        def raz(self):
            self.position.y = 0

        def afficher(self,core):
            pygame.draw.line(core.screen, (self.r, self.v, self.b), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)