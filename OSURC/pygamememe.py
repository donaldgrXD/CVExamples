import pygame

pygame.init() #initializes the game commands and functions

gameDisplay = pygame.display.set_mode((508,644)) #define the main display
pygame.display.set_caption('MEME') #sets the name of the window

black = (0,0,0) #defining black with RGB
white = (255,255,255) #defining white with RGB
green = (86, 176, 0)

background_image = pygame.image.load("image.png").convert()

clock = pygame.time.Clock() #ingame clock (for fps and time)

crashed = False

def square(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

x = 0
y = 0
x_change = 0
y_change = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
        print(event)
        
    x += x_change
    y += y_change

    if x < 0 or y < 0 or x > 494 or y > 634:
        x -= x_change
        y -= y_change

    pygame.image.save(gameDisplay,'temp.jpeg')
    gameDisplay.blit(background_image, [0, 0])
    square(x,y, 10, 10, black)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
