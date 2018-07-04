import pygame
import sys
import random
from tank import * 
from badguy import * 
from barrier import *
from shot import *

from pygame.sprite import Sprite

def draw_level(DISPLAYSURF, screen_height, screen_width):
	barGroup = pygame.sprite.Group()

	# construct default level - the box
	level = []
	level.append('#' * screen_width)
	for y in range(1, (screen_height/32)-1):
		level.append ('#' + ' ' * ((screen_width/32) - 2) + '#'	)
	level.append('#' * screen_width)
	print level

	# build and return the group of barriers
	board_x = 0
	board_y = 0
	for x in level:
		for y in x:
			if y == "#":
				bar = Barrier(DISPLAYSURF, board_x, board_y, (255,255,255))
				barGroup.add(bar)
			board_x += 32
		board_y += 32
		board_x = 0
	return barGroup

		
def run_game():
	pygame.init()	
	
	screen_width = 640
	screen_height = 480
	bg_color = (0,0,0)
	bar_color = (0,0,255)
	tank_color = (155,155,155)
	DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), 0, 32)
	DISPLAYSURF.fill(bg_color)
	DISPLAY = DISPLAYSURF.get_rect()	

	barGroup = draw_level(DISPLAYSURF, screen_height, screen_width)

	tank1 = Tank(DISPLAYSURF, screen_width/3, screen_height / 2, tank_color, 1)
	tank2 = Tank(DISPLAYSURF, screen_width/3 * 2, screen_height / 2, tank_color, 2)

	shotGroup_1 = pygame.sprite.Group()
	shotGroup_2 = pygame.sprite.Group()

	badguyGroup = pygame.sprite.Group()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				#Player 2 
				if event.key == pygame.K_SPACE:
					if len(shotGroup_2) < 3:
						bullet = Shot(DISPLAYSURF, tank1)
						shotGroup_2.add(bullet)
				if event.key == pygame.K_RIGHT: tank2.turn_right()
				if event.key == pygame.K_LEFT: tank2.turn_left()
				if event.key == pygame.K_UP: tank2.forward = 1
				if event.key == pygame.K_DOWN: tank2.backward = 1
				#Player 1
				if event.key == pygame.K_p:
					if len(shotGroup_1) < 3:
						bullet = Shot(DISPLAYSURF, tank2)
						shotGroup_1.add(bullet)
				if event.key == pygame.K_d: tank1.turn_right()
				if event.key == pygame.K_a: tank1.turn_left()
				if event.key == pygame.K_w: tank1.forward = 1
				if event.key == pygame.K_s: tank1.backward = 1
	
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP: tank2.forward = 0
				if event.key == pygame.K_DOWN: tank2.backward = 0
				if event.key == pygame.K_w: tank1.forward = 0
				if event.key == pygame.K_s: tank1.backward = 0

		while len(badguyGroup) < 3:
			rand_x = random.randint(0,screen_width)
			rand_y = random.randint(0,screen_height)
			rand_side = random.randint(0,3)
			
			if rand_side == 0: 			#left
				rand_x = 16 
			elif rand_side == 1: 		#top
				rand_y = 16
			elif rand_side == 2: 		#right
				rand_x = screen_width - 16
			else: 						#bottom
				rand_y = screen_height - 16 
			badguy = Badguy(DISPLAYSURF, rand_x, rand_y)
			badguyGroup.add(badguy)

		tank1.move(barGroup, badguyGroup)
		tank2.move(barGroup, badguyGroup)


		DISPLAYSURF.fill(bg_color)
		for bar in barGroup:
			bar.update()

		tank1.update()
		tank2.update()


		for badguy in badguyGroup:
			# badguy.move_to_middle(screen_width, screen_height)
			badguy.move_at_tanks(tank1, tank2)
			badguy.update()

		for bullet in shotGroup_1:
			bullet.update(shotGroup_1, barGroup, badguyGroup)

		for bullet in shotGroup_2:
			bullet.update(shotGroup_2, barGroup, badguyGroup)

		pygame.display.update()

		clock = pygame.time.Clock()
		clock.tick(60)
if __name__ == "__main__":
	run_game()



