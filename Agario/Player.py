import pygame
from pygame.math import Vector2, Vector3


class Player():

    def __init__(self):
        self.size = 20
        self.position = Vector2(50,50)
        self.direction = Vector2(50,50)
        self.forme = "rond"
        self.color = Vector3(255,0,0)

    def deplacer(self):

        self.position.x = self.direction.x

    def manger(self):

        pass

    def afficher(self,core):

        if self.forme == "rond":
            pygame.draw.circle(core.screen, (int(self.color.x),int(self.color.y),int(self.color.z)),(int(self.position.x),int(self.position.y)),self.size)

    def mourir(self):

        pass

pass





