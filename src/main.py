import pygame
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

	# infinite game loop
	while running:
		# fps
		clock.tick(60)
		# quit check
		for event in pygame.event.get():
			if event.type ==  pygame.QUIT:
				running = False
				pygame.quit()

		pygame.draw.rect(win, (100, 100, 100), [20, 20, 460, 460])
		pygame.draw.rect(win, (0, 0, 0), [20, 20, 460, 460], 5)
		pygame.display.update()

