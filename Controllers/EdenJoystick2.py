class Controller:
	def __init__(self,pygame):
		self.Joystick=pygame.joystick.Joystick(1)
		self.Joystick.init()
		self.current = False
	def Character(self,pygame):
		A=0
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
		"""last=self.current
		self.current=self.Joystick.get_button(Y)
		if (self.current != last) and (self.current == True):
			print("")
			print(self.Joystick.get_hat(0)[0])
			print(self.Joystick.get_hat(0)[1])"""

		return {
		"X":max(-1,int(self.Joystick.get_axis(0)*1.99)),
		"Y":max(-1,int(self.Joystick.get_axis(1)*1.99)),
		"Jump":self.Joystick.get_axis(1)<-0.5,
		"l":self.Joystick.get_button(Y),
		"m":self.Joystick.get_button(B),
		"h":self.Joystick.get_button(A),
		}
		pass
	pass