import pygame, random



class Player(pygame.sprite.Sprite):

	def __init__(self, health, pos, sprite_path):
		self.image = pygame.image.load(sprite_path)

		self.rect = pygame.Rect(pos[0], pos[1], 16,16)
		self.health = health
		self.speed = 4
		self.direction = [0,0]


	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction[0] = 1

		elif keys[pygame.K_LEFT]:
			self.direction[0] = -1
		else:
			self.direction[0] = 0

		if keys[pygame.K_DOWN]:
			self.direction[1] = 1

		elif keys[pygame.K_UP]:
			self.direction[1] = -1

		else:
			self.direction[1] = 0
		
	def update(self):
		self.get_input()
		if self.direction[0] and self.direction[1]:
			self.speed = 2
		else:
			self.speed = 4
		self.rect.x += self.speed * self.direction[0]
		self.rect.y += self.speed * self.direction[1]

		if self.rect.right >= 400:
			self.rect.right = 400
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= 400:
			self.rect.bottom = 400


class Obstacle():

	def __init__(self, size, pos):
		self.image = pygame.transform.scale(pygame.image.load(random.choice(['rock1.png','rock2.png','rock3.png'])), (size))

		self.rect = self.image.get_rect(center = pos)

	def update(self):
		self.rect.y += 2

class Power_up():

	def __init__(self, size, pos):
		self.image = pygame.image.load('heart_plus.png')
		self.origin = pos[0]
		self.rect = self.image.get_rect(center = pos)

		self.path = 1


	def update(self):
		self.rect.y += 2

		self.rect.x += 1 * self.path
		if self.rect.x > self.origin + 40:
			self.path = -1
		if self.rect.x < self.origin - 40:
			self.path = 1


