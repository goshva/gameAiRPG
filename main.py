import pygame
import random
import time
# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Выживание в лесу")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

# Load images
background_image = pygame.image.load("forest.jpg")
ring_image = pygame.image.load("ring.jpg")
screen.blit(background_image, (0, 0))


clock = pygame.time.Clock()

player_magic = 0
player_health = 1000
player_hunger = 0
player_thirst = 0


font = pygame.font.Font(None, 30)
def draw_text(text, x, y):
    text_obj = font.render(text, True, BLACK)
    temp_surface = pygame.Surface(text_obj.get_size())
    temp_surface.fill(WHITE)
    temp_surface.blit(text_obj, (0, 0))
    screen.blit(temp_surface, (x, y))

def do_eat():
    draw_text("Ты поел и насытился", 350, 250)
    global player_hunger
    global background_image
    background_image = pygame.image.load("do_eat.png")
    player_hunger = 0
def do_drink():
    draw_text("Ты попил", 350, 300)
    global player_thirst
    global background_image
    background_image = pygame.image.load("do_drink.png")    
    player_thirst = 0
def do_sleep():
    draw_text("Ты поспал", 350, 200)
    global player_health
    global background_image
    background_image = pygame.image.load("do_sleep.png")   
    if player_health < 990:
        player_health +=10

def take_damage(amount):
    global player_health
    global running
    player_health -= amount
    if player_health <= 0:
        draw_text("Игра закончена", 350, 150)
        time.sleep(3)  
        running = False
def take_magic(amount):
    global player_magic
    global running
    player_magic += amount
    if player_magic >= 1000:
        draw_text("Игра Пройдена!", 350, 150)    
        time.sleep(3)  
        running = False
#HealthBar
class HealthBar():
  def __init__(self, x, y, w, h, max_hp,color):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp
    self.color = color
  def draw(self, surface):
    #calculate health ratio
    ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, self.color, (self.x, self.y, self.w * ratio, self.h))

magic_bar  = HealthBar(50, 150, 300, 30, 1000,"WHITE")
health_bar = HealthBar(50, 200, 300, 30, player_health,"GREEN")
hunger_bar = HealthBar(50, 250, 300, 30, 100,"YELLOW")
thirst_bar = HealthBar(50, 300, 300, 30, 100,"BLUE")

def intro():
        draw_text("Вы оказываетесь в густом лесу. Воздух свежий, а деревья над головой.", 50, 50)
        draw_text("В твоей руке волшебное кольцо, дающее тебе силу льда.", 50, 100)
        draw_text("Что бы вы хотели сделать?", 50, 150)
        draw_text("1. Снять кольцо и жить нормальной жизнью.", 50, 200)
        draw_text("2. Отправиться в путешествие с кольцом и силой льда.", 50, 250)
        draw_text("3. Поесть", 50, 300)
        draw_text("4. Попить", 50, 350)
        draw_text("5. Поспать", 50, 400)
        pygame.display.flip()
        time.sleep(10)

def simple_life():
        screen.blit(background_image, (0, 0))
        draw_text("Вы отправляетесь жить простой прекрасной жизьню", 50, 50)
        draw_text("Что бы вы хотели сделать сегодня?", 50, 100)
        draw_text("3. Поесть", 50, 300)
        draw_text("4. Попить", 50, 350)
        draw_text("5. Поспать", 50, 400)
        time.sleep(3)


intro()

# Game loop
running = True
while running:
    screen.blit(background_image, (0, 0))


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            do_eat()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            do_drink()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            do_sleep()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            simple_life()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            simple_life()            
    player_hunger += random.randint(1, 5)
    player_thirst += random.randint(1, 10)
    if player_hunger >= 100:
        draw_text("Ты голоден", 350, 250)
        background_image = pygame.image.load("hungry.png")
        take_damage(20)
    if player_thirst >= 100:
        draw_text("Ты хочешь пить", 350, 300)
        background_image = pygame.image.load("hungry.png")
        take_damage(20)    
    if player_health >= 1000:
        draw_text("Ты здров твоя магия растет", 350, 150)
        background_image = pygame.image.load("magic.png")
        take_magic(10)  
    #draw health bar
    health_bar.hp = player_health
    health_bar.draw(screen)
    hunger_bar.hp = 100 -player_hunger
    hunger_bar.draw(screen)
    thirst_bar.hp = 100 - player_thirst
    thirst_bar.draw(screen)
    magic_bar.hp = player_magic
    magic_bar.draw(screen)
        
    # Update the display
    pygame.display.flip()
    clock.tick(1)


# Quit pygame
pygame.quit()
