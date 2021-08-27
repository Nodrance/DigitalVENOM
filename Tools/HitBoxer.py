from Renderers import Loli
import pygame

def ExitHitBoxer():
	return "Exit"

def Menu():
	return Loli.SlideMenu([
		Loli.MenuTitle("HitBoxer"),
		Loli.MenuLabel("Exit",Function=ExitHitBoxer),
		]).Open()

def Render():
	Loli.TrueWin.fill(0)
	pygame.display.update()
	pass

def Start():
	while 1:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_ESCAPE:
					X=Menu()
					if X=="Exit":
						return
					pass
		Render()