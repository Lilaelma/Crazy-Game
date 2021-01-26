import pygame


class Levier(pygame.sprite.Sprite) :

	def __init__(self) :

		super().__init__()
		self.rect = pygame.Rect(800, 86, 64, 64)
		self.levier_left = pygame.image.load("image/switchLeft.png").convert_alpha()
		self.levier_mid = pygame.image.load("image/switchMid.png").convert_alpha()
		self.switch = False
		self.block = pygame.Rect(1080, 0, 20, 400)
		self.get_next_to = pygame.Rect(1065, 305, 35, 45)
		self.sara = pygame.image.load("image/sara.png").convert_alpha()

	def ft_print(self, area) :

		if self.switch :
			area.blit(self.levier_mid, self.rect)
			area.blit(self.sara, self.get_next_to)

		else :
			area.blit(self.levier_left, self.rect)
			pygame.draw.rect(area, (255, 75, 0), self.block)

