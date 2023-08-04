import random

player_health = 100
player_hunger = 0
player_thirst = 0

def take_damage(amount):
    global player_health
    player_health -= amount
    if player_health <= 0:
        print("Game Over")

def eat_food():
    global player_hunger
    player_hunger -= random.randint(10, 20)
    if player_hunger < 0:
        player_hunger = 0
    print("You ate some food. Hunger decreased.")

def drink_water():
    global player_thirst
    player_thirst -= random.randint(10, 20)
    if player_thirst < 0:
        player_thirst = 0
    print("You drank some water. Thirst decreased.")

while True:
    choice = input("What would you like to do? (1 - Eat, 2 - Drink, 3 - Quit): ")
    
    if choice == "1":
        eat_food()
    elif choice == "2":
        drink_water()
    elif choice == "3":
        print("Game Over")
        break
    else:
        print("Invalid choice.")

    player_hunger += random.randint(5, 10)
    player_thirst += random.randint(5, 10)

    if player_hunger >= 100:
        print("You are starving!")
        take_damage(20)

    if player_thirst >= 100:
        print("You are dehydrated!")
        take_damage(20)

    print("Health:", player_health)
    print("Hunger:", player_hunger)
    print("Thirst:", player_thirst)