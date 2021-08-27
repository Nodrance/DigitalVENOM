class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame):
		keys=pygame.key.get_pressed()
		return {
		"X":keys[pygame.K_RIGHT]-keys[pygame.K_LEFT],
		"Y":keys[pygame.K_DOWN]-keys[pygame.K_UP],
		"Jump":keys[pygame.K_l],
		"Jab":keys[pygame.K_h],
		"Strong":keys[pygame.K_j],
		"Fierce":keys[pygame.K_k],
		"Short":keys[pygame.K_b] or (abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])and keys[pygame.K_UP]),
		"Forward":keys[pygame.K_n] or (abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])and keys[pygame.K_UP]),
		"Roundhouse":keys[pygame.K_m] or (abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])and keys[pygame.K_UP]),
		"Block":keys[pygame.K_g],
		"Special":keys[pygame.K_v],
		}
		pass
	pass