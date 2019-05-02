import pygame
from random import randint

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
		pygame.draw.circle(self.image, self.color, [self.rad, self.rad], self.rad, 0)

		#random placement
		val = randint(0, 3)
		if val == 0:
			self.rect.midtop = (randint(20, 480), 20)
		elif val == 1:
			self.rect.midright = (480, randint(20, 480))
		elif val == 2:
			self.rect.midbottom = (randint(20, 480), 480)
		elif val == 3:
			self.rect.midleft = (20, randint(20, 480))

	def move(self):
		pass
	
class Food(pygame.sprite.Sprite):
	def __init__(self, color=(255, 0, 0), rad=5):
		pygame.sprite.Sprite.__init__(self)
		#params
		self.color = color
		self.rad = rad
		#pygame sprite creation
		self.image = pygame.Surface([self.rad*2, self.rad*2])
		self.image.fill((200, 200, 200))
		self.rect = self.image.get_rect()
		pygame.draw.circle(self.image, self.color, [self.rad, self.rad], self.rad, 0)

		#random placement
		self.rect.center = (randint(50, 450), randint(50, 450))

		