from Renderers import Loli
import pygame
def Main():
	Debugging=1
	while Debugging:
		for Event in pygame.event.get():
			if Event.type==pygame.JOYBUTTONDOWN:
				print(Event.button)
			if Event.type==pygame.KEYDOWN:
				Debugging=0
		Loli.TrueWin.fill((0,255,255))
		Loli.UpdateTrueWin()
	pass