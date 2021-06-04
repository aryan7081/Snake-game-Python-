from math import trunc
import pygame
import time
import random

from pygame import key
from pygame.constants import K_LEFT, K_RIGHT

snake_speed = 15

# STORING WINDOW SIZE IN IN VAR

window_x = 720
window_y = 480


# storing colours in variables

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)


# INITIALIZING PYGAME
pygame.init()

# INITIALIZING GAME WINDOW

pygame.display.set_caption('Snake game (Aryan yadav)')
game_window = pygame.display.set_mode((window_x,window_y))


# SETTING FPS CONTROLLER

fps = pygame.time.Clock()




# DEFINING SNAKES DEFAULT POSITION

snake_position = [100,50]



# DEFINING FIRST FOUR BLOCKS
# BODY

snake_body = [
    [100,50],
    [90,50],
    [80,50],
    [70,50]
]


# FOOD POSITION

food_position = [random.randrange(1,(window_x//10)) * 10,
                random.randrange(1, (window_y//10)) * 10]

food_spawn = True

# DEFAULT DIRECTION OF SNAKE
# LEFT - RIGHT

direction = 'RIGHT'
change = direction



# STORING SCORE

score = 0

# SCORE DISPLAY FUNCTION

def display_score(choice, color, font, size):

    # CREATING FONT OBJECT
    score_font = pygame.font.SysFont(font, size)

    # SCORE SURFACE
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # TEXT SURFACE AREA

    score_rect = score_surface.get_rect() 

    # DISPLAY TEXT

    game_window.blit(score_surface, score_rect)



def game_over():
    # FONT OBJECT
    my_font = pygame.font.SysFont('times new roman', 50)

    # DISPLAY TEXT SURFACE

    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # RECTANGULAR TEXT SURFACE OBJECT
    game_over_rect = game_over_surface.get_rect()

    # POSITION OF THE TEXT
    game_over_rect.midtop = (window_x/2, window_y/4)


    # DRAWING TEXT ON SCREEN
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()


    # QUIT GAME JUST AFTER TWO SECONDS 
    time.sleep(2)

    # DEACTIVATING PYGAME LIBRARY
    pygame.quit()


    # QUIT THE PROGRAM
    quit()


#MAIN FUNCTION

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = 'UP'

            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change = 'RIGHT'


    # IF TWO KEY PRESSED SIMULTANEOUSLY

    if change == 'UP' and direction != 'DOWN':
        direction = 'UP'

    if change == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if change == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'

    if change == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


    # MOVING THE SNAKE
    if direction == 'UP':
        snake_position[1] -= 10

    if direction == 'DOWN':
        snake_position[1] +=10


    if direction == 'LEFT':
        snake_position[0] -=10



    if direction == 'RIGHT':
        snake_position[0] +=10


    # SNAKE BODY GROWING LOGIC

    snake_body.insert(0,list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False

    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1,(window_x//10))*10,
        random.randrange(1, (window_y//10)) * 10]

    food_spawn = True
    game_window.fill(black)


    for pops in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pops[0], pops[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_position
    [0], food_position[1], 10, 10))



    # GAME OVER

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # TOUCHING SNAKE

    for block in snake_body[1:]:
        if snake_position[0]== block[0] and snake_position[1] == block[1]:
            game_over()


    # DISPLAYING SCORE CONTINOUSLY

    display_score(1, white, 'times new roman', 20)

    # REFRESH GAME SCREEN 
    pygame.display.update()

    # FRAME RATE
    fps.tick(snake_speed)





    




