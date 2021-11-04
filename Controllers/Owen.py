class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame,PygameEvents):
		keys=pygame.key.get_pressed()
		R={
		"l":0,
		"m":0,
		"h":0,
		}
		R["X"]=keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]
		R["Y"]=keys[pygame.K_DOWN]-keys[pygame.K_UP]
		R["X2"]=0
		R["Y2"]=0
		R["Jump2"]=0
		R["Jump"]=keys[pygame.K_DOWN]-(keys[pygame.K_UP] or keys[pygame.K_g])==-1
		for Event in PygameEvents:
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_b:
					R["l"]=1
				if Event.key==pygame.K_n:
					R["m"]=1
				if Event.key==pygame.K_m:
					R["h"]=1
				if Event.key in [pygame.K_RIGHT or pygame.K_LEFT]:
					R["X2"]=R["X"]
				if Event.key in [pygame.K_UP or pygame.K_DOWN]:
					R["Y2"]=R["Y"]
					R["Jump2"]=max(-R["Y2"],0)
		return R
		"""return {
		"X":keys[pygame.K_RIGHT]-keys[pygame.K_LEFT],
		"Y":keys[pygame.K_DOWN]-(keys[pygame.K_UP] or keys[pygame.K_g]),
		"Jump":keys[pygame.K_DOWN]-(keys[pygame.K_UP] or keys[pygame.K_g])==-1,#keys[pygame.K_l],
		"Jab":0,#keys[pygame.K_h] or keys[pygame.K_g],
		"Strong":0,#keys[pygame.K_j] or keys[pygame.K_g],
		"Fierce":0,#keys[pygame.K_k] or keys[pygame.K_g],
		"Short":0,#keys[pygame.K_b] or (keys[pygame.K_v] and self.Frame%2),# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		"Forward":0,#keys[pygame.K_n],# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		"Roundhouse":0,#keys[pygame.K_m],# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		"l":keys[pygame.K_b],
		"m":keys[pygame.K_n],
		"h":keys[pygame.K_m],
		}"""
		pass
	pass