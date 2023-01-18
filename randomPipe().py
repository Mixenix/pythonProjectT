import random
from assets import ALL_SPRITES
SIZE = WIDTH, HEIGHT = 800, 600


def getRandomPipe():
    pipeHeight = ALL_SPRITES['pipe'][0].get_height()
    offset = HEIGHT / 4.5
    y2 = offset + random.randrange(0, int(HEIGHT - ALL_SPRITES['ground'].get_height() - 1.2 * offset)) # случайная высота
    pipeX = WIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # для верхних труб
        {'x': pipeX, 'y': y2}  # для нижних труб
    ]
    return pipe