import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor("bee")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("background", (0,0))
    flower.draw()
    bee.draw()

def place_flower():
    flower.x = random.randint(70,WIDTH -70)
    flower.y = random.randint(70,HEIGHT -70)

def update():
    if keyboard.right:
        bee.x = bee.x + 2 
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score = score + 10
        place_flower()

pgzrun.go()
