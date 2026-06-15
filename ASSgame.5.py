"""This is a program for a car dodging game."""

import pygame
import random

pygame.init()

# Screens dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colours
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# font of text
font = pygame.font.SysFont("arial", 20)

# Counts time
clock = pygame.time.Clock()

# Creates the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


# Function for creating messages
def message(msg, txt_colour, bkgd_colour, x_location, y_location):
    """Messages are structured."""
    txt = font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(x_location, y_location))
    screen.blit(txt, text_box)


class CARS:
    """Creates The CARS."""

    def __init__(self, image, car_x):
        """CAR Details."""
        self.car_x = car_x
        self.car_y = random.randrange(-200, -800, -100)
        self.angle = 180
        self.image = image
        self.speed = random.randrange(3, 6, 1)
        self.passed = False

    def make_car(self):
        """Spawning in the CAR."""
        self.rect = pygame.Rect(self.car_x, self.car_y, 90, 180)
        car_png = "car_" + str(self.image) + ".png"
        car_image = pygame.image.load(car_png).convert_alpha()
        resized_car_image = pygame.transform.smoothscale(car_image, [90, 180])
        rotated_img = pygame.transform.rotate(resized_car_image, self.angle)
        screen.blit(rotated_img, self.rect)

    def move(self):
        """How CAR Moves."""
        self.car_y += self.speed
        if self.car_y > 700:
            self.car_y = random.randrange(-200, -800, -100)
            self.speed = random.randrange(3, 6, 1)
            self.passed = False


def load_highscore():
    """LOAD HIGHSCORE."""
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0


def save_highscore(highscore):
    """SAVE HIGHSCORE."""
    with open("highscore.txt", "w") as f:
        f.write(str(highscore))


# Runs game loop
def game_loop():
    """Run Loop."""
    game_over = False
    quit_game = False
    player_x = 328
    player_y = 420
    player_x_change = 0
    player_y_change = 0
    highscore = load_highscore()
    score = 0

    # Creates 4 cars with their image and x value
    car1 = CARS(3, 330)
    car2 = CARS(2, 180)
    car3 = CARS(1, 480)
    car4 = CARS(4, 20)
    car_list = [car1, car2, car3, car4]

    pygame.display.update()

    while not quit_game:

        # Creates game over screen
        while game_over is True:
            if score > highscore:
                highscore = score
                save_highscore(highscore)
            message("You crashed! Press R to play again or Q to quit",
                    BLACK, WHITE, 300, 300)
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

            # When holding key move that direction
            keys = pygame.key.get_pressed()
            player_x_change = 0
            if keys[pygame.K_LEFT]:
                player_x_change = -8
                player_y_change = 0
            if keys[pygame.K_RIGHT]:
                player_x_change = 8
                player_y_change = 0

        player_x += player_x_change
        player_y += player_y_change

        # Creates barrier so car can't go off screen
        if player_x > 510:
            player_x = 510
        if player_x < 0:
            player_x = 0

        # Creates player's car
        player = pygame.image.load('car_1.png').convert_alpha()
        resized_player = pygame.transform.smoothscale(player, [90, 180])

        # Makes black background
        screen.fill(BLACK)

        # Runs the functions to create cars and move them
        for item in car_list:
            item.make_car()
            item.move()

            # Detects when player has passed cars
            if not item.passed and item.car_y > player_y:
                score += 1
                item.passed = True

        # Creates yellow lines for road
        lines = [150, 300, 450, ]
        for x in lines:
            pygame.draw.rect(screen, YELLOW, [x, 0, 10, 600])
        player_cords = pygame.Rect(player_x, player_y, 50, 100)
        screen.blit(resized_player, player_cords)

        # Detects when collisions occur
        crash = [car for car in car_list if player_cords.colliderect(car.rect)]
        if crash:
            game_over = True

        # Displays score/highscore
        message(f"Highscore: {highscore}", WHITE, BLUE, 70, 20)
        message(f"Score: {score}", WHITE, BLUE, 40, 40)
        pygame.display.update()

# Creates menu for game before you start playing


menu = True


while menu:
    icon = pygame.image.load("game_icon.png").convert_alpha()
    resized_icon = pygame.transform.smoothscale(icon, [180, 90])
    icon_cords = pygame.Rect(210, 400, 200, 100)
    screen.blit(resized_icon, icon_cords)
    message("Welcome to the car game press R to play or Q to quit",
            BLACK, WHITE, 300, 300)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_loop()
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

# Ends game loop
game_loop()
pygame.quit()
quit()
