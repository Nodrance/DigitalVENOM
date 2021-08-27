class Controller:
	def __init__(self,pygame):
		pass
	def Character(self,pygame):
		keys=pygame.key.get_pressed()
		return {
		"X":keys[pygame.K_d]-keys[pygame.K_a],
		"Y":keys[pygame.K_s]-keys[pygame.K_w],
		"Jump":keys[pygame.K_q],
		"Jab":keys[pygame.K_e],
		"Strong":keys[pygame.K_r],
		"Fierce":keys[pygame.K_t],
		"Short":keys[pygame.K_f],
		"Forward":keys[pygame.K_u],
		"Roundhouse":keys[pygame.K_y],
		"Block":0,#keys[pygame.K_o],
		"Special":0,#keys[pygame.K_i],
		}