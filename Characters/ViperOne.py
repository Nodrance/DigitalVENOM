class Default:
	def __init__(self,Player,DIR,MaxHealth=500,Offset=(0,-64),Height=128,Width=128):
		self.StartDistance=100
		self.MaxHealth=MaxHealth
		self.Player=Player
		self.Offset=Offset
		self.Height=Height
		self.Width=Width
		self.DIR=DIR
		pass
	def Reset(self,CHA):
		CHA.Health=self.MaxHealth
		CHA.MaxHealth=self.MaxHealth
		CHA.X=2*self.StartDistance*self.Player-self.StartDistance
		CHA.Y=0
		CHA.XV=0
		CHA.YV=0
		CHA.KV=0
		CHA.Grabbed=False
		CHA.Offset=self.Offset
		CHA.W=self.Width
		CHA.H=self.Height
		CHA.Combo=0
		CHA.Stun=0
		CHA.State=CHA.Idle
		CHA.StateFrame=0
		CHA.SSN="Idle"
		CHA.AirDashable=1
		CHA.AirDashTime=0
		CHA.HitLag=0
		CHA.BackState=CHA.Idle
		CHA.Sounds=[]
		CHA.HitLag=0
		CHA.LTags={}
		pass
	def ViperZero(self,AN):
		A=open(self.DIR+"/Attacks/"+AN+".vp0").read()
		B=A.split("\n\n")
		C={"Format":B[0],"Frames":int(B[1])-1,"Animation":B[2].split("\n"),"Triggers":[]}
		D=B[3]
		for i in D.split("\n"):
			E=[]
			for j in i.split(";"):
				F=j.split(",")
				try:
					E.append({
						"Box":[[int(F[0]),int(F[1])],[int(F[2]),int(F[3])]],
						"Type":"Hurt",
						})

				except:
					pass
			C["Triggers"].append(E)
		D=B[4]
		G=0
		for i in D.split("\n"):
			E=[]
			for j in i.split(";"):
				F=j.split(",")
				try:
					try:
						HL=int(F[9])
					except:
						HL=int(3)
					E.append({
						"Box":[[int(F[0]),int(F[1])],[int(F[2]),int(F[3])]],
						"Damage":int(F[4]),
						"Chip Damage":int(F[5]),
						"Type":"Hit",
						"Stun":int(F[6]),
						"Block Stun":int(F[7]),
						"Knockback":int(F[8]),
						"Hit Lag":HL,
						})
				except:
					pass
			for j in E:
				C["Triggers"][G].append(j)
			G+=1
		return C
		pass