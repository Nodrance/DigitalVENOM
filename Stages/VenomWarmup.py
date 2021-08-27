class Stage:
	def __init__(self,pygame):
		self.Fault=[
		F0(pygame),
		]
		self.DuelFaultCameraOffset=200
		self.FaultOffset=0
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/VenomWarmup/BG.bmp"),
		"X":0,
		"Y":0,
		"Z":0,
		"H":1500,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class F0:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/VenomWarmup/BG.bmp"),
		"X":0,
		"Y":0,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass