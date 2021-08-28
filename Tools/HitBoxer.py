from Renderers import Loli
import pygame
SelectedTrigger=0
Frame=0
AttackData=[
{
	"Triggers":
	[
	{
		"Box":[[-64,-64],[64,64]],
		"Type":"Hurt",
	},
	],
},
]

class TriggerSelecter:
	def __init__(self,i):
		self.i=i
	def Function(self):
		global SelectedTrigger
		SelectedTrigger=self.i

def ExitHitBoxer():
	return "Exit"

def SelectTrigger():
	global AttackData,Frame
	X=[]
	for i in range(len(AttackData[Frame]["Triggers"])):
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
	for i in range(len(AttackData[Frame]["Triggers"])):
		pass
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