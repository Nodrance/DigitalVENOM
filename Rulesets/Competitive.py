def Match(pygame,Renderer,Engine,P1C,P2C,F1,F2,BG):
	GameStartSound=pygame.mixer.Sound("Sounds/GameStart0.wav")
	GameOn=1
	P1=F1#(0,pygame)
	P2=F2#(1,pygame)
	while GameOn:
		P1.Reset(0)
		P2.Reset(1)
		Y,X=Engine.Game(P1,P2,Renderer,pygame,P1C,P2C,BG,GameStartSound,SaveReplay=1)
		if X and not Y:
			if Renderer.P1W:
				GameOn=False
				return 0,1
			else:
				Renderer.P1W+=1
		if Y and not X:
			if Renderer.P2W:
				GameOn=False
				return 1,0
			else:
				Renderer.P2W+=1
			pass
		if not (X or Y):
			return (0,0)
		pass
	pass