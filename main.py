import sys, pygame, char, intros

pygame.init()
clock = pygame.time.Clock() #keeps fps steady
moveCur = 0
moveMax = 2 #amount of frames between movement steps, pretty much the speed
#animation indices
walkAnimationIndex = 0
walkAnimationIndexMax = 80

c = pygame.display.set_mode((800, 600))
charPos = [0, 0] #x, y

#controls
interact = pygame.K_x

#begin to define stuff needed for the game
def bottomMessage(text):
	mono = pygame.font.SysFont("monospace", 32)
	downArrow = mono.render("↓ [Press X]", 1, (0, 0, 0)) #↓
	pokeFont = pygame.font.Font("fonts/PokemonGB.ttf", 64)#http://www.fontspace.com/jackster-productions/pokemon-gb
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
	while next == False:
				for event in pygame.event.get():
					if event.type == pygame.QUIT: sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == interact:
							next = True


def intro():
	bottomMessage(intros.introString[0])

#game loop
inGame = True #states of the game
inIntro = False
showChar = True
canMove = True

#stuff for animations
walking = False
up = False
down = False
left = False
right = False
male = True

if male == True:
	charUp = char.maleCharUp
	charDown = char.maleCharDown
	charLeft = char.maleCharLeft
	charRight = char.maleCharRight
else: 
	charUp = char.femaleCharUp
	charDown = char.femaleCharDown
	charLeft = char.femaleCharLeft
	charRight = char.femaleCharRight

while inGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: inGame = False #sys.exit() exit game
		if event.type == pygame.KEYUP: walking = False #to check when to use idle animation

	clock.tick(240)
	c.fill((0, 0, 0)) #clears screen after every frame
	if canMove:
		moveCur -= 1
		keys = pygame.key.get_pressed() #thanks to http://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

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
			if down:
				c.blit(charDown[0], char.charRect)
			if left:
				c.blit(charLeft[0], char.charRect)
			if right:
				c.blit(charRight[0], char.charRect)

		if walkAnimationIndex >= walkAnimationIndexMax:
			walkAnimationIndex = 0

	if inIntro:
		canMove = False
		showChar = False
		intro()
		inIntro = False

	pygame.display.flip()


#save game here, so it saves if you exit it normally in the game