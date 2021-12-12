from Renderers import Loli
import pygame,os

#This is story mode
#It's not going to be complete for a long time
#But I'm starting it just so I can get some lore out there
def UpdateCharacterScenes():
	"""
	Gets a list of scenes that the current character is in
	"""
	global CurrentCharacter,Scenes,CharacterScenes,CurrentScene,CurrentShot
	X=CharacterScenes[CurrentScene]
	"""Y=[]
	for i in Scenes:
		if CurrentCharacter in i.Characters:
			print(CurrentCharacter)
			print(i.Characters)
			Y.append(i)
	CharacterScenes=Y"""
	CharacterScenes=[i for i in Scenes if CurrentCharacter in i.Characters or CurrentCharacter=="Full Story"]
	if CurrentCharacter=="Full Story":
		CharacterScenes.pop(0)
	try:
		CurrentScene=CharacterScenes.index(X)
	except:
		CurrentScene=0
		CurrentShot=0
CurrentScene=0
Scenes=[]
CurrentCharacter="Story Select"
CurrentShot=0

class Character:
	def __init__(self,Name,Color):
		self.Name=Name
		self.Color=Color
		self.Images={
		"Template.png": pygame.image.load("Story/Images/Template.png")
		}
		Files = []
		Files2= []
		for (dirpath, dirnames, filenames) in os.walk("Story/Images/"+Name):
			Files.extend(dirpath+"\\"+i for i in filenames)
			Files2.extend(filenames)
		for j,i in enumerate(Files):
			if i.endswith(".png"):
				self.Images[Files2[j]]=pygame.image.load(i)
	def __call__(self,Text,Image):
		if not Image in self.Images:
			Image="Template.png"
		return Shot(
			Author=self.Name,
			Alerts=[
				AlertCutIn(self.Images[Image],BackgroundColor=self.Color),
				AlertText(Text,Color=self.Color),
			]
			)

def HandleShot(Plus=1):
	global CurrentShot,CurrentScene,CharacterScenes
	if Plus:
		CurrentShot+=1
	else:
		CurrentShot-=1
	if CurrentShot>len(CharacterScenes[CurrentScene].Shots)-1:
		CurrentScene+=1
		if CurrentScene>len(CharacterScenes)-1:
			CurrentScene-=1
			CurrentShot-=1
		else:
			CurrentShot=0
	elif CurrentShot<0:
		CurrentScene-=1
		if CurrentScene<0:
			CurrentScene=0
			CurrentShot=0
		else:
			CurrentShot=len(CharacterScenes[CurrentScene].Shots)-1
	pass

class Scene:
	def __init__(self,Background,Characters=[],Shots=[]):
		self.Background=pygame.image.load("Story/Images/Backgrounds/"+Background+".png")
		self.Characters=Characters
		self.Shots=Shots

class Shot:
	def __init__(self,Alerts=[],Author=None,Sounds=[]):
		self.Alerts=Alerts
		self.Author=Author
		self.Sounds=Sounds
		if not Author==None:
			self.Alerts.append(AlertText(Author,Side=0,Y=0))
		pass
	def __call__(self):
		for Sound in self.Sounds:
			Sound.play()
		Loli.LocalAlerts=[]
		for i in self.Alerts:
			i()

class AlertCutIn:
	def __init__(self,Sprite,Side=0,BackgroundColor=(255,255,0),Y=30,LifeTime=60):
		self.Sprite=Sprite
		self.Side=Side
		self.BackgroundColor=BackgroundColor
		self.Y=Y
		self.LifeTime=LifeTime
	def __call__(self):
		Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.Side,Sprite=self.Sprite,BackgroundColor=self.BackgroundColor,Y=self.Y,LifeTime=self.LifeTime))

class AlertText:
	def __init__(self,Text,Color=(255,255,0),Side=1,BackgroundColor=(0,0,0),Y=94,LifeTime=60):
		self.Text=Text
		self.Color=Color
		self.Side=Side
		self.BackgroundColor=BackgroundColor
		self.Y=Y
		self.LifeTime=LifeTime
	def __call__(self):
		Loli.LocalAlerts.append(Loli.AlertText(self.Text,Side=self.Side,Color=self.Color,BackgroundColor=self.BackgroundColor,Y=self.Y,LifeTime=self.LifeTime))

