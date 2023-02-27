import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, pos, speed, platform_group, *group):
        super().__init__(*group)
        self.speed = speed
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.platform_group = platform_group

    def walk(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.rect.x -= self.speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.rect.x += self.speed

    def fall(self):
        if pygame.sprite.spritecollideany(self, self.platform_group) is None:
            self.rect.y += self.speed

    def update(self, *args):
        if args:
            self.walk(args[0])


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 10))
        self.image.fill((190, 190, 190))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


def game(screen):
    # создадим группу, содержащую все спрайты
    FPS = 60
    tick = 0
    clock = pygame.time.Clock()
    hero = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if hero is None:
                        hero = Character(event.pos, 10, platform_group, player_group, all_sprites)
                    else:
                        hero.rect.x = event.pos[0]
                        hero.rect.y = event.pos[1]
                if event.button == 3:
                    Platform(event.pos, platform_group, all_sprites)
            player_group.update(event)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        if hero:
            hero.fall()
        tick += 1
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    game(screen)
