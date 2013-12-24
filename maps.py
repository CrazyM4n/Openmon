import pygame

mapIndex = dict() #all the maps 
mapIndex["spawn"] = 0

floors = dict() #dictionary with all the useable floors
floors["grass"] = pygame.transform.scale2x(pygame.image.load("img/maps/grass.png"))
floors["openMonCenterFloor"] = pygame.transform.scale2x(pygame.image.load("img/maps/whiteHardwoodFloor.png")) #credit to http://www.vg-resource.com/showthread.php?tid=8889

tiles = dict()
tiles["tallGrass"] = pygame.transform.scale2x(pygame.image.load("img/maps/tallgrass.png"))

mapAmount = len(mapIndex)
mapData = [[[("", "") for y in range(19)] for x in range(25)] for m in range(mapAmount)] #what map, x, y
mapCollisions = [[[0 for y in range(19)] for x in range(25)] for m in range(mapAmount)] #same as above, but 0 = nocollide, 1 = collide

#events
#* = not done yet
#*sign(text)
#*trainerBattle(uh, something will go here)
#*more stuff :D
mapEvents = [[[None for y in range(19)] for x in range(25)] for m in range(mapAmount)] #same, but gonna contain functions for when you collide with it

#start to define the maps
#floor material, tile material

#spawn room (choose starter openmon):
for x in range(len(mapData[mapIndex["spawn"]])): #make it all floor in the spawn room rectangle an actual floor
	for y in range(len(mapData[mapIndex["spawn"]][x])):
		if y in range(3, 15) and x in range(5, 20):
			mapData[mapIndex["spawn"]][x][y] = ("openMonCenterFloor", "")

#mapData[mapIndex["spawn"]][5][5] = ("grass", "tallGrass") example to set a tile on a map
