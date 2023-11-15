#pgzero
import random
# Game window
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("crack")
cell3 = Actor("bones")
size_w = 9 # Width of field in cells
size_h = 10 # Height of field in cells
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
map2 = random.randint(1, 2)
win = 0
mode = 'game'
TITLE = "Dungeons" # Title of the game window
FPS = 30 # Number of Frames Per Second
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 2, 1, 3, 1, 1, 0],
          [0, 1, 1, 1, 2, 1, 1, 1, 0],
          [0, 1, 3, 2, 1, 1, 3, 1, 0],
          [0, 1, 1, 1, 1, 3, 1, 1, 0],
          [0, 1, 1, 3, 1, 1, 2, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Attack and health power row
mymap = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 3, 2, 2, 1, 3, 1, 0],
         [0, 1, 3, 3, 1, 3, 2, 1, 0],
         [0, 2, 3, 1, 2, 3, 1, 2, 0], 
         [0, 1, 2, 3, 2, 2, 2 ,3, 0], 
         [0, 2, 3, 3, 1, 1, 1, 2, 0], 
         [0, 1, 1, 1, 2, 3, 3, 3, 0], 
         [0, 3, 2, 1, 1, 1, 1, 2, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
# Protagonist
char = Actor('stand')
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5
# Generating enemies
enemies = []
for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height
    enemy = Actor("enemy", topleft=(x, y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemy.bonus = random.randint(0, 2)
    enemies.append(enemy)

# Bonuses
hearts = []
swords = []


def map_draw():
    global map2, my_map, mymap, cell, cell1, cell2, cell3
    if map2 == 1:
        for i in range(len(my_map)):
            for j in range(len(my_map[0])):
                if my_map[i][j] == 0:
                    cell.left = cell.width * j
                    cell.top = cell.height * i
                    cell.draw()
                elif my_map[i][j] == 1:
                    cell1.left = cell.width * j
                    cell1.top = cell.height * i
                    cell1.draw()
                elif my_map[i][j] == 2:
                    cell2.left = cell.width * j
                    cell2.top = cell.height * i
                    cell2.draw()  
                elif my_map[i][j] == 3:
                    cell3.left = cell.width * j
                    cell3.top = cell.height * i
                    cell3.draw()
    if map2 == 2:
        for i in range(len(mymap)):
            for j in range(len(mymap[0])):
                if mymap[i][j] == 0:
                    cell.left = cell.width * j
                    cell.top = cell.height * i
                    cell.draw()
                elif mymap[i][j] == 1:
                    cell1.left = cell.width * j
                    cell1.top = cell.height * i
                    cell1.draw()
                elif mymap[i][j] == 2:
                    cell2.left = cell.width * j
                    cell2.top = cell.height * i
                    cell2.draw()  
                elif mymap[i][j] == 3:
                    cell3.left = cell.width * j
                    cell3.top = cell.height * i
                    cell3.draw()


def draw():
    global win, mode

    if mode == 'game':
        screen.fill("#2f3542")
        map_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 475), color='white', fontsize=20)
        screen.draw.text(str(char.health), center=(75, 475), color='white', fontsize=20)  # Convert health to string
        screen.draw.text("AP:", center=(375, 475), color='white', fontsize=20)
        screen.draw.text(str(char.attack), center=(425, 475), color='white', fontsize=20)  # Convert attack to string

        for i in range(len(enemies)):
            enemies[i].draw()

        for i in range(len(hearts)):
            hearts[i].draw()

        for i in range(len(swords)):
            swords[i].draw()

    if win == 1:
        screen.fill("#2f3542")
        screen.draw.text('You win!', center=(WIDTH // 2, HEIGHT // 2), color='white', fontsize=30)
    elif mode == "end" and win == -1:
        screen.fill("#2f3542")
        screen.draw.text('You lose', center=(WIDTH // 2, HEIGHT // 2), color='white', fontsize=30)


def on_key_down(key):
    global mode
    old_x = char.x
    print(old_x)
    old_y = char.y

    if (keyboard.right or keyboard.d) and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'stand'
    elif (keyboard.left or keyboard.a) and char.x - cell.width > cell.width:
        char.x -= cell.width
        char.image = 'left'
    elif (keyboard.down or keyboard.s) and char.y + cell.height < HEIGHT - cell.height*2:
        char.y += cell.height
    elif (keyboard.up or keyboard.w) and char.y - cell.height > cell.height:
        char.y -= cell.height

    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            if enemy.bonus == 1:
                heart = Actor('heart')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Actor('sword')
                sword.pos = enemy.pos
                swords.append(sword)
            enemies.pop(enemy_index)

        # Move the position reset inside the collision block
        char.x = old_x
        char.y = old_y


def victory():
    global win, mode
    if char.health > 0 and not enemies:
        win = 1
        mode = "end"


def defeat():
    global win, mode
    if char.health <= 0:
        win = -1
        mode = "end"


def update(dt):
    victory()
    defeat()
    for i in range(len(hearts)):
        if char.colliderect(hearts[i]):
            char.health += random.randint(2, 7)
            hearts.pop(i)
    for i in range(len(swords)):
        if char.colliderect(swords[i]):
            char.attack += random.randint(2, 7)
            swords.pop(i)
