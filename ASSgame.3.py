import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

font = pygame.font.SysFont("arial", 20)

Spawnpoint = [330, 170, 20, 480]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

def message(msg, txt_colour, bkgd_colour, x_location, y_location):
    """Messages are structured."""
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x_location, y_location))
    screen.blit(txt, text_box)

class cars:

    def __init__(self, image):
        self.car_x = random.choice(Spawnpoint)
        self.car_y = random.randrange(-50, -300, -10)
        self.angle = 180
        self.image = image
        self.speed = 4

    def make_car(self):
        if self.angle == 180:
            y_pos = 0
        self.rect = pygame.Rect(self.car_x, self.car_y, 90, 180)
        car_png = "car_" + str(self.image) + ".png"
        car_image = pygame.image.load(car_png).convert_alpha()
        resized_car_image = pygame.transform.smoothscale(car_image, [90, 180])
        rotated_img = pygame.transform.rotate(resized_car_image, self.angle)
        screen.blit(rotated_img, self.rect)

    def move(self):
        self.car_y += self.speed
        if self.car_y > 700:
            self.car_y = random.randrange(-50, -300, -10)
            self.car_x = random.choice(Spawnpoint)
            


def game_loop():
    game_over = False
    quit_game = False             
    player_x = 330
    player_y = 420
    player_x_change = 0
    player_y_change = 0

    car1 = cars(3)
    car2 = cars(2)
    car_list = [car1,car2]
    

    pygame.display.update()                
    
    while not quit_game:

        while game_over is True:
            message("You crashed! Press R to play again or Q to quit",
                    black, white, 300, 300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


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
            item.move()

        
        lines = [150, 300, 450]
        for x in lines:
            pygame.draw.rect(screen, yellow, [x, 0, 10, 600])
        player_cords = pygame.Rect(player_x, player_y, 50, 100)
        screen.blit(resized_player, player_cords)

        if player_cords.colliderect(item.rect):
            game_over = True
        pygame.display.update()
menu = True

while menu:
    message("Welcome to the car game press R to play or Q to quit",
            black, white, 300, 300)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_loop()
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
    
game_loop()

pygame.quit()
quit()
