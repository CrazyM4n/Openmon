import sys, pygame

maleCharUp = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup3.png"))]
maleCharDown = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown3.png"))]
maleCharLeft = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft1.png")),pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft3.png"))]
maleCharRight = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright3.png"))]
femaleCharUp = [pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkup1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkup2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkup3.png"))]
femaleCharDown = [pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkdown1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkdown2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkdown3.png"))]
femaleCharLeft = [pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkleft1.png")),pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkleft2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkleft3.png"))]
femaleCharRight = [pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkright1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkright2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/f/walkright3.png"))]

charRect = maleCharDown[0].get_rect()

def move(direction, amnt):
	
	if direction == "up":
		charRect.y += -1
		return -1
	elif direction == "down":
		charRect.y += 1
		return 1
	elif direction == "left":
		charRect.x += -1
		return -1
	elif direction == "right":
		charRect.x += 1
		return 1