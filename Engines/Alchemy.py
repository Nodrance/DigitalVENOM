import sys,numpy
def CheckOverlap1D(V1,V2): #Check for overlap between two 1D stretches.
	return (V1[0]<V2[1] and V2[0]<V1[1])
def CheckOverlap2D(Box1,Box2): #Check for overlap between two 2D boxes.
	return (CheckOverlap1D(Box1[0],Box2[0]) and CheckOverlap1D(Box1[1],Box2[1]))
def HitBoxGlobalizer(Box,X,Y): #Convert the hitboxes from local positions to global positions.
	return [[Box[0][0]+X,Box[0][1]+X],[Box[1][0]+Y,Box[1][1]+Y]]
def CheckCollisions(P1,P2): #Check all hurtboxes to find any collisions and return damage and chip damage values
	P1T=[]
	P2T=[]
	for X in P1.Triggers:
		for Y in P2.Triggers:
			if CheckOverlap2D(HitBoxGlobalizer(X["Box"],P1.X,P1.Y),HitBoxGlobalizer(Y["Box"],P2.X,P2.Y)):
				P1T.append([X,Y])
				P2T.append([Y,X])
	return P1T,P2T
	pass
def Frame(P1,P2,Renderer,pygame,P1C,P2C,BG): #This function runs one frame of gameplay.
	global RenderCount,Clock,Camera
	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if Event.type == pygame.KEYDOWN:
			if Event.key==pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
	keys=pygame.key.get_pressed()
	Fault=[0,numpy.sign(P2.X-P1.X)*numpy.sign(P1.X)][numpy.sign(P1.X)==numpy.sign(P2.X)]
	T1,T2 = CheckCollisions(P1,P2)
	P1T=P1.Frame({"Side":P1.X>P2.X,"Fault":Fault,"Triggers":T1,"Stage":BG,"Controller":P1C.Character(pygame),"Other Player":P2})
	P2T=P2.Frame({"Side":P2.X>P1.X,"Fault":-Fault,"Triggers":T2,"Stage":BG,"Controller":P2C.Character(pygame),"Other Player":P1})
	if P1.X<BG.Bounds[0]:
		P1.X=BG.Bounds[0]
		P1.XV=-P1.XV
	if P2.X<BG.Bounds[0]:
		P2.X=BG.Bounds[0]
		P2.XV=-P2.XV
	if P1.X>BG.Bounds[1]:
		P1.X=BG.Bounds[1]
		P1.XV=-P1.XV
	if P2.X>BG.Bounds[1]:
		P2.X=BG.Bounds[1]
		P2.XV=-P2.XV
	if P1.Y<BG.Bounds[2]:
		P1.Y=BG.Bounds[2]
		P1.YV=-P1.YV
	if P2.Y<BG.Bounds[2]:
		P2.Y=BG.Bounds[2]
		P2.YV=-P2.YV
	try:
		Clock.tick(24)
	except:
		Clock=pygame.time.Clock() #Creates a clock if one does not exist.
		Clock.tick(24)
	#print(Clock.get_fps())
	Renderer.Render(P1,P2,BG,0,P1T,P2T,Clock) #Calls the render function.
	return P1.Health<1, P2.Health<1
	pass
def Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStart):
	global Clock
	Clock=pygame.time.Clock()
	Renderer.Render(P1,P2,BG,1,{"Sounds":[GameStart]})
	pygame.time.wait(2000)
	while True:
		X,Y = Frame(P1,P2,Renderer,pygame,P1C,P2C,BG)
		if X or Y:
			return X,Y