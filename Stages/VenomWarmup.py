class Stage:
	def __init__(self,pygame):
		self.Bounds=[-750,750,-1000]
		self.Sprites=[{
		"Sprite":pygame.image.load("Stages/VenomWarmup/Background.png"),
		"X":0,
		"Y":0,
		"Z":3,
		"H":5000,
		"W":5000,
		"Large":1,
		"Blending":None,
		},
		{
		"Sprite":pygame.image.load("Stages/VenomWarmup/Floor.png"),
		"X":0,
		"Y":0,
		"Z":0,
		"H":2500,
		"W":2500,
		"Large":1,
		"Blending":None,
		}]
		pass