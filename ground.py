import pygame


class Ground(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()
		self.rect_level1 = pygame.Rect(0, 470, 1100, 130)
		self.rect_level2 = pygame.Rect(0, 535, 1100, 65)
		self.rect_level3 = pygame.Rect(0, 535, 1100, 65)
		

	def ft_print_level1(self, surface):

		pygame.draw.rect(surface, (255, 75, 0), self.rect_level1)

	def ft_print_level2(self, surface):

		pygame.draw.rect(surface, (255, 10, 10), self.rect_level2)
		

	def ft_print_level3(self, surface):

		pygame.draw.rect(surface, (255, 10, 10), self.rect_level3)