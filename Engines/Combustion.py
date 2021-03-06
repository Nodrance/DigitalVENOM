import sys,numpy,random,copy,json,time,pygame,cProfile,pstats
from Tools import HitBoxer
import threading
DuelFault=0
SimulatedFramerate=24
SimulatedFrames=0
StartTime=0
ReplayData=[]
MaxWallDurability=24
WallDurability1=MaxWallDurability
WallDurability2=MaxWallDurability
OverclockBalance=0
GameMode="Competitive"
HF=0
#TODO:
#Stop using time.time()
#It's not made for framerate calculations
#Look into the use of time.perf_counter()
AntiTurbo=[
{
	"l":0,
	"m":0,
	"h":0,
	"v":0,
},
{
	"l":0,
	"m":0,
	"h":0,
	"v":0,
}
]
AntiTurboStrength=5
AntiTurboTimer=0
NegativePenaltySound=pygame.mixer.Sound("Sounds/Negative Penalty.wav")
CameraZoom=0
Rendering3=0
WinIndex=[
"No Contest",
"Player Two Wins",
"Player One Wins",
"Double Knockout",
]
StayMaxTension=0
InputList=[]
Rendering2=1
PlayerSides=0
P1T=[]
P2T=[]
T1=[]
T2=[]
Tension=0
def EndGame():
	return "End Game"
def ToggleShowHitBoxes():
	global Renderer
	Renderer.HBR=1-Renderer.HBR
def SetupHitBoxer():
	global GlobalPlayer1
	HitBoxer.AttackData=GlobalPlayer1.HitBoxerFrameData
	HitBoxer.SpriteOffset=GlobalPlayer1.Offset
	HitBoxer.SpriteWidth=GlobalPlayer1.W
	HitBoxer.SpriteHeight=GlobalPlayer1.H
	HitBoxer.Sprites=GlobalPlayer1.Sprites
	HitBoxer.Start()
def TrainingResetGame():
	global GlobalPlayer1,GlobalPlayer2
	GlobalPlayer1.Reset(0)
	GlobalPlayer2.Reset(1)
	return 0
	pass
def TrainingFillMeters():
	global GlobalPlayer1,GlobalPlayer2
	try:
		GlobalPlayer1.Meter=GlobalPlayer1.MaxMeter
		GlobalPlayer2.Meter=GlobalPlayer2.MaxMeter
	except:
		pass
	pass
def SetOneHealth():
	global GlobalPlayer1,GlobalPlayer2
	try:
		GlobalPlayer1.Health=1
		GlobalPlayer2.Health=1
	except:
		pass
	pass
def PauseMenu(Renderer):
	return Renderer.SlideMenu([
		Renderer.MenuTitle("Game Paused"),
		Renderer.MenuLabel("HitBoxer",Function=SetupHitBoxer),
		Renderer.MenuLabel("End Game",Function=EndGame),
		]).Open()
	pass
def TrainingMenu(Renderer):
	return Renderer.SlideMenu([
		Renderer.MenuTitle("Game Paused"),
		Renderer.MenuLabel("Reset",Function=TrainingResetGame),
		Renderer.MenuLabel("Fill Meters",Function=TrainingFillMeters),
		Renderer.MenuLabel("Set One Health",Function=SetOneHealth),
		Renderer.MenuLabel("Toggle Trigger Rendering",Function=ToggleShowHitBoxes),
		Renderer.MenuLabel("HitBoxer",Function=SetupHitBoxer),
		Renderer.MenuLabel("End Game",Function=EndGame),
		]).Open()
	pass
def CheckOverlap1D(V1,V2): #Check for overlap between two 1D stretches.
	return (V1[0]<V2[1] and V2[0]<V1[1])
def CheckOverlap2D(Box1,Box2): #Check for overlap between two 2D boxes.
	return (CheckOverlap1D(Box1[0],Box2[0]) and CheckOverlap1D(Box1[1],Box2[1]))
def HitBoxGlobalizer(Box,X,Y): #Convert the hitboxes from local positions to global positions.
	return [[Box[0][0]+X,Box[0][1]+X],[Box[1][0]+Y,Box[1][1]+Y]]
