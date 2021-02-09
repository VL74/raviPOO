from pygame.math import Vector2, Vector3
import pygame

class Bille():

    def __init__(self):
        self.size = 5
        self.position_cible = Vector2(50,50)
        self.direction = Vector2(50,50)
        self.color = Vector3(50,50,50)

    def suivre(self):

        pass

    def mourir(self):

        pass

    def manger(self):

        pass

    def afficher(self):

        pygame.draw.circle(self.size,self.color,self.position_cible,)

    pass