import random
def Match(pygame,Renderer,Engine,P1C,P2C,F1,F2,BG):
	GSList=[
	pygame.mixer.Sound("Sounds/GameStart1.wav"),
	pygame.mixer.Sound("Sounds/GameStart2.wav"),
	]
	GameStartSound=random.choice(GSList)
	P1=F1(0,pygame)
	P2=F2(1,pygame)
	return Engine.Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStartSound)