from Renderers import Loli
import pygame
Triggers=[3,4]
SelectedTrigger=0
Frame=0
AttackData=0

class TriggerSelecter:
	def __init__(self,i):
		self.i=i
	def Function(self):
		global SelectTrigger
		SelectTrigger=self.i

def ExitHitBoxer():
	return "Exit"

def SelectTrigger():
	X=[]
	for i in range(len(Triggers)):
		X.append(Loli.MenuLabel("Trigger "+str(i),Function=TriggerSelecter(i).Function))
	return Loli.SlideMenu(X).Open()
	pass

def Menu():
	return Loli.SlideMenu([
		Loli.MenuTitle("HitBoxer"),
		Loli.MenuLabel("Select Trigger",Function=SelectTrigger),
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