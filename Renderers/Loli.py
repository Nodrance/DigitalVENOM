import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import pygame,random,math,numpy
import pygame.gfxdraw
from os import walk
from Tools import ParticleGenerator
#Here we define some basic variables.
RenderBenchmarking=0
P=pygame
pygame.mixer.pre_init()
pygame.init()
FakeTime=0
GlobalAlerts=[]
LocalAlerts=[]
Clock=pygame.time.Clock()
TrueWin=pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
#win=pygame.Surface((1366,768))
#win=pygame.Surface((683,384))
win=pygame.Surface((int(683/2),int(384/2)))
#win=pygame.display.set_mode((int(683/2),int(384/2)),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
#print(win.get_width()*2)
FZ=-1
HitFlashes=[]
"""for i in range(16):
	HitFlashes.append(ParticleGenerator.GenerateSpikes(256,10))
	pass"""
BlitBloom=0
win.set_alpha(None)
ImpactGlitch=1
LastOutlines=[[],[],[]]
try:
	globals()["c"]=pygame.image.load("coconut.jpg")
	pass
except:
	pass
#TrueWin=win
ReadyScreen=pygame.image.load("Sprites/Game Start Second Injection.png").convert_alpha()
MenuSounds=[
pygame.mixer.Sound("Sounds/Menu Screen/Switch.wav"),
pygame.mixer.Sound("Sounds/Menu Screen/Select.wav"),
]
CamCap=(win.get_width()*0.9)
P1W=0
P2W=0
HBR=0
pygame.mixer.set_num_channels(32)
SimScaling=4
TriggerSprites=[
pygame.image.load("Sprites/Trigger.png").convert(),
pygame.image.load("Sprites/Trigger2.png").convert()
]
P1WSprite=pygame.image.load("Sprites/Victory Cyan.png").convert()
P2WSprite=pygame.image.load("Sprites/Victory Magenta.png").convert()
KO2Sprite=pygame.image.load("Sprites/KO2.png").convert()
CSP1Image=pygame.image.load("Sprites/Character Select Screen/P1.png").convert_alpha()
CSP2Image=pygame.image.load("Sprites/Character Select Screen/P2.png").convert_alpha()
CSSImage=pygame.image.load("Sprites/Character Select Screen/Screen.png").convert()
CSBackground=pygame.image.load("Sprites/Character Select Screen/Background.png").convert()#.convert_alpha()
CSCharacters=[
pygame.image.load("Sprites/Character Select Screen/InjectionCubePortrait.png").convert_alpha(),
pygame.image.load("Sprites/Character Select Screen/QuWPortrait.png").convert_alpha(),
]
"""SoundtrackList=[
"Music/Lethal Injection.wav",
"Music/QT.wav",
]"""
SoundtrackList=[]
Files = []
for (dirpath, dirnames, filenames) in walk("Music"):
	Files.extend(dirpath+"\\"+i for i in filenames)
for i in Files:
	if i.endswith(".wav"):
		SoundtrackList.append(i)
pygame.mixer.music.load(random.choice(SoundtrackList))#"Music/Dusk and Daylight.wav")
pygame.mixer.music.play()
pygame.mixer.music.queue(random.choice(SoundtrackList))
#The above commented code began crashing the game, this has now been fixed.
Particles=[]
def FakeTimeFunction():
	global FakeTime
	return FakeTime

#pygame.time.get_ticks=FakeTimeFunction

def GenerateSlidingInvertText(Text,Size,Frame,Inverted=0,Color=(255,255,255)):
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",Size)
	Surface=win.copy()
	Colors=[[(0,0,0),Color],[Color,(0,0,0)]][Inverted]
	Surface.fill(Colors[0])
	Surface2=Font.render(Text,0,Colors[1],Colors[0])
	G=int(Surface2.get_width()/2)
	Surface3=pygame.transform.chop(Surface2,[(G-int(G/Frame),0),(2*int(G/Frame),0)])
	Surface.blit(Surface3,(int(Surface.get_width()/2-Surface3.get_width()/2),int(Surface.get_height()/2-Surface3.get_height()/2)))
	return Surface

class AbstractSign:
	def __init__(self,Stages):
		self.Stages=Stages
		self.Color=(255,255,255)
	def __call__(self,Size,Time,Color,BG):
		Surface=pygame.Surface((Size,Size))
		Surface.fill(BG)
		Centre=Size/2
		for i,Stage in enumerate(self.Stages):
			if i == int(Time):
				T=Time%1
				if T>0.5:
					T-=0.5
					T=(2*T*(1-T))+0.5
				else:
					T=2*T*T
				for j,Obj in enumerate(Stage):
					pygame.draw.rect(Surface,Color,[Centre+(Obj[0]*Size/20)+min(0,Obj[4]*Size/20*T),Centre+(Obj[1]*Size/20)+min(0,Obj[5]*Size/20*T),Obj[2]*Size/20+abs(Obj[4]*Size/20*T),Obj[3]*Size/20+abs(Obj[5]*Size/20*T)])
				break
			else:
				for j,Obj in enumerate(Stage):
					pygame.draw.rect(Surface,Color,[Centre+(Obj[0]*Size/20)+min(0,Obj[4]*Size/20),Centre+(Obj[1]*Size/20)+min(0,Obj[5]*Size/20),Obj[2]*Size/20+abs(Obj[4]*Size/20),Obj[3]*Size/20+abs(Obj[5]*Size/20)])
		return Surface

AbstractSigns={
"Competitive":AbstractSign([
	[
	[-7,7,2,0,0,-6],
	[5,7,2,0,0,-6],
	],
	[
	[-3,7,2,0,0,-10],
	[1,7,2,0,0,-10],
	],
	[
	[-3,-5,2,0,0,-2],
	[1,-5,2,0,0,-2],
	],
	]),
"Casual":AbstractSign([
	[
	[-7,5,0,2,6,0],
	[7,5,0,2,-6,0],
	],
	[
	[-7,1,0,2,6,0],
	[7,1,0,2,-6,0],
	],
	[
	[-7,-1,2,0,0,-6],
	[5,-1,2,0,0,-6],
	],
	]),
"Training":AbstractSign([
	[
	[-7,-7,0,2,6,0],
	[-7,-3,0,2,6,0],
	],
	[
	[-7,1,0,2,14,0],
	[1,5,0,2,6,0],
	],
	[
	[1,-1,2,0,0,-2],
	[5,-1,2,0,0,-2],
	],
	]),
}

