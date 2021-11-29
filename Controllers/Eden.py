class Controller:
	def __init__(self,pygame):
		self.Down=pygame.K_s
		self.Up=pygame.K_w
		self.Left=pygame.K_a
		self.Right=pygame.K_d
		self.l=pygame.K_u
		self.m=pygame.K_i
		self.h=pygame.K_o
		self.v=pygame.K_y
	def Character(self,pygame,PygameEvents):
		keys=pygame.key.get_pressed()
		R={
		"l":0,
		"m":0,
		"h":0,
		"v":0,
		}
		R["X"]=keys[self.Right]-keys[self.Left]
		R["Y"]=keys[self.Down]-keys[self.Up]
		R["X2"]=0
		R["Y2"]=0
		R["Jump2"]=0
		R["Jump"]=keys[self.Down]-keys[self.Up]==-1
		for Event in PygameEvents:
			if Event.type==pygame.KEYDOWN:
				if Event.key==self.l:
					R["l"]=1
				if Event.key==self.m:
					R["m"]=1
				if Event.key==self.h:
					R["h"]=1
				if Event.key==self.v:
					R["v"]=1
				if Event.key==self.Right or Event.key==self.Left:
					R["X2"]=R["X"]
				if Event.key==self.Up or Event.key==self.Down:
					R["Y2"]=R["Y"]
					R["Jump2"]=max(-R["Y2"],0)
		return R