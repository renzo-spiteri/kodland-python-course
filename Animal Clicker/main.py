#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Animal clicker"
FPS = 30

# Objects
animal = Actor("chick", (150, 250))
penguin = Actor("penguin", (120, 200))
dog = Actor("dog", (300, 200))
parrot = Actor('parrot', (480, 200))
background = Actor("background")
bonus1_1 = Actor("bonus1", (450, 100))
bonus1_2 = Actor("bonus1", (450, 200))
bonus1_3 = Actor("bonus1", (450, 300))
play = Actor("bonus1", (300, 100))
shop = Actor("bonus1", (300,200))
collection = Actor("bonus1", (300,300))
cross = Actor("cross", (580,20))
animals = []

# Variables
count = 0
click = 1
mode = 'menu'

def draw():
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        shop.draw()
        collection.draw()
        screen.draw.text("Play", center=(300, 100), color="black", fontsize = 40)
        screen.draw.text("Shop", center=(300,200), color="black", fontsize = 40)
        screen.draw.text("Collection", center=(300, 300), color="black", fontsize = 40)
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus1_1.draw()
        screen.draw.text("+1$ every 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("price: 15$", center=(450, 110), color="black", fontsize = 20)
        bonus1_2.draw()
        screen.draw.text("+15$ every 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("price: 200$", center=(450, 210), color="black", fontsize = 20)
        bonus1_3.draw()
        screen.draw.text("+50$ every 2s", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text("price: 600$", center=(450, 310), color="black", fontsize = 20)
        cross.draw()
    elif mode == 'shop':
        background.draw()
        penguin.draw()
        dog.draw()
        parrot.draw()
        cross.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("500$", center=(120, 300), color="white", fontsize = 36)
        screen.draw.text("2500$", center=(300, 300), color="white", fontsize = 36)
        screen.draw.text("7000$", center=(480, 300), color="white", fontsize = 36)
    elif mode == 'collection':
        background.draw()
        for i in range(len(animals)):
            animals[i].draw()
        cross.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("+2$", center=(120, 300), color="white", fontsize = 36)
        screen.draw.text("+3$", center=(300, 300), color="white", fontsize = 36)
        screen.draw.text("+4$", center=(480, 300), color="white", fontsize = 36)
def for_bonus1_1():
    global count
    count += 1

def for_bonus1_2():
    global count
    count += 15

def for_bonus1_3():
    global count
    count += 50

def on_mouse_down(button, pos):
    global count
    global mode
    global click
    if button == mouse.LEFT and mode =='menu':
        if shop.collidepoint(pos):
            shop.y = 205
            animate(shop, tween='bounce_end', duration=0.5, y=200)
        elif collection.collidepoint(pos):
            collection.y = 305
            animate(collection, tween='bounce_end', duration=0.5, y=300)
    if button == mouse.LEFT and mode == 'game':
        # Click on the animal object
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Click on the bonus1_1 button
        elif bonus1_1.collidepoint(pos):
            bonus1_1.y = 105
            animate(bonus1_1, tween='bounce_end', duration=0.5, y=100)
            if count >= 15:
                schedule_interval(for_bonus1_1, 2)
                count -= 15
        # Click on the bonus1_2 button  
        elif bonus1_2.collidepoint(pos):
            bonus1_2.y = 205
            animate(bonus1_2, tween='bounce_end', duration=0.5, y=200)
            if count >= 200:
                schedule_interval(for_bonus1_2, 2)
                count -= 200
        # Click on the bonus1_3 button
        elif bonus1_3.collidepoint(pos):
            bonus1_3.y = 305
            animate(bonus1_3, tween='bounce_end', duration=0.5, y=300)
            if count >= 600:
                schedule_interval(for_bonus1_3, 2)
                count -= 600
        elif cross.collidepoint(pos):
            mode = "menu"
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
        #shop mode        
        elif shop.collidepoint(pos):
            mode = "shop"
        #collection
        elif collection.collidepoint(pos):
            mode = "collection"
    #SHOP FUNCTIONALTY
    elif mode == "shop" and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = "menu"
            #penguin
        elif penguin.collidepoint(pos):
            penguin.y = 180
            animate(penguin, tween='bounce_end', duration=0.5, y=200)
            if penguin in animals:
                animal.image = "penguin"
            else:
                if count >= 500:
                    count -= 500
                    click = 2
                    animal.image = "penguin"
                    animals.append(penguin)
        elif dog.collidepoint(pos):
            dog.y = 180
            animate(dog, tween='bounce_end', duration=0.5, y=200)
            if dog in animals:
                animal.image = "dog"
            else:
                if count >= 2500:
                    count -= 2500
                    click = 3
                    animal.image = "dog"
                    animals.append(dog)
        elif parrot.collidepoint(pos):
            parrot.y = 180
            animate(parrot, tween='bounce_end', duration=0.5, y = 200)
            if parrot in animals:
                animal.image = "parrot"
            else:
                if count >= 7000:
                    count -= 7000
                    click = 4
                    animal.image = "parrot"
                    animals.append(parrot)
    #COLLECTION FUNCTIONALTY
    elif mode == "collection" and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = "menu"
            #penguin
        elif penguin.collidepoint(pos) and penguin in animals:
            penguin.y = 180
            animate(penguin, tween='bounce_end', duration=0.5, y=200)
            click = 2
            animal.image = "penguin"
        elif dog.collidepoint(pos) and dog in animals:
            dog.y = 180
            animate(dog, tween='bounce_end', duration=0.5, y=200)
            click = 3
            animal.image = "dog"
        elif parrot.collidepoint(pos) and parrot in animals:
            parrot.y = 180
            animate(parrot, tween='bounce_end', duration=0.5, y=200)
            click = 4
            animal.image = "parrot"