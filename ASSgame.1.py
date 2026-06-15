import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

black = (0, 0, 0)
yellow = (255, 255, 0)

Spawnpoint = [330, 170, 20, 480]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


class cars:

    def __init__(self):
        self.car_x = random.choice(Spawnpoint)
        self.car_y = 100
        self.angle = 180

    def make_car(self):
        if self.angle == 180:
            y_pos = 0
        self.rect = pygame.Rect(self.car_x, y_pos, 90, 180)
        car_image = pygame.image.load("car_1.png").convert_alpha()
        resized_car_image = pygame.transform.smoothscale(car_image, [90, 180])
        rotated_img = pygame.transform.rotate(resized_car_image, self.angle)
        screen.blit(rotated_img, self.rect)
        

def game_loop():
    quit_game = False
    player_x = 330
    player_y = 420
    player_x_change = 0
    player_y_change = 0

    car_list = [cars()]
    

    pygame.display.update()                
    
    while not quit_game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True


            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x_change = -5
                        player_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        player_x_change = 5
                        player_y_change = 0

        player_x += player_x_change
        player_y += player_y_change

        if player_x > 510:
            player_x = 510
        if player_x < 0:
            player_x = 0
        
    
        player = pygame.image.load('car_1.png').convert_alpha()
        resized_player = pygame.transform.smoothscale(player, [90, 180])
        
        screen.fill(black)

        for item in car_list:
            item.make_car()
        
        lines = [150, 300, 450]
        for x in lines:
            pygame.draw.rect(screen, yellow, [x, 0, 10, 600])
        player_cords = pygame.Rect(player_x, player_y, 50, 100)
        screen.blit(resized_player, player_cords)
        pygame.display.update()
game_loop()
pygame.quit()
quit()
