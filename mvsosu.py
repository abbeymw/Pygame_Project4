import random
import sys
import pygame
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN

x_max = 800
y_max = 600

left, right, up, down = 0, 1, 3, 4
start, stop = 0, 1

class UMsprite(pygame.sprite.Sprite):
	def __init__(self, groups, weapon_groups):
		self.image = pygame.image.load("wolv.bmp").convert()
		self.rect = self.image.get_rect()
		self.rect.center = (x_max/2, y_max - 40)
		self.dx = self.fy = 0
		self.firing = self.shot = False
		self.health = 100
		self.score = 0

		self.groups = [groups, weapon_groups]

		self.mega = 1

		self.autopilot = False
		self.in_position = False
		self.velocity = 3