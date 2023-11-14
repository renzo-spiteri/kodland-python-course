import turtle
import random

t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)

# race field
for i in range(15):
    t.write(i)
    t.right(90)
    t.fd(200)
    t.up()
    t.bk(200)
    t.left(90)
    t.down()
    t.fd(20)

# On your marks...
#first racer
r1 = turtle.Turtle()
r1.up()
r1.shape("turtle")
r1.color("red")
r1.goto(-120,70)
r1.down()
#second racer
r2 = turtle.Turtle()
r2.up()
r2.shape("turtle")
r2.color("blue")
r2.goto(-120,40)
r2.down()
#third racer
r3 = turtle.Turtle()
r3.up()
r3.shape("turtle")
r3.color("yellow")
r3.goto(-120,10)
r3.down()
#Add the fans

#guessing
win = input ("Which turtle will win:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("You think that the winner will be " + win)
#go!
r1_dist = 0
r2_dist = 0
r3_dist = 0
while True:
    if r1_dist >= 305:
        text.clear()
        text.write("And the winner of this race is red!")
        break
    elif r2_dist >= 305:
        text.clear()
        text.write("And the winner of this race is blue!")
        break
    elif r3_dist >= 305:
        text.clear()
        text.write("And the winner of this race is yellow!")
        break
    else:
        r1m = random.randint(1,5)
        r2m = random.randint(1,5)
        r3m = random.randint(1,5)
        r1_dist = r1_dist + r1m
        r2_dist = r2_dist + r2m
        r3_dist = r3_dist + r3m
        r1.fd(r1m)
        r2.fd(r2m)
        r3.fd(r3m)

