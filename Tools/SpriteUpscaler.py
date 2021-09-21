import pygame
from os import walk
Files=[]
Sprites=[]
for (dirpath, dirnames, filenames) in walk("64Cyan"):
	Files.extend(dirpath+"\\"+i for i in filenames)
for i in Files:
	if i.endswith(".png"):
		Sprites.append(i)
for i in Sprites:
	pygame.image.save(pygame.transform.scale2x(pygame.image.load(i)),i)