def CheckCollisions(P1,P2): #Check all hurtboxes to find any collisions and return damage and chip damage values
	global Fault,OverclockBalance
	P1T=[]
	P2T=[]
	for X in P1.Triggers:
		for Y in P2.Triggers:
			if CheckOverlap2D(HitBoxGlobalizer(X["Box"],P1.X,P1.Y),HitBoxGlobalizer(Y["Box"],P2.X,P2.Y)):
				D=copy.deepcopy(X)
				D2=copy.deepcopy(Y)
				try:
					DamageScale1=1+0.5*(Fault+DuelFault*2)+2*OverclockBalance
					DamageScale2=-DamageScale1+2
					if DamageScale1>1:
						D["Damage"]*=DamageScale1
						#D["Chip Damage"]+=1*(Fault+DuelFault*2)
					if DamageScale2>1:
						D2["Damage"]*=DamageScale2
						#D2["Chip Damage"]+=1*-(Fault+DuelFault*2)
				except:
					pass
				P1T.append([D,D2])
				P2T.append([D2,D])
	return P1T,P2T
	pass
PygameEvents=[]
HalfTime=0
def Frame(P1,P2,Renderer,pygame,P1C,P2C,BG,Training=0): #This function runs one frame of gameplay.
	global HalfTime,OverclockBalance,AntiTurboTimer,AntiTurbo,AntiTurboStrength,StayMaxTension,Tension,PlayerSides,Rendering2,CameraZoom,HF,MaxWallDurability,WallDurability1,WallDurability2,RenderCount,Clock,Camera,LFC1,LFC2,P1C1,P1C2,P2C1,P2C2,PreFault,Fault,DuelFault,StartTime,SimulatedFrames,SimulatedFramerate,ReplayData,P1T,P2T,T1,T2,GlobalPlayer1,GlobalPlayer2,PygameEvents,keys
	i=0
	PygameEvents=pygame.event.get()
	for Event in PygameEvents:
		i+=1
		if Event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if Event.type == pygame.KEYDOWN:
			if Event.key==pygame.K_ESCAPE:
				if Training:
					Rendering2=0
					pygame.time.delay(100)
					L=TrainingMenu(Renderer)
				else:
					Rendering2=0
					pygame.time.delay(100)
					L=PauseMenu(Renderer)
				if L=="End Game":
					return 2,"End Game"
				Rendering2=1
				StartTime=time.time()
				SimulatedFrames=0
				#pygame.quit()
				#sys.exit()
	GlobalPlayer1=P1
	GlobalPlayer2=P2
	Fault=[0,numpy.sign(P2.X-P1.X)*numpy.sign(P1.X)][numpy.sign(P1.X)==numpy.sign(P2.X)]
	if Tension>50:
		Renderer.Particles.append(Renderer.CircleParticle((random.randint(BG.Bounds[0],BG.Bounds[1]),0),(random.randint(-8,8),random.randint(-64,-16)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
		Renderer.Particles.append(Renderer.LineParticle((random.randint(BG.Bounds[0],BG.Bounds[1]),0),(random.randint(-8,8),random.randint(-64,-16)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
	try:
		if Fault != PreFault:
			if Fault==0:
				for i in range(10):
					Renderer.Particles.append(Renderer.CircleParticle((0,0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
					Renderer.Particles.append(Renderer.LineParticle((0,0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			else:
				for i in range(10):
					Renderer.Particles.append(Renderer.CircleParticle(([P2.X,(P1.X+P2.X)/2,P1.X][int(Fault+1)],0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
					Renderer.Particles.append(Renderer.LineParticle(([P2.X,(P1.X+P2.X)/2,P1.X][int(Fault+1)],0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			"""if Fault==-PreFault:
				for i in range(50):
					Renderer.Particles.append(Renderer.LineParticle(((P1.X+P2.X)/2,0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			else:
				for i in range(50):
					Renderer.Particles.append(Renderer.LineParticle((0,0),(random.randint(-8,8),random.randint(-64,0)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))"""
			PreFault=Fault
	except Exception as e:
		PreFault=Fault
	T1,T2 = CheckCollisions(P1,P2)
	OverclockBalance=P1.Overclock-P2.Overclock
	for C in T1:
		try:
			P1.HitSounds[random.choice(C[0]["HitSounds"])].play()
		except Exception as e:
			#print(C)
			#print(e)
			pass
		try:
			P2.HitSounds[random.choice(C[1]["HitSounds"])].play()
		except Exception as e:
			#print(C)
			#print(e)
			pass
	P1C1=P1C.Character(pygame,PygameEvents)
	P2C1=P2C.Character(pygame,PygameEvents)
	if AntiTurboTimer<=0:
		AntiTurbo[0]["l"]+=P1C1["l"]*AntiTurboStrength
		AntiTurbo[0]["m"]+=P1C1["m"]*AntiTurboStrength
		AntiTurbo[0]["h"]+=P1C1["h"]*AntiTurboStrength
		AntiTurbo[0]["v"]+=P1C1["v"]*AntiTurboStrength
		AntiTurbo[1]["l"]+=P2C1["l"]*AntiTurboStrength
		AntiTurbo[1]["m"]+=P2C1["m"]*AntiTurboStrength
		AntiTurbo[1]["h"]+=P2C1["h"]*AntiTurboStrength
		AntiTurbo[1]["v"]+=P2C1["v"]*AntiTurboStrength
		AntiTurbo[0]["l"]=max(0,AntiTurbo[0]["l"]-1)
		AntiTurbo[0]["m"]=max(0,AntiTurbo[0]["m"]-1)
		AntiTurbo[0]["h"]=max(0,AntiTurbo[0]["h"]-1)
		AntiTurbo[0]["v"]=max(0,AntiTurbo[0]["v"]-1)
		AntiTurbo[1]["l"]=max(0,AntiTurbo[1]["l"]-1)
		AntiTurbo[1]["m"]=max(0,AntiTurbo[1]["m"]-1)
		AntiTurbo[1]["h"]=max(0,AntiTurbo[1]["h"]-1)
		AntiTurbo[1]["v"]=max(0,AntiTurbo[1]["v"]-1)
		if max([AntiTurbo[0][i] for i in AntiTurbo[0].keys()])>5:
			P1.Health-=int(P1.MaxHealth/2)
			NegativePenaltySound.play()
			AntiTurbo=[{"l":0,"m":0,"h":0,"v":0},{"l":0,"m":0,"h":0,"v":0}]
		if max([AntiTurbo[1][i] for i in AntiTurbo[1].keys()])>5:
			P2.Health-=int(P2.MaxHealth/2)
			NegativePenaltySound.play()
			AntiTurbo=[{"l":0,"m":0,"h":0,"v":0},{"l":0,"m":0,"h":0,"v":0}]
	else:
		#print(AntiTurboTimer)
		AntiTurbo=[{"l":0,"m":0,"h":0,"v":0},{"l":0,"m":0,"h":0,"v":0}]
		AntiTurboTimer-=1
	"""try:
		LFC1
		LFC2
	except:
		LFC1=copy.deepcopy(P1C1)
		LFC2=copy.deepcopy(P2C1)
		P1C2=copy.deepcopy(P1C1)
		P2C2=copy.deepcopy(P2C1)
	for i in P1C1.keys():
		if P1C1[i]==LFC1[i]:
			P1C2[i]=0
		else:
			P1C2[i]=P1C1[i]
		if P2C1[i]==LFC2[i]:
			P2C2[i]=0
		else:
			P2C2[i]=P2C1[i]
		#P1C2[i]=(P1C1[i]==1 and LFC1[i]==0)
		#P2C2[i]=(P2C1[i]==1 and LFC2[i]==0)
	P1C2["X2"]=P1C2["X"]
	P2C2["X2"]=P2C2["X"]
	P1C2["Y2"]=P1C2["Y"]
	P2C2["Y2"]=P2C2["Y"]
	P1C2["Jump2"]=P1C2["Jump"]
	P2C2["Jump2"]=P2C2["Jump"]
	P1C2["X"]=P1C1["X"]
	P2C2["X"]=P2C1["X"]
	P1C2["Y"]=P1C1["Y"]
	P2C2["Y"]=P2C1["Y"]
	P1C2["Jump"]=P1C1["Jump"]
	P2C2["Jump"]=P2C1["Jump"]
	#P1C2={P1C1[i] and not LFC1[i] for i in P1C1.keys()}
	#P2C2={P2C1[i] and not LFC2[i] for i in P2C1.keys()}
	LFC1=P1C1
	LFC2=P2C1"""
	ReplayData.append([P1C1,P2C1])
	P1T=P1({"Side":P1.X>P2.X,"Fault":Fault,"Triggers":T1,"Stage":BG,"Controller":P1C1,"Other Player":P2})
	P2T=P2({"Side":P2.X>P1.X,"Fault":-Fault,"Triggers":T2,"Stage":BG,"Controller":P2C1,"Other Player":P1})
	if StayMaxTension:
		Tension=100
	else:
		Tension=(50*
			(2-
				P1.Health/P1.MaxHealth-
				P2.Health/P2.MaxHealth
				)
			)
	D=[[P1,P2],[P2,P1]][PlayerSides]
	if D[0].X+32>D[1].X:
		D[0].X=D[1].X=(D[1].X+D[0].X)/2
		D[0].X-=16
		D[1].X+=16
	if D[0].X+400<D[1].X:
		D[0].X=D[1].X=(D[1].X+D[0].X)/2
		D[0].X-=200
		D[1].X+=200
	if D[0].X<BG.Bounds[0]:
		if WallDurability1<0:
			WallDurability1=MaxWallDurability
			WallDurability2=MaxWallDurability
			DuelFault=max(-BG.FaultOffset,DuelFault-1)
			D[0].X=BG.Bounds[1]-500
			D[1].X=BG.Bounds[1]
			Renderer.Camera.X=BG.Bounds[1]+BG.DuelFaultCameraOffset
			DuelFaultChangeSound.play()
			for i in range(100):
				Renderer.Particles.append(Renderer.LineParticle((BG.Bounds[1],random.randint(BG.Bounds[2],0)),(random.randint(-64,-16),random.randint(-8,8)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			#P1.XV=-P1.XV
		else:
			D[0].X=BG.Bounds[0]
			WallDurability1-=1
	if D[1].X>BG.Bounds[1]:
		if WallDurability2<0:
			WallDurability1=MaxWallDurability
			WallDurability2=MaxWallDurability
			DuelFault=min(BG.FaultOffset,DuelFault+1)
			D[0].X=BG.Bounds[0]
			D[1].X=BG.Bounds[0]+500
			Renderer.Camera.X=BG.Bounds[0]-BG.DuelFaultCameraOffset
			DuelFaultChangeSound.play()
			for i in range(100):
				Renderer.Particles.append(Renderer.LineParticle((BG.Bounds[0],random.randint(BG.Bounds[2],0)),(random.randint(16,64),random.randint(-8,8)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			#P2.XV=-P2.XV
		else:
			D[1].X=BG.Bounds[1]
			WallDurability2-=1
	if D[0].Y<BG.Bounds[2]:
		D[0].Y=BG.Bounds[2]
		D[0].YV=-D[0].YV
	if D[1].Y<BG.Bounds[2]:
		D[1].Y=BG.Bounds[2]
		D[1].YV=-D[1].YV
	HFF=0
	try:
		HFF+=P1T["Hit Lag"]
	except Exception as e:
		pass
	try:
		HFF+=P2T["Hit Lag"]
	except Exception as e:
		pass
	try:
		if P1T["Fault Reversal"] or P2T["Fault Reversal"]:
			PlayerSides+=1
			PlayerSides%=2
	except:
		pass
	#print(SimulatedFrames/((pygame.time.get_ticks()-StartTime)/1000))
	#if (pygame.time.get_ticks()-StartTime)/SimulatedFrames<1000/SimulatedFramerate:
	#while ((pygame.time.get_ticks()-StartTime)/SimulatedFrames)+100<1000/SimulatedFramerate:
		#pygame.time.delay(1)
		#pygame.time.delay(int(((pygame.time.get_ticks()-StartTime)-SimulatedFrames*(1000/SimulatedFramerate))/2))"""
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
	SimulatedFrames+=1+HFF
	if HFF>0:
		AntiTurboTimer=3
		#Renderer.Particles.append(Renderer.StarParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-8,8),random.randint(32,64)),random.randint(1,5)/10,0.6,(255,255,255)))
		for i in range(HFF*5):
			Renderer.Particles.append(Renderer.LineParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-64,64),random.randint(-64,64)),random.randint(5,20)/10,0.6,(255,255,0)))
		for i in range(HFF*5):
			Renderer.Particles.append(Renderer.CircleParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-64,64),random.randint(-64,64)),random.randint(5,20)/10,0.6,(255,255,0)))
		#for i in range(min(RenderFrames,10)):
		#	Particles.append(SpikeParticle((int((P1.X+P2.X)/2),int((P1.Y+P2.Y)/2)-32),(random.randint(-5,5),random.randint(-5,5)),random.randint(1,5)/10,random.randint(1,3)*1000,EffectColor))
		#"""
	ET=SimulatedFrames/60
	if HFF>0:
		if HFF>15:
			CameraZoom=1
		else:
			CameraZoom=0
		HF=1
		for F in range(HFF):
			#print((pygame.time.get_ticks()-StartTime)/SimulatedFrames)
			ET2=(time.time()-StartTime)
			if ET>ET2 and ET-ET2<2:
				#print(SimulatedFrames/(time.time()-StartTime))
				#print(ET-ET2)
				time.sleep(max(ET-ET2,0))
	else:
		CameraZoom=0
		HF=0
	CameraZoom+=HalfTime
	ET2=(time.time()-StartTime)
	if ET>ET2:
		if ET-ET2<0.1:
			time.sleep(max(0,ET-ET2))
			pass
		else:
			StartTime=time.time()
			SimulatedFrames=0
	return P1.Health<1, P2.Health<1
	pass
def GameplayThread(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay=0,Rendering=1,Training=0):
	global MaxWallDurability,WallDurability1,WallDurability2,Clock,DuelFault,DuelFaultChangeSound,StartTime,ReplayData,Rendering2
	while 1:
		X,Y = Frame(P1,P2,Renderer,pygame,P1C,P2C,BG,Training=Training)
		#Clock.tick(24)
		if X==2:
			if Y=="End Game":
				return (0,0)
		if X or Y:
			return X,Y
	pass
def RenderSetup(a,b,c,d,e,f,g,h,i,j,k):
	global Rendering2,MaxWallDurability,keys,PygameEvents,WallDurability1,WallDurability2,Clock,DuelFault,DuelFaultChangeSound,StartTime,ReplayData,P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training,CameraZoom
	CameraZoom=0
	P1=a
	P2=b
	Renderer=c
	CV=[random.randint(-750,750),random.randint(-750,750)+0.5]
	CV=numpy.divide(numpy.multiply(CV,750),numpy.linalg.norm(CV))
	Renderer.Camera.X=CV[0]
	Renderer.Camera.Y=CV[1]
	Renderer.Camera.Z=-0.3
	pygame=d
	P1C=e
	P2C=f
	BG=g
	GameStart=h
	SaveReplay=i
	Rendering=j
	Training=k
	pass
def GetCurrentList(L):
	X=L.copy()
	for i in range(len(X)):
		L.pop(0)
	pass
def RenderThread():
	global Tension,HF,GameMode,Rendering2,CameraZoom,MaxWallDurability,keys,PygameEvents,WallDurability1,WallDurability2,Clock,DuelFault,DuelFaultChangeSound,StartTime,ReplayData,P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training
	while 1:
		if Rendering2:
			Renderer.Render(P1,P2,BG.Fault[DuelFault+BG.FaultOffset],max(0,StartTime-time.time()),P1T,P2T,Collisions=T1,HF=HF,Impact=HF,CameraZoom=CameraZoom,Tension=Tension,GameMode=GameMode)
			time.sleep(0)
def Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay=0,Rendering=1,Training=0):
	global CameraZoom,WinIndex,AntiTurboTimer,Tension,PlayerSides,MaxWallDurability,Rendering2,Rendering3,WallDurability1,WallDurability2,Clock,DuelFault,DuelFaultChangeSound,SimuatedFrames,StartTime,ReplayData
	WallDurability1=MaxWallDurability
	WallDurability2=MaxWallDurability
	Tension=0
	PlayerSides=0
	pygame.mixer.music.set_volume(100)
	ReplayData=[{
	"Engine Module Name":__name__,
	"Engine Module Hash":hash(sys.modules[__name__]),
	"Renderer Module  Name":Renderer.__name__,
	"Renderer Module Hash":hash(sys.modules[Renderer.__name__]),
	"Player 1 Character Module Name":P1.__module__,
	"Player 1 Character Module Hash":hash(sys.modules[P1.__module__]),
	"Player 2 Character Module Name":P2.__module__,
	"Player 2 Character Module Hash":hash(sys.modules[P2.__module__]),
	"Stage Module Name":BG.__module__,
	"Stage Module Hash":hash(sys.modules[BG.__module__]),
	}]
	DuelFaultChangeSound=pygame.mixer.Sound("Sounds/Duel Fault Change.wav")
	SimulatedFrames=0
	DuelFault=0
	FrameRenderList=[]
	Clock=pygame.time.Clock()
	if Rendering:
		Renderer.Render(P1,P2,BG.Fault[BG.FaultOffset],1,{"Sounds":[GameStart]})
	SimulatedFrames=0
	try:
		del LFC1
		del LFC2
	except:
		pass
	#threading.Thread(target=RenderThread,args=(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training)).start()
	Rendering2=1
	pygame.event.get()
	AntiTurboTimer=3
	RenderSetup(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training)
	if not Rendering3:
		Rendering3=1
		RTT=threading.Thread(target=RenderThread)
		RTT.daemon=True
		RTT.start()#,args=(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training)).start()
	StartTime=time.time()+4
	pygame.time.wait(2000)
	GameStart.play()
	pygame.time.wait(2000)
	Results=GameplayThread(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay,Rendering,Training)
	Renderer.Particles.append(Renderer.SlidingInvertTextParticle(WinIndex[Results[0]+Results[1]*2],1,Size=35))
	CameraZoom=0
	if Results!=(0,0):
		TT=pygame.time.get_ticks()
		if SaveReplay:
			json.dump(ReplayData,open("Replays/"+str(time.time())+".json","w"))
		pygame.time.wait(max(1000-pygame.time.get_ticks()+TT,0))
		Rendering2=0
		time.sleep(0.5)
	return Results