class LineParticle:
	def __init__(self,Pos,Vel,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.XV=Vel[0]
		self.YV=Vel[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		T2=TT+self.Length*(self.Life-TT/10)
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		if win.get_width()>(int(X+self.XV*TT)>0 and win.get_height()>int(Y+self.YV*TT+TT**2))>0:
			pygame.draw.line(win,self.Color,(X+self.XV*TT,Y+self.YV*TT+TT**2),(X+self.XV*T2,Y+self.YV*T2+T2**2),5)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class BlitParticle:
	def __init__(self,Pos,Width,Height,Animation,Life,Blend=None):
		self.StartTime=pygame.time.get_ticks()
		self.Pos=(Pos[0],Pos[1],0)
		self.Life=Life
		self.Width=Width
		self.Height=Height
		self.Blend=Blend
		self.Animation=Animation
	def Render(self,Camera):
		RenderSprite(self.Animation[int((pygame.time.get_ticks()-self.StartTime)/17)%len(self.Animation)],self.Pos,self.Width,self.Height,Camera,Blending=self.Blend)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class ScreenSpaceParticle:
	def __init__(self,Width,Height,Animation,Life,Blend=None):
		global Camera
		self.StartTime=pygame.time.get_ticks()
		self.Pos=(Camera.X,Camera.Y,0)
		self.Life=Life
		self.Width=Width
		self.Height=Height
		self.Blend=Blend
		self.Animation=Animation
	def Render(self,Camera):
		self.Pos=(Camera.X,Camera.Y,Camera.Z+1+((pygame.time.get_ticks()-self.StartTime)/1000/self.Life/10))
		RenderSprite(self.Animation[int((pygame.time.get_ticks()-self.StartTime)/17)%len(self.Animation)],self.Pos,self.Width,self.Height,Camera,Blending=self.Blend)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class SlidingInvertTextParticle:
	def __init__(self,Text,Life,Size=50):
		global Camera
		self.StartTime=pygame.time.get_ticks()
		self.Life=Life
		self.Text=Text
		self.Size=Size
	def Render(self,Camera):
		win.blit(GenerateSlidingInvertText(self.Text,self.Size,max(int((pygame.time.get_ticks()-self.StartTime)/5/self.Life),1),Inverted=(pygame.time.get_ticks()-self.StartTime)<self.Life*500,Color=(255,255,255)),(0,0),special_flags=pygame.BLEND_ADD)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class InverseLineParticle:
	def __init__(self,Pos,Vel,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.XV=Vel[0]
		self.YV=Vel[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=self.Life*10-(pygame.time.get_ticks()-self.StartTime)/100
		T2=TT+self.Length*(self.Life-TT/10)
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		pygame.draw.line(win,self.Color,(X+self.XV*TT,Y+self.YV*TT+TT**2),(X+self.XV*T2,Y+self.YV*T2+T2**2),5)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class SpikeParticle:
	def __init__(self,Pos,Vel,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.XV=Vel[0]
		self.YV=Vel[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		T2=TT+self.Length*(self.Life-TT/10)
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		CornerValue=((Camera.Z/Camera.FOV)*(win.get_width()/2),(Camera.Z/Camera.FOV)*(win.get_height()/2))
		pygame.draw.polygon(win,self.Color,[(X,Y),(X+self.XV*100-self.YV*T2,Y+self.YV*100+self.XV*T2),(X+self.XV*100+self.YV*T2,Y+self.YV*100-self.XV*T2)])
		pygame.draw.polygon(win,(255,255,255),[(X+self.XV*10,Y+self.YV*10),(X+self.XV*100-self.YV*T2,Y+self.YV*100+self.XV*T2),(X+self.XV*100+self.YV*T2,Y+self.YV*100-self.XV*T2)])
		#pygame.draw.line(win,self.Color,(X+self.XV*TT,Y+self.YV*TT+TT**2),(X+self.XV*T2,Y+self.YV*T2+T2**2),5)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class StarParticle:
	def __init__(self,Pos,Vel,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.XV=Vel[0]
		self.YV=abs(Vel[1])
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		T2=50*self.Length*(self.Life-TT/10)
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		L1=(X+self.XV*T2,Y+self.YV*T2)
		L2=(X+5,Y+5)
		L3=(X+self.YV*T2,Y-self.XV*T2)
		L4=(X+5,Y-5)
		L5=(X-self.XV*T2,Y-self.YV*T2)
		L6=(X-5,Y-5)
		L7=(X-self.YV*T2,Y+self.XV*T2)
		L8=(X-5,Y+5)
		pygame.draw.polygon(win,self.Color,[L1,L2,L3,L4,L5,L6,L7,L8])
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class CircleParticle:
	def __init__(self,Pos,Vel,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.XV=Vel[0]
		self.YV=Vel[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		T2=self.Length*(self.Life-TT/10)
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		try:
			if win.get_width()>(int(X+self.XV*TT)>0 and win.get_height()>int(Y+self.YV*TT+TT**2))>0:
				pygame.draw.circle(win,self.Color,(int(X+self.XV*TT),int(Y+self.YV*TT+TT**2)),int(10*T2))
				pygame.draw.circle(win,(255,255,255),(int(X+self.XV*TT),int(Y+self.YV*TT+TT**2)),int(8*T2))
		except:
			pass
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class PulseParticle:
	#Creates a pulse effect. Used for cancels.
	def __init__(self,Pos,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		#TODO:
		#Clean up this code a little.
		H=3
		H2=(1-((pygame.time.get_ticks()-self.StartTime)/1000/self.Life))**H
		H3=1-H2
		H4=self.Length*H3
		try:
			pygame.draw.circle(win,self.Color,(int(X),int(Y)),int(H4),width=2)
		except:
			pass
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class ClockParticle:
	#Creates a clock effect. Used for overclock.
	def __init__(self,Pos,Life,Length,Color):
		self.StartTime=pygame.time.get_ticks()
		self.X=Pos[0]
		self.Y=Pos[1]
		self.Life=Life
		self.Length=Length
		self.Color=Color
	def Render(self,Camera):
		TT=(pygame.time.get_ticks()-self.StartTime)/100
		X=self.X-Camera.X
		Y=self.Y-Camera.Y
		X/=-Camera.Z*Camera.FOV
		Y/=-Camera.Z*Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		#TODO:
		#Clean up this code a little.
		H=(pygame.time.get_ticks()-self.StartTime)/self.Life/1000
		H*=numpy.pi*2
		SA=numpy.pi/2
		EA=-H+SA
		pygame.draw.arc(win,self.Color,[(X-self.Length,Y-self.Length),(2*self.Length,2*self.Length)],SA,EA, width=self.Length)
		pygame.draw.arc(win,self.Color,[(X+1-self.Length,Y-self.Length),(2*self.Length,2*self.Length)],SA,EA, width=self.Length)
		pygame.draw.arc(win,self.Color,[(X-self.Length,Y+1-self.Length),(2*self.Length,2*self.Length)],SA,EA, width=self.Length)
		pygame.draw.arc(win,self.Color,[(X+1-self.Length,Y+1-self.Length),(2*self.Length,2*self.Length)],SA,EA, width=self.Length)
			#pygame.draw.circle(win,self.Color,(int(X),int(Y)),int(H4),width=2)
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class LoliCamera: #Defines the camera object.
	def __init__(self,X,Y,Z,FOV):
		self.X=X
		self.Y=Y
		self.Z=Z
		self.FOV=FOV
Camera=LoliCamera(0,-15,-1,1)
def UpdateTrueWin():
	global GlobalAlerts
	GlobalAlerts=[i for i in GlobalAlerts if i.Time<i.LifeTime]
	for i in GlobalAlerts:
		S=i.Render()
		if i.Side:
			TrueWin.blit(S,(TrueWin.get_width()-S.get_width(),i.Y))
		else:
			TrueWin.blit(S,(0,i.Y))
	pygame.display.flip()

def ScaleWin():
	pygame.transform.scale(win,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	#pygame.transform.scale(pygame.transform.scale(win,(int(win.get_width()/2),int(win.get_height()/2))),(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	#pygame.transform.scale2x(win,TrueWin)
	#pygame.transform.scale(pygame.transform.scale2x(pygame.transform.scale2x(win)),(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	UpdateTrueWin()

def HandleMusic():
	global SoundtrackList
	if P.mixer.music.get_busy()==0:
		P.mixer.music.load(random.choice(SoundtrackList))
		P.mixer.music.play()
		P.mixer.music.queue(random.choice(SoundtrackList))
def CreateShadow(Sprite,Color,Highlight,Angle):
	Mask=pygame.mask.from_surface(Sprite)
	Shadow=Mask.to_surface(setcolor=Color,unsetcolor=Highlight)
	Sprite.blit(Shadow,Angle,special_flags=pygame.BLEND_MULT)
	return Sprite
	#Surface.set_colorkey((255,255,255))

def CreateOutline(Sprite,Position,Color=(0,0,0)):
	Mask=pygame.mask.from_surface(Sprite)
	Surface=Mask.to_surface(setcolor=Color,unsetcolor=(255,255,252))
	Surface.set_colorkey((255,255,252))
	return [
	(Surface,(Position[0]+1,Position[1])),
	(Surface,(Position[0]-1,Position[1])),
	(Surface,(Position[0],Position[1]+1)),
	(Surface,(Position[0],Position[1]-1)),
	]

def PolygonVertexShader(Points,Camera): #Defines the sprite render function.
	#X/(Z*FOV) - Reminder of the perspective projection equation.
	L=[]
	for Pos in Points:
		Pos2=(Pos[0]-Camera.X,Pos[1]-Camera.Y,Pos[2]-Camera.Z) #Subtracts the camera position to find out where the sprite should be rendered relatively
		Pos3=(Pos2[0]/(Pos2[2]*Camera.FOV),Pos2[1]/(Pos2[2]*Camera.FOV)) #Uses the perspective projection equation to calculate the 2D position of the sprite.
		X=(win.get_width()/2,win.get_height()/2) #Divides the screen size by two to find the center.
		Pos4=(Pos3[0]+X[0],Pos3[1]+X[1]) #Accounts for the centers of the sprite and screen to set the origin point at zero.
		L.append(Pos4)
	return L

def PolygonPixelShader(Polygon,Shaded=0):
	if Shaded:
		Surface=win.copy()
		#print(Polygon["Color"])
		Surface.fill((0,0,0))
		pygame.draw.polygon(Surface,Polygon["Color"],PolygonVertexShader(Polygon["Points"],Camera))
		Texture=pygame.transform.smoothscale(pygame.transform.smoothscale(Surface,(2,2)),(win.get_width(),win.get_height()))
		try:
			pygame.gfxdraw.textured_polygon(win,PolygonVertexShader(Polygon["Points"],Camera),Texture,0,0)
		except:
			pass
	else:
		pygame.draw.polygon(win,Polygon["Color"],PolygonVertexShader(Polygon["Points"],Camera))

def RenderSprite(Sprite,Pos,Width,Height,Camera,Blending=None,Smooth=0,Blit=1):#Defines the standard sprite render function.
	#Once upon a time I understood this math.
	#Then I compressed the shit out of it, but it still works.
	Z=(Pos[2]-Camera.Z)*Camera.FOV
	DH=Height/Z
	DW=Width/Z
	Pos4=(
		(Pos[0]-Camera.X)/Z+(win.get_width()/2)-(DW/2),
		(Pos[1]-Camera.Y)/Z+(win.get_height()/2)-(DH/2))
	if Smooth==0:
		Sprite2=P.transform.scale(Sprite,(int(DW),int(DH))) #Scales the sprite to the correct size.
	else:
		if Smooth==1:
			Sprite2=P.transform.smoothscale(Sprite,(int(DW),int(DH))) #Scales the sprite to the correct size.
		if Smooth==2:
			Sprite1B=P.transform.scale(Sprite,((int(DW/Sprite.get_width())+1)*Sprite.get_width(),(int(DH/Sprite.get_height())+1)*Sprite.get_height())) #Scales the sprite to the correct size.
			Sprite2=P.transform.smoothscale(Sprite1B,(int(DW),int(DH))) #Scales the sprite to the correct size.
	if Blit:
		if Blending==None:
			win.blit(Sprite2,Pos4) #Blits the sprite to the screen.
		else:
			win.blit(Sprite2,Pos4,special_flags=Blending) #Blits the sprite to the screen.
	else:
		if Blending==None:
			return Sprite2,Pos4
		else:
			return Sprite2,Pos4,None,Blending

def RenderSpriteQuick(Sprite,Pos,Width,Height,Camera):#Crushed bytecode
	#Once upon a time I understood this math.
	#Then I compressed the shit out of it, but it still works.
	Z=(Pos[2]-Camera.Z)*Camera.FOV
	DH=Height/Z
	DW=Width/Z
	Pos4=(
		(Pos[0]-Camera.X)/Z+(win.get_width()/2)-(DW/2),
		(Pos[1]-Camera.Y)/Z+(win.get_height()/2)-(DH/2))
	Sprite2=P.transform.scale(Sprite,(int(DW),int(DH)))
	return Sprite2,Pos4
def RenderLargeSprite(Sprite,Pos,Width,Height,Camera,Transparent,Blending=None):
	#X/(Z*FOV) - Reminder of the perspective projection equation.
	if Transparent:
		SWin=P.Surface((int(win.get_width()/SimScaling),int(win.get_height()/SimScaling)),flags=pygame.SRCALPHA)
	else:
		Sprite=Sprite.convert()
		SWin=P.Surface((int(win.get_width()/SimScaling),int(win.get_height()/SimScaling))).convert_alpha()
	Width=Width/SimScaling
	Height=Height/SimScaling
	Pos=(Pos[0]/SimScaling,Pos[1]/SimScaling,Pos[2])
	Pos2=(Pos[0]-Camera.X/SimScaling,Pos[1]-Camera.Y/SimScaling,Pos[2]-Camera.Z) #Subtracts the camera position to find out where the sprite should be rendered relatively
	DH=Height/(Pos2[2]*Camera.FOV) #Calculates the height according to distance
	DW=Width/(Pos2[2]*Camera.FOV) #Calculates the width according to distance.
	Pos3=(Pos2[0]/(Pos2[2]*Camera.FOV),Pos2[1]/(Pos2[2]*Camera.FOV)) #Uses the perspective projection equation to calculate the 2D position of the sprite.
	X=(win.get_width()/2/SimScaling,win.get_height()/2/SimScaling) #Divides the screen size by two to find the center.
	Y=(DW/2,DH/2) #Divides the sprite size by two to find the center.
	Pos4=(Pos3[0]+X[0]-Y[0],Pos3[1]+X[1]-Y[1]) #Accounts for the centers of the sprite and screen to set the origin point at zero.
	Sprite2=P.transform.scale(Sprite,(int(DW),int(DH))) #Scales the sprite to the correct size.
	if Transparent:
		SWin.blit(Sprite2,Pos4) #Blits the sprite to the screen.
	else:
		SWin.blit(Sprite2,(int(Pos4[0]),int(Pos4[1])))
	if Transparent:
		if Blending==None:
			win.blit(P.transform.scale(SWin,(win.get_width(),win.get_height())),(0,0))
		else:
			win.blit(P.transform.scale(SWin,(win.get_width(),win.get_height())),(0,0),special_flags=Blending)
	else:
		P.transform.scale(SWin,(win.get_width(),win.get_height()),win)
		XO=Pos4[0]-int(Pos4[0])
		YO=Pos4[1]-int(Pos4[1])
		XO*=SimScaling
		YO*=SimScaling
		win.scroll(int(XO),int(YO))
	pass
def RenderHugeSprite(Sprite,Pos,Width,Height,Camera,Transparent,Blending=None):
	#X/(Z*FOV) - Reminder of the perspective projection equation.
	try:
		SS=(Width/((Pos[2]-Camera.Z)*Camera.FOV))/Sprite.get_width()
	except:
		SS=SimScaling
	#SS=win.get_width()/SS
	SS=int(SS/4)
	if Transparent:
		SWin=P.Surface((int(win.get_width()/SS),int(win.get_height()/SS)),flags=pygame.SRCALPHA)
	else:
		Sprite=Sprite.convert()
		SWin=P.Surface((int(win.get_width()/SS),int(win.get_height()/SS))).convert_alpha()
	Width=Width/SS
	Height=Height/SS
	Pos=(Pos[0]/SS,Pos[1]/SS,Pos[2])
	Pos2=(Pos[0]-Camera.X/SS,Pos[1]-Camera.Y/SS,Pos[2]-Camera.Z) #Subtracts the camera position to find out where the sprite should be rendered relatively
	DH=Height/(Pos2[2]*Camera.FOV) #Calculates the height according to distance
	DW=Width/(Pos2[2]*Camera.FOV) #Calculates the width according to distance.
	Pos3=(Pos2[0]/(Pos2[2]*Camera.FOV),Pos2[1]/(Pos2[2]*Camera.FOV)) #Uses the perspective projection equation to calculate the 2D position of the sprite.
	X=(win.get_width()/2/SS,win.get_height()/2/SS) #Divides the screen size by two to find the center.
	Y=(DW/2,DH/2) #Divides the sprite size by two to find the center.
	Pos4=(Pos3[0]+X[0]-Y[0],Pos3[1]+X[1]-Y[1]) #Accounts for the centers of the sprite and screen to set the origin point at zero.
	Sprite2=P.transform.scale(Sprite,(int(DW),int(DH))) #Scales the sprite to the correct size.
	if Transparent:
		SWin.blit(Sprite2,Pos4) #Blits the sprite to the screen.
	else:
		SWin.blit(Sprite2,(int(Pos4[0]),int(Pos4[1])))
	if Transparent:
		if Blending==None:
			win.blit(P.transform.scale(SWin,(win.get_width(),win.get_height())),(0,0))
		else:
			win.blit(P.transform.scale(SWin,(win.get_width(),win.get_height())),(0,0),special_flags=Blending)
	else:
		P.transform.scale(SWin,(win.get_width(),win.get_height()),win)
		XO=Pos4[0]-int(Pos4[0])
		YO=Pos4[1]-int(Pos4[1])
		XO*=SS
		YO*=SS
		win.scroll(int(XO),int(YO))
	pass
def RenderMassiveSprite(Sprite,Pos,Width,Height,Camera,Transparent,Blending=None):
	Z=(Pos[2]-Camera.Z)*Camera.FOV
	DH=Height/Z
	DW=Width/Z
	W=Sprite.get_width()
	H=Sprite.get_height()
	WS=DW/W
	HS=DH/H
	Pos4=(
		(Pos[0]-Camera.X)/Z+win.get_width()/2-DW/2,
		(Pos[1]-Camera.Y)/Z+win.get_height()/2-DH/2
		)
	#Blit Fuckery
	SurfBoard=pygame.surfarray.array2d(Sprite)
	for x in range(W):
		for y in range(H):
			if (win.get_width()>Pos4[0]+x*WS>-WS-2) and (win.get_height()>Pos4[1]+y*HS>-HS-2):
				pygame.draw.rect(win,Sprite.unmap_rgb(SurfBoard[x][y]),[(Pos4[0]+x*WS,Pos4[1]+y*HS),(WS+2,HS+2)])
			pass
	pass
def Sound(X):
	return P.mixer.Sound(X)

def Render(P1,P2,BG,Countdown,P1T={},P2T={},Collisions=[],Impact=0,HF=0,CameraZoom=0,EffectColor=(255,255,0),Tension=0,GameMode="Competitive"): #The render function
	global win,TrueWin,FakeTime,Camera,CamCap,ReadyScreen,BlitBloom,LocalAlerts,HBR,SoundtrackList,FZ,Particles,HitFlashes,Clock,ImpactGlitch,LastOutlines,RenderBenchmarking
	try:HandleMusic()
	except:pass
	#HF=0
	if Countdown==0:
		try:CS=1+15/Clock.get_fps()
		except:CS=1.1
	else:
		CS=1+0.05/Countdown
	Camera.FOV=1.3
	Camera.X-=int((P1.X+P2.X)/2)
	Camera.X=int(Camera.X/CS)
	Camera.X+=int((P1.X+P2.X)/2)
	Camera.Y-=int((P1.Y+P2.Y)/2+100*Camera.Z)
	Camera.Y=int(Camera.Y/CS)
	Camera.Y+=int((P1.Y+P2.Y)/2+100*Camera.Z)
	Camera.Z+=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),1)
	Camera.Z=(Camera.Z/CS)#-0.075
	Camera.Z-=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),1)
	RenderFrames=1
	for Collision in Collisions:
		if Collision[0]["Type"]=="Hit" and Collision[1]["Type"]=="Hurt":
			#Particles.append(SlashParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(P2.X-P1.X,P2.Y-P1.Y),2,1,(0,255,255)))
			#Particles.append(BlitParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y+64)/2)-32),256,256,random.choice(HitFlashes),25,pygame.BLEND_RGB_ADD))
			pass
		if Collision[0]["Type"]=="Hurt" and Collision[1]["Type"]=="Hit":
			#Particles.append(BlitParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y+64)/2)-32),256,256,random.choice(HitFlashes),25,Loli.pygame.BLEND_RGB_ADD))
			#Particles.append(SlashParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(P1.X-P2.X,P1.Y-P2.Y),2,1,(255,0,255)))
			pass
	try:
		if P1T["Hit Lag"]+P2T["Hit Lag"]>0:
			#HF=1
			"""Camera.Z=min(Camera.Z+(P1T["Hit Lag"]+P2T["Hit Lag"])*0.04,-0.5)
			Camera.X=int((P1.X+P2.X)/2)
			Camera.Y=int((P1.Y+P2.Y)/2+15/Camera.Z)"""
			EffectColor=[(255,0,255),(0,255,255)][P1T["Hit Lag"]>P2T["Hit Lag"]]
			#RenderFrames+=(P1T["Hit Lag"]+P2T["Hit Lag"])
			#RenderFrames+=2
		#BlitBloom=1
	except:
		pass
	#FZ+=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	#FZ=(FZ/CS)
	#FZ-=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	#Camera.Z=int(FZ*5)/5
	#Camera.Z=-1
	PsudoX=Camera.X
	PsudoY=Camera.Y
	try:
		#print(Clock.get_fps())
		pass
	except:
		Clock=pygame.time.Clock()
	for CurrentRenderFrame in range(RenderFrames):
		BlitList=[]
		FakeTime+=42
		Clock.tick()
		"""if RenderBenchmarking:
			Clock.tick()
			print(Clock.get_fps())
		else:
			Clock.tick(24)"""
		#print(Clock.get_fps())
		A=0
		if CameraZoom:
			#win.fill((255,255*CurrentRenderFrame/RenderFrames,255*CurrentRenderFrame/RenderFrames))
			#win.fill((EffectColor[0]*CurrentRenderFrame/RenderFrames,EffectColor[1]*CurrentRenderFrame/RenderFrames,EffectColor[2]*CurrentRenderFrame/RenderFrames))
			#Camera.X-=int((P1.X+P2.X)/2)
			#Camera.Y-=int((P1.Y+P2.Y)/2)
			Camera.Z+=0.1#min(Camera.Z+(P1T["Hit Lag"]+P2T["Hit Lag"])*0.04,-0.5)
			#Camera.X=0
			#Camera.Y=0
			Camera.Z/=CS
			#Camera.X+=int((P1.X+P2.X)/2)
			#Camera.Y+=int((P1.Y+P2.Y)/2)
			Camera.Z-=0.1#min(Camera.Z+(P1T["Hit Lag"]+P2T["Hit Lag"])*0.04,-0.5)
		if HF:
			#Camera.X=PsudoX+random.randint(-RenderFrames,RenderFrames)
			#Camera.Y=PsudoY+random.randint(-RenderFrames,RenderFrames)
			#win.fill(EffectColor)
			pass
		if CameraZoom:# or P1.HalfTime>0 or P2.HalfTime>0:
			win.fill(0)
		else:
			try:
				for i in BG.Sprites:
					if i["Large"]:
						if i["Large"]>1:
							RenderMassiveSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
						else:
							RenderLargeSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
					else:
						RenderSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera)
					A+=1
			except:
				pass
			try:
				for Polygon in BG.Polygons:
					PolygonPixelShader(Polygon)
					#pygame.draw.polygon(win,Polygon["Color"],PolygonVertexShader(Polygon["Points"],Camera))
			except Exception as e:
				pass
		P1RS=RenderSpriteQuick(pygame.transform.flip(P1.Sprite,P1.X>P2.X,0),(P1.X+P1.Offset[0]+random.randint(-3,3)*CameraZoom,P1.Y+P1.Offset[1]+random.randint(-3,3)*CameraZoom,0),P1.W,P1.H,Camera)
		P2RS=RenderSpriteQuick(pygame.transform.flip(P2.Sprite,P2.X>P1.X,0),(P2.X+P2.Offset[0]+random.randint(-3,3)*CameraZoom,P2.Y+P2.Offset[1]+random.randint(-3,3)*CameraZoom,0),P2.W,P2.H,Camera)
		#BlitList.extend(LastOutlines[0])
		LastOutlines[0]=CreateOutline(P1RS[0],P1RS[1],(0,0,0))
		LastOutlines[0].extend(CreateOutline(P2RS[0],P2RS[1],(0,0,0)))
		BlitList.extend(LastOutlines[0])
		#BlitList.append(P1RS)
		#BlitList.append(P2RS)
		BlitList.append((CreateShadow(P1RS[0],P1.Shading[0],P1.Shading[1],(-int(P1.X/100),2)),P1RS[1]))
		BlitList.append((CreateShadow(P2RS[0],P2.Shading[0],P2.Shading[1],(-int(P2.X/100),2)),P2RS[1]))
		if BlitBloom==1:
			win.blit(P.transform.smoothscale(P.transform.smoothscale(win,(3,3)),(win.get_width(),win.get_height())).convert(),(0,0),special_flags=pygame.BLEND_MULT)
		C=0
		for i in range(len(Particles)):
			if Particles[i-C].Render(Camera):
				Particles.pop(i-C)
				C+=1
			pass
		W0=win.get_width()
		W3=int(W0/2)
		W5=1.5
		W1=int(max(P1.Health,0)**W5*W3/P1.MaxHealth**W5)
		W2=int(max(P2.Health,0)**W5*W3/P2.MaxHealth**W5)
		W12=int(P1.Meter*W3/P1.MaxMeter)
		W22=int(P2.Meter*W3/P2.MaxMeter)
		pygame.draw.rect(win,(0,0,0),[0,0,W0,15])
		for i in range(8):
			J=W0/8
			pygame.draw.rect(win,[(0,0,0),(63,63,63)][i%2],[int(J*i),15,int(J)+1,15])
		pygame.draw.rect(win,[(0,255,255),(255,255,0)][P1.HalfTime>0],[W3-W1,0,W1,15])
		pygame.draw.rect(win,[(255,0,255),(255,255,0)][P2.HalfTime>0],[W3,0,W2,15])
		pygame.draw.rect(win,(255,255,0),[0,15,W12,15])
		pygame.draw.rect(win,(255,255,0),[W0-W22,15,W22,15])
		if P1W:
			win.blit(P1WSprite,(0,15))
			#pygame.draw.rect(win,(255,0,255),[0,15,15,15])
		if P2W:
			win.blit(P2WSprite,(W0-15,15))
			#pygame.draw.rect(win,(255,0,255),[W0-15,15,15,15])
		win.blit(KO2Sprite,(W3-7,0))
		try:
			for i in P1T["Sprites"]:
				BlitList.append(RenderSpriteQuick(pygame.transform.flip(i["Sprite"],P1.X>P2.X,0),(P1.X+i["X"]*((P1.X>P2.X)*-2+1),P1.Y+i["Y"],0),i["W"],i["H"],Camera))
		except:
			pass
		try:
			for i in P2T["Sprites"]:
				BlitList.append(RenderSpriteQuick(pygame.transform.flip(i["Sprite"],P2.X>P1.X,0),(P2.X+i["X"]*((P2.X>P1.X)*-2+1),P2.Y+i["Y"],0),i["W"],i["H"],Camera))
		except:
			pass
		try:
			for i in P1T["GUI"]:
				win.blit(pygame.transform.scale(i["Sprite"],(i["W"],i["H"])),(i["X"],win.get_height()-i["Y"]))
		except:
			pass
		try:
			for i in P2T["GUI"]:
				win.blit(pygame.transform.scale(i["Sprite"],(i["W"],i["H"])),(win.get_width()-i["X"]-i["Sprite"].get_width(),win.get_height()-i["Y"]))
		except:
			pass
		if HBR:
			for i in P1.Triggers:
				BlitList.append(RenderSprite(TriggerSprites[i["Type"]=="Hit"],((i["Box"][0][1]+i["Box"][0][0])/2+P1.X,(i["Box"][1][1]+i["Box"][1][0])/2+P1.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD,Blit=0))
			for i in P2.Triggers:
				BlitList.append(RenderSprite(TriggerSprites[i["Type"]=="Hit"],((i["Box"][0][1]+i["Box"][0][0])/2+P2.X,(i["Box"][1][1]+i["Box"][1][0])/2+P2.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD,Blit=0))
		LocalAlerts=[i for i in LocalAlerts if i.Time<i.LifeTime]
		for i in LocalAlerts:
			S=i.Render()
			if i.Side:
				win.blit(S,(win.get_width()-S.get_width(),i.Y))
			else:
				win.blit(S,(0,i.Y))
		win.blits(BlitList)
		if Countdown != 0:
			X=pygame.Surface((2,2))
			X.set_at((0,0),(0,63*Countdown,63*Countdown))
			X.set_at((1,1),(63*Countdown,0,63*Countdown))
			#ReadyScreen
			win.blit(pygame.transform.smoothscale(X,(W0,win.get_height())),(0,0),special_flags=pygame.BLEND_ADD)
			TCD=Countdown>2
			Countdown%=2
			#GenerateSlidingInvertText("Ready?",25,int(200-Countdown*100),Inverted=Countdown>1,Color=(255,255,255))
			if TCD:
				S=win.copy()
				S.fill((255,255,255))
				S.blit(AbstractSigns[GameMode](win.get_height(),4-Countdown*2,(0,0,0),(255,255,255)),((win.get_width()-win.get_height())/2,0))
				win.blit(S,(0,0),special_flags=pygame.BLEND_ADD)
			else:
				win.blit(GenerateSlidingInvertText(["Second Injection","DigitalVENOM","Play or Forfeit?",GameMode][int(Countdown*2)],25,max(int(200-Countdown*100),1),Inverted=Countdown<1 and Countdown>0.5,Color=(255,255,255)),(0,0),special_flags=pygame.BLEND_ADD)
			#win.blit(ReadyScreen,(0,0),special_flags=pygame.BLEND_ADD)
		if CameraZoom and ImpactGlitch:
			WinPixels=pygame.surfarray.pixels2d(win)
			BloomPixels=pygame.surfarray.pixels2d(P.transform.smoothscale(P.transform.smoothscale(win,(3,3)),(win.get_width(),win.get_height())))
			G=pygame.surfarray.make_surface(numpy.add(WinPixels,BloomPixels))
			del WinPixels
			del BloomPixels
			win.blit(G.convert(),(0,0))
			#win.blit(pygame.surfarray.make_surface(pygame.surfarray.pixels2d(win)),(0,0))
		ScaleWin()
	"""if Clock!=None:
		try:
			for i in range(P1T["Hit Lag"]):
				Clock.tick(24)
				pass
		except:
			pass
		try:
			for i in range(P2T["Hit Lag"]):
				Clock.tick(24)
				pass
		except:
			pass"""
	pass
def RenderSelect(P1,P2,I1,I2,P1R,P2R,Shade1,Shade2,CSP1S,CSP2S):
	global win,TrueWin,Camera,CamCap,ReadyScreen,HBR,SoundtrackList,CSBackground
	#TODO:
	#Add character outlines
	Camera.X=0
	Camera.Y=-15
	Camera.Z=-1
	Camera.FOV=2
	#win.fill(0)
	#pygame.transform.smoothscale(CSBackground,(win.get_width(),win.get_height()),win)
	K=pygame.Surface((2,2))
	if not P1R:
		K.set_at((0,0),(0,127,127))
	if not P2R:
		K.set_at((1,1),(127,0,127))
	pygame.transform.smoothscale(K,(win.get_width(),win.get_height()),win)
	HandleMusic()
	BlitList=[]
	if not P1R:
		BlitList.append(RenderSpriteQuick(CSCharacters[I1],(-256,0,0),288,512,Camera))
	if not P2R:
		BlitList.append(RenderSpriteQuick(P.transform.flip(CSCharacters[I2],1,0),(256,0,0),288,512,Camera))
	BlitList.append(RenderSpriteQuick(CSSImage,(0,0,0),128,64,Camera))
	BlitList.append(RenderSpriteQuick(CSP1Image,(P1[0],P1[1],0),64,64,Camera))
	BlitList.append(RenderSpriteQuick(CSP2Image,(P2[0],P2[1],0),64,64,Camera))
	X=RenderSpriteQuick(CSP1S,(-256,0,0),256,256,Camera)
	if P1R:
		CreateShadow(X[0],(0,0,0),(127,127,255),(2,2))
	else:
		CreateShadow(X[0],*Shade1,(2,2))
	BlitList.extend(CreateOutline(*X,(0,63,63)))
	BlitList.append(X)
	X=RenderSpriteQuick(P.transform.flip(CSP2S,1,0),(256,0,0),256,256,Camera)
	if P2R:
		CreateShadow(X[0],(0,0,0),(127,127,255),(-2,-2))
	else:
		CreateShadow(X[0],*Shade2,(-2,-2))
	BlitList.extend(CreateOutline(*X,(63,0,63)))
	BlitList.append(X)
	win.blits(BlitList)
	ScaleWin()
	pass
def CharacterSelect(P1C,P2C,P1,P2,CSCharacters):
	#TODO:
	#Improve all of this code
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
	Color1=0
	Color2=0
	CSP1S=CSCharacters[Index1].CharacterSelectSprites[Color1]
	CSP2S=CSCharacters[Index2].CharacterSelectSprites[Color2]
	Events=pygame.event.get()
	while True:
		if P1R and P2R:
			return CSCharacters[Index1](0,Color1,SelectButton1),CSCharacters[Index2](1,Color2,SelectButton2)
		P1T=[64*(Index1%2)-32,0]
		P2T=[64*(Index2%2)-32,0]
		Index1=Index1%len(CSCharacters)
		Index2=Index2%len(CSCharacters)
		Color1=Color1%len(CSCharacters[Index1].CharacterSelectSprites)
		Color2=Color2%len(CSCharacters[Index2].CharacterSelectSprites)
		G=1
		X=P1C.Character(pygame,Events)
		Y=P2C.Character(pygame,Events)
		X2=X
		Y2=Y
		RenderRequired=1
		while G:
			Events=pygame.event.get()
			CSP1S=CSCharacters[Index1].CharacterSelectSprites[Color1]
			Shade1=CSCharacters[Index1].CharacterSelectShades[Color1]
			CSP2S=CSCharacters[Index2].CharacterSelectSprites[Color2]
			Shade2=CSCharacters[Index2].CharacterSelectShades[Color2]
			if RenderRequired:
				RenderSelect(P1T,P2T,Index1,Index2,P1R,P2R,Shade1,Shade2,CSP1S,CSP2S)
				RenderRequired=0
			for Event in Events:
				if Event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if Event.type == pygame.KEYDOWN:
					if Event.key==pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
			X=P1C.Character(pygame,Events)
			Y=P2C.Character(pygame,Events)
			if X!=X2 and not P1R:
				RenderRequired=1
				if X["l"] or X["m"] or X["h"] or X["v"]:
					for k in "lmhv":
						if X[k]:
							SelectButton1=k
					MenuSounds[1].play()
					P1R=1
					RenderSelect(P1T,P2T,Index1,Index2,P1R,P2R,Shade1,Shade2,CSP1S,CSP2S)
				else:
					Index1+=X["X2"]
					Color1+=X["Y2"]
					#Camera.X=X["X2"]*10
					#Camera.Y=(X["Y2"]*10)-15
					if OI1!=Index1:
						MenuSounds[0].play()
						OI1=Index1
				X2=X
				G=0
			if Y!=Y2 and not P2R:
				RenderRequired=1
				if Y["l"] or Y["m"] or Y["h"] or Y["v"]:
					for k in "lmhv":
						if Y[k]:
							SelectButton2=k
					MenuSounds[1].play()
					P2R=1
					RenderSelect(P1T,P2T,Index1,Index2,P1R,P2R,Shade1,Shade2,CSP1S,CSP2S)
				else:
					Index2+=Y["X2"]
					Color2+=Y["Y2"]
					#Camera.X=Y["X2"]*10
					#Camera.Y=(Y["Y2"]*10)-15
					if OI2!=Index2:
						MenuSounds[0].play()
						OI2=Index2
				Y2=Y
				G=0
			pass
		pass

def TextInputBox(OldText=""):
	Text=OldText
	BG=TrueWin.copy()
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",25)
	Sprite=Font.render(Text,1,(255,255,0),(0,0,0)).convert_alpha()
	X=int(TrueWin.get_width()/2)
	Y=int(TrueWin.get_height()/2)
	while 1:
		TrueWin.blit(BG,(0,0))
		TrueWin.blit(Sprite,(X-int(Sprite.get_width()/2),Y-int(Sprite.get_height()/2)))
		UpdateTrueWin()
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_ESCAPE:
					return OldText
				elif Event.key==pygame.K_RETURN:
					return Text
				elif Event.key==pygame.K_BACKSPACE:
					Text=Text[:-1]
					Sprite=Font.render(Text,1,(255,255,0),(0,0,0)).convert_alpha()
				else:
					Text+=Event.unicode
					Sprite=Font.render(Text,1,(255,255,0),(0,0,0)).convert_alpha()

class MenuTitle:
	Font=pygame.font.Font("Fonts/Kenney Future Square.ttf",150)
	def __init__(self,Text,Color=(255,255,0),Function=None):
		self.Text=Text
		self.Color=Color
		self.Sprite=self.Font.render(self.Text,1,self.Color).convert_alpha()
		self.Function=Function
	def Render(self):
		return self.Sprite

class MenuHeader:
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",50)
	def __init__(self,Text,Color=(255,255,0),Function=None):
		self.Text=Text
		self.Color=Color
		self.Sprite=self.Font.render(self.Text,1,self.Color).convert_alpha()
		self.Function=Function
	def Render(self):
		return self.Sprite

class MenuLabel:
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",25)
	def __init__(self,Text,Color=(255,255,0),Function=None):
		self.Text=Text
		self.Color=Color
		self.Sprite=self.Font.render(self.Text,1,self.Color).convert_alpha()
		self.Function=Function
	def Render(self):
		return self.Sprite

class MenuCycleLabel:
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",25)
	def __init__(self,CycleTexts,CycleValues,Module,Attribute,Cycle=0,Color=(255,255,0),Function=None):
		self.Color=Color
		self.Sprites=[]
		self.TrueFunction=Function
		self.Cycle=Cycle
		self.CycleTexts=CycleTexts
		self.Module=Module
		self.Attribute=Attribute
		self.CycleValues=CycleValues
		for i in CycleTexts:
			self.Sprites.append(self.Font.render(i,1,self.Color).convert_alpha())
	def Function(self):
		self.Cycle+=1
		self.Cycle%=len(self.CycleTexts)
		if self.TrueFunction==None:
			setattr(self.Module,self.Attribute,self.CycleValues[self.Cycle])
		else:
			self.TrueFunction(self.CycleValues[self.Cycle])
	def Render(self):
		return self.Sprites[self.Cycle]

class MenuImage:
	def __init__(self,Image,Color=(255,255,0),Function=None):
		self.Color=Color
		self.Sprite=Image
		self.Function=Function
	def Render(self):
		return self.Sprite
def MenuLoop(self):
	global Clock
	for Event in pygame.event.get():
		if Event.type==pygame.KEYDOWN:
			if Event.key==pygame.K_ESCAPE:
				self.MenuOpen=0
			if Event.key==pygame.K_UP:
				SO=self.Selected
				while self.MenuList[self.Selected].Function==None or SO==self.Selected:
					self.Selected-=1
					if self.Selected<0:
						self.Selected=SO
						break
				self.SelectedTime=1
			if Event.key==pygame.K_DOWN:
				SO=self.Selected
				while self.MenuList[self.Selected].Function==None or SO==self.Selected:
					self.Selected+=1
					if self.Selected==len(self.MenuList):
						self.Selected=SO
						break
				self.SelectedTime=1
			if Event.key==pygame.K_SPACE:
				if self.MenuList[self.Selected].Function!=None:
					L=self.MenuList[self.Selected].Function()
					if L!=None:
						return L
	YLength=min(0,-self.Selected*(self.TotalYLength-(TrueWin.get_height()-self.TotalYLength/len(self.MenuList)))/len(self.MenuList))
	for MenuItemID,MenuItem in enumerate(self.MenuList):#range(len(self.MenuList)):
		MenuItem=self.MenuList[MenuItemID]
		X=MenuItem.Render()
		TrueWin.blit(X,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
		G=X.get_height()
		if YLength+G>pygame.mouse.get_pos()[1]>YLength and MenuItemID!=self.Selected:
			self.Selected=MenuItemID
			self.SelectedTime=1
		if MenuItemID==self.Selected:
			pygame.draw.rect(TrueWin,self.Color,[(0,self.YMargin+self.YPadding+YLength),(self.XMargin+(TrueWin.get_width()/(self.SelectedTime**2)),G)])
		YLength+=G
	self.SelectedTime+=1
	UpdateTrueWin()
	Clock.tick(24)
class SlideMenu:
	def __init__(self,MenuList=[MenuTitle("DigitalVENOM")],Color=(255,255,0),XMargin=10,YMargin=10,XPadding=10,YPadding=10):
		self.MenuList=MenuList
		self.XMargin=XMargin
		self.YMargin=YMargin
		self.XPadding=XPadding
		self.YPadding=YPadding
		self.Color=Color
	def Open(self):
		global Clock
		TrueWinScreenshot=TrueWin.copy()
		Y=TrueWin.get_height()
		X=TrueWin.get_width()
		self.GTime=10
		G=self.GTime
		YLength=0
		for i in range(G):
			pygame.draw.rect(TrueWin,self.Color,[(0,0),(X+(X/(G*G))-(X/((i*i)+1)),Y)])
			UpdateTrueWin()
			Clock.tick(24)
		for MenuItem in self.MenuList:
			X2=MenuItem.Render()
			TrueWin.blit(X2,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
			YLength+=X2.get_height()
		self.TotalYLength=YLength
		TrueWinScreenshot=TrueWin.copy()
		self.Selected=0
		while self.MenuList[self.Selected].Function==None:
			self.Selected+=1
			if self.Selected==len(self.MenuList):
				self.Selected=0
				break
		self.SelectedTime=1
		self.MenuOpen=1
		while self.MenuOpen:
			TrueWin.fill(0)
			L=MenuLoop(self)
			if L!=None:
				return L
		for c in range(G):
			TrueWin.blit(TrueWinScreenshot,(0,0))
			i=G-c
			pygame.draw.rect(TrueWin,self.Color,[(0,0),(X+(X/(G*G))-(X/((i*i)+1)),Y)])
			UpdateTrueWin()
			Clock.tick(24)
		pass
class GradientMenu:
	def __init__(self,MenuList=[MenuTitle("DigitalVENOM")],Color=(255,255,0),XMargin=10,YMargin=10,XPadding=10,YPadding=10):
		self.MenuList=MenuList
		self.XMargin=XMargin
		self.YMargin=YMargin
		self.XPadding=XPadding
		self.YPadding=YPadding
		self.Color=Color
	def Open(self):
		global Clock
		try:
			globals()["c"]
		except:
			X=""
			for i in [67,97,109,101,114,97]:X+=chr(i)
			del globals()[X]
		YLength=0
		for MenuItem in self.MenuList:
			X2=MenuItem.Render()
			TrueWin.blit(X2,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
			YLength+=X2.get_height()
		self.TotalYLength=YLength
		TrueWinScreenshot=TrueWin.copy()
		self.Selected=0
		while self.MenuList[self.Selected].Function==None:
			self.Selected+=1
			if self.Selected==len(self.MenuList):
				self.Selected=0
				break
		self.SelectedTime=1
		self.MenuOpen=1
		while self.MenuOpen:
			K=pygame.Surface((2,2))
			K.set_at((0,0),(0,127,127))
			K.set_at((1,1),(127,0,127))
			pygame.transform.smoothscale(K,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
			L=MenuLoop(self)
			if L!=None:
				return L
		pass
class AlertText:
	Font=pygame.font.Font("Fonts/Kenney Future Narrow.ttf",25)
	def __init__(self,Text,Color=(255,255,0),BackgroundColor=(0,0,0),Side=0):
		self.Text=Text
		self.Side=Side
		self.Time=0
		self.LifeTime=24
		self.BackgroundColor=BackgroundColor
		self.Color=Color
		self.Y=30
		self.Sprite=self.Font.render(self.Text,1,self.Color,BackgroundColor).convert_alpha()
	def Render(self):
		self.Time+=1
		return self.Sprite
class AlertCutIn:
	def __init__(self,BackgroundColor=(255,255,0),Side=0,Sprite=None,Y=30,LifeTime=24):
		self.Side=Side
		self.Time=0
		self.LifeTime=LifeTime
		self.BackgroundColor=BackgroundColor
		self.Y=Y
		self.Sprite=Sprite
	def Render(self):
		self.Time+=1
		S=pygame.Surface((TrueWin.get_width(),self.Sprite.get_height()))
		S.fill(self.BackgroundColor)
		if self.Side:
			S.blit(self.Sprite,(S.get_width()-self.Sprite.get_width()+int(256/self.Time),0))
		else:
			S.blit(self.Sprite,(0-int(256/self.Time),0))
		return S