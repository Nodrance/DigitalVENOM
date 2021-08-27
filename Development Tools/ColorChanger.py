#This script is used for the purposes of development only and should not be executed during DigitalVENOM runtime.
import os,pygame;DIR=[]
for file in os.listdir("64Alt/"):
	if file.endswith(".png"):DIR.append("64Alt/"+file)
C={
	"(255, 0, 255, 255)":(0,255,255),
	"(0, 255, 255, 255)":(255,0,255),
}
for i in DIR:
	Image=pygame.image.load(i);S=pygame.surfarray.array2d(Image)
	for X in range(Image.get_width()):
		for Y in range(Image.get_height()):
			try:Image.set_at((X,Y),C[str(Image.unmap_rgb(S[X][Y]))])
			except:pass
	pygame.image.save(Image,i)