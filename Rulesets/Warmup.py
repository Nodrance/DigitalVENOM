import random
def Match(pygame,Renderer,Engine,P1C,P2C,F1,F2,BG):
	GameStartSound=pygame.mixer.Sound("Sounds/GameStart1.wav")
	P1=F1
	P1.Reset(0,pygame)
	P2=F2
	P2.Reset(1,pygame)
	return Engine.Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStartSound)