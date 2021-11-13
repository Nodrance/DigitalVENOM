class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame,PygameEvents):
		keys=pygame.key.get_pressed()
		R={
		"l":0,
		"m":0,
		"h":0,
		"v":0,
		}
		R["X"]=keys[pygame.K_d]-keys[pygame.K_a]
		R["Y"]=keys[pygame.K_s]-keys[pygame.K_w]
		R["X2"]=0
		R["Y2"]=0
		R["Jump2"]=0
		R["Jump"]=keys[pygame.K_s]-keys[pygame.K_w]==-1
		for Event in PygameEvents:
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_u:
					R["l"]=1
				if Event.key==pygame.K_i:
					R["m"]=1
				if Event.key==pygame.K_o:
					R["h"]=1
				if Event.key==pygame.K_y:
					R["y"]=1
				if Event.key in [pygame.K_d or pygame.K_a]:
					R["X2"]=R["X"]
				if Event.key in [pygame.K_w or pygame.K_s]:
					R["Y2"]=R["Y"]
					R["Jump2"]=max(-R["Y2"],0)
		return R
		"""keys=pygame.key.get_pressed()
		return {
		"X":keys[pygame.K_d]-keys[pygame.K_a],
		"Y":keys[pygame.K_s]-keys[pygame.K_w],
		"Jump":keys[pygame.K_0],
		"Jab":0,#keys[pygame.K_7],
		"Strong":0,#keys[pygame.K_8],
		"Fierce":0,#keys[pygame.K_9],
		"Short":0,#keys[pygame.K_u],
		"Forward":0,#keys[pygame.K_i],
		"Roundhouse":0,#keys[pygame.K_o],
		"l":keys[pygame.K_u],
		"m":keys[pygame.K_i],
		"h":keys[pygame.K_o],
		}"""