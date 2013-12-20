import sys, pygame, char, intros, parse_key_codes

pygame.init()
clock = pygame.time.Clock() #keeps fps steady
moveCur = 0
moveMax = 2 #amount of frames between movement steps, pretty much the speed
#animation indices
walkAnimationIndex = 0
walkAnimationIndexMax = 80

c = pygame.display.set_mode((800, 600))
charPos = [0, 0] #x, y

#fonts
pokeFont = pygame.font.Font("fonts/PokemonGB.ttf", 64)#http://www.fontspace.com/jackster-productions/pokemon-gb
pokeFontU = pygame.font.Font("fonts/PokemonGBU.ttf", 64)
pokeFontU.set_underline(True)
mono = pygame.font.SysFont("monospace", 32)

#controls
interact = pygame.K_x

#player constants
name = ""
male = False

#begin to define stuff needed for the game
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
							if yesSelected: enter = True; c.fill((0, 0, 0))
							elif yesSelected == False: askForName(); c.fill((0, 0, 0))

						elif event.key == pygame.K_LEFT or pygame.K_RIGHT:
							yesSelected = not yesSelected

	askForName()
				
#game loop, states of the game
inGame = True
inIntro = True
showChar = True
canMove = True

#stuff for animations
walking = False
up = False
down = False
left = False
right = False

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
			elif down:
				c.blit(charDown[0], char.charRect)
			elif left:
				c.blit(charLeft[0], char.charRect)
			elif right:
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