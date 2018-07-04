import pygame
from pygame.sprite import Sprite 
import random

class Badguy(Sprite):
	def __init__(self, screen, x, y):
		super(Badguy, self).__init__()
		self.screen = screen
		self.color = (200,0,0)  
		self.x = x 
		self.y = y 
		self.badguySurf = pygame.Surface((25,25), pygame.SRCALPHA).convert()
		self.rect = self.badguySurf.get_rect()
		self.rect.centerx = self.x 
		self.rect.centery = self.y 
		pygame.draw.rect(self.badguySurf, self.color, self.rect)
		screen.blit(self.badguySurf, self.rect)
		self.active_countdown = 30
		self.badguy_speed = 1

	# def move_to_middle(self, screen_width, screen_height):
	# 	if self.rect.centerx > screen_width / 2:
	# 		self.rect.centerx -= 1
	# 	elif self.rect.centerx < screen_width /2:
	# 		self.rect.centerx += 1
	# 	if self.rect.centery > screen_height / 2:
	# 		self.rect.centery -= 1
	# 	elif self.rect.centery < screen_height /2:
	# 		self.rect.centery += 1

	def move_at_tanks(self, tank1, tank2):
		if self.active_countdown <= 1:
			self.color = (200,0,0)
			if (abs(tank1.rect.centerx - self.rect.centerx) + abs(tank1.rect.centery - self.rect.centery)) < (abs(tank2.rect.centerx - self.rect.centerx) + abs(tank2.rect.centery - self.rect.centery)):
				if self.rect.centerx > tank1.rect.centerx:
					self.rect.centerx -= self.badguy_speed
				elif self.rect.centerx < tank1.rect.centerx:
					self.rect.centerx += self.badguy_speed
				if self.rect.centery > tank1.rect.centery:
					self.rect.centery -= self.badguy_speed
				elif self.rect.centery < tank1.rect.centery:
					self.rect.centery += self.badguy_speed
			else:
				if self.rect.centerx > tank2.rect.centerx:
					self.rect.centerx -= self.badguy_speed
				elif self.rect.centerx < tank2.rect.centerx:
					self.rect.centerx += self.badguy_speed
				if self.rect.centery > tank2.rect.centery:
					self.rect.centery -= self.badguy_speed
				elif self.rect.centery < tank2.rect.centery:
					self.rect.centery += self.badguy_speed
		else:
			color_g = random.randint(10,200)
			self.color = (200,color_g,color_g+10)
			self.active_countdown -= 1
	
	def update(self):
		self.badguySurf.fill(self.color)
		self.screen.blit(self.badguySurf, self.rect)