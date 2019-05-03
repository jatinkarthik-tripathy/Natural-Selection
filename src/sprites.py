import pygame
from random import randint

class Blob(pygame.sprite.Sprite):
	def __init__(self, color, rad=11):
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
			self.x = randint(40, 460)
			self.y = 40
			self.rect.midtop = (self.x, self.y)
		elif val == 1:
			self.x = 460
			self.y = randint(40, 460)
			self.rect.midright = (self.x, self.y)
		elif val == 2:
			self.x = randint(40, 460)
			self.y = 460
			self.rect.midbottom = (self.x, self.y)
		elif val == 3:
			self.x = 40
			self.y = randint(40, 460)
			self.rect.midleft = (self.x, self.y)

	def update(self):
		val = randint(0, 1)
		if val == 0:
			if self.x <= 460:
				self.x += 5
			else:
				self.x -= 5
		else:
			if self.x >= 40:
				self.x -= 5
			else:
				self.x += 5

		val = randint(0, 1)
		if val == 0:
			if self.y <= 460:
				self.y += 5
			else:
				self.y -= 5
		else:
			if self.y >= 40:
				self.y -= 5
			else:
				self.y += 5

		self.rect.center = (self.x, self.y)

	
class Food(pygame.sprite.Sprite):
	def __init__(self, color=(211, 0, 0), rad=5):
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
		self.rect.center = (randint(100, 400), randint(100, 400))

		