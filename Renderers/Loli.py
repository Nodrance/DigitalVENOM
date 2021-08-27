import pygame,random
#Here we define some basic variables.
P=pygame
pygame.init()
#win=pygame.Surface((1366,768))
ReadyScreen=pygame.image.load("Sprites/Game Start.png")
win=pygame.Surface((683,384))
FZ=-1
#win=pygame.Surface((683*2,384*2))
win.set_alpha(None)
TrueWin=pygame.display.set_mode((0,0),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
TrueWin.convert()
CamCap=(win.get_width()*0.9)
P1W=0
P2W=0
HBR=0
SimScaling=4
P1WSprite=pygame.image.load("Sprites/Victory Cyan.png")
P2WSprite=pygame.image.load("Sprites/Victory Magenta.png")
KO2Sprite=pygame.image.load("Sprites/KO2.png")
CSP1Image=pygame.image.load("Sprites/Character Select Screen/P1.png")
CSP2Image=pygame.image.load("Sprites/Character Select Screen/P2.png")
CSSImage=pygame.image.load("Sprites/Character Select Screen/Screen.png").convert()
CSBackground=pygame.image.load("Sprites/Character Select Screen/Background.png").convert()#.convert_alpha()
CSCharacters=[
pygame.image.load("Sprites/Character Select Screen/InjectionCubePortrait.png"),
pygame.image.load("Sprites/Character Select Screen/QuWPortrait.png"),
]
SoundtrackList=[
"Music/Lethal Injection.wav",
"Music/QT.wav",
]
pygame.mixer.music.load(random.choice(SoundtrackList))
pygame.mixer.music.play()
pygame.mixer.music.queue(random.choice(SoundtrackList))
class LoliCamera: #Defines the camera object.
	def __init__(self,X,Y,Z,FOV):
		self.X=X
		self.Y=Y
		self.Z=Z
		self.FOV=FOV
Camera=LoliCamera(0,-15,-1,1)
def RenderSprite(Sprite,Pos,Width,Height,Camera,Blending=None,Smooth=0): #Defines the sprite render function.
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
	if Blending==None:
		win.blit(Sprite2,Pos4) #Blits the sprite to the screen.
	else:
		win.blit(Sprite2,Pos4,special_flags=Blending) #Blits the sprite to the screen.
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
	print(SS)
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
	print(Sprite2.get_width(),Sprite2.get_height())
	print(Sprite.get_width(),Sprite.get_height())
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
def Sound(X):
	return P.mixer.Sound(X)
def Render(P1,P2,BG,Countdown,P1T={},P2T={},Clock=None): #The render function
	global win,TrueWin,Camera,CamCap,ReadyScreen,HBR,SoundtrackList,FZ
	if pygame.mixer.music.get_busy()==0:
		P.mixer.music.load(random.choice(SoundtrackList))
		P.mixer.music.play()
		P.mixer.music.queue(random.choice(SoundtrackList))
	#win.fill(0)
	BlitBloom=0
	CS=1.5
	Camera.X-=int((P1.X+P2.X)/2)
	Camera.X=int(Camera.X/CS)
	Camera.X+=int((P1.X+P2.X)/2)
	Camera.Y-=int((P1.Y+P2.Y)/2-15)
	Camera.Y=int(Camera.Y/CS)
	Camera.Y+=int((P1.Y+P2.Y)/2-15)
	Camera.Z+=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	Camera.Z=(Camera.Z/CS)-0.1
	Camera.Z-=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	#FZ+=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	#FZ=(FZ/CS)
	#FZ-=min(max(0.75,(abs(P1.X-P2.X)/CamCap),(abs(P1.Y-P2.Y)/CamCap*2)),5)
	#Camera.Z=int(FZ*5)/5
	#Camera.Z=-1
	A=0
	for i in BG.Sprites:
		if i["Large"]:
			if i["Large"]>1:
				RenderHugeSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
			else:
				RenderLargeSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera,A>0,i["Blending"])
		else:
			RenderSprite(i["Sprite"],(i["X"],i["Y"],i["Z"]),i["W"],i["H"],Camera)
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
	RenderSprite(pygame.transform.flip(P1.Sprite,P1.X>P2.X,0),(P1.X+P1.Offset[0],P1.Y+P1.Offset[1],0),P1.W,P1.H,Camera,Smooth=0)
	RenderSprite(pygame.transform.flip(P2.Sprite,P2.X>P1.X,0),(P2.X+P2.Offset[0],P2.Y+P2.Offset[1],0),P2.W,P2.H,Camera,Smooth=0)
	try:
		for i in P1T["Sprites"]:
			RenderSprite(pygame.transform.flip(i["Sprite"],P1.X>P2.X,0),(P1.X+i["X"]*((P1.X>P2.X)*-2+1),P1.Y+i["Y"],0),i["W"],i["H"],Camera)
	except:
		pass
	try:
		for i in P2T["Sprites"]:
			RenderSprite(pygame.transform.flip(i["Sprite"],P2.X>P1.X,0),(P2.X+i["X"]*((P2.X>P1.X)*-2+1),P2.Y+i["Y"],0),i["W"],i["H"],Camera)
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
			RenderSprite(pygame.image.load("Sprites/Trigger.png"),((i["Box"][0][1]+i["Box"][0][0])/2+P1.X,(i["Box"][1][1]+i["Box"][1][0])/2+P1.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD)
		for i in P2.Triggers:
			RenderSprite(pygame.image.load("Sprites/Trigger.png"),((i["Box"][0][1]+i["Box"][0][0])/2+P2.X,(i["Box"][1][1]+i["Box"][1][0])/2+P2.Y,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD)
	if not Countdown == 0:
		win.blit(pygame.transform.scale(ReadyScreen,(W0,win.get_height())),(0,0))
	if BlitBloom==1:
		win.blit(P.transform.smoothscale(P.transform.smoothscale(win,(2,2)),(win.get_width(),win.get_height())),(0,0),special_flags=pygame.BLEND_ADD)
	if BlitBloom==2:
		A=P.Surface((1,1),pygame.SRCALPHA)
		A.set_alpha(0)
		A.fill(P.transform.average_color(win))
		win.blit(P.transform.scale(A,(win.get_width(),win.get_height())),(0,0),special_flags=pygame.BLEND_RGBA_ADD)
	pygame.transform.scale(win,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	if Clock!=None:
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
			pass
	pygame.display.flip()
	pass
def RenderSelect(P1,P2,I1,I2):
	global win,TrueWin,Camera,CamCap,ReadyScreen,HBR,SoundtrackList,CSBackground
	Camera.X=0
	Camera.Y=-15
	Camera.Z=-1
	Camera.FOV=1
	#win.fill(0)
	pygame.transform.smoothscale(CSBackground,(win.get_width(),win.get_height()),win)
	if pygame.mixer.music.get_busy()==0:
		P.mixer.music.load(random.choice(SoundtrackList))
		P.mixer.music.play()
		P.mixer.music.queue(random.choice(SoundtrackList))
	RenderSprite(CSCharacters[I1],(-256,0,0),288,512,Camera,Smooth=0)
	RenderSprite(P.transform.flip(CSCharacters[I2],1,0),(256,0,0),288,512,Camera,Smooth=0)
	RenderSprite(CSSImage,(0,0,0),128,64,Camera,Smooth=0)
	RenderSprite(CSP1Image,(P1[0],P1[1],0),64,64,Camera,Smooth=0)
	RenderSprite(CSP2Image,(P2[0],P2[1],0),64,64,Camera,Smooth=0)
	P.transform.scale(win,(TrueWin.get_width(),TrueWin.get_height()),TrueWin)
	P.display.flip()
	pass