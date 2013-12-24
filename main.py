import sys, pygame, char, intros, parse_key_codes, maps

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
clock = pygame.time.Clock() #keeps fps steady
moveCur = 0
moveMax = 1 #amount of frames between movement steps, pretty much the speed
#animation indices
walkAnimationIndex = 0
walkAnimationIndexMax = 80

c = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#character stuff
charPos = [0, 0] #x, y
currentMap = "spawn"

#fonts
pokeFont = pygame.font.Font("fonts/PokemonGB.ttf", 64)#http://www.fontspace.com/jackster-productions/pokemon-gb
pokeFontU = pygame.font.Font("fonts/PokemonGBU.ttf", 64)
pokeFontU.set_underline(True)
mono = pygame.font.SysFont("monospace", 32)

#controls
interact = pygame.K_x

#player constants
name = ""
male = True

#begin to define stuff needed for the game
def boyOrGirl():
    if male == True: return "boy"
    if male == False: return "girl"

def bottomMessage(text):
    downArrow = mono.render("↓ [Press X]", 1, (0, 0, 0)) #↓
    box = pygame.image.load("img/box.png")
    boxRect = box.get_rect()
    boxRect.y = 400
    c.blit(box, boxRect)
    xIndex = 0
    yIndex = 0
    for byte in text:
        pygame.time.delay(20)
        screenLetter = pokeFont.render(byte, 1, (0, 0, 0))
        c.blit(screenLetter, ((xIndex*30)+20, (yIndex*50)+430)) #with old font: c.blit(screenLetter, ((xIndex*20)+20, (yIndex*40)+420))
        pygame.display.flip()
        xIndex += 1
        if xIndex >= 25: #amount of characters in a line old = 38
            xIndex = 0
            yIndex += 1
        if yIndex >= 2:
            yIndex = 0
            next = False
            c.blit(downArrow, (550, 550))
            pygame.display.flip()
            while next == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == interact:
                            c.blit(box, boxRect)
                            next = True
    next = False 
    c.blit(downArrow, (550, 550))
    pygame.display.flip()
    while next == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == interact:
                            next = True

def bottomMessageNoScroll(text):
    box = pygame.image.load("img/box.png")
    boxRect = box.get_rect()
    boxRect.y = 400
    c.blit(box, boxRect)
    textToRender = pokeFont.render(text, 1, (0, 0, 0))
    c.blit(textToRender, (20, 430))
    pygame.display.flip()

