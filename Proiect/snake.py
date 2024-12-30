import pygame
import time
import random

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(213, 50, 80)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(50, 153, 213)

#game variables
window_x = 720
window_y = 480
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

#snake
snake_pos = [100, 50]
snake_body = [ [100, 50], [90, 50], [80, 50], [70, 50]]
snake_speed = 15
direction = 'RIGHT'
change_to = direction

#fruit
fruit_spawn = True
fruit_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

#score
score = 0
def show_score(choice, color, font, size):
    sfont = pygame.font.SysFont(font, size)
    ssurface = sfont.render('Score: ' + str(score), True, color)
    srect = ssurface.get_rect()
    game_window.blit(ssurface, srect)

def gmae_over():
    font = pygame.font.SysFont('arial', 50)
    gameover_surface = font.render('Your Score is: ' + str(score), True, red)
    gameover_rect = gameover_surface.get_rect()
    gameover_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(gameover_surface, gameover_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def main():
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
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
            score = score + 10
            fruit_spawn = False
        else:
            snake_body.pop()
        

        if not fruit_spawn:
            fruit_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            gmae_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            gmae_over()

        for part in snake_body[1:]:
            if snake_pos[0] == part[0] and snake_pos[1] == part[1]:
                gmae_over()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        fps.tick(snake_speed)




if __name__ == '__main__':
    main()