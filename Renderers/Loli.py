import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import pygame,random,math,numpy
from os import walk
#Here we define some basic variables.
P=pygame
pygame.mixer.pre_init()
pygame.init()
FakeTime=0
Clock=pygame.time.Clock()
#win=pygame.Surface((1366,768))
win=pygame.Surface((683,384))
FZ=-1
BlitBloom=0
win.set_alpha(None)
ImpactGlitch=1
TrueWin=pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
TrueWin.convert()
ReadyScreen=pygame.image.load("Sprites/Game Start.png").convert_alpha()
CamCap=(win.get_width()*0.9)
P1W=0
P2W=0
HBR=0
pygame.mixer.set_num_channels(32)
SimScaling=4
TriggerSprite=pygame.image.load("Sprites/Trigger.png").convert()
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
pygame.mixer.music.load(random.choice(SoundtrackList))
pygame.mixer.music.play()
pygame.mixer.music.queue(random.choice(SoundtrackList))
#The above commented code began crashing the game, this has now been fixed.
Particles=[]
def FakeTimeFunction():
	global FakeTime
	return FakeTime

pygame.time.get_ticks=FakeTimeFunction

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
		X/=-Camera.Z/Camera.FOV
		Y/=-Camera.Z/Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		if win.get_width()>(int(X+self.XV*TT)>0 and win.get_height()>int(Y+self.YV*TT+TT**2))>0:
			pygame.draw.line(win,self.Color,(X+self.XV*TT,Y+self.YV*TT+TT**2),(X+self.XV*T2,Y+self.YV*T2+T2**2),5)
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
		X/=-Camera.Z/Camera.FOV
		Y/=-Camera.Z/Camera.FOV
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
		X/=-Camera.Z/Camera.FOV
		Y/=-Camera.Z/Camera.FOV
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
		X/=-Camera.Z/Camera.FOV
		Y/=-Camera.Z/Camera.FOV
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
		X/=-Camera.Z/Camera.FOV
		Y/=-Camera.Z/Camera.FOV
		X+=win.get_width()/2
		Y+=win.get_height()/2
		try:
			if win.get_width()>(int(X+self.XV*TT)>0 and win.get_height()>int(Y+self.YV*TT+TT**2))>0:
				pygame.draw.circle(win,self.Color,(int(X+self.XV*TT),int(Y+self.YV*TT+TT**2)),int(10*T2))
				pygame.draw.circle(win,(255,255,255),(int(X+self.XV*TT),int(Y+self.YV*TT+TT**2)),int(8*T2))
		except:
			pass
		return (pygame.time.get_ticks()-self.StartTime)/1000>self.Life
class LoliCamera: #Defines the camera object.
	def __init__(self,X,Y,Z,FOV):
		self.X=X
		self.Y=Y
		self.Z=Z
		self.FOV=FOV
Camera=LoliCamera(0,-15,-1,1)

def UpdateTrueWin():
	pygame.display.flip()

