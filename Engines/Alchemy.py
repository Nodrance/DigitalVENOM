import sys,numpy,random,copy,json,time,pygame,cProfile,pstats
from Tools import HitBoxer
DuelFault=0
SimulatedFramerate=24
SimulatedFrames=0
StartTime=0
ReplayData=[]
MaxWallDurability=24
WallDurability1=MaxWallDurability
WallDurability2=MaxWallDurability
InputList=[]
def EndGame():
	return "End Game"
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
	GlobalPlayer1.Reset(0,pygame)
	GlobalPlayer2.Reset(1,pygame)
	return 0
	pass
def TrainingFillMeters():
	global GlobalPlayer1,GlobalPlayer2
	try:
		GlobalPlayer1.Panchira=25
		GlobalPlayer2.Panchira=25
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
	global Fault
	P1T=[]
	P2T=[]
	for X in P1.Triggers:
		for Y in P2.Triggers:
			if CheckOverlap2D(HitBoxGlobalizer(X["Box"],P1.X,P1.Y),HitBoxGlobalizer(Y["Box"],P2.X,P2.Y)):
				D=copy.deepcopy(X)
				D2=copy.deepcopy(Y)
				try:
					if Fault+DuelFault*2>0:
						D["Damage"]+=5*(Fault+DuelFault*2)
						D["Chip Damage"]+=1*(Fault+DuelFault*2)
					if Fault+DuelFault*2<0:
						D2["Damage"]+=5*-(Fault+DuelFault*2)
						D2["Chip Damage"]+=1*-(Fault+DuelFault*2)
				except:
					pass
				P1T.append([D,D2])
				P2T.append([D2,D])
	return P1T,P2T
	pass
def Frame(P1,P2,Renderer,pygame,P1C,P2C,BG,Training=0): #This function runs one frame of gameplay.
	global MaxWallDurability,WallDurability1,WallDurability2,RenderCount,Clock,Camera,LFC1,LFC2,P1C1,P1C2,P2C1,P2C2,PreFault,Fault,DuelFault,StartTime,SimulatedFrames,SimulatedFramerate,ReplayData,P1T,P2T,T1,T2,GlobalPlayer1,GlobalPlayer2
	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if Event.type == pygame.KEYDOWN:
			if Event.key==pygame.K_ESCAPE:
				if Training:
					L=TrainingMenu(Renderer)
				else:
					L=PauseMenu(Renderer)
				if L=="End Game":
					return 2,"End Game"
				#pygame.quit()
				#sys.exit()
	keys=pygame.key.get_pressed()
	GlobalPlayer1=P1
	GlobalPlayer2=P2
	Fault=[0,numpy.sign(P2.X-P1.X)*numpy.sign(P1.X)][numpy.sign(P1.X)==numpy.sign(P2.X)]
	#Renderer.Particles.append(Renderer.CircleParticle((random.randint(BG.Bounds[0],BG.Bounds[1]),0),(random.randint(-8,8),random.randint(-64,-16)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
	#Renderer.Particles.append(Renderer.LineParticle((random.randint(BG.Bounds[0],BG.Bounds[1]),0),(random.randint(-8,8),random.randint(-64,-16)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
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
		#print(e)
		PreFault=Fault
	T1,T2 = CheckCollisions(P1,P2)
	P1C1=P1C.Character(pygame)
	P2C1=P2C.Character(pygame)
	try:
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
	LFC2=P2C1
	ReplayData.append([P1C1,P2C1])
	P1T=P1.Frame({"Side":0,"Fault":Fault,"Triggers":T1,"Stage":BG,"Controller":P1C2,"Other Player":P2})
	P2T=P2.Frame({"Side":1,"Fault":-Fault,"Triggers":T2,"Stage":BG,"Controller":P2C2,"Other Player":P1})
	if P1.X+32>P2.X:
		P1.X=P2.X=(P2.X+P1.X)/2
		P1.X-=16
		P2.X+=16
	if P1.X<BG.Bounds[0]:
		if WallDurability1<0:
			WallDurability1=MaxWallDurability
			DuelFault=max(-BG.FaultOffset,DuelFault-1)
			P1.X=BG.Bounds[1]-200
			P2.X=BG.Bounds[1]-100
			Renderer.Camera.X=BG.Bounds[1]+BG.DuelFaultCameraOffset
			DuelFaultChangeSound.play()
			for i in range(100):
				Renderer.Particles.append(Renderer.LineParticle((BG.Bounds[1],random.randint(BG.Bounds[2],0)),(random.randint(-64,-16),random.randint(-8,8)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			#P1.XV=-P1.XV
		else:
			P1.X=BG.Bounds[0]
			WallDurability1-=1
	if P2.X>BG.Bounds[1]:
		if WallDurability2<0:
			WallDurability2=MaxWallDurability
			DuelFault=min(BG.FaultOffset,DuelFault+1)
			P1.X=BG.Bounds[0]+100
			P2.X=BG.Bounds[0]+200
			Renderer.Camera.X=BG.Bounds[0]-BG.DuelFaultCameraOffset
			DuelFaultChangeSound.play()
			for i in range(100):
				Renderer.Particles.append(Renderer.LineParticle((BG.Bounds[0],random.randint(BG.Bounds[2],0)),(random.randint(16,64),random.randint(-8,8)),random.randint(5,20)/10,0.6,[(255,0,255),(255,255,0),(0,255,255)][int(Fault+1)]))
			#P2.XV=-P2.XV
		else:
			P2.X=BG.Bounds[1]
			WallDurability2-=1
	if P1.Y<BG.Bounds[2]:
		P1.Y=BG.Bounds[2]
		P1.YV=-P1.YV
	if P2.Y<BG.Bounds[2]:
		P2.Y=BG.Bounds[2]
		P2.YV=-P2.YV
	try:
		SimulatedFrames+=P1T["Hit Lag"]
	except Exception as e:
		pass
	try:
		SimulatedFrames+=P2T["Hit Lag"]
	except Exception as e:
		pass
	SimulatedFrames+=1
	#print(SimulatedFrames/((pygame.time.get_ticks()-StartTime)/1000))
	#if (pygame.time.get_ticks()-StartTime)/SimulatedFrames<1000/SimulatedFramerate:
	#while ((pygame.time.get_ticks()-StartTime)/SimulatedFrames)+100<1000/SimulatedFramerate:
		#pygame.time.delay(1)
		#pygame.time.delay(int(((pygame.time.get_ticks()-StartTime)-SimulatedFrames*(1000/SimulatedFramerate))/2))"""
	return P1.Health<1, P2.Health<1
	pass
def Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart,SaveReplay=0,Rendering=1,Training=0):
	global MaxWallDurability,WallDurability1,WallDurability2,Clock,DuelFault,DuelFaultChangeSound,StartTime,ReplayData
	WallDurability1=MaxWallDurability
	WallDurability2=MaxWallDurability
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
	pygame.time.wait(2000)
	StartTime=pygame.time.get_ticks()
	try:
		del LFC1
		del LFC2
	except:
		pass
	while True:
		X,Y = Frame(P1,P2,Renderer,pygame,P1C,P2C,BG,Training=Training)
		if X==2:
			if Y=="End Game":
				return (0,0)
		if Rendering:
			Renderer.Render(P1,P2,BG.Fault[DuelFault+BG.FaultOffset],0,P1T,P2T,Collisions=T1)
		if X or Y:
			if SaveReplay:
				json.dump(ReplayData,open("Replays/"+str(time.time())+".json","w"))
			return X,Y