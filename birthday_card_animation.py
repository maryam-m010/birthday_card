import pygame, sys, time

pygame.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("birthday card animation")
screen.fill("white")

balloon = pygame.image.load("balloon.png")
balloon_resized = pygame.transform.scale(balloon, (WIDTH, HEIGHT))

presents = pygame.image.load("presents.png")
presents_resized = pygame.transform.scale(presents, (WIDTH, HEIGHT))

cake = pygame.image.load("cake.png")
cake_resized = pygame.transform.scale(cake, (WIDTH, HEIGHT))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(balloon_resized, (0,0))
    font = pygame.font.SysFont("Times New Roman", 70)
    text = font.render("Happy Birthday!", True, (66, 161, 245))
    screen.blit(text, (75,200))
    pygame.display.update()
    time.sleep(3)

    screen.blit(presents_resized, (0,0))
    font1 = pygame.font.SysFont("Times New Roman", 35)
    text1 = font1.render("Wishing you a bright future ahead!", True, (219, 118, 245))
    screen.blit(text1, (50,50))
    pygame.display.update()
    time.sleep(3)

    screen.blit(cake_resized, (0,0))
    pygame.display.update()
    time.sleep(3)