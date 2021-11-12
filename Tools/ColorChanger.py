import os,pygame;DIR=[]
def Old():
	#This script is used for the purposes of development only and should not be executed during DigitalVENOM runtime.
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
def SwapColors(dictionary,color_grid,colors_id):
	#This can run on runtime, but it's slow and now obsolete
	Image=color_grid;S=pygame.surfarray.array2d(Image)
	C={}
	for X in range(Image.get_width()):
		try:C[str(Image.unmap_rgb(S[X][0]))]=Image.unmap_rgb(S[X][colors_id])
		except:pass
	for i in dictionary.keys():
		Image=dictionary[i];S=pygame.surfarray.array2d(Image)
		for X in range(Image.get_width()):
			for Y in range(Image.get_height()):
				try:Image.set_at((X,Y),C[str(Image.unmap_rgb(S[X][Y]))])
				except:pass
def FastSwapColors(dictionary,color_grid,colors_id):
	#This shit is built to last
	Image=color_grid;S=pygame.surfarray.array2d(Image);L=Image.get_width()
	for i in dictionary.keys():
		for X in range(L):
			try:pygame.transform.threshold(dictionary[i],dictionary[i],Image.unmap_rgb(S[X][0]),threshold=(0,0,0,0),set_color=Image.unmap_rgb(S[X][colors_id]),inverse_set=1)
			except:pass
		pygame.transform.threshold(dictionary[i],dictionary[i],(0,0,0),threshold=(0,0,0,0),set_color=(0,0,0,0),inverse_set=1)
def FastSwapImageColors(image,color_grid,colors_id):
	#Same as the last function, but for just one image.
	pygame.transform.threshold(image,image,(0,0,0,0),threshold=(0,0,0,0),set_color=(132,65,93),inverse_set=1)
	Image=color_grid;S=pygame.surfarray.array2d(Image);L=Image.get_width()
	for X in range(L):
		try:pygame.transform.threshold(image,image,Image.unmap_rgb(S[X][0]),threshold=(0,0,0,0),set_color=Image.unmap_rgb(S[X][colors_id]),inverse_set=1)
		except:pass
	pygame.transform.threshold(image,image,(132,65,93),threshold=(0,0,0,0),set_color=(0,0,0,0),inverse_set=1)
	return image
def FasterSwapColors(dictionary,color_grid,colors_id):
	#The speed is getting out of hand
	Image=color_grid;S=pygame.surfarray.array2d(Image);L=Image.get_width()
	for i in dictionary.keys():
		image_pixel_array=pygame.PixelArray(dictionary[i])
		for X in range(L):
			try:image_pixel_array.replace(Image.unmap_rgb(S[X][0]),Image.unmap_rgb(S[X][colors_id]))
			except:pass
def FasterSwapImageColors(image,color_grid,colors_id):
	#The above function, but for only one image
	Image=color_grid;S=pygame.surfarray.array2d(Image);L=Image.get_width()
	image_pixel_array=pygame.PixelArray(image)
	for X in range(L):
		try:image_pixel_array.replace(Image.unmap_rgb(S[X][0]),Image.unmap_rgb(S[X][colors_id]))
		except:pass
	return image