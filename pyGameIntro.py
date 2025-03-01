import pygame
import time
import random

pygame.init()

# Defines size of game window
display_width = 800
display_height = 600

# Initializes the display
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Title of the game window
pygame.display.set_caption('A bit Racey')

# Defines colors in rgb format
black = ( 0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Defines width of car image
car_width = 70
car_height = 70

# Defines clock to track time in game
clock = pygame.time.Clock()
# Defines variable to check when to quit the game
crashed = False
# Defines image of racecar from file
carImg = pygame.image.load('./assets/racecar.png')

#Function to track number of things dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

# Function that creates obstacles
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])

# Function to draw the car image scaled to display
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

# Function that draws the text on the screen
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function handles where and how text displays
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)


# Function that runs when car image hits boundry and displays crash message
def crash():
    message_display("You Crashed")
    gameLoop()

# Function that handles the gameplay loop
def gameLoop():
    # Variables that scales depending on display size
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    # Randomly creates starting value for thing
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thing_count = 1

    dodged = 0

    # Defines variable to check when to quit the game
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Checks for if left or right arrow key is pressed and sets x_change accordingly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # Resets x_change to 0 if left or right arrow key is let go
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Moves racecar image based off the key pressed
        x += x_change
            

        gameDisplay.fill(white)

        # Draws thing and moves it based off the speed
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, (display_width))
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
        
        if y < (thing_starty + thing_height):
            #print('y crossover')
            if (x + car_width) > (thing_startx) and x < (thing_startx + thing_width):
                crash()

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()