def intro():
    #say some stuff
    bottomMessage(intros.introString[0])

    def askForName():
        bottomMessage(intros.introString[1])
        bottomMessageNoScroll("_")
        global name
        enter = False #is true when the person presses enter/continues with x
        while enter == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        enter = True

                    elif event.key == pygame.K_BACKSPACE:
                        try:
                            name = name[:len(name)-1]
                            bottomMessageNoScroll(name+"_")
                        except: 
                            name = ""
                            bottomMessageNoScroll(name+"_")

                    else:
                        if event.key in parse_key_codes.aToZ:
                            name = name + parse_key_codes.parse(event.key) + ""
                            bottomMessageNoScroll(name+"_")

        #lets get back to the intro...
        c.fill((0, 0, 0))
        bottomMessage(intros.introString[2]+name+intros.introString[3]+"")

        #ask if name is correct
        yesSelected = True #which option is selected
        enter = False #when they press x
        box = pygame.image.load("img/box.png") #making a box above the other box
        boxRect = box.get_rect()
        boxRect.y = 200
        #making the options
        yesUnderlined = pokeFontU.render("Yes", 1, (0, 0, 0))
        no = pokeFont.render("No", 1, (0, 0, 0))
        yes = pokeFont.render("Yes", 1, (0, 0, 0))
        noUnderlined = pokeFontU.render("No", 1, (0, 0, 0))
        noRect = no.get_rect()
        noRect.x = 600
        noRect.y = 250
        yesRect = yes.get_rect()
        yesRect.x = 200
        yesRect.y = 250
        while enter == False:
            if yesSelected:
                c.blit(box, boxRect)
                c.blit(yesUnderlined, yesRect)
                c.blit(no, noRect)
                pygame.display.flip()
            elif yesSelected == False:
                c.blit(box, boxRect)
                c.blit(yes, yesRect)
                c.blit(noUnderlined, noRect)
                pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            c.fill((0, 0, 0))
                            if yesSelected:
                                enter = True
                            elif yesSelected == False:
                                enter = True
                                askForName()

                        elif event.key == pygame.K_LEFT or pygame.K_RIGHT:
                            yesSelected = not yesSelected

    askForName()

    def askForGender():
        #literally copied and pasted askForName()
        c.fill((0, 0, 0))
        bottomMessage(intros.introString[4])
        boySelected = True #which option is selected
        enter = False #when they press x
        box = pygame.image.load("img/box.png") #making a box above the other box
        boxRect = box.get_rect()
        boxRect.y = 200
        #making the options
        boyUnderlined = pokeFontU.render("Boy", 1, (0, 0, 0))
        girl = pokeFont.render("Girl", 1, (0, 0, 0))
        boy = pokeFont.render("Boy", 1, (0, 0, 0))
        girlUnderlined = pokeFontU.render("Girl", 1, (0, 0, 0))
        girlRect = girl.get_rect()
        girlRect.x = 600
        girlRect.y = 250
        boyRect = boy.get_rect()
        boyRect.x = 200
        boyRect.y = 250
        while enter == False:
            if boySelected:
                c.blit(box, boxRect)
                c.blit(boyUnderlined, boyRect)
                c.blit(girl, girlRect)
                pygame.display.flip()
            elif boySelected == False:
                c.blit(box, boxRect)
                c.blit(boy, boyRect)
                c.blit(girlUnderlined, girlRect)
                pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            if boySelected: enter = True; c.fill((0, 0, 0)); return True; print("male");
                            elif boySelected == False: enter = True; c.fill((0, 0, 0)); return False; print("female"); 

                        elif event.key == pygame.K_LEFT or pygame.K_RIGHT:
                            boySelected = not boySelected

    global male
    male = askForGender()
    print("up "+boyOrGirl())

    #finally done asking stuff ;_;
    bottomMessage(intros.introString[5]+boyOrGirl()+intros.introString[6]+name+intros.introString[7]+"") #hold on i'll be back
    bottomMessage(intros.introString[8])

def parseMap(mapIndex):

    for x in range(len(maps.mapData[mapIndex])):
        for y in range(len(maps.mapData[mapIndex][x])):    
            floor, tile = maps.mapData[mapIndex][x][y]

            #draw floor
            if floor == "": 
                floorRect = pygame.Rect(0, 0, 32, 32)
                floorRect.x = x*32
                floorRect.y = y*32
                c.fill((0, 0, 0), floorRect)
            else:
                floorRect = maps.floors[floor].get_rect()
                floorRect.x = x*32
                floorRect.y = y*32
                c.blit(maps.floors[floor], floorRect)

            #draw tiles
            if tile == "": 
                pass
            else:
                tileRect = maps.tiles[tile].get_rect()
                tileRect.x = x*32
                tileRect.y = y*32
                c.blit(maps.tiles[tile], tileRect)

