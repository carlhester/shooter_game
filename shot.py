import pygame
from pygame.sprite import Sprite 

class Shot(Sprite):
	def __init__(self, screen, tank):
		super(Shot, self).__init__()
		self.screen = screen
		self.shotSurface = pygame.Surface((5,5), pygame.SRCALPHA).convert()
		self.rect = self.shotSurface.get_rect()
		self.rect.centerx = tank.rect.centerx
		self.rect.centery = tank.rect.centery
		self.shot_speed = 10
		self.color = tank.color
		self.direction = tank.facing
		pygame.draw.rect(self.shotSurface, tank.color, self.rect)
		self.screen.blit(self.shotSurface, self.rect)

	def update(self, shot_group, barrier_group, badguy_group):
		self.shotSurface.fill(self.color)
		self.screen.blit(self.shotSurface, self.rect.center)
		if self.direction == 0: 
			self.rect.centerx += self.shot_speed
		if self.direction == 1:
			self.rect.centerx += self.shot_speed
			self.rect.centery += self.shot_speed
		if self.direction == 2: 
			self.rect.centery += self.shot_speed
		if self.direction == 3:
			self.rect.centerx -= self.shot_speed
			self.rect.centery += self.shot_speed
		if self.direction == 4: 
			self.rect.centerx -= self.shot_speed
		if self.direction == 5:
			self.rect.centerx -= self.shot_speed
			self.rect.centery -= self.shot_speed
		if self.direction == 6: 
			self.rect.centery -= self.shot_speed
		if self.direction == 7:
			self.rect.centerx += self.shot_speed
			self.rect.centery -= self.shot_speed
	
		if pygame.sprite.spritecollideany(self, barrier_group, collided = None):
			shot_group.remove(self)
		
		bad_guy_hit = pygame.sprite.spritecollideany(self, badguy_group, collided = None)
		if bad_guy_hit:
			badguy_group.remove(bad_guy_hit)
			shot_group.remove(self)