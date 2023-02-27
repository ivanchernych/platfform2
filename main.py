import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('date', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Game_over(pygame.sprite.Sprite):
    def __init__(self, image, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(-600, 0, 600, 300)

    def drive(self):
        self.rect.x += 8
        if self.rect.x == 0:
            self.rect.x = -600

    def update(self):
        self.drive()


class Game:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        self.start_game()

    def start_game(self):
        game_over_group = pygame.sprite.Group()
        image = load_image('gameover.png', 1)
        screen = pygame.display.set_mode(size)
        Game_over(image, game_over_group)

        FPS = 60
        tick = 0
        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            screen.fill((0, 0, 255))

            tick += 1
            clock.tick(FPS)

            game_over_group.update()
            game_over_group.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height, = 600, 300
    Game(size)