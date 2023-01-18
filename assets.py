import pygame
ALL_SPRITES = {}
SOUNDS = {}
pygame.init()
pygame.display.set_mode((800, 600))
SOUNDS['hit'] = pygame.mixer.Sound('data\sounds\hit.wav')
SOUNDS['point'] = pygame.mixer.Sound('data\sounds\point.wav')
SOUNDS['wing'] = pygame.mixer.Sound('data\sounds\wing.wav')
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
ALL_SPRITES['background'] = pygame.image.load('data\sprites\\bg.png').convert_alpha()
ALL_SPRITES['player'] = pygame.image.load('data\sprites\\bird.png').convert_alpha()
ALL_SPRITES['intro'] = pygame.image.load('data\sprites\intro.png').convert_alpha()
ALL_SPRITES['ground'] = pygame.image.load('data\sprites\\ground.png').convert_alpha()
ALL_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load('data\sprites\\pipe.png').convert_alpha(), 180),
    pygame.image.load('data\sprites\\pipe.png').convert_alpha()  #### LOWER PIPES
)