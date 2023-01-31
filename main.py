import sys
import pygame
from assets import ALL_SPRITES, SOUNDS
from randomPipe import getRandomPipe

FPS = 60
clock = pygame.  time.Clock()
SIZE = WIDTH, HEIGHT = 800, 600
GROUNDY = HEIGHT * 0.8


def welcomeScreen():  # сцена экрана приветствия
    playerx = int(WIDTH / 5)
    playery = int(HEIGHT - ALL_SPRITES['player'].get_height()) / 2
    introx = int(WIDTH - ALL_SPRITES['intro'].get_width()) / 2
    introy = int(HEIGHT * 0.13)
    groundx = 0
    playbutton = pygame.Rect(108, 222, 68, 65)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                return
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if pygame.mouse.get_pos()[0] > playbutton[0] and pygame.mouse.get_pos()[0] < playbutton[0] + playbutton[2]:
                if pygame.mouse.get_pos()[1] > playbutton[1] and pygame.mouse.get_pos()[1] < playbutton[1] + playbutton[
                    3]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if playbutton.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mainGame()
            else:
                SCREEN.blit(ALL_SPRITES['background'], (0, 0))
                SCREEN.blit(ALL_SPRITES['player'], (playerx, playery))
                SCREEN.blit(ALL_SPRITES['intro'], (introx, introy))
                SCREEN.blit(ALL_SPRITES['ground'], (groundx, GROUNDY))
                pygame.mixer.music.load('data/sounds/backmusic.mp3')
                pygame.mixer.music.play(loops=-1)
                pygame.display.flip()
                clock.tick(FPS)


def mainGame():  # основная сцена
    # запуск музыки в микшере
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/sounds/backmusic.mp3')
    pygame.mixer.music.play(loops=-1)
    score = 0
    playerx = int(WIDTH / 5)
    playery = int(HEIGHT / 2)
    groundx = 0
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    # трубы со смещением
    upperPipes = [
        {'x': WIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': WIDTH + 200 + (WIDTH / 2), 'y': newPipe2[0]['y']}
    ]
    lowerPipes = [
        {'x': WIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': WIDTH + 200 + (WIDTH / 2), 'y': newPipe2[1]['y']}
    ]
    # скорости выведенные путём тестов
    pipespeedX = -4
    playerspeedY = -9
    playermaxspeedY = 10
    playeraccelerationY = 1
    playerspeedwhenflappping = -8
    playerflapbl = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_q):
                # рывок на клавишу Q
                if event.key == pygame.K_q:
                    pipespeedX = pipespeedX * 4
                else:
                    pipespeedX = -4
                if playery > 0:
                    playerspeedY = playerspeedwhenflappping
                    playerflapbl = True
                    SOUNDS['wing'].play()
        crashed = collided(playerx, playery, upperPipes,
                           lowerPipes)
        if crashed:
            return
        playermiddleposition = playerx + ALL_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + ALL_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playermiddleposition < pipeMidPos + 4:
                score += 1
                SOUNDS['point'].play()
        if playerspeedY < playermaxspeedY and not playerflapbl:
            playerspeedY += playeraccelerationY
        if playerflapbl:
            playerflapbl = False
        playerHeight = ALL_SPRITES['player'].get_height()
        playery = playery + min(playerspeedY, GROUNDY - playery - playerHeight)
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipespeedX
            lowerPipe['x'] += pipespeedX
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        if upperPipes[0]['x'] < -ALL_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        SCREEN.blit(ALL_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(ALL_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(ALL_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        SCREEN.blit(ALL_SPRITES['ground'], (groundx, GROUNDY))
        SCREEN.blit(ALL_SPRITES['player'], (playerx, playery))
        numbers = [int(x) for x in list(str(score))]
        # получение ширины букв для их правильного отображения
        width = 0
        for number in numbers:
            width += ALL_SPRITES['numbers'][number].get_width()
        Xoffset = (WIDTH - width) / 2
        for number in numbers:
            SCREEN.blit(ALL_SPRITES['numbers'][number], (Xoffset, HEIGHT * 0.12))
            Xoffset += ALL_SPRITES['numbers'][number].get_width()
        pygame.display.flip()
        clock.tick(FPS)


def collided(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 25 or playery < 0:
        SOUNDS['hit'].play()
        pygame.mixer.music.stop()
        gameOver()
    for pipe in upperPipes:
        pipeHeight = ALL_SPRITES['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < ALL_SPRITES['pipe'][0].get_width() - 20:
            SOUNDS['hit'].play()
            print(playerx, pipe['x'], )
            pygame.mixer.music.stop()
            gameOver()
    for pipe in lowerPipes:
        if (playery + ALL_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < \
                ALL_SPRITES['pipe'][0].get_width() - 20:
            SOUNDS['hit'].play()
            pygame.mixer.music.stop()
            gameOver()
    return False


def gameOver():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird от Амира')
    ALL_SPRITES['OVER'] = pygame.image.load('data/sprites/gameover.png').convert_alpha()
    ALL_SPRITES['RETRY'] = pygame.image.load('data/sprites/retry.png').convert_alpha()
    ALL_SPRITES['HOME'] = pygame.image.load('data/sprites/Home.png').convert_alpha()
    SCREEN.blit(ALL_SPRITES['background'], (0, 0))
    SCREEN.blit(ALL_SPRITES['HOME'], (10, 10))
    SCREEN.blit(ALL_SPRITES['RETRY'], (75, 10))
    SCREEN.blit(ALL_SPRITES['OVER'], (int(WIDTH - ALL_SPRITES['OVER'].get_width()) / 2, 0))
    SCREEN.blit(ALL_SPRITES['ground'], (0, GROUNDY))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mainGame()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if pygame.mouse.get_pos()[0] > 75 and pygame.mouse.get_pos()[0] < 75 + ALL_SPRITES['RETRY'].get_width():
                if pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 10 + ALL_SPRITES[
                    'RETRY'].get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mainGame()
            if pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 10 + ALL_SPRITES['HOME'].get_width():
                if pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 10 + ALL_SPRITES[
                    'HOME'].get_height():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        welcomeScreen()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Flappy Bird от Сафина')
    SCREEN = pygame.display.set_mode(SIZE)
    while True:
        welcomeScreen()
        mainGame()
