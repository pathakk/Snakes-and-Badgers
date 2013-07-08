#---Import libraries--
import pygame
from pygame.locals import*

#--Initialize the game window
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width,height))

#--Set fields	
#-W,A,S,D
keys = [False, False, False, False]
playerpos = [100,100]

#--Load player image
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")



#--Perform the following during entire execution
while 1:
	#--Always fill screen after wiping it out
	screen.fill(0)
	
	#--Scale and add scenery/background
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))

	#--Designate where to draw elements
	screen.blit(player,playerpos)
	#--Update screen contents
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		
		# TO-D0: just looop and make all false???
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				keys[0] = False;
			elif event.key == pygame.K_a:
				keys[1] = False;
			elif event.key == pygame.K_s:
				keys[2] = False;
			elif event.key == pygame.K_d:
				keys[3] = False;

	if keys[2]:
		nextpos = playerpos[1]+5
		if nextpos <470:
			playerpos[1] = nextpos
	elif keys[3]:
		nextpos = playerpos[0] + 5
		if nextpos <600:
			playerpos[0] = nextpos
	elif keys[0]:
		nextpos = playerpos[1]-5
		if nextpos >= 5:
			playerpos[1] = nextpos
	elif keys[1]:
		nextpos = playerpos[0] -5
		if nextpos >=5:
			playerpos[0] = nextpos