class AlertOverlay:
	def __init__(self,Sprite,LifeTime=60):
		self.Sprite=Sprite
		self.LifeTime=LifeTime
	def __call__(self):
		Loli.LocalAlerts.append(Loli.AlertCutIn(Sprite=self.Sprite,LifeTime=self.LifeTime))

#Here we define some characters
#For the purposes of the story select menu we need a (FullStoryCharacter)
FullStoryCharacter=Character("Full Story",(255,255,255))

#FirstInjectionAnnouncer=Character("First Injection Announcer",(255,255,0))
Narrator=Character("Narrator",(255,255,255))
InjectionCube=Character("Injection Cube",(0,255,255))

QuW=Character("QuW",(255,0,255))
Hans=Character("Hans",(160,64,32))

OwenCMYK=Character("Owen CMYK",(0,255,255))
Eden=Character("Eden",(255,0,0))

ERic=Character("ERic",(255,64,0))



#Here we start defining actualy story scenes
Scenes=[
#Firstly is the story select, it's technically considered a scene
Scene(
	Background="Default",
	Characters=["Story Select"],
	Shots=[
		FullStoryCharacter("Select Story","Template.png"),
		QuW("Select Story","Venom2.png"),
		ERic("Select Story","Venom3.png"),
	]
	),
Scene(
	Background="First Injection Beta",
	Characters=["QuW"],
	Shots=[
		Shot(),
		OwenCMYK("A champion is born!","Venom3.png"),
		QuW("","Venom5.png"),
		QuW("","Venom6.png"),
		QuW("I was just...","Venom1.png"),
		QuW("What is this place?","Venom1.png"),
		OwenCMYK("DigitalVENOM","Venom3.png"),
		OwenCMYK("First Injection","Venom3.png"),
		OwenCMYK("Play or Forfeit?","Venom3.png"),
		QuW("Play?","Venom1.png"),
		InjectionCube("","Venom2.png"),
		QuW("I...","Venom1.png"),
		QuW("What is that?","Venom1.png"),
		InjectionCube("","Venom5.png"),
		InjectionCube("","Venom4.png"),
		Narrator("The Cube struck QuW","Template.png"),
		Narrator("A sharp needle pierced through her stomach,","Template.png"),
		Narrator("shredding her open from the inside.","Template.png"),
	]
	),
Scene(
	Background="First Injection Beta",
	Characters=["ERic","QuW"],
	Shots=[
		Shot(),
		ERic("What happened?","Venom1.png"),
		QuW("So this is the second one I take it.","Venom2.png"),
		OwenCMYK("DigitalVENOM","Venom3.png"),
		OwenCMYK("Second Injection","Venom3.png"),
		OwenCMYK("Play or Forfeit?","Venom3.png"),
		QuW("We'll play!","Venom2.png"),
		QuW("I'm not losing this time.","Venom2.png"),
		ERic("What?","Venom1.png"),
	]
	),
]

CharacterScenes=[i for i in Scenes if CurrentCharacter in i.Characters]

def Main(P1C):
	global CurrentShot,CharacterScenes,CurrentScene,CurrentCharacter
	CurrentScene=0
	CurrentCharacter="Story Select"
	CurrentShot=0
	UpdateCharacterScenes()
	CharacterScenes[CurrentScene].Shots[CurrentShot]()
	while 1:
		Events=pygame.event.get()
		for Event in Events:
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_ESCAPE:
					return
		C=P1C.Character(pygame,Events)
		if C["X2"]==1:
			HandleShot(1)
			CharacterScenes[CurrentScene].Shots[CurrentShot]()
		elif C["X2"]==-1:
			HandleShot(0)
			CharacterScenes[CurrentScene].Shots[CurrentShot]()
		if C["v"]:
			if not CharacterScenes[CurrentScene].Shots[CurrentShot].Author==None:
				CurrentCharacter=CharacterScenes[CurrentScene].Shots[CurrentShot].Author
				UpdateCharacterScenes()
				CharacterScenes[CurrentScene].Shots[CurrentShot]()
		#Loli.win.fill(0)
		Loli.win.blit(CharacterScenes[CurrentScene].Background,(0,0))
		Loli.HandleLocalAlerts(Cull=0)
		Loli.ScaleWin()