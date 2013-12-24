#tiles:
#0: grass
#1: tall grass

#1000-1999:indoor tiles
#1000: hardwood floor

#
import pygame
grass = pygame.transform.scale2x(pygame.image.load("img/maps/grass.png"))
tallGrass = pygame.transform.scale2x(pygame.image.load("img/maps/tallgrass.png"))

mapIndex = dict() #all the maps 
mapIndex["spawn"] = 0

floors = dict() #dictionary with all the useable floors
floors["grass"] = grass

tiles = dict()
tiles["tallGrass"] = tallGrass

mapAmount = len(mapIndex)
mapData = [[[("", "") for y in range(19)] for x in range(25)] for m in range(mapAmount)] #what map, x, y

#start to define the maps
#spawn room (choose starter openmon):
for x in range(len(mapData[mapIndex["spawn"]])): #make it all floor in the spawn room rectangle an actual floor
	for y in range(len(mapData[mapIndex["spawn"]][x])):
		if y in range(5, 11) and x in range(5, 11):
			mapData[mapIndex["spawn"]][x][y] = ("grass", "")

mapData[mapIndex["spawn"]][5][5] = ("grass", "tallGrass") #floor material, tile material
