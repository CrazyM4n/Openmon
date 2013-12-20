import sys, pygame

maleCharUp = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkup3.png"))]
maleCharDown = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkdown3.png"))]
maleCharLeft = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft1.png")),pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkleft3.png"))]
maleCharRight = [pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright1.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright2.png")), pygame.transform.scale2x(pygame.image.load("img/char/walk/m/walkright3.png"))]
charRect = maleCharDown[0].get_rect()

def move(direction, amnt):
	x = charRect.x
	y = charRect.y

	if direction == "up":
		return -1
	elif direction == "down":
		return 1
	elif direction == "left":
		return -1
	elif direction == "right":
		return 1