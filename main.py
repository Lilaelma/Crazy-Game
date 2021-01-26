import pygame
import sys

from pygame.sprite import Group
from player import Player
from platform import Platform
from ground import Ground
from levier import Levier


class Play :

	def __init__(self) :

		windows_resolution = (1100, 600)
		self.window = pygame.display.set_mode(windows_resolution)
		self.rect = pygame.Rect(0, 0, windows_resolution[0], windows_resolution[1])
		self.window.fill((100, 181, 246))
		self.fps = 150
		self.horloge = pygame.time.Clock()
		self.run_1 = True
		self.run_2 = True
		self.run_3 = True
		self.levier = Levier()
		self.player = Player(5, 420)
		self.sara = pygame.image.load("image/sara.png").convert_alpha()
		self.player_vx = 0
		self.gravity = (0, 1)
		self.resistance = (0, 0)
		self.ground = Ground()
		self.collision_ground = False
		self.platform_groupe = Group()
				


	def level_1(self) :

		self.platform_list_rect = [
			pygame.Rect(200, 300, 250, 25), pygame.Rect(650, 150, 250, 25),
			pygame.Rect(800, 440, 300, 30), pygame.Rect(860, 410, 240, 30),
			pygame.Rect(920, 380, 180, 30), pygame.Rect(980, 350, 120, 30)
		]

		pygame.display.set_caption("Crazy Adventure - Level 1")

		while self.run_1 :
			self.fps = 150
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					sys.exit();

				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 2

					if event.key == pygame.K_LEFT :
						self.player_vx = -2

					if event.key == pygame.K_UP :
						self.player.jumped = True
						self.player.number_jump += 1

				if event.type == pygame.KEYUP :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 0

					if event.key == pygame.K_LEFT :
						self.player_vx = 0

			if self.ground.rect_level1.colliderect(self.player.rect) :
				self.resistance = (0, -1)
				self.collision_ground = True
				self.player.number_jump = 0

			else :
				self.resistance = (0, 0)
			
			if self.player.jumped and self.collision_ground :
				if self.player.number_jump < 1 :
					self.player.ft_jump()

			for rect in self.platform_list_rect:
				platform = Platform(rect)
				self.platform_groupe.add(platform)
				if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top \
						and self.player.rect.colliderect(rect):
					self.resistance = (0, -1)
					self.player.number_jump = 0

			if self.levier.rect.colliderect(self.player.rect) :
				self.levier.switch = True

			if self.levier.get_next_to.colliderect(self.player.rect) :
				self.run_1 = False
			
			self.player.move(self.player_vx)
			self.gravity_game()
			self.player.rect.clamp_ip(self.rect)
			self.window.fill((100, 181, 246))
			self.player.ft_print(self.window)
			self.ground.ft_print_level1(self.window)
			self.levier.ft_print(self.window)
			
			for platform in self.platform_groupe :
				platform.ft_print(self.window)

			pygame.draw.rect(self.window, (255, 0, 0), self.rect, 1)
			self.horloge.tick(self.fps)
			pygame.display.flip()

			

	def level_2(self) :

		self.platform_list_rect = [
			pygame.Rect(60, 470, 120, 130), pygame.Rect(285, 470, 120, 130),
			pygame.Rect(860, 480, 240, 30), pygame.Rect(860, 60, 240, 30),
			pygame.Rect(400, 200, 300, 130), pygame.Rect(0, 60, 240, 5),
			pygame.Rect(290, 130, 60, 5)
		]
		self.player = Player(75, 420)
		self.rect_sara = pygame.Rect(5, 15, 35, 45)
		self.teleporter = pygame.Rect(1074, 454, 2, 2)

		pygame.display.set_caption("Crazy Adventure - Level 2")

		while self.run_2 :

			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					sys.exit();

				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 2

					if event.key == pygame.K_LEFT :
						self.player_vx = -2

					if event.key == pygame.K_UP :
						self.player.jumped = True
						self.player.number_jump += 1

				if event.type == pygame.KEYUP :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 0

					if event.key == pygame.K_LEFT :
						self.player_vx = 0

			if self.ground.rect_level2.colliderect(self.player.rect) :
				self.run_2 = False
				self.game_over()

			else :
				self.resistance = (0, 0)
			
			if self.player.jumped and self.collision_ground :
				if self.player.number_jump < 1 :
					self.player.ft_jump()


			if self.teleporter.colliderect(self.player.rect) :
				self.player = Player(1050, 20)

			if self.rect_sara.colliderect(self.player.rect) :
				self.run_2 = False
				self.run_3 = True

			for rect in self.platform_list_rect:
				platform = Platform(rect)
				self.platform_groupe.add(platform)
				if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top \
						and self.player.rect.colliderect(rect):
					self.resistance = (0, -1)
					self.collision_ground = True
					self.player.number_jump = 0
			
			self.player.move(self.player_vx)
			self.gravity_game()
			self.player.rect.clamp_ip(self.rect)
			self.window.fill((100, 181, 246))
			self.ground.ft_print_level2(self.window)
			self.window.blit(self.sara, self.rect_sara)
			
			for platform in self.platform_groupe :
				platform.ft_print(self.window)

			self.player.ft_print(self.window)

			pygame.draw.circle(self.window, [255, 180, 0], [1075, 455], 20)
			pygame.draw.circle(self.window, [0, 255, 100], [1075, 35], 20)
			pygame.draw.rect(self.window, (255, 0, 0), self.rect, 1)
			self.horloge.tick(200)
			pygame.display.flip()

	def level_3(self) :

		self.platform_list_rect = [
			pygame.Rect(0, 60, 900, 5), pygame.Rect(950, 60, 150, 5), 
			pygame.Rect(200, 120, 10, 10),
			pygame.Rect(50, 180, 10, 10), pygame.Rect(350, 180, 10, 10),
			pygame.Rect(200, 240, 10, 10),
			pygame.Rect(300, 300, 20, 50), pygame.Rect(330, 300, 20, 50),
			pygame.Rect(0, 510, 150, 5), pygame.Rect(210, 510, 600, 50), pygame.Rect(880, 450, 40, 150),
		]
		self.player = Player(550, 5)
		self.rect_sara = pygame.Rect(880, 405, 35, 45)
		self.teleporter1 = pygame.Rect(1074, 34, 2, 2)
		self.teleporter2 = pygame.Rect(24, 34, 2, 2)

		pygame.display.set_caption("Crazy Adventure - Level 3")

		while self.run_3 :

			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					sys.exit();

				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 2

					if event.key == pygame.K_LEFT :
						self.player_vx = -2

					if event.key == pygame.K_UP :
						self.player.jumped = True
						self.player.number_jump += 1

				if event.type == pygame.KEYUP :
					if event.key == pygame.K_RIGHT :
						self.player_vx = 0

					if event.key == pygame.K_LEFT :
						self.player_vx = 0

			if self.ground.rect_level3.colliderect(self.player.rect) :
				self.run_3 = False
				self.game_over()

			else :
				self.resistance = (0, 0)
			
			if self.player.jumped and self.collision_ground :
				if self.player.number_jump < 1 :
					self.player.ft_jump()


			if self.teleporter1.colliderect(self.player.rect) :
				self.player = Player(25, 460)

			if self.teleporter2.colliderect(self.player.rect) :
				self.player = Player(1075, 455)

			if self.rect_sara.colliderect(self.player.rect) :
				self.run_3 = False

			for rect in self.platform_list_rect:
				platform = Platform(rect)
				self.platform_groupe.add(platform)
				if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top \
						and self.player.rect.colliderect(rect):
					self.resistance = (0, -1)
					self.collision_ground = True
					self.player.number_jump = 0
			
			self.player.move(self.player_vx)
			self.gravity_game()
			self.player.rect.clamp_ip(self.rect)
			self.window.fill((100, 181, 246))
			self.ground.ft_print_level2(self.window)
			self.window.blit(self.sara, self.rect_sara)
			
			for platform in self.platform_groupe :
				platform.ft_print(self.window)

			pygame.draw.circle(self.window, [255, 180, 0], [1075, 455], 20)
			pygame.draw.circle(self.window, [0, 255, 100], [1075, 35], 20)
			pygame.draw.circle(self.window, [255, 180, 0], [25, 455], 20)
			pygame.draw.circle(self.window, [0, 255, 100], [25, 35], 20)

			self.player.ft_print(self.window)

			pygame.draw.rect(self.window, (255, 0, 0), self.rect, 1)
			self.horloge.tick(200)
			pygame.display.flip()

	def gravity_game(self) :

		self.player.rect.y += self.gravity[1] + self.resistance[1];

	def game_over(self) :

		self.window.fill((0, 0, 0))
		pygame.display.set_caption("Crazy Adventure - Game Over")
		font = pygame.font.SysFont("Arial", 50)
		text = font.render("Game Over", True, (255, 255, 255), (0, 0, 0))
		self.window.blit(text, [450, 250])
		pygame.display.flip()
		while 1 :
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					sys.exit();

	def credits(self) :

		pygame.display.set_caption("Crazy Adventure - Credits")
		self.credits = pygame.image.load("image/credits.png").convert_alpha()
		self.credits = pygame.transform.scale(self.credits, (1100, 600))
		self.window.blit(self.credits, [0, 0])
		pygame.display.flip()
		while 1 :
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					sys.exit();


if __name__ == "__main__" :
	pygame.init()
	Play().level_1()
	Play().level_2()
	Play().level_3()
	Play().credits()
	pygame.quit()