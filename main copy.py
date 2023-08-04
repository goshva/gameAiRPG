import pygame
import random
import time

player_health = 100
player_hunger = 0
player_thirst = 0
eat_food_do =False
drink_water_do =False
# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Forest Adventure")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
background_image = pygame.image.load("forest.jpg")
ring_image = pygame.image.load("ring.jpg")

# Set up fonts
font = pygame.font.Font(None, 30)
pygame.display.flip()

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))


def forest():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    simple_life()                
                if event.key == pygame.K_2:
                    journey()

        screen.blit(background_image, (0, 0))
        draw_text("Вы оказываетесь в густом лесу. Воздух свежий, а деревья над головой.", 50, 50)
        draw_text("В твоей руке волшебное кольцо, дающее тебе силу льда.", 50, 100)
        draw_text("Что бы вы хотели сделать?", 50, 150)
        draw_text("1. Снять кольцо и жить нормальной жизнью.", 50, 200)
        draw_text("2. Отправиться в путешествие с кольцом и силой льда.", 50, 250)

        pygame.display.flip()

def simple_life():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text("Вы отправляетесь жить простой прекрасной жизьню", 50, 50)
        draw_text("Что бы вы хотели сделать сегодня?", 50, 100)
        draw_text("1. Охота за едой.", 50, 150)
        draw_text("2. Исследовать окрестности.", 50, 200)
        draw_text("3. Отдыхай и восстанавливайся.", 50, 250)

        pygame.display.flip()

def journey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text("Вы отправляетесь в путешествие с кольцом и силой льда.", 50, 50)
        draw_text("Что бы вы хотели сделать сегодня?", 50, 100)
        draw_text("1. Охота за едой.", 50, 150)
        draw_text("2. Исследовать окрестности.", 50, 200)
        draw_text("3. Отдыхай и восстанавливайся.", 50, 250)

        pygame.display.flip()

def hunt():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text("You set out to hunt for food.", 50, 50)
        
        success = random.choice([True, False])
        if success:
            draw_text("Вы успешно поймали дикого кабана, используя свои ледяные силы.", 50, 100)
            draw_text("У вас достаточно еды, чтобы прокормиться еще на один день.", 50, 150)
        else:
            draw_text("Ваша попытка охоты не удалась, и вы голодали весь день.", 50, 100)
        
        pygame.display.flip()

def explore():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text("Вы решили исследовать окрестности.", 50, 50)
        draw_text("Углубляясь в лес, вы встречаете женщину.", 50, 100)
        draw_text("Что бы вы хотели сделать?", 50, 150)
        draw_text("1. Пойти с ней в деревню.", 50, 200)
        draw_text("2. Пойти дальше по лесу.", 50, 250)

        pygame.display.flip()

def rest():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text("Вы решили отдохнуть и восстановиться.", 50, 50)
        draw_text("Вы нашли безопасное место и получили заслуженный отдых.", 50, 100)
        draw_text("После хорошего ночного сна вы просыпаетесь отдохнувшим и готовым к следующему дню.", 50, 150)

        pygame.display.flip()

# Start the game
#forest()
def take_damage(amount):
    global player_health
    player_health -= amount
    if player_health <= 0:
        draw_text("Game Over", 50, 150)

def eat_food():
    global player_hunger
    player_hunger -= random.randint(10, 20)
    if player_hunger < 0:
        player_hunger = 0
    draw_text("You ate some food. Hunger decreased.", 50, 150)

def drink_water():
    global player_thirst
    player_thirst -= random.randint(10, 20)
    if player_thirst < 0:
        player_thirst = 0
    draw_text("You drank some water. Thirst decreased.", 50, 150)

def start_day():
    global player_health
    global player_hunger
    global player_thirst
    global eat_food_do
    global drink_water_do
    while(player_health>0):
        draw_text("Здоровье: "+ str(player_health), 50, 150)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                eat_food_do = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                drink_water_do = True

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                break

        if eat_food == True:
            eat_food()   
        if drink_water == True:
            drink_water()  
        #player_hunger += random.randint(5, 10)
        #player_thirst += random.randint(5, 10)

        if player_hunger >= 100:
            draw_text("You are starving!: "+ str(player_health), 50, 150)

            take_damage(20)

        if player_thirst >= 100:
            draw_text("You are dehydrated!", 50, 150)
            take_damage(20)
        screen.blit(background_image, (0, 0))
        draw_text("Здоровье: "+ str(player_health), 50, 150)
        draw_text("Голод: "+str(player_hunger), 50, 200)
        draw_text("Жажда: "+str(player_thirst), 50, 250)
        pygame.display.flip()




start_day()