def ScaleWin():
	pygame.transform.scale(win,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	UpdateTrueWin()

def HandleMusic():
	global SoundtrackList
	if P.mixer.music.get_busy()==0:
		P.mixer.music.load(random.choice(SoundtrackList))
		P.mixer.music.play()
		P.mixer.music.queue(random.choice(SoundtrackList))

def CreateOutline(Sprite,Position):
	Mask=pygame.mask.from_surface(Sprite)
	Surface=Mask.to_surface(setcolor=(0,0,0),unsetcolor=(255,255,255))
	Surface.set_colorkey((255,255,255))
	return [
	(Surface,(Position[0]+1,Position[1])),
	(Surface,(Position[0]-1,Position[1])),
	(Surface,(Position[0],Position[1]+1)),
	(Surface,(Position[0],Position[1]-1)),
	]

def RenderSprite(Sprite,Pos,Width,Height,Camera,Blending=None,Smooth=0,Blit=1): #Defines the sprite render function.
	#X/(Z*FOV) - Reminder of the perspective projection equation.
	Pos2=(Pos[0]-Camera.X,Pos[1]-Camera.Y,Pos[2]-Camera.Z) #Subtracts the camera position to find out where the sprite should be rendered relatively
	DH=Height/(Pos2[2]*Camera.FOV) #Calculates the height according to distance
	DW=Width/(Pos2[2]*Camera.FOV) #Calculates the width according to distance.
	Pos3=(Pos2[0]/(Pos2[2]*Camera.FOV),Pos2[1]/(Pos2[2]*Camera.FOV)) #Uses the perspective projection equation to calculate the 2D position of the sprite.
	X=(win.get_width()/2,win.get_height()/2) #Divides the screen size by two to find the center.
	Y=(DW/2,DH/2) #Divides the sprite size by two to find the center.
	Pos4=(Pos3[0]+X[0]-Y[0],Pos3[1]+X[1]-Y[1]) #Accounts for the centers of the sprite and screen to set the origin point at zero.
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
	Pos2=(Pos[0]-Camera.X,Pos[1]-Camera.Y,Pos[2]-Camera.Z) #Subtracts the camera position to find out where the sprite should be rendered relatively
	DH=Height/(Pos2[2]*Camera.FOV) #Calculates the height according to distance
	DW=Width/(Pos2[2]*Camera.FOV) #Calculates the width according to distance.
	Pos3=(Pos2[0]/(Pos2[2]*Camera.FOV),Pos2[1]/(Pos2[2]*Camera.FOV)) #Uses the perspective projection equation to calculate the 2D position of the sprite.
	X=(win.get_width()/2,win.get_height()/2) #Divides the screen size by two to find the center.
	Y=(DW/2,DH/2) #Divides the sprite size by two to find the center.
	W=Sprite.get_width()
	H=Sprite.get_height()
	WS=DW/W
	HS=DH/H
	Pos4=(Pos3[0]+X[0]-Y[0],Pos3[1]+X[1]-Y[1]) #Accounts for the centers of the sprite and screen to set the origin point at zero.
	SurfBoard=pygame.surfarray.array2d(Sprite)
	for x in range(W):
		for y in range(H):
			#print([(Pos4[0]+x*(DW/Width),Pos4[1]+y*(DH/Height)),(Pos4[0]+(x+1)*(DW/Width),Pos4[1]+(y+1)*(DH/Height))])
			if (win.get_width()>Pos4[0]+x*WS>-WS-2) and (win.get_height()>Pos4[1]+y*HS>-HS-2):
				pygame.draw.rect(win,Sprite.unmap_rgb(SurfBoard[x][y]),[(Pos4[0]+x*WS,Pos4[1]+y*HS),(WS+2,HS+2)])
			pass
	pass
def Sound(X):
	return P.mixer.Sound(X)
def Render(P1,P2,BG,Countdown,P1T={},P2T={},Collisions=[],Impact=0): #The render function
	global win,TrueWin,FakeTime,Camera,CamCap,ReadyScreen,BlitBloom,HBR,SoundtrackList,FZ,Particles,Clock,ImpactGlitch
	HandleMusic()
	try:
		for i in P1T["Sounds"]:
			i.play()
	except:
		pass
	try:
		for i in P2T["Sounds"]:
			i.play()
	except:
		pass
	#win.fill(0)
	HF=0
	CS=1.5
	Camera.X-=int((P1.X+P2.X)/2)
	Camera.X=int(Camera.X/CS)
	Camera.X+=int((P1.X+P2.X)/2)
	Camera.Y-=int((P1.Y+P2.Y)/2+100*Camera.Z)
	Camera.Y=int(Camera.Y/CS)
	Camera.Y+=int((P1.Y+P2.Y)/2+100*Camera.Z)
	Camera.Z+=min(max(0.5,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	Camera.Z=(Camera.Z/CS)-0.075
	Camera.Z-=min(max(0.5,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	RenderFrames=1
	try:
		if P1T["Hit Lag"]+P2T["Hit Lag"]>0:
			Camera.Z=min(Camera.Z+(P1T["Hit Lag"]+P2T["Hit Lag"])*0.04,-0.5)
			RenderFrames+=(P1T["Hit Lag"]+P2T["Hit Lag"])
			HF=1
			EffectColor=[(255,0,255),(0,255,255)][P1T["Hit Lag"]>P2T["Hit Lag"]]
			Camera.X=int((P1.X+P2.X)/2)
			Camera.Y=int((P1.Y+P2.Y)/2+15/Camera.Z)
		#BlitBloom=1
	except:
		pass
	if HF:
		Particles.append(StarParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-8,8),random.randint(32,64)),random.randint(1,5)/10,0.6,(255,255,255)))
		for i in range(min(RenderFrames*5,50)):
			Particles.append(LineParticle((int((P1.X+P2.X)/2)+random.randint(-64,64),int((P1.Y+P2.Y)/2)-32+random.randint(-64,64)),(random.randint(-64,64),random.randint(-64,64)),random.randint(5,20)/10,0.6,EffectColor))
		for i in range(min(RenderFrames*5,50)):
			Particles.append(CircleParticle((int((P1.X+P2.X)/2)+random.randint(-64,64),int((P1.Y+P2.Y)/2)-32+random.randint(-64,64)),(random.randint(-64,64),random.randint(-64,64)),random.randint(5,20)/10,0.6,EffectColor))
		#for i in range(min(RenderFrames,10)):
		#	Particles.append(SpikeParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-5,5),random.randint(-5,5)),random.randint(1,5)/10,random.randint(1,3)*1000,EffectColor))
		#"""
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
		Clock.tick(24)
		#print(Clock.get_fps())
		A=0
		if HF and (Impact or RenderFrames>5):
			#win.fill((255,255*CurrentRenderFrame/RenderFrames,255*CurrentRenderFrame/RenderFrames))
			win.fill((EffectColor[0]*CurrentRenderFrame/RenderFrames,EffectColor[1]*CurrentRenderFrame/RenderFrames,EffectColor[2]*CurrentRenderFrame/RenderFrames))
			Camera.X=PsudoX+random.randint(-RenderFrames,RenderFrames)
			Camera.Y=PsudoY+random.randint(-RenderFrames,RenderFrames)
		else:
			for i in BG.Sprites:
				if i["Large"]:
					if i["Large"]>1:
						RenderMassiveSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
					else:
						RenderLargeSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
				else:
					BlitList.append(RenderSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,Blit=0))
				A+=1
		W0=win.get_width()
		W1=int(P1.Health*W0/P1.MaxHealth/2)
		W2=int(P2.Health*W0/P2.MaxHealth/2)
		W3=int(W0/2)
		pygame.draw.rect(win,(0,255,255),[W3-W1,0,W1,15])
		pygame.draw.rect(win,(255,0,255),[W3,0,W2,15])
		if P1W:
			win.blit(P1WSprite,(0,15))
			#pygame.draw.rect(win,(255,0,255),[0,15,15,15])
		if P2W:
			win.blit(P2WSprite,(W0-15,15))
			#pygame.draw.rect(win,(255,0,255),[W0-15,15,15,15])
		win.blit(KO2Sprite,(W3-7,0))
		P1RS=RenderSprite(pygame.transform.flip(P1.Sprite,P1.X>P2.X,0),(P1.X+P1.Offset[0],P1.Y+P1.Offset[1],0),P1.W,P1.H,Camera,Smooth=0,Blit=0)
		P2RS=RenderSprite(pygame.transform.flip(P2.Sprite,P2.X>P1.X,0),(P2.X+P2.Offset[0],P2.Y+P2.Offset[1],0),P2.W,P2.H,Camera,Smooth=0,Blit=0)
		BlitList.extend(CreateOutline(P1RS[0],P1RS[1]))
		BlitList.extend(CreateOutline(P2RS[0],P2RS[1]))
		BlitList.append(P1RS)
		BlitList.append(P2RS)
		if BlitBloom==1:
			win.blit(P.transform.smoothscale(P.transform.smoothscale(win,(3,3)),(win.get_width(),win.get_height())).convert(),(0,0),special_flags=pygame.BLEND_ADD)
		try:
			for i in P1T["Sprites"]:
				BlitList.append(RenderSprite(pygame.transform.flip(i["Sprite"],P1.X>P2.X,0),(P1.X+i["X"]*((P1.X>P2.X)*-2+1),P1.Y+i["Y"],0),i["W"],i["H"],Camera,Blit=0))
		except:
			pass
		try:
			for i in P2T["Sprites"]:
				BlitList.append(RenderSprite(pygame.transform.flip(i["Sprite"],P2.X>P1.X,0),(P2.X+i["X"]*((P2.X>P1.X)*-2+1),P2.Y+i["Y"],0),i["W"],i["H"],Camera,Blit=0))
		except:
			pass
		C=0
		for i in range(len(Particles)):
			if Particles[i-C].Render(Camera):
				Particles.pop(i-C)
				C+=1
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
				BlitList.append(RenderSprite(TriggerSprite,((i["Box"][0][1]+i["Box"][0][0])/2+P1.X,(i["Box"][1][1]+i["Box"][1][0])/2+P1.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD,Blit=0))
			for i in P2.Triggers:
				BlitList.append(RenderSprite(TriggerSprite,((i["Box"][0][1]+i["Box"][0][0])/2+P2.X,(i["Box"][1][1]+i["Box"][1][0])/2+P2.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD,Blit=0))
		win.blits(BlitList)
		if not Countdown == 0:
			win.blit(pygame.transform.scale(ReadyScreen,(W0,win.get_height())).convert_alpha(),(0,0))
		if HF and ImpactGlitch:
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
def RenderSelect(P1,P2,I1,I2):
	global win,TrueWin,Camera,CamCap,ReadyScreen,HBR,SoundtrackList,CSBackground
	Camera.X=0
	Camera.Y=-15
	Camera.Z=-1
	Camera.FOV=1
	#win.fill(0)
	#pygame.transform.smoothscale(CSBackground,(win.get_width(),win.get_height()),win)
	K=pygame.Surface((2,2))
	K.set_at((0,0),(127,0,127))
	K.set_at((1,1),(0,127,127))
	pygame.transform.smoothscale(K,(win.get_width(),win.get_height()),win)
	HandleMusic()
	RenderSprite(CSCharacters[I1],(-256,0,0),288,512,Camera,Smooth=0)
	RenderSprite(P.transform.flip(CSCharacters[I2],1,0),(256,0,0),288,512,Camera,Smooth=0)
	RenderSprite(CSSImage,(0,0,0),128,64,Camera,Smooth=0)
	RenderSprite(CSP1Image,(P1[0],P1[1],0),64,64,Camera,Smooth=0)
	RenderSprite(CSP2Image,(P2[0],P2[1],0),64,64,Camera,Smooth=0)
	ScaleWin()
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
		GTime=10
		G=GTime
		YLength=0
		for i in range(G):
			pygame.draw.rect(TrueWin,self.Color,[(0,0),(X+(X/(G*G))-(X/((i*i)+1)),Y)])
			UpdateTrueWin()
			Clock.tick(24)
		for i in range(G):
			pygame.draw.rect(TrueWin,(0,0,0),[(0,0),(X+(X/(G*G))-(X/((i*i)+1)),Y)])
			YLength=0
			for MenuItem in self.MenuList:
				X2=MenuItem.Render()
				TrueWin.blit(X2,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
				YLength+=X2.get_height()
			UpdateTrueWin()
			Clock.tick(24)
		Selected=0
		while self.MenuList[Selected].Function==None:
			Selected+=1
			if Selected==len(self.MenuList):
				Selected=0
				break
		SelectedTime=1
		MenuOpen=1
		while MenuOpen:
			for Event in pygame.event.get():
				if Event.type==pygame.KEYDOWN:
					if Event.key==pygame.K_ESCAPE:
						MenuOpen=0
					if Event.key==pygame.K_UP:
						SO=Selected
						while self.MenuList[Selected].Function==None or SO==Selected:
							Selected-=1
							if Selected<0:
								Selected=SO
								break
						SelectedTime=1
					if Event.key==pygame.K_DOWN:
						SO=Selected
						while self.MenuList[Selected].Function==None or SO==Selected:
							Selected+=1
							if Selected==len(self.MenuList):
								Selected=SO
								break
						SelectedTime=1
					if Event.key==pygame.K_SPACE:
						if self.MenuList[Selected].Function!=None:
							L=self.MenuList[Selected].Function()
							if L!=None:
								return L
			TrueWin.fill(0)
			YLength=0
			for MenuItemID in range(len(self.MenuList)):
				MenuItem=self.MenuList[MenuItemID]
				X=MenuItem.Render()
				TrueWin.blit(X,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
				G=X.get_height()
				if MenuItemID==Selected:
					pygame.draw.rect(TrueWin,self.Color,[(0,self.YMargin+self.YPadding+YLength),(self.XMargin+(TrueWin.get_width()/(SelectedTime*SelectedTime)),G)])
				YLength+=G
			SelectedTime+=1
			UpdateTrueWin()
			Clock.tick(24)
		Y=TrueWin.get_height()
		X=TrueWin.get_width()
		YLength=0
		G=GTime
		for c in range(G):
			TrueWin.fill(self.Color)
			i=G-c
			pygame.draw.rect(TrueWin,(0,0,0),[(0,0),(X+(X/(G*G))-(X/((i*i)+1)),Y)])
			YLength=0
			for MenuItem in self.MenuList:
				X2=MenuItem.Render()
				TrueWin.blit(X2,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
				YLength+=X2.get_height()
			UpdateTrueWin()
			Clock.tick(24)
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
		TrueWinScreenshot=TrueWin.copy()
		Selected=0
		while self.MenuList[Selected].Function==None:
			Selected+=1
			if Selected==len(self.MenuList):
				Selected=0
				break
		SelectedTime=1
		MenuOpen=1
		while MenuOpen:
			for Event in pygame.event.get():
				if Event.type==pygame.KEYDOWN:
					if Event.key==pygame.K_ESCAPE:
						MenuOpen=0
					if Event.key==pygame.K_UP:
						SO=Selected
						while self.MenuList[Selected].Function==None or SO==Selected:
							Selected-=1
							if Selected<0:
								Selected=SO
								break
						SelectedTime=1
					if Event.key==pygame.K_DOWN:
						SO=Selected
						while self.MenuList[Selected].Function==None or SO==Selected:
							Selected+=1
							if Selected==len(self.MenuList):
								Selected=SO
								break
						SelectedTime=1
					if Event.key==pygame.K_SPACE:
						if self.MenuList[Selected].Function!=None:
							L=self.MenuList[Selected].Function()
							if L!=None:
								return L
			K=pygame.Surface((2,2))
			K.set_at((0,0),(127,0,127))
			K.set_at((1,1),(0,127,127))
			pygame.transform.smoothscale(K,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
			YLength=0
			for MenuItemID in range(len(self.MenuList)):
				MenuItem=self.MenuList[MenuItemID]
				X=MenuItem.Render()
				TrueWin.blit(X,(self.XMargin+self.XPadding,YLength+self.YMargin+self.YPadding))
				G=X.get_height()
				if MenuItemID==Selected:
					pygame.draw.rect(TrueWin,self.Color,[(0,self.YMargin+self.YPadding+YLength),(self.XMargin+(TrueWin.get_width()/(SelectedTime*SelectedTime)),G)])
				YLength+=G
			SelectedTime+=1
			UpdateTrueWin()
			Clock.tick(24)
		pass