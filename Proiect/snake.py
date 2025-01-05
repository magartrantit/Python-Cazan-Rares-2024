import pygame
import time
import random
import sys
import json

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(213, 50, 80)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(50, 153, 213)
grey = pygame.Color(150, 150, 150)

#game variables
window_x = 500
window_y = 500
obstavles = []
pygame.init()
pygame.display.set_caption('Snake Game')
fps = pygame.time.Clock()

def put_obstacles():
    for obs in obstacles:
        pygame.draw.rect(game_window, grey, pygame.Rect(obs[0], obs[1], 20, 20))

def load_dimensions(file):
    global window_x, window_y, obstacles
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            window_x, window_y = data.get("board_size", [720, 480])
            obstacles = data.get("obstacles", [])
    except Exception as e:
        print("Nu s-a putut citi fisierul de configurare: {e}")
        sys.exit()

#snake
snake_pos = [120, 80]
snake_body = [[120, 80], [100, 60], [80, 40], [60, 20]]
snake_speed = 15
direction = 'RIGHT'
change_to = direction

#fruit
fruit_spawn = True
fruit_pos = [random.randrange(0, (window_x//20)) * 20, random.randrange(0, (window_y//20)) * 20]

#score
score = 0
high_score = 0

def show_score(choice, color, font, size):
    sfont = pygame.font.SysFont(font, size)
    ssurface = sfont.render('Score: ' + str(score), True, color)
    srect = ssurface.get_rect()
    game_window.blit(ssurface, srect)

def update_high_score():
    global high_score
    if score>high_score:
        high_score = score

def set_game():
    global snake_pos, snake_body, snake_speed, direction, change_to, fruit_pos, fruit_spawn, score
    snake_pos = [120, 80]
    snake_body = [[120, 80], [100, 60], [80, 40], [60, 20]]
    snake_speed = 15
    direction = 'RIGHT'
    change_to = direction
    fruit_spawn = True
    fruit_pos = [random.randrange(0, (window_x//20)) * 20, random.randrange(0, (window_y//20)) * 20]
    score = 0

def quit_game():
    game_window.fill(black)
    font = pygame.font.SysFont('arial', 50)
    high_score_surface = font.render('High Score: ' + str(high_score), True, red)
    high_score_rect = high_score_surface.get_rect()
    high_score_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(high_score_surface, high_score_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def game_over():
    global high_score
    update_high_score()

    while True:
        game_window.fill(black)
        
        font = pygame.font.SysFont('arial', 50)
        gameover_surface = font.render('Your Score is: ' + str(score), True, red)
        gameover_rect = gameover_surface.get_rect()
        gameover_rect.midtop = (window_x/2, window_y/4)
        game_window.blit(gameover_surface, gameover_rect)
        
        retry_button_x = (window_x/2) - 50 - 150
        retry_button_y = (window_y/2)
        retry_button = pygame.Rect(retry_button_x, retry_button_y, 150, 50)
        pygame.draw.rect(game_window, green, retry_button)
        retry_font = pygame.font.SysFont('arial', 20)
        retry_surface = retry_font.render('Retry', True, white)
        retry_rect = retry_surface.get_rect(center = retry_button.center)
        game_window.blit(retry_surface, retry_rect)

        quit_button_x = (window_x/2) + 50
        quit_button_y = (window_y/2)
        quit_button = pygame.Rect(quit_button_x, quit_button_y, 150, 50)
        pygame.draw.rect(game_window, green, quit_button)
        quit_font = pygame.font.SysFont('arial', 20)
        quit_surface = quit_font.render('Quit', True, white)
        quit_rect = quit_surface.get_rect(center = quit_button.center)
        game_window.blit(quit_surface, quit_rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if retry_button.collidepoint(x, y):
                    set_game()
                    main()
                if quit_button.collidepoint(x, y):
                    quit_game()

def valid_pos(pos):
    for obs in obstacles:
        if pos == obs:
            return False
    return True

def main():
    global change_to, direction, fruit_pos, fruit_spawn, score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 20
        if direction == 'DOWN':
            snake_pos[1] += 20
        if direction == 'LEFT':
            snake_pos[0] -= 20
        if direction == 'RIGHT':
            snake_pos[0] += 20

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
            score = score + 10
            fruit_spawn = False
        else:
            snake_body.pop()
        

        if not fruit_spawn:
            while True:
                new_fruit_pos = [random.randrange(0, (window_x//20)) * 20, random.randrange(0, (window_y//20)) * 20]
                if valid_pos(fruit_pos):
                    fruit_pos = new_fruit_pos
                    break

        fruit_spawn = True
        game_window.fill(black)

        put_obstacles()

        for pos in snake_body:
            pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 20, 20))
        
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos[0], fruit_pos[1], 20, 20))

        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            game_over()

        for part in snake_body[1:]:
            if snake_pos[0] == part[0] and snake_pos[1] == part[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        fps.tick(snake_speed)




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Trebuie sa dati fisierul de configurare")
        sys.exit()
    load_dimensions(sys.argv[1])
    game_window = pygame.display.set_mode((window_x, window_y))
    main()