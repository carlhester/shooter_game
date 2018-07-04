import pygame
from pygame.sprite import Sprite 

class Barrier(Sprite):
	def __init__(self, screen, x, y, color):
		super(Barrier, self).__init__()
		self.x = x
		self.y = y
		self.screen = screen
		self.color = color
		self.barSurface = pygame.Surface((32,32), pygame.SRCALPHA).convert()
		self.rect = self.barSurface.get_rect()
		self.rect.left = self.x
		self.rect.top = self.y
		pygame.draw.rect(self.barSurface, self.color, self.rect)
		self.screen.blit(self.barSurface, self.rect)

	def update(self):
		self.barSurface.fill(self.color)
		self.screen.blit(self.barSurface, self.rect)