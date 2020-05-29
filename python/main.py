from .screen_dimensions import *

# initializing pygame
import pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("The helios attack")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)

# loading images
poison_ = pygame.image.load('Image/32px/poison.png')
fire_ = pygame.image.load('Image/32px/fire.png')
plasma_ = pygame.image.load('Image/32px/plasma_small.png')
goc_ = pygame.image.load('Image/32px/space.png')


# putting images on screen
def spells():
    screen.blit(poison_, (sw(0.73), sh(90.66)))
    screen.blit(fire_, (sw(3.66), sh(90.66)))
    screen.blit(plasma_, (sw(6.59), sh(90.66)))
    screen.blit(goc_, (sw(9.51), sh(90.66)))


def troops():
    pass


def controls():
    pass


# mouse click events

def poison():
    print('Poison')
    pass


def fire():
    print('Incinerate')
    pass


def plasma():
    print('Plasma')
    pass


def goc():
    print('God of Chaos')
    pass


"""
GAME LOOPS BELOW
"""


# Menu Loop
def menu():
    active = True
    while active:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if 619+128 > x > 619 and 384+64 > y > 384:
                    game()
                    active = False

        pygame.draw.rect(screen, (0, 255, 0), (619, 384, 128, 64))
        pygame.display.update()




# Main loop
def game():
    running = True
    while running:

        screen.fill((0, 0, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)

                # calling function if mouse is clicked when cursor is over dimensions of specific image
                if 10+32 > x > 10 and 660+32 > y > 660:
                    poison()
                elif 50+32 > x > 10 and 660+32 > y > 660:
                    fire()
                elif 90+32 > x > 10 and 660+32 > y > 660:
                    plasma()
                elif 130+32 > x > 10 and 660+32 > y > 660:
                    goc()

        spells()
        pygame.display.update()


'''
GAMES FLOW OF CONTROL
'''
menu()

pygame.quit()
