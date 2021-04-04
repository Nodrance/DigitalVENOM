from Controllers import Owen, Eden, EdenJoystick
from Characters import InjectionCube,QuW
from Renderers import Loli
from Engines import Alchemy
from Rulesets import Competitive,Warmup
from Stages import VenomCompetitive,VenomWarmup
import sys,random
pygame=Loli.P

CSCharacters=[InjectionCube.Character,QuW.Character]
#BG=pygame.image.load("Stages/Test1/Test1.bmp")
TitleScreenImage=pygame.image.load("Sprites/Title Screen/Title Screen.png").convert_alpha()
P1WImage=pygame.image.load("Sprites/Win Screen/Player 1 Wins.png").convert_alpha()
P2WImage=pygame.image.load("Sprites/Win Screen/Player 2 Wins.png").convert_alpha()
MenuImages=[
	pygame.image.load("Sprites/Menu Screen/Menu Screen Competitive.png").convert_alpha(),
	pygame.image.load("Sprites/Menu Screen/Menu Screen Training.png").convert_alpha(),
	pygame.image.load("Sprites/Menu Screen/Menu Screen Casual.png").convert_alpha(),
]
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
					P1=CSCharacters[Index1]
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
					P2=CSCharacters[Index2]
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
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
	return Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
def TrainingF():
	Loli.HBR=1
	Loli.P1W=0
	Loli.P2W=0
	while True:
		Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
def CasualF():
	Loli.HBR=0
	Loli.P1W=0
	Loli.P2W=0
	return Warmup.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG)
	#X=Competitive.Match(pygame,Loli,Alchemy,P1C,P2C,P1,P2,BG2)
	#print(WinIndex[X[0]*2+X[1]])
MenuFunctions=[
CompetitiveF,
TrainingF,
CasualF,
]
def MenuScreen():
	global MenuImages,MenuFunctions,MenuSounds
	Index=0
	OI=0
	while True:
		pygame.transform.smoothscale(MenuImages[Index%3],(Loli.TrueWin.get_width(),Loli.TrueWin.get_height()),Loli.TrueWin)
		pygame.display.update()
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
					if Event.key==pygame.K_0:
						pygame.mixer.music.load(random.choice(Loli.SoundtrackList))
						pygame.mixer.music.play()
					if Event.key==pygame.K_1:
						pygame.mixer.music.load("Music/Lethal Injection.wav")
						pygame.mixer.music.play()
					if Event.key==pygame.K_2:
						pygame.mixer.music.load("Music/QT.wav")
						pygame.mixer.music.play()
			X=P1C.Character(pygame)
			Y=P2C.Character(pygame)
			if X!=X2 or Y!=Y2:
				Index+=X["Y"]+Y["Y"]
				if OI!=Index:
					MenuSounds[0].play()
					G=0
					OI=Index
				if X["Jab"] or Y["Jab"]:
					MenuSounds[1].play()
					CharacterSelect()
					M=MenuFunctions[Index%3]()
					WinScreen(M[0])
					G=0
				X2=X
				Y2=Y
			pass
		pass
TitleScreen()
MenuScreen()
#print(WinIndex[str(Alchemy.Game(P1,P2,Loli,pygame,P1C,P2C,BG))])

#while True:
	#Alchemy.Frame(P1,P2,Loli,pygame,P1C,P2C,BG)