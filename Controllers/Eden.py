class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame):
		keys=pygame.key.get_pressed()
		return {
		"X":keys[pygame.K_d]-keys[pygame.K_a],
		"Y":keys[pygame.K_s]-keys[pygame.K_w],
		"Jump":keys[pygame.K_0],
		"Jab":keys[pygame.K_7],
		"Strong":keys[pygame.K_8],
		"Fierce":keys[pygame.K_9],
		"Short":keys[pygame.K_u],
		"Forward":keys[pygame.K_i],
		"Roundhouse":keys[pygame.K_o],
		}