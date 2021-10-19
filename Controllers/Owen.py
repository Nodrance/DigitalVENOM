class Controller:
	def __init__(self,pygame):
		self.Frame=0
		pass
	def Character(self,pygame):
		keys=pygame.key.get_pressed()
		self.Frame+=1
		return {
		"X":keys[pygame.K_RIGHT]-keys[pygame.K_LEFT],
		"Y":keys[pygame.K_DOWN]-(keys[pygame.K_UP] or keys[pygame.K_g]),
		"Jump":keys[pygame.K_l],
		"Jab":keys[pygame.K_h] or keys[pygame.K_g],
		"Strong":keys[pygame.K_j] or keys[pygame.K_g],
		"Fierce":keys[pygame.K_k] or keys[pygame.K_g],
		"Short":keys[pygame.K_b] or (keys[pygame.K_v] and self.Frame%2),# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		"Forward":keys[pygame.K_n],# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		"Roundhouse":keys[pygame.K_m],# or abs(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]),
		}
		pass
	pass