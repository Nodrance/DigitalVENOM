import os,sys
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from Controllers import Owen,OwenJoystick,Eden,EdenJoystick,Replayer,EdenJoystick2
from Characters import InjectionCube,QuW,ERic
from Renderers import Loli
from Rulesets import Competitive,Warmup,Training
from Engines import Alchemy,Combustion
from Stages import VenomCompetitive,VenomWarmup,City,CityLights,NightLight,RoyalDuel
from Tools import HitBoxer,ControllerDebug
import sys,copy,json,pygame,dis,inspect,Debug
#sys.stdout = open("OutputLog.txt", "w")
#sys.stderr = open("ErrorLog.txt", "w")
"""
Camera=Loli.LoliCamera(0,-15,-1,1)
BlitzLogo=pygame.image.load("Sprites/BlitzLogoTransparent.png")
for i in range(12):
	Loli.win.fill(0)
	Loli.RenderSprite(BlitzLogo,(0,0,(-3/(i*2+1))+3),500,500,Camera)
	Loli.ScaleWin()
	pygame.time.delay(50)
	pass
"""

"""  
TODO:
Fix cancelling am>am2
""" 

CSCharacters=[ERic.Character,QuW.Character]
TitleScreenImage=pygame.image.load("Sprites/Title Screen/Title Screen.png").convert()
P1WImage=pygame.image.load("Sprites/Win Screen/Player 1 Wins.png").convert()
P2WImage=pygame.image.load("Sprites/Win Screen/Player 2 Wins.png").convert()

try:
	P1C=OwenJoystick.Controller(pygame)
	P2C=EdenJoystick2.Controller(pygame)
except:
	try:
		P1C=Owen.Controller(pygame)
		P2C=OwenJoystick.Controller(pygame)
	except:
		P1C=Owen.Controller(pygame)
		P2C=Eden.Controller(pygame)
#ControllerDebug.Main()
P1=QuW.Character#(0,pygame)
P2=QuW.Character#(1,pygame)
BG=VenomWarmup.Stage(pygame)
BG2=VenomCompetitive.Stage(pygame)

WinIndex=[
"Nobody Wins?",
"Player 2 Wins!",
"Player 1 Wins!",
"It was a tie?",
]

