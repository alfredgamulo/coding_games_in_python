from random import randint

import pgzrun

apple = Actor("apple")


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


place_apple()


def draw():
    screen.clear()
    apple.draw()


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed.")
        quit()


pgzrun.go()
