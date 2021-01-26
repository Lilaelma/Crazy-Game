import pygame


class Platform(pygame.sprite.Sprite):

	def __init__(self, rect):

		super().__init__()
		self.rect = rect

	def ft_print(self, surface):

		pygame.draw.rect(surface, (88, 88, 88), self.rect)
		#surface.blit(self.image, self.rect)