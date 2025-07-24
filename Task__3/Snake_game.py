# SNAKE GAME

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width = 600
height = 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

# Snake block size and speed
block_size = 20
speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

# Display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game')

clock = pygame.time.Clock()

def draw_score(score):
    value = score_font.render("Score: " + str(score), True, blue)
    screen.blit(value, [10, 10])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    # Food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            draw_score(length - 1)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block_size
                    dx = 0

        # Move the snake
        x += dx
        y += dy

        # Check boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        # Collision with self
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake)
        draw_score(length - 1)

        pygame.display.update()

        # Eating food
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
