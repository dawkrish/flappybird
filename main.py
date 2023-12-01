import pygame
import math
WIDTH, HEIGHT = 800, 600


class Bird:
    def __init__(self, jump, init_x, init_y) -> None:
        self.jump = jump
        self.speed = 1
        self.angle = 0
        self.isJumping = False
        self.image = pygame.image.load('bird.png').convert_alpha()
        self.surface = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.surface.get_rect(center=(init_x, init_y))
        


class Game:
    def __init__(self, running) -> None:
        self.running = running
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.state = "home_screen"
        self.bird = Bird(60, WIDTH // 2, HEIGHT // 2)
        self.score = 0
        self.game_loop()

    def game_loop(self):

        while self.running:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.state == "game_screen" and event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                    self.bird.isJumping = True
                    self.bird.rect.y -= self.bird.jump
                    self.bird.speed = 1

            if self.state == "home_screen":
                self.display_home_screen()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                    self.state = "game_screen"

            if self.state == "game_screen":
                print("jumping " ,self.bird.angle )
                if not self.bird.isJumping: self.bird.angle -= 1.4
                else :
                    self.bird.angle = 55
                    self.bird.isJumping =  False
                rotated_surface = pygame.transform.rotate(self.bird.surface, self.bird.angle)
                rotated_rect = rotated_surface.get_rect(center=self.bird.rect.center)
                self.screen.blit(rotated_surface, rotated_rect)
                self.bird.rect = rotated_rect  # Update the bird's rect with the rotated rect
                self.bird.speed += 0.18

                if self.bird.speed > 8:self.bird.speed = 8

                self.bird.rect.y += self.bird.speed
                if self.bird.rect.y >= HEIGHT:
                    self.state = "end_screen"


            if self.state == "end_screen":
                self.bird.rect.y = 240
                self.bird.speed = 1
                self.bird.angle = 0
                self.display_end_screen()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                    self.state = "game_screen"

            pygame.display.update()
            self.clock.tick(60)

    def display_home_screen(self):
        retro_font = pygame.font.Font('retrofont.ttf', 30)
        home_text_surface = retro_font.render(
            "Press SPACE to start the game", True, (0, 0, 0))
        home_text_rect = home_text_surface.get_rect(center=(WIDTH // 2, 200))
        self.screen.blit(home_text_surface, home_text_rect)

    def display_end_screen(self):

        retro_font = pygame.font.Font('retrofont.ttf', 30)

        end_text_surface_1 = retro_font.render("GaMe OvEr", True, (0, 0, 0))
        end_text_rect_1 = end_text_surface_1.get_rect(center=(WIDTH//2, 200))

        end_text_surface_2 = retro_font.render(
            f"ScOrE : {self.score}", True, (0, 0, 0))
        end_text_rect_2 = end_text_surface_2.get_rect(center=(WIDTH // 2, 240))

        end_text_surface_3 = retro_font.render(
            "Press space to restart the game", True, (0, 0, 0))
        end_text_rect_3 = end_text_surface_3.get_rect(center=(WIDTH // 2, 280))

        self.screen.blit(end_text_surface_1, end_text_rect_1)
        self.screen.blit(end_text_surface_2, end_text_rect_2)
        self.screen.blit(end_text_surface_3, end_text_rect_3)


pygame.init()

game = Game(True)

pygame.quit()
