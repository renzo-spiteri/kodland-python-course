#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Space Journey"
FPS = 30

# Objects and variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("ship1",(100,200))
type2 = Actor("ship2",(300,200))
type3 = Actor("ship3",(500,200))
count = 0

# Making the enemy list
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
# Making the meteor list
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

# Function to restart the game
def restart_game():
    global mode
    global count

    # Reset variables
    count = 0
    mode = 'game'

    # Reset ship position
    ship.pos = (300, 400)

    # Reset lists
    enemies[:] = []  # Reassign an empty list
    meteors[:] = []  # Reassign an empty list
    bullets[:] = []  # Reassign an empty list

    # Refill enemy list
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        enemy = Actor("enemy", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)

    # Refill meteor list
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        meteor = Actor("meteor", (x, y))
        meteor.speed = random.randint(2, 10)
        meteors.append(meteor)

# Add this function to handle key presses
def on_key_down(key):
    global mode
    if key == keys.SPACE and mode == 'end':
        restart_game()

# Drawing up
def draw():
    global mode
    global count
    #menu mode
    if mode == "menu":
        space.draw()
        screen.draw.text('Сhoose a ship', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    # Game mode
    if mode == 'game':
        space.draw()
        screen.draw.text(count, pos=(10, 10), color="white", fontsize = 30, fontname = 'Viga')
        planets[0].draw()
        # Drawing meteors up
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Drawing enemies up
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(bullets)):
            bullets[i].draw()
    # Game over window   
    elif mode == 'end':
        space.draw()
        screen.draw.text(count, pos=(10, 10), color="white", fontsize = 30, fontname = 'Viga')
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text("Press Enter", pos=(230, 240), color="white", fontsize = 30, fontname = 'Viga', bold = True, italic = True, underline = True)
    if keyboard.enter and mode == "end":
        mode = "game"
        count = 0
        for a in range(len(planets)):
            a = a + 1
            planets.remove(planets[a])
        for b in range(len(enemies)):
            b = b + 1
            enemies.remove(enemies[b])
        for c in range(len(meteors)):
            c = c + 1
            meteors.remove(meteors[c])
        for i in range(len(bullets)):
            d = d + 1
            bullets.remove(bullets[d])
# Controls
def on_mouse_move(pos):
    ship.pos = pos

# Adding new enemies to the list
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Enemy movement
def enemy_ship():
    global count
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            count = count + 1
            enemies.pop(i)
            new_enemy()

# Planet movement
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Meteor movement
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)


# Collisions
def collisions():
    global mode
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        # Projectile collisions
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]):
                count = count + 1
                enemies.pop(i)
                bullets.pop(j)
                new_enemy()
                break
def update(dt):
    global count
    global mode
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        for i in range(len(bullets)):
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10
def on_mouse_down(button, pos):
    global mode
    if type1.collidepoint(pos) and mode == "menu":
        ship.image = "ship1"
        mode = "game"
    if type2.collidepoint(pos) and mode == "menu":
        ship.image = "ship2"
        mode = "game"
    if type3.collidepoint(pos) and mode == "menu":
        ship.image = "ship3"
        mode = "game"
    if (keyboard.rctrl or keyboard.lctrl) and (keyboard.rshift or keyboard.lshift) and keyboard.e and mode == "menu":
        ship.image = "skeldmap"
        mode = "game"

    #shooting
    if mode == "game" and button == mouse.LEFT:
        bullet = Actor('missiles')
        bullet.pos = ship.pos
        bullets.append(bullet)