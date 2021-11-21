import pygame
from os import walk
SpriteList=[]
Files = []
for (dirpath, dirnames, filenames) in walk("l"):
	Files.extend(i for i in filenames)
	break
for i in Files:
	if i.endswith(".png"):
		SpriteList.append(i)
for i in SpriteList:
	print(i)
	X=pygame.image.load("l/"+i)
	Y=pygame.image.load("v/"+i)
	X.blit(Y,(0,0),special_flags=pygame.BLEND_SUB)
	X.set_colorkey((0,0,0))
	Y.blit(X,(0,0))
	pygame.image.save(Y,i)