import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
ЧЁРНЫЙ = (0, 0, 0)
БЕЛЫЙ = (255, 255, 255)
КРАСНЫЙ = (255, 0, 0)
ЗЕЛЁНЫЙ = (0, 255, 0)

# Размеры экрана
ШИРИНА, ВЫСОТА = 1280, 720
РАЗМЕР_КЛЕТКИ = 20

# Создание окна игры
ЭКРАН = pygame.display.set_mode((ШИРИНА, ВЫСОТА))
pygame.display.set_caption("Змейка")

# Часы Pygame
ЧАСЫ = pygame.time.Clock()

# Шрифты
ШРИФТ_ОЧКИ = pygame.font.SysFont(None, 48)
ШРИФТ_КОНЕЦ = pygame.font.SysFont(None, 72)

def игровой_цикл():
    геймовер = False
    конец_игры = False

    # Начальные координаты головы змейки
    голова_x = ШИРИНА / 2
    голова_y = ВЫСОТА / 2

    # Начальная скорость змейки
    скорость_x = 0
    скорость_y = 0

    # Начальная длина змейки
    длина_змейки = 1
    хвост_змейки = []

    # Начальные координаты яблока
    яблоко_x = round(random.randrange(0, ШИРИНА - РАЗМЕР_КЛЕТКИ) / РАЗМЕР_КЛЕТКИ) * РАЗМЕР_КЛЕТКИ
    яблоко_y = round(random.randrange(0, ВЫСОТА - РАЗМЕР_КЛЕТКИ) / РАЗМЕР_КЛЕТКИ) * РАЗМЕР_КЛЕТКИ

    while not геймовер:
        while конец_игры == True:
            ЭКРАН.fill(ЧЁРНЫЙ)
            конец_текст = ШРИФТ_КОНЕЦ.render("Игра окончена! Повторить? (Y/N)", True, БЕЛЫЙ)
            ЭКРАН.blit(конец_текст, [ШИРИНА / 2 - конец_текст.get_width() / 2, ВЫСОТА / 2 - конец_текст.get_height() / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        игровой_цикл()
                    if event.key == pygame.K_n:
                        геймовер = True
                        конец_игры = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                геймовер = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    скорость_x = -РАЗМЕР_КЛЕТКИ
                    скорость_y = 0
                elif event.key == pygame.K_RIGHT:
                    скорость_x = РАЗМЕР_КЛЕТКИ
                    скорость_y = 0
                elif event.key == pygame.K_UP:
                    скорость_y = -РАЗМЕР_КЛЕТКИ
                    скорость_x = 0
                elif event.key == pygame.K_DOWN:
                    скорость_y = РАЗМЕР_КЛЕТКИ
                    скорость_x = 0

        if голова_x >= ШИРИНА or голова_x < 0 or голова_y >= ВЫСОТА or голова_y < 0:
            конец_игры = True

        голова_x += скорость_x
        голова_y += скорость_y

        ЭКРАН.fill(ЧЁРНЫЙ)

        pygame.draw.rect(ЭКРАН, ЗЕЛЁНЫЙ, [яблоко_x, яблоко_y, РАЗМЕР_КЛЕТКИ, РАЗМЕР_КЛЕТКИ])

        голова = []
        голова.append(голова_x)
        голова.append(голова_y)
        хвост_змейки.append(голова)

        if len(хвост_змейки) > длина_змейки:
            del хвост_змейки[0]

        for x in хвост_змейки[:-1]:
            if x == голова:
                конец_игры = True

        for сегмент_змейки in хвост_змейки:
            pygame.draw.rect(ЭКРАН, ЗЕЛЁНЫЙ, [сегмент_змейки[0], сегмент_змейки[1], РАЗМЕР_КЛЕТКИ, РАЗМЕР_КЛЕТКИ])

        pygame.display.update()

        if голова_x == яблоко_x and голова_y == яблоко_y:
            яблоко_x = round(random.randrange(0, ШИРИНА - РАЗМЕР_КЛЕТКИ) / РАЗМЕР_КЛЕТКИ) * РАЗМЕР_КЛЕТКИ
            яблоко_y = round(random.randrange(0, ВЫСОТА - РАЗМЕР_КЛЕТКИ) / РАЗМЕР_КЛЕТКИ) * РАЗМЕР_КЛЕТКИ
            длина_змейки += 1

        ЧАСЫ.tick(10)

    pygame.quit()

# Запуск игрового цикла
игровой_цикл()