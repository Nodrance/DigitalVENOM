class Controller:
	def __init__(self,pygame):
		self.Joystick=pygame.joystick.Joystick(0)
		self.Joystick.init()
		pass
	def Character(self,pygame):
		return {
		"X":max(-1,int(self.Joystick.get_axis(0)*2)),
		"Y":max(-1,int(self.Joystick.get_axis(1)*2)),
		"Jump":self.Joystick.get_axis(1)<-0.5,
		"Jab":self.Joystick.get_button(0),
		"Strong":self.Joystick.get_button(1),
		"Fierce":self.Joystick.get_button(2),
		"Short":self.Joystick.get_button(3),
		"Forward":self.Joystick.get_button(4),
		"Roundhouse":self.Joystick.get_button(5),
		"Block":self.Joystick.get_axis(2)<-0.5,
		"Special":self.Joystick.get_axis(2)>0.5,
		}
		pass
	pass