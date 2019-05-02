import pygame
from sprites import Blob, Food

pygame.init()

if __name__ == '__main__':
	# setting up the env in pygame 
	width = 500
	height = 500
	win = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Natural Selection')
	win.fill((255, 255, 255))
	running = True
	clock = pygame.time.Clock()

	# blob sprites
	blob_grp = pygame.sprite.Group()
	blob = Blob((0, 0, 255))
	blob_grp.add(blob)
	
	# infinite game loop
	while running:
		# fps
		clock.tick(60)
		# quit check
		for event in pygame.event.get():
			if event.type ==  pygame.QUIT:
				running = False
				pygame.quit()

		pygame.draw.rect(win, (200, 200, 200), [20, 20, 460, 460])
		pygame.draw.rect(win, (0, 0, 0), [20, 20, 460, 460], 5)

		blob_grp.draw(win)

		pygame.display.flip()

