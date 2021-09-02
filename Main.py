from Controllers import Owen,Owen2,Eden,EdenJoystick,Replayer
from Characters import InjectionCube,QuW
from Renderers import Loli
from Rulesets import Competitive,Warmup
from Engines import Alchemy
from Stages import VenomCompetitive,VenomWarmup
from Tools import HitBoxer
import sys,copy,json,pygame
#CSCharacters=[InjectionCube.Character,QuW.Character]
CSCharacters=[QuW.Character,QuW.Character]
#BG=pygame.image.load("Stages/Test1/Test1.bmp")
TitleScreenImage=pygame.image.load("Sprites/Title Screen/Title Screen.png").convert()
P1WImage=pygame.image.load("Sprites/Win Screen/Player 1 Wins.png").convert()
P2WImage=pygame.image.load("Sprites/Win Screen/Player 2 Wins.png").convert()
MenuSounds=[
pygame.mixer.Sound("Sounds/Menu Screen/Switch.wav"),
pygame.mixer.Sound("Sounds/Menu Screen/Select.wav"),
]

P1C=Owen.Controller(pygame)
try:
	P2C=EdenJoystick.Controller(pygame)
except:
	P2C=Eden.Controller(pygame)
#P2C=EdenJoystick.Controller(pygame)
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

def TitleScreen():
	pygame.transform.smoothscale(TitleScreenImage,(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
	pygame.display.update()
	G=1
	while G:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				G=0
def WinScreen(Index):
	pygame.transform.smoothscale([P1WImage,P2WImage][Index],(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
	pygame.display.update()
	G=1
	pygame.time.wait(1000)
	while G:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				G=0
def CharacterSelect():
	global P1C,P2C,P1,P2,CSCharacters
	P1S=0
	P2S=0
	R=0
	P1T=[-32,0]
	P2T=[-32,0]
	P1R=0
	P2R=0
	Index1=0
	Index2=0
	OI1=Index1
	OI2=Index2
	while True:
		if P1R and P2R:
			return Index1,Index2
		P1T=[64*(Index1%2)-32,0]
		P2T=[64*(Index2%2)-32,0]
		Index1=Index1%len(CSCharacters)
		Index2=Index2%len(CSCharacters)
		Loli.RenderSelect(P1T,P2T,Index1,Index2)
		G=1
		X=P1C.Character(pygame)
		Y=P2C.Character(pygame)
		X2=X
		Y2=Y
		while G:
			for Event in pygame.event.get():
				if Event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if Event.type == pygame.KEYDOWN:
					if Event.key==pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
			X=P1C.Character(pygame)
			Y=P2C.Character(pygame)
			if X!=X2 and not P1R:
				if X["Jab"]:
					MenuSounds[1].play()
					P1=CSCharacters[Index1](0,pygame)
					P1R=1
				else:
					Index1+=X["X"]
					if OI1!=Index1:
						MenuSounds[0].play()
						OI1=Index1
				X2=X
				G=0
			if Y!=Y2 and not P2R:
				if Y["Jab"]:
					MenuSounds[1].play()
					P2=CSCharacters[Index2](1,pygame)
					P2R=1
				else:
					Index2+=Y["X"]
					if OI2!=Index2:
						MenuSounds[0].play()
						OI2=Index2
				Y2=Y
				G=0
			pass
		pass
	pass
def CompetitiveF():
	CharacterSelect()
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	#Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
	return Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
def TrainingF():
	CharacterSelect()
	Loli.HBR=1
	Loli.P1W=0
	Loli.P2W=0
	while True:
		X=Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
		if X==(0,0):
			return X
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
def CasualF():
	CharacterSelect()
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	return Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
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
		return Alchemy.Game(P1,P2,Loli,pygame,Replayer1,Replayer2,BG,pygame.mixer.Sound("Sounds/GameStart0.wav"),SaveReplay=0,Rendering=1)
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
		#Loli.MenuLabel("HitBoxer",Function=HitBoxer.Start),
		Loli.MenuLabel("TextBoxTest",Function=Loli.TextInputBox),
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