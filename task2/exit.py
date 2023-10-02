import pygame
import sys
import os

class Plane:

    width = 250
    height = 250

    def __init__(self, startx, starty):
        exe_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath(".")
        image_path = os.path.join(exe_path, "plane.png")
        self.x = startx
        self.y = starty
        self.full_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.full_image, (self.width, self.height))
        self.velocity = 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.velocity
        