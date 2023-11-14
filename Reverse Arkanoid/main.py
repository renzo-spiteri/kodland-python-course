#pgzero
import random
WIDTH = 1000
HEIGHT = 600

TITLE = "Reverse Arkanoid"
FPS = 30

INITIALNUMBEROFBALLS = 2
MAXORIGINALSPEED=10
MINORIGINALSPEED=4
PLAYERMOVESPEED = 20
SPEEDINCREMENT=0.2
MAXIMUMBALLS=10
MAXIMUMLIVES=3
BALLRADIUS=23
STARTXLEFT = BALLRADIUS
STARTXRIGHT = WIDTH - BALLRADIUS
playerScore = 0
highScore = 0
level = 1
lives = MAXIMUMLIVES
player = Actor("Player", (WIDTH//2,HEIGHT//2))
balls = []
hearts = []
mode = "pregame"
numberofballs = INITIALNUMBEROFBALLS
def refresh():
    global balls
    balls = []
    makeballs()
    makehearts()
def restart():
    global balls, playerScore, level, lives, i, numberofballs
    balls = []
    numberofballs = INITIALNUMBEROFBALLS
    lives = MAXIMUMLIVES
    playerScore = 0
    level = 1

def makeballs():
    for i in range(numberofballs):
        balls.append(makeball())
def makehearts():
    global hearts
    hearts = []
    for i in range(lives):
        hearts.append(makeheart(i))
def makeball():
    #do not start with an already collided ball
    collisionFound = True
    while collisionFound:
        collisionFound = False
        startRight = random.randint(0,1)
        ballcolor = random.randint(1,5)
        random_y = random.randint(BALLRADIUS, HEIGHT - BALLRADIUS)
        start_x = STARTXRIGHT if startRight == 1 else STARTXLEFT
        baseSpeed = level * SPEEDINCREMENT
        xspeed = random.uniform(MINORIGINALSPEED + baseSpeed, MAXORIGINALSPEED + baseSpeed) * (1 if startRight else -1)
        yspeed = random.uniform(MINORIGINALSPEED, MAXORIGINALSPEED)
        ball = Actor("ball" + str(ballcolor), (start_x, random_y))
        ball.original_pos = (start_x, random_y)
        ball.xspeed = xspeed
        ball.yspeed = yspeed

        for other_ball in balls:
            if other_ball != ball and ball.colliderect(other_ball):
                collisionFound = True
    return ball
def makeheart(i):
    heartx = 30 * (1+i)
    hearty = 86
    heart = Actor("heart", (heartx, hearty))
    return heart  # Return the created heart
#Ball movement
def ballsfunc():
    for ball in balls:
        ballMoveX(ball)
        ballMoveY(ball)
        for other_ball in balls:
            if other_ball != ball and ball.colliderect(other_ball):
                ball.xspeed = ball.xspeed * -1
                ball.x = ball.x + ball.xspeed
                ball.yspeed = ball.yspeed * -1     
                ball.y = ball.y + ball.yspeed

def ballMoveX(ball):
    global playerScore
    if ball.x >= (WIDTH - BALLRADIUS) or ball.x <= BALLRADIUS:
        ball.xspeed = ball.xspeed * -1
        playerScore += 1
        if ball.x <= BALLRADIUS:
            ball.x = BALLRADIUS + 1
        else:
            ball.x = WIDTH - BALLRADIUS - 1
    ball.x = ball.x + ball.xspeed

def ballMoveY(ball):
    global playerScore
    if ball.y >= (HEIGHT - BALLRADIUS) or ball.y <= BALLRADIUS:
        ball.yspeed = ball.yspeed * -1
        playerScore += 1
        if ball.y <= BALLRADIUS:
            ball.y = BALLRADIUS + 1
        else:
            ball.y = HEIGHT - BALLRADIUS - 1
    ball.y = ball.y + ball.yspeed


def draw():
    global mode, highScore
    screen.clear()
    if mode == "game":
        screen.draw.text("Level: "+str(level), center=(65, 20), color="green", fontsize = 36)
        screen.draw.text("Score: "+str(playerScore), center=(75, 56), color="white", fontsize = 36)
        
        player.draw()
        for i in range(len(balls)):
            balls[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
    elif mode == "pregame":
        screen.draw.text("Press Enter To Start", center = (WIDTH//2,HEIGHT//2), color = "white",fontsize = 40)
    elif mode == "gameover":
        screen.draw.text("Game Over!", center = (WIDTH//2,HEIGHT//2 - 80), color = "red", fontsize = 80)
        screen.draw.text("Your Score: " + str(playerScore), center = (WIDTH//2,HEIGHT//2 + 40), color = "white", fontsize = 40)
        if playerScore >= highScore:
            highScore = playerScore
            screen.draw.text("NEW HIGHSCORE", center = (WIDTH//2,HEIGHT//2 - 150), color = "red", fontsize=80)

def speedupballs():
    global level
    level = level + 1
    for ball in balls:
        if (ball.xspeed > 0):
            ball.xspeed = ball.xspeed + SPEEDINCREMENT
        else:
            ball.xspeed = ball.xspeed - SPEEDINCREMENT
            
        if (ball.yspeed > 0):
            ball.yspeed = ball.yspeed + SPEEDINCREMENT
        else:
            ball.yspeed = ball.yspeed - SPEEDINCREMENT
            
def update(dt):
    global mode, NUMBEROFBALLS, balls, playerScore, lives, numberofballs
    if mode == "game":
        ballsfunc()
        if (keyboard.up or keyboard.w) and player.y > 20:
            player.y -= PLAYERMOVESPEED
        elif (keyboard.down or keyboard.s) and player.y < HEIGHT - 20:
            player.y += PLAYERMOVESPEED
        x = player.collidelist(balls)
        if x != -1:
            lives -=1
            if lives == 0:
                mode = "gameover"
            else:
                refresh()
        if playerScore % 20 == 0 and len(balls) < MAXIMUMBALLS:
            numberofballs += 1
            balls.append(makeball())
        if playerScore % 10 == 0 and playerScore / 10 == level:
            speedupballs()
    elif mode == "pregame" or mode == "gameover":
            if keyboard.enter:
                restart()
                refresh()
                mode = "game"
def on_key_down(key):
    if (keyboard.left or keyboard.right):
        if player.image == "Player":
            player.image = "Playervertical"
        else:
            player.image = "Player"