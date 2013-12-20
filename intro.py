import pygame

c = None

def intro(screen):
	c = screen

def bottomMessage(text):
	box = pygame.image.load("img/box.png")
	boxRect = box.get_rect()
	boxRect.y = 400
	c.blit(box, boxRect)
	index = 0
	for byte in text:
		pygame.time.wait(100)
		screenLetter = mono.render(byte, 1, (0, 0, 0))
		c.blit(screenLetter, ((index*10)+20, 450))
		pygame.display.flip()

def go():
	bottomMessage("Hello! I'm Cutman")