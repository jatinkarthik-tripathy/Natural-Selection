import pygame
class Blob(pygame.sprite.Sprite):
	def __init__(self, color, rad=15):
		pygame.sprite.Sprite.__init__(self)
		#params
		self.color = color
		self.rad = rad
		#pygame sprite creation
		self.image = pygame.Surface([self.rad*2, self.rad*2])
		self.image.fill((200, 200, 200))
		self.rect = self.image.get_rect()
		self.rect.center = (250, 250)
		pygame.draw.circle(self.image, self.color, [self.rad, self.rad], self.rad, 0)

	def move(self):
		pass
	
class Food:
	def __init__(self):
		pass