import pygame
from pygame.sprite import Sprite
import sys

class Tank(Sprite):
	def __init__(self, screen, x, y, color, player):
		super(Tank, self).__init__()
		self.x = x
		self.y = y
		self.screen = screen
		self.color = color
		self.forward_speed = 5
		self.backward_speed = 3
		if player == 1:
			self.tankSurf = pygame.image.load('tank-red.png')
			self.tankSurf = pygame.transform.scale(self.tankSurf, (32, 32))
			self.tankSurf2 = pygame.image.load('tank-red-45.png')
			self.tankSurf2 = pygame.transform.scale(self.tankSurf2, (32, 32))
			self.facing = 0

		if player == 2:
			self.tankSurf = pygame.image.load('tank-blue.png')
			self.tankSurf = pygame.transform.scale(self.tankSurf, (32, 32))
			self.tankSurf2 = pygame.image.load('tank-blue-45.png')
			self.tankSurf2 = pygame.transform.scale(self.tankSurf2, (32, 32))

		self.drawnSurf = self.tankSurf
		self.rect = self.tankSurf.get_rect()	
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.tankSurf, self.rect)
		self.orig45 = 1
		self.facing = 0
		self.turned_left = 0
		self.turned_right = 0
		self.forward = 0
		self.backward = 0

	def move(self, barrier_group, badguy_group):
		save_center = self.rect.center
		if self.forward == 1:
			self.backward = 0
			if self.facing == 0: 
				self.rect.centerx += self.forward_speed
			if self.facing == 1: 
				self.rect.centery += self.forward_speed
				self.rect.centerx += self.forward_speed
			if self.facing == 2: 
				self.rect.centery += self.forward_speed
			if self.facing == 3: 
				self.rect.centery += self.forward_speed
				self.rect.centerx -= self.forward_speed
			if self.facing == 4: 
				self.rect.centerx -= self.forward_speed
			if self.facing == 5: 
				self.rect.centery -= self.forward_speed
				self.rect.centerx -= self.forward_speed
			if self.facing == 6: 
				self.rect.centery -= self.forward_speed
			if self.facing == 7: 
				self.rect.centerx += self.forward_speed
				self.rect.centery -= self.forward_speed

		if self.backward == 1:
			if self.facing == 0: 
				self.rect.centerx -= self.backward_speed
			if self.facing == 1: 
				self.rect.centery -= self.backward_speed
				self.rect.centerx -= self.backward_speed
			if self.facing == 2: 
				self.rect.centery -= self.backward_speed
			if self.facing == 3: 
				self.rect.centery -= self.backward_speed
				self.rect.centerx += self.backward_speed
			if self.facing == 4: 
				self.rect.centerx += self.backward_speed
			if self.facing == 5: 
				self.rect.centery += self.backward_speed
				self.rect.centerx += self.backward_speed
			if self.facing == 6: 
				self.rect.centery += self.backward_speed
			if self.facing == 7: 
				self.rect.centerx -= self.backward_speed
				self.rect.centery += self.backward_speed

		if pygame.sprite.spritecollideany(self, badguy_group, collided = None):
			#just kill it for now if we lose
			SPLAT

		if pygame.sprite.spritecollideany(self, barrier_group, collided = None):
			self.rect.center = save_center


	def turn_right(self):
		self.facing += 1
		if self.facing > 7:
			self.facing = 0
		self.set_facing(self.facing)

	def turn_left(self):
		self.facing -= 1
		if self.facing < 0:
			self.facing = 7 
		self.turned_left = 1
		self.set_facing(self.facing)

	def set_facing(self, direction):
		if direction == 0:
			self.drawnSurf = self.tankSurf
		if direction == 1:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf2, -90)
		if direction == 2:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf, -90)
		if direction == 3:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf2, 180)
		if direction == 4:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf, 180)
		if direction == 5:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf2, 90)
		if direction == 6:
	 		self.drawnSurf = pygame.transform.rotate(self.tankSurf, 90)
		if direction == 7:
	 		self.drawnSurf = self.tankSurf2

	def update(self):
		self.screen.blit(self.drawnSurf, self.rect)