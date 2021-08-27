class Controller:
	def __init__(self,pygame):
		self.Joystick=pygame.joystick.Joystick(0)
		self.Joystick.init()
		self.current = False
		pass

	def Character(self,pygame):
		
		Y=0
		B=1
		A=2
		X=3
		L=4
		R=5
		ZL=6
		ZR=7
		Minus=8
		Plus=9
		JSL=10
		JSR=11
		Home=12
		Capture=13
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
		"Jab":self.Joystick.get_button(Y),
		"Strong":self.Joystick.get_button(X),
		"Fierce":self.Joystick.get_button(L),
		"Short":self.Joystick.get_button(B) or self.Joystick.get_button(R),
		"Forward":self.Joystick.get_button(A) or self.Joystick.get_button(R),
		"Roundhouse":self.Joystick.get_button(ZR) or self.Joystick.get_button(R),
		"Block":0,#self.Joystick.get_button(ZL),
		"Special":0,#self.Joystick.get_button(R),
		}
		pass
	pass