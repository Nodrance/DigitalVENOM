class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame):
		keys=pygame.key.get_pressed()
		return {
		"X":keys[pygame.K_d]-keys[pygame.K_a],
		"Y":keys[pygame.K_s]-keys[pygame.K_w],
		"Jump":keys[pygame.K_0],
		"Jab":0,#keys[pygame.K_7],
		"Strong":0,#keys[pygame.K_8],
		"Fierce":0,#keys[pygame.K_9],
		"Short":0,#keys[pygame.K_u],
		"Forward":0,#keys[pygame.K_i],
		"Roundhouse":0,#keys[pygame.K_o],
		"l":keys[pygame.K_u],
		"m":keys[pygame.K_i],
		"h":keys[pygame.K_o],
		}