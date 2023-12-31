import pygame

pygame.init()

pygame.display.set_caption('my name is bojack horseman')

screen = pygame.display.set_mode((750,500))

image = pygame.image.load('bojack.png')

image2 = pygame.image.load('horse2.jpg')
image2r = pygame.transform.scale(image2,(400,350))

imgrect = image.get_rect()
imgrect.center = ((375,250))

#music for bojack
music = pygame.mixer.music.load('Rehab was supposed to be a fresh start.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(500)

while True:

    screen.fill('purple')
    # screen.blit(image, (0,0))
    screen.blit(image, imgrect)
    screen.blit(image2r, (-100,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()







