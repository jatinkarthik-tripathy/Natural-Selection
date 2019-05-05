import pygame
from sprites import Blob, Food

pygame.init()

if __name__ == '__main__':
	# setting up the env in pygame 
	width = 500
	height = 500
	num_blobs = 50
	num_food = 25
	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Natural Selection')
	win.fill((255, 255, 255))
	running = True
	clock = pygame.time.Clock()

	# blob sprites
	blob_grp = pygame.sprite.Group()
	blob = [ Blob((0, 0, 255)) for i in range(num_blobs) ]
	blob_grp.add(blob)

	#food sprites
	food_grp = pygame.sprite.Group()
	food = [ Food() for i in range(num_food) ]
	food_grp.add(food)
	
	# infinite game loop
	while running:
		# fps
		clock.tick(60)
		# quit check
		for event in pygame.event.get():
			if event.type ==  pygame.QUIT:
				running = False
				pygame.quit()

		#drawing the BG
		pygame.draw.rect(win, (200, 200, 200), [20, 20, 460, 460])
		pygame.draw.rect(win, (0, 0, 0), [20, 20, 460, 460], 5)

		#Updates
		blob_grp.update()
		#food hit check
		food_hit = pygame.sprite.groupcollide(blob_grp, food_grp, False, False, pygame.sprite.collide_circle)
		for b, f in food_hit.items():
			if b.food_count == 0:
				f[0].kill()
				b.food_count += 1
			else:
				pass
		#drawing the blobs and food
		blob_grp.draw(win)
		food_grp.draw(win)

		#display updates
		pygame.display.flip()

