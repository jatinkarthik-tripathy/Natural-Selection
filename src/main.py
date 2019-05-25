import pygame
import time
from sprites import Blob, Food

pygame.init()

if __name__ == '__main__':
	# setting up the env in pygame 
	width = 750
	height = 750
	num_blobs = 50
	num_food = 50
	lvl_time = 30
	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Natural Selection')
	win.fill((255, 255, 255))
	running = True
	clock = pygame.time.Clock()

	# blob sprites
	blob_grp = pygame.sprite.Group()
	blob = [ Blob((0, 0, 255)) for i in range(num_blobs) ]
	blob_grp.add(blob)

	for blob in blob_grp.sprites():
		blob.start_pos()
	#food sprites
	food_grp = pygame.sprite.Group()
	food = [ Food() for i in range(num_food) ]
	food_grp.add(food)

	#level time start
	start = time.time()
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
		pygame.draw.rect(win, (200, 200, 200), [20, 20, 710, 710])
		pygame.draw.rect(win, (0, 0, 0), [20, 20, 710, 710], 5)

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


		end = time.time()

		if (end - start) > lvl_time:
			start = end
			
			for blob in blob_grp.sprites():
				if blob.food_count > 0:
					blob.start_pos()
					blob.food_count = 0
				else:
					blob.kill()
			food_grp.empty()
			food = [ Food() for i in range(num_food) ]
			food_grp.add(food)
		else:
			#display updates
			pygame.display.flip()	

