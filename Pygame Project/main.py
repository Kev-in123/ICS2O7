# ***********************************************
#
# Program Author: Kevin Cai
# Revision Date: June 4th 2021
# Program Name:  Pygame Project
# Descptrion: Pygame Project About World War 2
#
# ***********************************************

import pygame
import random
pygame.init()

# variable declaration and initialization
clock = pygame.time.Clock()
correctamt = 0
black = (0, 0, 0)
gray = (80, 80, 80)
light_gray = (200, 200, 200)
white = (255, 255, 255)
size = (1100, 800)
xpos = 500
background = pygame.image.load("images/titleBackground.jpg")
background = pygame.transform.scale(background, size)
game_background = pygame.image.load("images/water.png")
game_background = pygame.transform.scale(game_background, size)
myfont = pygame.font.SysFont("Cuckoo", 50)
smallText = pygame.font.SysFont("Cuckoo", 75)
gameDisplay = pygame.display.set_mode(size)
shipImg = pygame.image.load("images\ship.png")
missileImg = pygame.image.load("images\missile.png")

# set a caption
pygame.display.set_caption("Pygame Project - Kevin Cai")

# function for a text object


def text_objects(text, font):
    # create a text surface
    textSurface = font.render(text, True, white)
    # return value
    return textSurface, textSurface.get_rect()

# function to display text


def message_display(text, x, y):
    # render text
    message = myfont.render(text, True, white)
    # display the text
    gameDisplay.blit(message, (x, y))

# function to create a button


