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
		"Sprite":pygame.image.load("Stages/VenomCompetitive/Background.png"),
		"X":0,
		"Y":-750,
		"Z":3,
		"H":1500,
		"W":1500,
		"Large":2,
		"Blending":None,
		}]
		self.Polygons=[
		{
		"Color":(0,255,255),
		"Points":[
		(-750,0,-0.5),
		(-750,0,3),
		(0,0,3),
		(0,0,-0.5),
		]
		},
		{
		"Color":(255,0,255),
		"Points":[
		(0,0,-0.5),
		(0,0,3),
		(750,0,3),
		(750,0,-0.5),
		]
		},
		{
		"Color":(0,255,255),
		"Points":[
		(-750,-1500,-0.5),
		(-750,-1500,3),
		(0,-1500,3),
		(0,-1500,-0.5),
		]
		},
		{
		"Color":(255,0,255),
		"Points":[
		(0,-1500,-0.5),
		(0,-1500,3),
		(750,-1500,3),
		(750,-1500,-0.5),
		]
		},
		{
		"Color":(0,255,255),
		"Points":[
		(-750,-1500,-0.5),
		(-750,-1500,3),
		(-750,0,3),
		(-750,0,-0.5),
		]
		},
		{
		"Color":(255,0,255),
		"Points":[
		(750,-1500,-0.5),
		(750,-1500,3),
		(750,0,3),
		(750,0,-0.5),
		]
		},
		]
		"""{
		"Color":(255,255,255),
		"Points":[
		(-750,0,3),
		(-750,-750,3),
		(750,-750,3),
		(750,0,3),
		]
		},"""
		pass