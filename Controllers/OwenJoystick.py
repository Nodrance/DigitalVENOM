class Controller:
	def __init__(self,pygame):
		self.Joystick=pygame.joystick.Joystick(0)
		self.Joystick.init()
		self.current = False
		self.OX=0
		self.OY=0
	def Character(self,pygame,PygameEvents):
		"""A=0
		B=1
		X=2
		Y=3
		L=4
		R=5
		L=9
		R=10
		ZL=6
		ZR=7
		Minus=4
		Plus=6
		#JSL=10
		#JSR=11
		#Home=12
		#Capture=13
		JS1RL=0
		JS1DU=1
		JS2RL=2
		JS2DU=3
		#hat(0)[0] is RL, hat(0)[1] is DU 
		#last=self.current
		#self.current=self.Joystick.get_button(Y)
		#if (self.current != last) and (self.current == True):
		#	print("")
		#	print(self.Joystick.get_hat(0)[0])
		#	print(self.Joystick.get_hat(0)[1])

		return {
		"Jump":self.Joystick.get_axis(1)<-0.5,
		"l":self.Joystick.get_button(Y),
		"m":self.Joystick.get_button(B),
		"h":self.Joystick.get_button(A),
		}"""
		R={
		"l":0,
		"m":0,
		"h":0,
		"v":0,
		"X":max(-1,int(self.Joystick.get_axis(0)*1.99)),
		"Y":max(-1,int(self.Joystick.get_axis(1)*1.99)),
		}
		R["X2"]=0
		R["Y2"]=0
		R["Jump2"]=0
		R["Jump"]=self.Joystick.get_axis(1)<-0.5
		for Event in PygameEvents:
			if Event.type==pygame.JOYBUTTONDOWN:
				if Event.instance_id==self.Joystick.get_instance_id():
					if Event.button==3:
						R["l"]=1
					if Event.button==1:
						R["m"]=1
					if Event.button==0:
						R["h"]=1
					if Event.button==2:
						R["v"]=1
			if Event.type==pygame.JOYAXISMOTION:
				if Event.instance_id==self.Joystick.get_instance_id():
					if R["X"]!=self.OX: #Event.axis==0
						R["X2"]=R["X"]
					if R["Y"]!=self.OY: #Event.axis==1
						R["Y2"]=R["Y"]
						R["Jump2"]=max(-R["Y2"],0)
		self.OX=R["X"]
		self.OY=R["Y"]
		return R
	pass