def button(msg, x, y, w, h, inactive_colour, active_colour, action, fontsize):
    # get the mouse position
    mouse = pygame.mouse.get_pos()
    # checks if the mouse is pressed
    click = pygame.mouse.get_pressed()
    # checks if the mouse is over the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # display the rectangle as a button in its active state
        pygame.draw.rect(gameDisplay, active_colour, (x, y, w, h))
        # if the left mouse button is clicked
        if click[0] == 1:
            # checks the action and performs the corresponding function
            if action == "game_menu":
                game_menu()
            if action == "start_game":
                game()
            if action == "lessons":
                lesson()
            if action == "quiz":
                quiz()
            if action == "results":
                results()
            if action == "exit":
                _exit()
            if action == "main_menu":
                main_menu()
            if action == "lesson1":
                lesson1()
            if action == "lesson2":
                lesson2()
            if action == "lesson3":
                lesson3()
            if action == "lesson4":
                lesson4()
            if action == "lesson5":
                lesson5()
            if action == "quiz1":
                quiz1()
            if action == "quiz2":
                quiz2()
            if action == "quiz3":
                quiz3()
            if action == "quiz4":
                quiz4()
            if action == "quiz5":
                quiz5()
            if action == "correct1":
                correct1()
            if action == "incorrect1":
                incorrect1()
            if action == "correct2":
                correct2()
            if action == "incorrect2":
                incorrect2()
            if action == "correct3":
                correct3()
            if action == "incorrect3":
                incorrect3()
            if action == "correct4":
                correct4()
            if action == "incorrect4":
                incorrect4()
            if action == "correct5":
                correct5()
            if action == "incorrect5":
                incorrect5()
            if action == "None":
                pass

    else:
        # if the mouse isnt over the button
        pygame.draw.rect(gameDisplay, inactive_colour, (x, y, w, h))

    # display the text on the button
    smallText = pygame.font.SysFont("Cuckoo", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

# Title screen function


def titleScreen():
    # checks if the window is closed
    TitleScreen = True
    while TitleScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # display the background
        gameDisplay.blit(background, (0, 0))
        # render text
        message_display("WW2 By: Kevin Cai", 800, 225)
        message_display("June 3rd, 2021", 800, 275)
        message_display("ICS2O7", 800, 325)
        # create button
        button("Next", 800, 650, 100, 50, gray, light_gray, "main_menu", 40)
        # update screen
        pygame.display.update()

# functions for correct and incorrect answers


def correct1():
    # adds 1 point
    global correctamt
    correctamt += 1
    # display the message
    message_display("correct", 550, 400)
    # makes the buttons stay but disabling them
    button("Britain, The Soviet Union, and The United States",
           150, 300, 250, 100, gray, gray, "None", 25)
    button("     France, Canada, and Italy", 500,
           300, 250, 100, gray, gray, "None", 25)
    button("Brazil, India, and The United States",
           150, 450, 250, 100, gray, gray, "None", 25)
    button("     Germany, Japan, and Australia", 500,
           450, 250, 100, gray, gray, "None", 25)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz2()


def incorrect1():
    # display the message
    message_display("incorrect", 550, 400)
    # makes the buttons stay but disabling them
    button("Britain, The Soviet Union, and The United States",
           150, 300, 250, 100, gray, gray, "None", 25)
    button("     France, Canada, and Italy", 500,
           300, 250, 100, gray, gray, "None", 25)
    button("Brazil, India, and The United States",
           150, 450, 250, 100, gray, gray, "None", 25)
    button("     Germany, Japan, and Australia", 500,
           450, 250, 100, gray, gray, "None", 25)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz2()


def correct2():
    # adds 1 point
    global correctamt
    correctamt += 1
    # display the message
    message_display("correct", 550, 400)
    # makes the buttons stay but disabling them
    button("Brazil, India, and The United States",
           150, 300, 250, 100, gray, gray, "None", 25)
    button("     Britain, The Soviet Union, and The United States",
           500, 300, 250, 100, gray, gray, "None", 25)
    button("Germany, Japan, and Italy", 150,
           450, 250, 100, gray, gray, "None", 25)
    button("     Canada, France, and Australia", 500,
           450, 250, 100, gray, gray, "None", 25)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz3()


def incorrect2():
    # display the message
    message_display("incorrect", 550, 400)
    # makes the buttons stay but disabling them
    button("Brazil, India, and The United States",
           150, 300, 250, 100, gray, gray, "None", 25)
    button("     Britain, The Soviet Union, and The United States",
           500, 300, 250, 100, gray, gray, "None", 25)
    button("Germany, Japan, and Italy", 150,
           450, 250, 100, gray, gray, "None", 25)
    button("     Canada, France, and Australia", 500,
           450, 250, 100, gray, gray, "None", 25)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz3()


def correct3():
    # adds 1 point
    global correctamt
    correctamt += 1
    # display the message
    message_display("correct", 550, 400)
    # makes the buttons stay but disabling them
    button("Charles de Gaulle, William Lyon Mackenzie King",
           150, 300, 250, 100, gray, gray, "None", 20)

    # manually display text because the created function displays text that is too large
    # and the button is too small to fit all the text
    font = pygame.font.SysFont("Cuckoo", 20)
    text = font.render("and Benito Mussolini", True, white)
    gameDisplay.blit(text, (155, 360))
    button("    Franklin Roosevelt, Winston Churchill, and Joseph Stalin",
           500, 300, 250, 100, gray, gray, "None", 20)
    button("Napoleon Bonaparte and Joseph Stalin",
           150, 450, 250, 100, gray, gray, "None", 20)
    button("    Adolf Hitler, Benito Mussolini, and Michinomiya Hirohito",
           500, 450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz4()


def incorrect3():
    # display the message
    message_display("incorrect", 550, 400)
    # makes the buttons stay but disabling them
    button("Charles de Gaulle, William Lyon Mackenzie King",
           150, 300, 250, 100, gray, gray, "None", 20)
    # manually display text because the created function displays text that is too large
    # and the button is too small to fit all the text
    font = pygame.font.SysFont("Cuckoo", 20)
    text = font.render("and Benito Mussolini", True, white)
    gameDisplay.blit(text, (155, 360))
    button("    Franklin Roosevelt, Winston Churchill, and Joseph Stalin",
           500, 300, 250, 100, gray, gray, "None", 20)
    button("Napoleon Bonaparte and Joseph Stalin",
           150, 450, 250, 100, gray, gray, "None", 20)
    button("    Adolf Hitler, Benito Mussolini, and Michinomiya Hirohito",
           500, 450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz4()


def correct4():
    # adds 1 point
    global correctamt
    correctamt += 1
    # display the message
    message_display("correct", 550, 400)
    # makes the buttons stay but disabling them
    button("Third Battle of Kharkov", 150, 300,
           250, 100, gray, gray, "None", 20)
    button("    Battle of Kursk", 500, 300, 250, 100, gray, gray, "None", 20)
    button("Battle of Stalingrad", 150, 450, 250, 100, gray, gray, "None", 20)
    button("    Battle of the Atlantic", 500,
           450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz5()


def incorrect4():
    # display the message
    message_display("incorrect", 550, 400)
    # makes the buttons stay but disabling them
    button("Third Battle of Kharkov", 150, 300,
           250, 100, gray, gray, "None", 20)
    button("    Battle of Kursk", 500, 300, 250, 100, gray, gray, "None", 20)
    button("Battle of Stalingrad", 150, 450, 250, 100, gray, gray, "None", 20)
    button("    Battle of the Atlantic", 500,
           450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # go to the next question
    quiz5()


def correct5():
    # adds 1 point
    global correctamt
    correctamt += 1
    # display the message
    message_display("correct", 550, 400)
    # makes the buttons stay but disabling them
    button("Third Battle of Kharkov", 150, 300,
           250, 100, gray, gray, "None", 20)
    button("    Battle of Kursk", 500, 300, 250, 100, gray, gray, "None", 20)
    button("Battle of Stalingrad", 150, 450, 250, 100, gray, gray, "None", 20)
    button("    Battle of the Atlantic", 500,
           450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # end the quiz
    main_menu()


def incorrect5():
    # display the message
    message_display("incorrect", 550, 400)
    # makes the buttons stay but disabling them
    button("Third Battle of Kharkov", 150, 300,
           250, 100, gray, gray, "None", 20)
    button("    Battle of Kursk", 500, 300, 250, 100, gray, gray, "None", 20)
    button("Battle of Stalingrad", 150, 450, 250, 100, gray, gray, "None", 20)
    button("    Battle of the Atlantic", 500,
           450, 250, 100, gray, gray, "None", 20)
    # update screen
    pygame.display.update()
    # wait for 1 second
    pygame.time.delay(1000)
    # end the quiz
    main_menu()


# main menu
def main_menu():
    # checks if the window is closed
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # display backgound
        gameDisplay.blit(background, (0, 0))
        # display buttons
        button("Game", 50, 125, 250, 100, gray, light_gray, "game_menu", 32)
        button("Lessons", 50, 250, 250, 100, gray, light_gray, "lessons", 32)
        button("Quiz", 50, 375, 250, 100, gray, light_gray, "quiz", 32)
        button("Results", 50, 500, 250, 100, gray, light_gray, "results", 32)
        button("Exit", 50, 625, 250, 100, gray, light_gray, "exit", 32)
        # update screen
        pygame.display.flip()


# Menu for game
def game_menu():
    # checks if the window is closed
    _game_menu = True
    while _game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # renders background
        gameDisplay.blit(background, (0, 0))
        # displays text
        message_display("Game", 50, 150)
        message_display("Left - Right arrow keys to move", 50, 200)
        message_display("Dodge the missiles", 50, 250)
        # displays buttons
        button("Start", 500, 650, 250, 100, gray, light_gray, "start_game", 40)
        button("Back", 800, 650, 250, 100, gray, light_gray, "main_menu", 40)
        # update screen
        pygame.display.flip()


# create a message when the user gets hit
def hit():
    # display the message
    message_display("You Got Hit", 550, 400)
    # update screen
    pygame.display.flip()
    # pause for 2 seconds
    pygame.time.delay(2000)

# make a counter for missles dodged


def missilesDodged(count):
    # create the font
    font = pygame.font.SysFont(None, 25)
    # generate text
    text = font.render(f"Score: {count}", True, (0, 0, 0))
    # add the text to the screen
    gameDisplay.blit(text, (0, 0))


# lambda function to dispaly missiles
def missiles(x, y): return gameDisplay.blit(missileImg, (x, y))
# lambda function to draw a ship
def ship(x, y): return gameDisplay.blit(shipImg, (x, y))


def game():
    # local variables
    display_width = 1100
    display_height = 800
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    xVelocity = 0
    ship_width = shipImg.get_width()
    obstacleStartX = random.randrange(0, display_width)
    obstacleStartY = -600
    obstacleSpeed = 10
    obstacleWidth = missileImg.get_width()
    obstacleHeight = missileImg.get_height()
    dodged = 0
    # checks if the window is is closed
    gameExit = False
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # detect keypress
            if event.type == pygame.KEYDOWN:
                # if the left arrow key is pressed move left
                if event.key == pygame.K_LEFT:
                    xVelocity = -5

                # if the right arrow key is pressed move right
                elif event.key == pygame.K_RIGHT:
                    xVelocity = 5

            # detect a released keypress
            if event.type == pygame.KEYUP:
                # if the left or right arrow key is released stop moving
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xVelocity = 0

        # update the ships position
        x += xVelocity
        # update background
        gameDisplay.blit(game_background, (0, 0))
        # launch missile
        missiles(obstacleStartX, obstacleStartY)
        # move the missile
        obstacleStartY += obstacleSpeed
        # display the ship
        ship(x, y)
        # shows the amount of missiles dodges
        missilesDodged(dodged)
        # if the ship moves out of the screen
        if x > display_width - shipImg.get_width() or x < 0:
            # call the hit() function
            hit()
            # reset the ships position
            x = (display_width * 0.45)
            y = (display_height * 0.8)
            ship(x, y)
            # set the dodged amount to 0
            dodged = 0

        # if the ship isnt hit and the missile moves out
        if obstacleStartY > display_height:
            obstacleStartY = 0 - obstacleHeight
            obstacleStartX = random.randrange(0, display_width)
            # add 1 to the dodged amount
            dodged += 1

        # if the ship is hit
        if y < obstacleStartY+obstacleHeight:
            if (x > obstacleStartX and x < obstacleStartX + obstacleWidth) or (x + ship_width > obstacleStartX and x + ship_width < obstacleStartX + obstacleWidth):
                # call the hit() function
                hit()
                # reset the ships position
                x = (display_width * 0.45)
                y = (display_height * 0.8)
                ship(x, y)
                # set dodged to 0
                dodged = 0

        # back button
        button("Back", 900, 700, 100, 50, gray, light_gray, "main_menu", 40)
        # update screen
        pygame.display.update()


# lesson
def lesson():
    # checks if the window is closed
    lesson = True
    while lesson:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # render background
        gameDisplay.blit(background, (0, 0))
        # display message
        message_display("Lessons", 50, 150)
        # displays buttons
        button("Start", 500, 650, 250, 100, gray, light_gray, "lesson1", 40)
        button("Back", 800, 650, 250, 100, gray, light_gray, "main_menu", 40)
        # update screen
        pygame.display.flip()

# first page of the lessons


def lesson1():
    # checks if the window is closed
    lesson1 = True
    while lesson1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display message    s
            message_display("Page 1", 50, 150)
            message_display("The main Allied powers were:", 50, 250)
            message_display(
                "Britain, The Soviet Union, and The United States", 50, 300)
            # displays buttons
            button("Next", 500, 650, 250, 100, gray, light_gray, "lesson2", 40)
            button("Back", 800, 650, 250, 100, gray, light_gray, "lessons", 40)
            # update screen
            pygame.display.update()

# second page of the lessons


def lesson2():
    # checks if the window is closed
    lesson2 = True
    while lesson2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Page 2", 50, 150)
            message_display("The main Axis powers were:", 50, 250)
            message_display("Germany, Japan, and Italy", 50, 300)
            # displays buttons
            button("Next", 500, 650, 250, 100, gray, light_gray, "lesson3", 40)
            button("Back", 800, 650, 250, 100, gray, light_gray, "lesson1", 40)
            pygame.display.update()

# third page of the lessons


def lesson3():
    # checks if the window is closed
    lesson3 = True
    while lesson3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Page 3", 50, 150)
            message_display("The main Allied leaders were:", 50, 250)
            message_display("Franklin Roosevelt of The United States", 50, 300)
            message_display("Winston Churchill of Britain", 50, 350)
            message_display("Joseph Stalin of The Soviet Union", 50, 400)
            # displays buttons
            button("Next", 500, 650, 250, 100, gray, light_gray, "lesson4", 40)
            button("Back", 800, 650, 250, 100, gray, light_gray, "lesson2", 40)
            # update screen
            pygame.display.update()

# fourth page of the lessons


def lesson4():
    # checks if the window is closed
    lesson4 = True
    while lesson4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Page 4", 50, 150)
            message_display("The main Axis leaders were:", 50, 250)
            message_display("Adolf Hitler from Germany", 50, 300)
            message_display("Benito Mussolini of Italy", 50, 350)
            message_display("Michinomiya Hirohito of Japan", 50, 400)
            # displays buttons
            button("Next", 500, 650, 250, 100, gray, light_gray, "lesson5", 40)
            button("Back", 800, 650, 250, 100, gray, light_gray, "lesson3", 40)
            # update screen
            pygame.display.update()

# fifth page of the lessons


def lesson5():
    # checks if the window is closed
    lesson5 = True
    while lesson5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Page 5", 50, 150)
            message_display(
                "The longest battle of WWII was the Battle of the Atlantic", 50, 250)
            message_display("which lasted from 1939-1945", 50, 300)
            # displays buttons
            button("Main Menu", 500, 650, 250, 100,
                   gray, light_gray, "main_menu", 40)
            button("Back", 800, 650, 250, 100, gray, light_gray, "lesson4", 40)
            # update screen
            pygame.display.update()


# quiz
def quiz():
    # checks if the window is closed
    quiz = True
    while quiz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # reset correctamt
            global correctamt
            correctamt = 0
            # render background
            gameDisplay.blit(background, (0, 0))
            # display message
            message_display("Quiz", 50, 150)
            # displays buttons
            button("Start", 500, 650, 250, 100, gray, light_gray, "quiz1", 40)
            button("Back", 800, 650, 250, 100, gray,
                   light_gray, "main_menu", 40)
            # update screen
            pygame.display.update()

# first question of the quiz


def quiz1():

    # checks if the window is closed
    quiz1 = True
    while quiz1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Question 1", 50, 150)
            message_display("The main Allied powers were?", 50, 250)
            # displays buttons
            button("Britain, The Soviet Union, and The United States",
                   150, 300, 250, 100, gray, light_gray, "correct1", 25)
            button("     France, Canada, and Italy", 500, 300,
                   250, 100, gray, light_gray, "incorrect1", 25)
            button("Brazil, India, and The United States", 150, 450,
                   250, 100, gray, light_gray, "incorrect1", 25)
            button("     Germany, Japan, and Australia", 500, 450,
                   250, 100, gray, light_gray, "incorrect1", 25)
            # update screen
            pygame.display.update()

# second question of the quiz


def quiz2():
    # checks if the window is closed
    quiz2 = True
    while quiz2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Question 2", 50, 150)
            message_display("The main Axis powers were?", 50, 250)
            # displays buttons
            button("Brazil, India, and The United States", 150, 300,
                   250, 100, gray, light_gray, "incorrect2", 25)
            button("     Britain, The Soviet Union, and The United States",
                   500, 300, 250, 100, gray, light_gray, "incorrect2", 25)
            button("Germany, Japan, and Italy", 150, 450,
                   250, 100, gray, light_gray, "correct2", 25)
            button("     Canada, France, and Australia", 500, 450,
                   250, 100, gray, light_gray, "incorrect2", 25)
            # update screen
            pygame.display.update()

# third question of the quiz


def quiz3():
    # allow message to display

    # checks if the window is closed
    quiz3 = True
    while quiz3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Question 3", 50, 150)
            message_display("The main Allied Leaders were?", 50, 250)
            button("Charles de Gaulle, William Lyon Mackenzie King",
                   150, 300, 250, 100, gray, light_gray, "incorrect3", 20)

            # manually display text because the created function displays text that is too large
            # and the button is too small to fit all the text
            font = pygame.font.SysFont("Cuckoo", 20)
            text = font.render("and Benito Mussolini", True, white)
            gameDisplay.blit(text, (155, 360))

            # displays buttons
            button("    Franklin Roosevelt, Winston Churchill, and Joseph Stalin",
                   500, 300, 250, 100, gray, light_gray, "correct3", 20)
            button("Napoleon Bonaparte and Joseph Stalin", 150, 450,
                   250, 100, gray, light_gray, "incorrect3", 20)
            button("    Adolf Hitler, Benito Mussolini, and Michinomiya Hirohito",
                   500, 450, 250, 100, gray, light_gray, "incorrect3", 20)
            # update screen
            pygame.display.update()

# fourth question of the quiz


def quiz4():
    # allow message to display

    # checks if the window is closed
    quiz4 = True
    while quiz4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Question 4", 50, 150)
            message_display("The main Axis Leaders were?", 50, 250)
            button("Adolf Hitler, Benito Mussolini ", 150, 300,
                   250, 100, gray, light_gray, "correct4", 20)
            # manually display text because the created function displays text that is too large
            # and the button is too small to fit all the text
            font = pygame.font.SysFont("Cuckoo", 20)
            text = font.render("and Michinomiya Hirohito", True, white)
            gameDisplay.blit(text, (180, 360))
            # displays buttons
            button("    Franklin Roosevelt, Winston Churchill, and Joseph Stalin",
                   500, 300, 250, 100, gray, light_gray, "incorrect4", 25)
            button("Adolf Hitler and Joseph Stalin", 150, 450,
                   250, 100, gray, light_gray, "incorrect4", 25)
            button("    Winston Churchill, Michinomiya Hirohito, and Franklin Roosevelt",
                   500, 450, 250, 100, gray, light_gray, "incorrect4", 25)
            # update screen
            pygame.display.update()

# fifth question of the quiz


def quiz5():
    # allow message to display

    # checks if the window is closed
    quiz5 = True
    while quiz5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Question 5", 50, 150)
            message_display("What was the longest battle during WW2", 50, 250)
            # displays buttons
            button("Third Battle of Kharkov", 150, 300, 250,
                   100, gray, light_gray, "incorrect5", 20)
            button("    Battle of Kursk", 500, 300, 250,
                   100, gray, light_gray, "incorrect5", 20)
            button("Battle of Stalingrad", 150, 450, 250,
                   100, gray, light_gray, "incorrect5", 20)
            button("    Battle of the Atlantic", 500, 450,
                   250, 100, gray, light_gray, "correct5", 20)
            # update screen
            pygame.display.update()

# results


def results():
    # checks if the window is closed
    result = True
    while result:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("Results", 100, 275)
            message_display(
                f"you got {correctamt}/5 ({int((correctamt/5)*100)}%)", 100, 375)
            # displays button
            button("Back", 800, 650, 250, 100, gray,
                   light_gray, "main_menu", 40)
            # update screen
            pygame.display.update()

# exit


def _exit():
    # checks if the window is closed
    exit_ = True
    while exit_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # render background
            gameDisplay.blit(background, (0, 0))
            # display messages
            message_display("credits", 100, 75)
            message_display(
                "ship background: https://wallpaperaccess.com/battleship", 100, 175)
            message_display("water background in game: drawn by me", 100, 275)
            message_display("ship image: drawn by me", 100, 375)
            message_display("missile image: drawn by me", 100, 475)
            # update screen
            pygame.display.update()
            # pause for 10 seconds (10000 milliseconds)
            pygame.time.delay(10000)
            # exits
            exit()


# main function
def Main():
    # checks if the window is closed
    gameExit = False
    while gameExit == False:
        titleScreen()


Main()
