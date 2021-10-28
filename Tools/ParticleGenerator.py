import pygame,random,math
def GenerateSlash(Res,Point1,Point2):
	X=pygame.Surface(Res)
	for i in range(256):
		Y=pygame.Surface(Res)
		P1=(Point1[0]+random.randint(-16,16),Point1[1]+random.randint(-16,16))
		P2=(Point2[0]+random.randint(-16,16),Point2[1]+random.randint(-16,16))
		pygame.draw.line(Y,(1,0,1),P1,P2,random.randint(8,16))
		X.blit(Y,(0,0),special_flags=pygame.BLEND_RGB_ADD)
	return X
def GenerateRadial(Res):
	X=pygame.Surface((Res,Res))
	for i in range(256):
		Y=pygame.Surface((Res,Res))
		pygame.draw.circle(Y,(1,0,1),(Res/2,Res/2),int(Res/2*i/256))
		X.blit(Y,(0,0),special_flags=pygame.BLEND_RGB_ADD)
	return X
def GenerateSpikes(Res,Points):
	X=pygame.Surface((Res,Res))
	Z=[]
	for i in range(Points):
		L=random.randint(1,256)
		Z.append((L/256*(Res-16)/2*math.sin(i/Points*math.pi*2),L/256*(Res-16)/2*math.cos(i/Points*math.pi*2)))
	G=[]
	Color=[random.randint(0,1),random.randint(0,1),random.randint(0,1)]
	Color[random.randint(0,2)]=1
	Color=tuple(Color)
	for i in range(256):
		NewZ=[(P[0]+random.randint(-16,16)+int(Res/2),P[1]+random.randint(-16,16)+int(Res/2)) for P in Z]
		Y=pygame.Surface((Res,Res))
		pygame.draw.polygon(Y,Color,NewZ)
		X.blit(Y,(0,0),special_flags=pygame.BLEND_RGB_ADD)
		if i%10==0:
			G.insert(0,X.copy())
	return G