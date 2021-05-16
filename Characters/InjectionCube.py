import copy
class Character:
	def __init__(self,P,pygame):
		self.X=500*P-250
		self.Y=0
		self.Offset=(0,-32)
		self.XV=0
		self.YV=0
		self.W=64
		self.H=64
		self.KV=0
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Health=500
		self.MaxHealth=500
		self.Sprites={
		"blank":pygame.image.load("Characters/InjectionCube/Sprites/blank.png").convert(),
		"idle_1":pygame.image.load("Characters/InjectionCube/Sprites/idle_1.png").convert(),
		"idle_2":pygame.image.load("Characters/InjectionCube/Sprites/idle_2.png").convert(),
		"error_404":pygame.image.load("Characters/InjectionCube/Sprites/error_404.png").convert(),
		"attack_right":pygame.image.load("Characters/InjectionCube/Sprites/attack_right.png").convert(),
		"wifi_1":pygame.image.load("Characters/InjectionCube/Sprites/wifi_1.png").convert(),
		"wifi_2":pygame.image.load("Characters/InjectionCube/Sprites/wifi_2.png").convert(),
		"wifi_3":pygame.image.load("Characters/InjectionCube/Sprites/wifi_3.png").convert(),
		"wifi_4":pygame.image.load("Characters/InjectionCube/Sprites/wifi_4.png").convert(),
		"loading_1":pygame.image.load("Characters/InjectionCube/Sprites/loading_1.png").convert(),
		"loading_2":pygame.image.load("Characters/InjectionCube/Sprites/loading_2.png").convert(),
		"loading_3":pygame.image.load("Characters/InjectionCube/Sprites/loading_3.png").convert(),
		"loading_4":pygame.image.load("Characters/InjectionCube/Sprites/loading_4.png").convert(),
		"loading_5":pygame.image.load("Characters/InjectionCube/Sprites/loading_5.png").convert(),
		"loading_6":pygame.image.load("Characters/InjectionCube/Sprites/loading_6.png").convert(),
		"loading_7":pygame.image.load("Characters/InjectionCube/Sprites/loading_7.png").convert(),
		"loading_8":pygame.image.load("Characters/InjectionCube/Sprites/loading_8.png").convert(),
		"startup_1":pygame.image.load("Characters/InjectionCube/Sprites/startup_1.png").convert(),
		"startup_2":pygame.image.load("Characters/InjectionCube/Sprites/startup_2.png").convert(),
		"startup_3":pygame.image.load("Characters/InjectionCube/Sprites/startup_3.png").convert(),
		"beam_1":pygame.image.load("Characters/InjectionCube/Sprites/beam_1.png"),
		"beam_2":pygame.image.load("Characters/InjectionCube/Sprites/beam_2.png"),
		"beam_3":pygame.image.load("Characters/InjectionCube/Sprites/beam_3.png"),
		}
		self.Sprite=self.Sprites["blank"]
		self.Stun=0
		self.State=self.Idle
		self.StateFrame=0
		self.BackState=self.Idle
		self.JabData=self.ViperZero("Jab")
		self.StrongData=self.ViperZero("Strong")
		self.FierceData=self.ViperZero("Fierce")
		self.ShortData=self.ViperZero("Short")
		self.ForwardData=self.ViperZero("Forward")
		self.RoundhouseData=self.ViperZero("Roundhouse")
		self.ForwardDashData=self.ViperZero("Forward Dash")
		self.BackDashData=self.ViperZero("Back Dash")
		self.AirDashTime=0
		self.AirDashable=1
		self.DF=0
		self.HitSound=0
		self.HitSounds=[
		pygame.mixer.Sound("Characters/InjectionCube/Sounds/HitSound1.wav"),
		pygame.mixer.Sound("Characters/InjectionCube/Sounds/HitSound2.wav"),
		pygame.mixer.Sound("Characters/InjectionCube/Sounds/HitSound3.wav"),
		pygame.mixer.Sound("Characters/InjectionCube/Sounds/HitSound4.wav"),
		]
	def Reset(self,P,pygame):
		self.X=500*P-250
		self.Y=0
		self.Offset=(0,-32)
		self.XV=0
		self.YV=0
		self.W=64
		self.H=64
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Health=500
		self.MaxHealth=500
		self.Sprite=self.Sprites["blank"]
		self.Stun=0
		self.State=self.Idle
		self.StateFrame=0
		self.BackState=self.Idle
		self.AirDashTime=0
		self.AirDashable=1
		self.DF=0
		self.HitSound=0
	def ViperZero(self,AN):
		A=open("Characters/InjectionCube/Attacks/"+AN+".vp0").read()
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
					E.append({
						"Box":[[int(F[0]),int(F[1])],[int(F[2]),int(F[3])]],
						"Damage":int(F[4]),
						"Chip Damage":int(F[5]),
						"Type":"Hit",
						"Stun":int(F[6]),
						"Block Stun":int(F[7]),
						"Knockback":int(F[8]),
						"Hit Lag":int(3),
						})
				except:
					pass
			for j in E:
				C["Triggers"][G].append(j)
			G+=1
		return C
		pass
	def HitFlip(self):
		T=[]
		for H in copy.deepcopy(self.Triggers):
			X=H
			H["Box"]=[[-H["Box"][0][1],-H["Box"][0][0]],[H["Box"][1][0],H["Box"][1][1]]]
			T.append(H)
		self.Triggers=T
	def Frame(self,Tags):
		Damage=0
		ChipDamage=0
		Stun=0
		BlockStun=0
		Knockback=0
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hurt" and i[1]["Type"]=="Hit":
				Damage+=i[1]["Damage"]
				ChipDamage+=i[1]["Chip Damage"]
				Stun+=i[1]["Stun"]
				BlockStun+=i[1]["Block Stun"]
				Knockback+=i[1]["Knockback"]
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt":
				self.XV=Tags["Side"]*10-5
		if Damage>0:
			if not self.DF:
				if self.State==self.Block or self.State==self.BlockStun:
					self.Health-=ChipDamage
					self.XV=Tags["Side"]*20-10
					self.State=self.BlockStun
					self.Stun=BlockStun
				else:
					self.Health-=Damage
					if Knockback>0:
						self.YV=-Knockback
						self.XV=Knockback*2*Tags["Side"]-Knockback
						self.KV=Knockback
					self.State=self.HitStun
					self.Stun=Stun
			self.DF=1
		else:
			self.DF=0
		if self.State==self.BackState:
			self.StateFrame+=1
		else:
			self.StateFrame=0
			self.BackState=self.State
		R=self.State(Tags)
		self.X+=self.XV
		self.Y+=self.YV
		if self.Y>0:
			self.Y=0
		if Tags["Side"]==1:
			#self.Sprite=self.Sprites["blank"]
			self.HitFlip()
		return R
	def Idle(self,Tags):
		self.XV=0
		if self.StateFrame%48 in [26,27,28]:
			self.Sprite=self.Sprites["idle_2"]
		else:
			self.Sprite=self.Sprites["idle_1"]
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		if Tags["Controller"]["Jab"]:
			self.State=self.Jab
		if Tags["Controller"]["Strong"]:
			self.State=self.Strong
		if Tags["Controller"]["Fierce"]:
			self.State=self.Fierce
		if Tags["Controller"]["Short"]:
			self.State=self.Short
		if Tags["Controller"]["Forward"]:
			self.State=self.Forward
		if Tags["Controller"]["Roundhouse"]:
			self.State=self.Roundhouse
		if Tags["Controller"]["Block"]:
			self.State=self.Block
		self.Y=0
		self.YV=0
		if Tags["Controller"]["Jump"]:
			self.YV=-30
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == 0:
				if Tags["Controller"]["X"] == Tags["Side"]*2-1:
					self.State=self.BackWalk
				else:
					self.State=self.Walk
		return {}
	def Jump(self,Tags):
		if self.StateFrame < 1:
			self.XV=Tags["Controller"]["X"]*20
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["idle_1"]
		if Tags["Controller"]["Jab"] and self.AirDashable:
			self.AirDashTime=5
			self.XV=Tags["Side"]*-20+10
			self.State=self.AirDash
		if Tags["Controller"]["Strong"] and self.AirDashable:
			self.AirDashTime=5
			self.XV=Tags["Side"]*-40+20
			self.State=self.AirDash
		if Tags["Controller"]["Fierce"] and self.AirDashable:
			self.AirDashTime=7
			self.XV=Tags["Side"]*-50+25
			self.State=self.AirDash
		if Tags["Controller"]["Short"] and self.AirDashable:
			self.AirDashTime=5
			self.XV=Tags["Side"]*20-10
			self.State=self.AirDash
		if Tags["Controller"]["Forward"] and self.AirDashable:
			self.AirDashTime=5
			self.XV=Tags["Side"]*40-20
			self.State=self.AirDash
		if Tags["Controller"]["Roundhouse"] and self.AirDashable:
			self.AirDashTime=7
			self.XV=Tags["Side"]*50-25
			self.State=self.AirDash
		if self.Y<0 or self.YV<0:
			self.YV+=3
		else:
			self.Y=0
			self.YV=0
			if Tags["Controller"]["X"] == 0:
				self.XV=0
				self.State=self.Idle
			else:
				if Tags["Controller"]["X"] == Tags["Side"]*2-1:
					self.State=self.BackWalk
				else:
					self.State=self.Walk
		return {}
		pass
	def HitStun(self, Tags):
		self.AirDashable=1
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["error_404"]
		if self.Y<0 or self.YV<0:
			self.YV+=3
			if self.XV>0:
				self.XV=self.KV
			else:
				if self.XV<0:
					self.XV=-self.KV
				else:
					self.XV=Tags["Side"]*(self.KV*2)-self.YV
		else:
			self.XV=Tags["Side"]*20-10
			self.YV=0
			self.Y=0
		if self.StateFrame>self.Stun:
			self.Stun=0
			#self.XV=0
			if self.Y<0:
				self.State=self.Jump
			else:
				self.State=self.Idle
		if self.StateFrame==0:
			self.HitSound+=1
			self.HitSound=self.HitSound%4
			return {"Sounds":[self.HitSounds[self.HitSound]]}
		else:
			return {}
		pass
	def BlockStun(self, Tags):
		self.AirDashable=1
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["startup_3"]
		if self.Y<0 or self.YV<0:
			self.YV+=10
		else:
			self.YV=0
			self.Y=0
		self.XV=Tags["Side"]*20-10
		if self.StateFrame>self.Stun:
			self.Stun=0
			#self.XV=0
			if self.Y<0:
				self.State=self.Jump
			else:
				self.State=self.Block
		return {}
		pass
	def Walk(self,Tags):
		self.Sprite=self.Sprites["idle_1"]
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		if Tags["Controller"]["Jab"]:
			self.State=self.Jab
		if Tags["Controller"]["Strong"]:
			self.State=self.Strong
		if Tags["Controller"]["Fierce"]:
			self.State=self.Fierce
		if Tags["Controller"]["Short"]:
			self.State=self.Short
		if Tags["Controller"]["Forward"]:
			self.State=self.Forward
		if Tags["Controller"]["Roundhouse"]:
			self.State=self.Roundhouse
		if Tags["Controller"]["Block"]:
			self.State=self.Block
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*20
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*4
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		if Tags["Controller"]["Jump"]:
			self.YV=-35
			self.AirDashable=1
			self.State=self.Jump
		else:
			if Tags["Controller"]["X"] == 0:
				self.XV=0
				self.State=self.Idle
			else:
				if Tags["Controller"]["X"] == Tags["Side"]*2-1:
					self.State=self.BackWalk
		return {}
	def BackWalk(self,Tags):
		self.Sprite=self.Sprites["idle_1"]
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		if Tags["Controller"]["Jab"]:
			self.State=self.Jab
		if Tags["Controller"]["Strong"]:
			self.State=self.Strong
		if Tags["Controller"]["Fierce"]:
			self.State=self.Fierce
		if Tags["Controller"]["Short"]:
			self.State=self.Short
		if Tags["Controller"]["Forward"]:
			self.State=self.Forward
		if Tags["Controller"]["Roundhouse"]:
			self.State=self.Roundhouse
		if Tags["Controller"]["Block"]:
			self.State=self.Block
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*20
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*4
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		if Tags["Controller"]["Jump"]:
			self.YV=-35
			self.AirDashable=1
			self.State=self.Jump
		else:
			if Tags["Controller"]["X"] == 0:
				self.XV=0
				self.State=self.Idle
			else:
				if Tags["Controller"]["X"] != Tags["Side"]*2-1:
					self.State=self.Walk
		return {}
	def Jab(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.JabData["Animation"][self.StateFrame]]
		self.Triggers=self.JabData["Triggers"][self.StateFrame]
		if self.StateFrame == self.JabData["Frames"]:
			self.State=self.Idle
		return {}
	def Strong(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.StrongData["Animation"][self.StateFrame]]
		self.Triggers=self.StrongData["Triggers"][self.StateFrame]
		if self.StateFrame == self.StrongData["Frames"]:
			self.State=self.Idle
		if self.StateFrame==5:
			return {"Sprites":[{"Sprite":self.Sprites["beam_2"],"X":64,"Y":-64,"W":64,"H":128}]}
		else:
			return {}
	def Fierce(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.FierceData["Animation"][self.StateFrame]]
		self.Triggers=self.FierceData["Triggers"][self.StateFrame]
		if self.StateFrame == self.FierceData["Frames"]:
			self.State=self.Idle
		if self.StateFrame==13 or self.StateFrame==14:
			return {"Sprites":[{"Sprite":self.Sprites["beam_2"],"X":0,"Y":-128,"W":64,"H":128}]}
		else:
			return {}
	def Short(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.ShortData["Animation"][self.StateFrame]]
		self.Triggers=self.ShortData["Triggers"][self.StateFrame]
		if self.StateFrame == self.ShortData["Frames"]:
			self.State=self.Idle
		if self.StateFrame==0:
			return {"Sprites":[{"Sprite":self.Sprites["beam_1"],"X":96,"Y":-32,"W":128,"H":64}]}
		else:
			return {}
	def Forward(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.ForwardData["Animation"][self.StateFrame]]
		self.Triggers=self.ForwardData["Triggers"][self.StateFrame]
		if self.StateFrame == self.ForwardData["Frames"]:
			self.State=self.Idle
		if self.StateFrame==8:
			return {"Sprites":[{"Sprite":self.Sprites["beam_1"],"X":96,"Y":-32,"W":128,"H":64}]}
		else:
			return {}
	def Roundhouse(self,Tags):
		self.YV=0
		self.XV=0
		self.Sprite=self.Sprites[self.RoundhouseData["Animation"][self.StateFrame]]
		self.Triggers=self.RoundhouseData["Triggers"][self.StateFrame]
		if self.StateFrame == self.RoundhouseData["Frames"]:
			self.State=self.Idle
		if self.StateFrame==16 or self.StateFrame==17:
			return {"Sprites":[{"Sprite":self.Sprites["beam_1"],"X":96,"Y":-32,"W":128,"H":64}]}
		else:
			return {}
	def AirDash(self,Tags):
		self.YV=0
		if Tags["Controller"]["Jump"]:
			self.XV=0
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["blank"]
		if self.StateFrame==0:
			if (self.XV>0)!=(Tags["Side"]==1):
				self.Triggers=self.ForwardDashData["Triggers"][0]
				return {"Sprites":[{"Sprite":self.Sprites["beam_3"],"X":-96,"Y":-32,"W":128,"H":64}]}
			else:
				self.Triggers=self.BackDashData["Triggers"][0]
				return {"Sprites":[{"Sprite":self.Sprites["beam_1"],"X":96,"Y":-32,"W":128,"H":64}]}
		if self.AirDashTime==0:
			#self.XV=int(self.XV/10)
			self.AirDashable=0
			self.State=self.Jump
		else:
			self.AirDashTime-=1
		return {}
	def Block(self,Tags):
		self.XV=0
		self.YV=0
		self.Sprite=self.Sprites["startup_3"]
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		if Tags["Controller"]["Block"]==0:
			self.State=self.Idle