class Stage:
	def __init__(self,pygame):
		self.Fault=[
		P2F2(pygame),
		P2F1(pygame),
		F0(pygame),
		P1F1(pygame),
		P1F2(pygame),
		]
		self.DuelFaultCameraOffset=200
		self.FaultOffset=2
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
		"Sprite":pygame.image.load("Stages/RoyalDuel/NF.png"),
		"X":0,
		"Y":-100,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass
class P1F1:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/RoyalDuel/P1F1.png"),
		"X":0,
		"Y":-100,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass
class P2F1:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/RoyalDuel/P2F1.png"),
		"X":0,
		"Y":-100,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass
class P1F2:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/RoyalDuel/P1F2.png"),
		"X":0,
		"Y":-100,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass
class P2F2:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-750]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/RoyalDuel/P2F2.png"),
		"X":0,
		"Y":-100,
		"Z":0,
		"H":3000,
		"W":3000,
		"Large":2,
		"Blending":None,
		}]
		pass