def WinScreen(X):
	Y=int(X[0])-int(X[1])
	G=0
	if Y==1:
		pygame.transform.smoothscale(P2WImage,(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
		Loli.UpdateTrueWin()
		pygame.time.delay(2000)
		G=1
	if Y==-1:
		pygame.transform.smoothscale(P1WImage,(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
		Loli.UpdateTrueWin()
		pygame.time.delay(2000)
		G=1
	while G:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				G=0
	pass
def TitleScreen():
	pygame.transform.smoothscale(TitleScreenImage,(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
	pygame.display.update()
	G=1
	while G:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				G=0
"""def WinScreen(Index):
	pygame.transform.smoothscale([P1WImage,P2WImage][Index],(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
	pygame.display.update()
	G=1
	pygame.time.wait(1000)
	while G:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				G=0"""
def CompetitiveF():
	global P1C,P2C,P1,P2,CSCharacters
	Combustion.GameMode="Competitive"
	P1,P2=Loli.CharacterSelect(P1C,P2C,P1,P2,CSCharacters)
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	#Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
	WinScreen(Competitive.Match(pygame,Loli,Combustion,P1C,P2C,P1,P2,BG2))
def TrainingF():
	global P1C,P2C,P1,P2,CSCharacters
	Combustion.GameMode="Training"
	P1,P2=Loli.CharacterSelect(P1C,P2C,P1,P2,CSCharacters)
	#This line shows Triggers in the Loli renderer
	#Loli.HBR=1
	Loli.P1W=0
	Loli.P2W=0
	while True:
		#X=Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
		X=Training.Match(pygame,Loli,Combustion,P1C,P2C,P1,P2,BG)
		if X==(0,0):
			return X
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
def CasualF():
	global P1C,P2C,P1,P2,CSCharacters
	Combustion.GameMode="Casual"
	P1,P2=Loli.CharacterSelect(P1C,P2C,P1,P2,CSCharacters)
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	WinScreen(Warmup.Match(pygame,Loli,Combustion,P1C,P2C,P1,P2,BG))
	#Warmup.Match(pygame,Loli,Combustion,P1C,P2C,P1,P2,BG)
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
def ReplayF():
	#CharacterSelect()
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	ReplayData=ReplayData=json.load(open("Replay.json","r"))
	P1=sys.modules[ReplayData[0]["Player 1 Character Module Name"]].Character(0,pygame)
	P2=sys.modules[ReplayData[0]["Player 2 Character Module Name"]].Character(1,pygame)
	P1.Reset(0,pygame)
	P2.Reset(1,pygame)
	BG=sys.modules[ReplayData[0]["Stage Module Name"]].Stage(pygame)
	Replayer1=Replayer.Controller(pygame,Player=0,ReplayData=ReplayData)
	Replayer2=Replayer.Controller(pygame,Player=1,ReplayData=ReplayData)
	if ReplayData[0]["Engine Module Name"]=="Engines.Alchemy":
		#return Warmup.Match(pygame,Loli,Alchemy,Replayer1,Replayer2,P1,P2,BG)
		WinScreen(Alchemy.Game(P1,P2,Loli,pygame,Replayer1,Replayer2,BG,pygame.mixer.Sound("Sounds/GameStart0.wav"),SaveReplay=0,Rendering=1))
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
def QuitGame():
	pygame.quit()
	sys.exit()
MenuFunctions=[
CompetitiveF,
TrainingF,
CasualF,
]

def MenuScreen():
	Loli.GradientMenu([
		Loli.MenuTitle("DigitalVENOM"),
		Loli.MenuLabel("Competitive",Function=CompetitiveF),
		Loli.MenuLabel("Training",Function=TrainingF),
		Loli.MenuLabel("Casual",Function=CasualF),
		Loli.MenuLabel("Replay",Function=ReplayF),
		Loli.MenuLabel("Development Menu",Function=Debug.DebugMenu),
		Loli.MenuLabel("Settings",Function=Settings.Menu),
		Loli.MenuLabel("Quit",Function=QuitGame),
		]).Open()
class Settings:
	def Menu():
		Loli.SlideMenu([
			Loli.MenuTitle("Settings"),
			Loli.MenuHeader("Render Settings:"),
			Loli.MenuCycleLabel([
				"Extreme Impacts Off",
				"Extreme Impacts On",
				],
				[
				0,
				1,
				],Module=Loli,Attribute="ImpactGlitch",Cycle=Loli.ImpactGlitch),#,Function=Settings.ExtremeImpacts),
			Loli.MenuCycleLabel([
				"Blit Bloom Off",
				"Blit Bloom On",
				],
				[
				0,
				1,
				],Module=Loli,Attribute="BlitBloom",Cycle=Loli.BlitBloom),#,Function=Settings.BlitBloom),
			]).Open()
		Settings.SaveSettings()
		pass
	def SaveSettings():
		json.dump(
			{
			"Extreme Impacts":Loli.ImpactGlitch,
			"Blit Bloom":Loli.BlitBloom,
			}
			,open("Settings.config","w"))
		pass
	def LoadSettings():
		try:
			X=json.load(open("Settings.config","r"))
			Loli.ImpactGlitch=X["Extreme Impacts"]
			Loli.BlitBloom=X["Blit Bloom"]
		except:
			pass
		pass
	def ExtremeImpacts(Text):
		Loli.ImpactGlitch=(Text=="Extreme Impacts On")
	def BlitBloom(Text):
		Loli.BlitBloom=(Text=="Blit Bloom On")
Settings.LoadSettings()
if __name__=="__main__":
	TitleScreen()
	while 1:MenuScreen()
