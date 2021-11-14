class Stage:
	def __init__(self,pygame):
		self.Fault=[
		P2F3(pygame),
		P2F2(pygame),
		P2F1(pygame),
		F0(pygame),
		P1F1(pygame),
		P1F2(pygame),
		P1F3(pygame),
		]
		self.DuelFaultCameraOffset=200
		self.FaultOffset=3
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/F0"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":875,
		"Z":0,
		"H":1750,
		"W":2500,
		"Large":2,
		"Blending":None,
		}]
		pass
class F0:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/F0"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P1F1:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P1F1.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P2F1:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P2F1.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P1F2:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P1F2.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P2F2:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P2F2.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P1F3:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P1F3.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass
class P2F3:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/City Lights/P2F3.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":2,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/City Lights/P0Floor.png"),
		"X":0,
		"Y":375,
		"Z":0,
		"H":750,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		pass