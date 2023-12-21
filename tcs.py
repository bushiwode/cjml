import pygame
import time
import random

pygame.init()

# 游戏参数
width, height = 800, 600
snake_size = 20
snake_speed = 15

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 初始化游戏窗口
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('贪吃蛇游戏')

# 初始化时钟
clock = pygame.time.Clock()

# 设置字体
font = pygame.font.SysFont(None, 30)

# 绘制蛇
def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_size, snake_size])

# 显示得分
def Your_score(score):
    score_text = font.render("得分: " + str(score), True, white)
    game_display.blit(score_text, [0, 0])

# 游戏循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置和长度
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # 随机生成食物的位置
    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -snake_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = snake_size
                    lead_x_change = 0

        # 边界碰撞检测
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)

        pygame.display.update()

        # 食物碰撞检测
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()


import pygame
import time
import random

pygame.init()

# 游戏参数
width, height = 800, 600
snake_size = 20
snake_speed = 15

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 初始化游戏窗口
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('贪吃蛇游戏')

# 初始化时钟
clock = pygame.time.Clock()

# 设置字体
font = pygame.font.SysFont(None, 30)

# 绘制蛇
def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_size, snake_size])

# 显示得分
def Your_score(score):
    score_text = font.render("得分: " + str(score), True, white)
    game_display.blit(score_text, [0, 0])

# 游戏循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置和长度
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # 随机生成食物的位置
    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -snake_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = snake_size
                    lead_x_change = 0

        # 边界碰撞检测
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)

        pygame.display.update()

        # 食物碰撞检测
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
