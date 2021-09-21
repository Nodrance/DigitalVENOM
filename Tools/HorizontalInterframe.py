import pygame

def InterH(SurfList):
	S1=R3D(SurfList)
	S2=[]
	for i in S1:
		S2.append(pygame.transform.scale2x(i))
	S3=[]
	for i in S2:
		S3.append(pygame.transform.scale(i,(SurfList[0].get_width(),i.get_height())))
	OutputList=R3D(S3)
	return OutputList

def R3D(SurfList):
	OutputList=[]
	for i in range(SurfList[0].get_height()):
		OutputList.append(pygame.Surface((SurfList[0].get_width(),len(SurfList))))
	for i in range(len(OutputList)):
		for X in range(OutputList[i].get_width()):
			for Y in range(OutputList[i].get_height()):
				OutputList[i].set_at((X,Y),SurfList[Y].get_at((X,i)))
	return OutputList

if __name__ == "__main__":
	I1=pygame.transform.scale2x(pygame.image.load("Forward1.png"))
	I2=pygame.transform.scale2x(pygame.image.load("Forward2.png"))
	pygame.image.save(I1,"Output/I1.png")
	pygame.image.save(I2,"Output/I2.png")
	X=InterH([I1,I2])
	j=0
	for i in X:
		pygame.image.save(i,"Output/frame"+str(j)+".png")
		j+=1