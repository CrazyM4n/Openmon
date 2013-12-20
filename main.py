import sys, pygame, char

pygame.init()
clock = pygame.time.Clock() #keeps fps steady
mono = pygame.font.SysFont("monospace", 32)
moveCur = 0
moveMax = 2 #amount of frames between movement steps, pretty much the speed
#animation indices
walkAnimationIndex = 0
walkAnimationIndexMax = 80

c = pygame.display.set_mode((800, 600))
charPos = [0, 0] #x, y

#begin to define stuff needed for the game
def bottomMessage(text):
	box = pygame.image.load("img/box.png")
	boxRect = box.get_rect()
	boxRect.y = 400
	c.blit(box, boxRect)
	xIndex = 0
	yIndex = 0
	downArrow = mono.render("↓", 1, (0, 0, 0))
	for byte in text:
		pygame.time.delay(20)
		screenLetter = mono.render(byte, 1, (0, 0, 0))
		c.blit(screenLetter, ((xIndex*20)+20, (yIndex*40)+440))
		pygame.display.flip()
		xIndex += 1
		if xIndex >= 38: #amount of characters in a line
			xIndex = 0
			yIndex += 1
		if yIndex >= 3:
			yIndex = 0
			c.blit(downArrow, (740, 550))

	pygame.time.delay(100000)

def intro():
	bottomMessage("Hello, I'm your new professor, Cutman. Today we will learn about why you shouldn't take too many showers. sfksgrjhgredjhgjhfgkjxdrgfgkgsfz")


#game loop
inGame = True #states of the game
inIntro = True
showChar = True
canMove = True

#stuff for animations
walking = False
up = False
down = False
left = False
right = False
male = True
female = False

while inGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: inGame = False #sys.exit() exit game
		if event.type == pygame.KEYUP: walking = False

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
					c.blit(char.maleCharUp[1], char.charRect)
				else:
					c.blit(char.maleCharUp[2], char.charRect)
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
					c.blit(char.maleCharDown[1], char.charRect)
				else:
					c.blit(char.maleCharDown[2], char.charRect)
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
					c.blit(char.maleCharLeft[1], char.charRect)
				else:
					c.blit(char.maleCharLeft[2], char.charRect)
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
					c.blit(char.maleCharRight[1], char.charRect)
				else:
					c.blit(char.maleCharRight[2], char.charRect)
				walkAnimationIndex += 1

		if walking == False and showChar == True:
			if up:
				c.blit(char.maleCharUp[0], char.charRect)
			if down:
				c.blit(char.maleCharDown[0], char.charRect)

		if walkAnimationIndex >= walkAnimationIndexMax:
			walkAnimationIndex = 0

	if inIntro:
		canMove = False
		showChar = False
		intro()
		inIntro = False

	pygame.display.flip()
