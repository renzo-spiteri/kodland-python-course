#pgzero
#ignore the fact that its called duck(1)... you'll see once you play
import random
WIDTH = 600 # Window width
HEIGHT = 300 # Window height

TITLE = "Alien Runner" # Title for the game window
FPS = 30 # Number of frames per second

# Objects
flyheight = random.randint(120,180)
alien = Actor('stand', (50, 240))
background = Actor("background")
worm = Actor('worm', (550, 265))
new_image = 'stand' #Tracking the current image
fly = Actor('fly', (550, 175))
go = Actor("background")
game_over = 0
count = 0
enemy = random.randint(1,2)
speed = 5
def draw():
    background.draw()
    alien.draw()
    if enemy == 1:
        fly.draw()
    else:
        worm.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    
    if game_over == 1:
        go.draw()
        screen.draw.text('Press Enter to restart', pos=(WIDTH//2, HEIGHT//2), color= "white", fontsize = 36)

def bees():
    global count
    global enemy
    global speed
    # Bee movement
    if fly.x > -20:
        fly.x = fly.x - speed
    else:
        flyheight = random.randint(120,180)
        fly.y = flyheight
        fly.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1

def boxes():
    global count
    global enemy
    global speed
    # Box movement
    if worm.image == 'worm':
        worm.image = 'worm1'
    else:
        worm.image = 'worm'
    if worm.x > -20:
        worm.x = worm.x - speed
    else:
        worm.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1

def update(dt):
    global new_image
    global game_over
    global count
    global speed
    if enemy == 1:
        bees()
    else:
        boxes()
    # Controls
    if keyboard.left or keyboard.a and alien.x > 20:
        alien.x = alien.x - 5
        if new_image != 'left':
            alien.image = 'left'
            new_image = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580:
        alien.x = alien.x + 5
        if new_image != 'right':
            alien.image = 'right'
            new_image = 'right'
    elif keyboard.down or keyboard.s:
        if new_image != 'duck(1)':
            alien.image = 'duck(1)'
            new_image = 'duck(1)'
            alien.y = 250
    else:
        if alien.y > 240 and new_image == 'duck(1)':
            alien.image = 'stand'
            new_image = 'stand'
            alien.y = 240
    
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        speed = 5
        alien.pos = (50, 240)
        worm.pos = (550, 265)
        fly.pos = (850, 175)
    
    # Collision
    if alien.colliderect(worm) or alien.colliderect(fly):
        game_over = 1
        
def on_key_down(key):
    # Jump
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)