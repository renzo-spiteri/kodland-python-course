import random
import pygame
from pygame.locals import *
import sys

pygame.init()
WIDTH = 1000
HEIGHT = 600
TITLE = "Reverse Arkanoid"
FPS = 30
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Rest of the code 
class Actor:
    def __init__(self, image, position):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self):
        window.blit(self.image, self.rect)

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
player = Actor("Player.png", (WIDTH//2,HEIGHT//2))
balls = []
hearts = []
mode = "pregame"
numberofballs = INITIALNUMBEROFBALLS
death_sfx = pygame.mixer.Sound("deathsound.mp3")
run = True
while run:
    clock.tick(FPS)
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
            ball = Actor("ball" + str(ballcolor) + ".png", (start_x, random_y))
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
        heart = Actor("heart.png", (heartx, hearty))
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

# Update the draw function
def draw():
    global mode, highScore, player, balls, hearts, level, playerScore
    window.fill((0, 0, 0))  # Fill window with black color
    if mode == "game":
        font = pygame.font.Font(None, 36)
        text = font.render("Level: " + str(level), True, (0, 255, 0))
        window.blit(text, (65, 20))
        text = font.render("Score: " + str(playerScore), True, (255, 255, 255))
        window.blit(text, (75, 56))

        player.draw()
        for ball in balls:
            ball.draw()
        for heart in hearts:
            heart.draw()
    elif mode == "pregame":
        font = pygame.font.Font(None, 40)
        text = font.render("Press Enter To Start", True, (255, 255, 255))
        window.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    elif mode == "gameover":
        font = pygame.font.Font(None, 80)
        text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(text, (WIDTH // 2 - 160, HEIGHT // 2 - 80))
        font = pygame.font.Font(None, 40)
        text = font.render("Your Score: " + str(playerScore), True, (255, 255, 255))
        window.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 + 40))
        if playerScore >= highScore:
            font = pygame.font.Font(None, 80)
            text = font.render("NEW HIGHSCORE", True, (255, 0, 0))
            window.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 - 150))

# Rest of the code 
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
            if pygame.event.type == pygame.KEYDOWN:
                if (KEYDOWN == pygame.K_.up or KEYDOWN == pygame.K_.w) and player.y > 20:
                    player.y -= PLAYERMOVESPEED
                elif (KEYDOWN == pygame.K_.down or KEYDOWN == pygame.K_.s) and player.y < HEIGHT - 20:
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
                if KEYDOWN == pygame.K_.enter:
                    restart()
                    refresh()
                    mode = "game"
    def on_key_down(key):
        if (KEYDOWN == pygame.K_.left or KEYDOWN == pygame.K_.right):
            if player.image == "Player":
                player.image = "Playervertical"
            else:
                player.image = "Player"
pygame.go()
pygame.quit()