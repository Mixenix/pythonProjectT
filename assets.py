import pygame
ALL_SPRITES = {}
SOUNDS = {}
pygame.init() # инициализация всех файлов библиотеки
pygame.display.set_mode((800, 600)) # режим окна
# добавление звуков
SOUNDS['hit'] = pygame.mixer.Sound('data\sounds\hit.wav')
SOUNDS['point'] = pygame.mixer.Sound('data\sounds\point.wav')
SOUNDS['wing'] = pygame.mixer.Sound('data\sounds\wing.wav')
# добавление спрайтов, а также их увеличение
ALL_SPRITES['numbers'] = (
    pygame.transform.scale2x(pygame.image.load('data\sprites\\0.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\1.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\2.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\3.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\4.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\5.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\6.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\7.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\8.png').convert_alpha()),
    pygame.transform.scale2x(pygame.image.load('data\sprites\\9.png').convert_alpha()),
)
# добавление спрайтов без увеличен
ALL_SPRITES['OVER'] = pygame.image.load('data/sprites/gameover.png').convert_alpha()
ALL_SPRITES['RETRY'] = pygame.image.load('data/sprites/retry.png').convert_alpha()
ALL_SPRITES['HOME'] = pygame.image.load('data/sprites/Home.png').convert_alpha()
ALL_SPRITES['savebttn'] = pygame.image.load('data\sprites\\savebttn.png').convert_alpha()
ALL_SPRITES['background'] = pygame.image.load('data\sprites\\bg.png').convert_alpha()
ALL_SPRITES['player'] = pygame.image.load('data\sprites\\bird.png').convert_alpha()
ALL_SPRITES['playergreen'] = pygame.image.load('data\sprites\\birdgreen.png').convert_alpha()
ALL_SPRITES['playerblue'] = pygame.image.load('data\sprites\\birdblue.png').convert_alpha()
ALL_SPRITES['intro'] = pygame.image.load('data\sprites\intro.png').convert_alpha()
ALL_SPRITES['ground'] = pygame.image.load('data\sprites\\ground.png').convert_alpha()
ALL_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load('data\sprites\\pipe.png').convert_alpha(), 180),
    pygame.image.load('data\sprites\\pipe.png').convert_alpha()
)