def moveChar():
    if canMove:
        global moveCur, walking, up, down, left, right, walkAnimationIndex
        moveCur -= 1
        keys = pygame.key.get_pressed() #thanks to http://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

        print("checking "+str(charPos[0])+" in 0 to "+str(WINDOW_WIDTH)+" and "+str(charPos[1])+" in 0 to "+str(WINDOW_HEIGHT))

        if charPos[1] >= WINDOW_HEIGHT - char.charRect.height: #check wall boundaries, will work on this later. itll be cool trust me pls you will be able to transition maps TODO
            charPos[1] -= 1
        elif charPos[1] <= 0:
            charPos[1] += 1

        if charPos[0] >= WINDOW_WIDTH - char.charRect.width:
            charPos[0] -= 1
        elif charPos[0] <= 0:
            charPos[0] += 1

        if keys[pygame.K_UP]:
            if moveCur <= 0:
                moveCur = moveMax
                charPos[1] += char.move("up", 1)
            if showChar:
                walking = True
                up = True
                down = False
                left = False
                right = False
                char.charRect.x = charPos[0]
                char.charRect.y = charPos[1]
                if walkAnimationIndex >= walkAnimationIndexMax/2: #animates the walking animation
                    c.blit(charUp[1], char.charRect)
                else:
                    c.blit(charUp[2], char.charRect)
                walkAnimationIndex += 1

        elif keys[pygame.K_DOWN]:
            if moveCur <= 0:
                moveCur = moveMax
                charPos[1] += char.move("down", 1)
            if showChar:
                walking = True
                up = False
                down = True
                left = False
                right = False
                char.charRect.x = charPos[0]
                char.charRect.y = charPos[1]
                if walkAnimationIndex >= walkAnimationIndexMax/2:
                    c.blit(charDown[1], char.charRect)
                else:
                    c.blit(charDown[2], char.charRect)
                walkAnimationIndex += 1

        elif keys[pygame.K_LEFT]:
            if moveCur <= 0:
                moveCur = moveMax
                charPos[0] += char.move("left", 1)
            if showChar:
                walking = True
                up = False
                down = False
                left = True
                right = False
                char.charRect.x = charPos[0]
                char.charRect.y = charPos[1]
                if walkAnimationIndex >= walkAnimationIndexMax/2:
                    c.blit(charLeft[1], char.charRect)
                else:
                    c.blit(charLeft[2], char.charRect)
                walkAnimationIndex += 1

        elif keys[pygame.K_RIGHT]:
            if moveCur <= 0:
                moveCur = moveMax
                charPos[0] += char.move("right", 1)
            if showChar:
                walking = True
                up = False
                down = False
                left = False
                right = True
                char.charRect.x = charPos[0]
                char.charRect.y = charPos[1]
                if walkAnimationIndex >= walkAnimationIndexMax/2:
                    c.blit(charRight[1], char.charRect)
                else:
                    c.blit(charRight[2], char.charRect)
                walkAnimationIndex += 1

        if walking == False and showChar == True:
            if up:
                c.blit(charUp[0], char.charRect)
            elif down:
                c.blit(charDown[0], char.charRect)
            elif left:
                c.blit(charLeft[0], char.charRect)
            elif right:
                c.blit(charRight[0], char.charRect)

        if walkAnimationIndex >= walkAnimationIndexMax:
            walkAnimationIndex = 0


                
#game loop, states of the game
inIntro = False #important for debugging

inGame = True
showChar = True
canMove = True
drawMap = True

#stuff for animations
walking = False
up = False
down = False
left = False
right = False

#other random stuff
justSpawned = True

while inGame:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: inGame = False #sys.exit() exit game
        if event.type == pygame.KEYUP: walking = False #to check when to use idle animation

    if inIntro:
        canMove = False
        showChar = False
        drawMap = False
        intro()
        inIntro = False
        canMove = True
        showChar = True
        drawMap = True
        justSpawned = True

    if drawMap:
        c.fill((0, 0, 0)) #clears screen after every frame

        #change the spawning point for all maps that need it
        if justSpawned and currentMap == "spawn":
            charPos = [400, 400]
            if male == True: #set the genders
                charUp = char.maleCharUp
                charDown = char.maleCharDown
                charLeft = char.maleCharLeft
                charRight = char.maleCharRight
            if male == False: 
                charUp = char.femaleCharUp
                charDown = char.femaleCharDown
                charLeft = char.femaleCharLeft
                charRight = char.femaleCharRight
            justSpawned = False

        parseMap(maps.mapIndex[currentMap])
        moveChar()

    pygame.display.flip()


#save game here, so it saves if you exit it normally in the game