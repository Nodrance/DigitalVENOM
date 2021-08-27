import copy,types
class Button:
	def __init__(Start,End,Key,State):
		self.Start=Start
		self.End=End
		self.Key=Key
		self.State=State
class State:
	def __init__(self,Name,Settings):
		self.Settings=Settings
		self.FrameData=ViperZero(Name)
		self.JumpCancel=-1
		self.Buttons=[]
	def ViperZero(self,AN):
		A=open(self.Settings.DIR+"/Attacks/"+AN+".vp0").read()
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
class Settings:
	def __init__(self):
		self.Health=500
		self.MaxHealth=500
		self.Height=128
		self.Width=128
		self.Speed=10
		self.BackSpeed=6
		self.Offset=(0,-55)
		self.DIR=""
		self.Sprites={}
class Character:
	class ExtraFunctions:
		def PreFrame(self,Tags):pass
		def PostFrame(self,Tags):pass
		def Reset(self,P,pygame):pass
	def __init__(self,P=None,pygame=None):
		self.GlobalFrame=0
		pass
	def RNG(self):
		self.RNGV+=1+self.StateFrame+self.pygame.time.get_ticks()
		return self.RNGV
		pass
	def Reset(self,P,pygame):
		self.X=200*P-100
		self.Y=0
		self.Offset=self.Settings.Offset
		self.XV=0
		self.YV=0
		self.KV=0
		self.W=self.Settings.Width
		self.H=self.Settings.Height
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Health=self.Settings.Health
		self.SSN="Idle"
		self.Combo=0
		self.States={}
		self.MaxHealth=self.Settings.MaxHealth
		self.Costume="64Cyan"
		self.Hearts=[]
		self.pygame=pygame
		self.Sprites={}
		self.TS=[]
		for i in self.Settings.Sprites:
			self.Sprites[i]=pygame.image.load(self.Settings.Sprites[i])
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
		self.AirDashTime=0
		self.AirDashable=1
		self.DF=0
		self.Sounds=[]
		self.RNGV=0
		self.HitSound=0
		self.HitSounds={
		"Pangeki": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki3.wav"),
			],
		"Nogeki": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki3.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki4.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki5.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Nogeki6.wav"),
			]
		}
		self.MiscSounds={
		"Panchira Increase": pygame.mixer.Sound("Characters/QuW/Sounds/Panchira Increase.wav"),
		"Gopan": pygame.mixer.Sound("Characters/QuW/Sounds/Gopan.wav"),}
		self.Panchira=0
		self.PanchiraGuage=[
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/0.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/1.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/2.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/3.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/4.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/5.png"),
		]
		self.HitLag=0
		self.GlobalFrame+=1
		self.ExtraFunctions.Reset(self,P,pygame)
	def ViperZero(self,AN):
		A=open(self.Settings.DIR+"/Attacks/"+AN+".vp0").read()
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
	def HitFlip(self):
		T=[]
		for H in copy.deepcopy(self.Triggers):
			X=H
			H["Box"]=[[-H["Box"][0][1],-H["Box"][0][0]],[H["Box"][1][0],H["Box"][1][1]]]
			T.append(H)
		self.Triggers=T
	def Nogeki(self):
		#if self.RNG()%3==0:
			#self.Sounds.append(self.Voices["Attack"][self.RNG()%len(self.Voices["Attack"])])
		self.Sounds.append(self.HitSounds["Nogeki"][self.RNG()%len(self.HitSounds["Nogeki"])])
		self.Panchira=0
		pass
	def Pangeki(self):
		#if self.RNG()%3==0:
			#self.Sounds.append(self.Voices["Panchira"][self.RNG()%len(self.Voices["Panchira"])])
		self.Sounds.append(self.HitSounds["Pangeki"][self.RNG()%len(self.HitSounds["Pangeki"])])
		if self.Panchira%5==4:
			self.Sounds.append(self.MiscSounds["Panchira Increase"])
		if self.Panchira==24:
			self.Sounds.append(self.MiscSounds["Gopan"])
		self.Panchira+=1
		pass
	def Frame(self,Tags):
		self.HitLag=0
		self.TS=[]
		self.Sounds=[]
		Damage=0
		ChipDamage=0
		Stun=0
		BlockStun=0
		Knockback=0
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hurt" and i[1]["Type"]=="Hit":
				Damage+=i[1]["Damage"]
				ChipDamage+=i[1]["Chip Damage"]
				Stun=i[1]["Stun"]
				BlockStun+=i[1]["Block Stun"]
				Knockback+=i[1]["Knockback"]
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt" and self.Y==0:
				self.XV=Tags["Side"]*10-5
		if Damage>0:
			if not self.DF:
				self.Health-=Damage
				if Knockback>0:
					self.YV=-Knockback*0.75
					self.XV=Knockback*0.1*(Tags["Side"]-0.5)
					self.KV=Knockback*0.2
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
		self.ExtraFunctions.PreFrame(self,Tags)
		try:
			self.R=self.State(Tags)
		except:
			self.State2(Tags)
		if not type(self.R)==dict:
			print(type(R))
			self.R={}
		self.ExtraFunctions.PostFrame(self,Tags)
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt":
				self.HitLag+=i[0]["Hit Lag"]
				if Tags["Other Player"].SSN=="HitStun":
					self.Combo+=1
				else:
					self.Combo=1
		self.X+=self.XV
		self.Y+=self.YV
		self.R["Hit Lag"]=self.HitLag
		self.R["Sounds"]=self.Sounds
		self.R["Sprites"]=self.TS
		if self.Y>0:
			self.Y=0
		if Tags["Side"]==1:
			#self.Sprite=self.Sprites["blank"]
			self.HitFlip()
		return self.R
	def Idle(self,Tags):
		self.XV=0
		self.Sprite=self.Sprites[["idle1","idle2","idle3","idle2"][int(self.StateFrame/12)%4]]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.Roundhouse
		if Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.Forward
		if Tags["Controller"]["Short"]:
			self.Pangeki()
			self.State=self.Short
		if Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.Fierce
		if Tags["Controller"]["Strong"]:
			self.Nogeki()
			self.State=self.Strong
		if Tags["Controller"]["Jab"]:
			self.Nogeki()
			self.State=self.Jab
		if Tags["Controller"]["Special"]:
			#self.Nogeki()
			self.State=self.Kiss
		if Tags["Controller"]["Jump"]:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == 0:
				if Tags["Controller"]["X"] == Tags["Side"]*2-1:
					self.State=self.BackWalk
				else:
					self.State=self.Walk
		return {}
	def Walk(self,Tags):
		self.SSN="Walk"
		self.Sprite=self.Sprites[["walk1","walk2","walk3","walk4"][int(self.StateFrame/5)%4]]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*self.Settings.Speed
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*self.Settings.Speed/5
		if Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.Roundhouse
		if Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.Forward
		if Tags["Controller"]["Short"]:
			self.Pangeki()
			self.State=self.Short
		if Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.Fierce
		if Tags["Controller"]["Strong"]:
			self.Nogeki()
			self.State=self.Strong
		if Tags["Controller"]["Jab"]:
			self.Nogeki()
			self.State=self.Jab
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		if Tags["Controller"]["Jump"]:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == Tags["Side"]*-2+1:
				self.State=self.Idle
		return {}
	def BackWalk(self,Tags):
		self.SSN="BackWalk"
		self.Sprite=self.Sprites[["walk2","walk1","walk4","walk3"][int(self.StateFrame/8)%4]]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*self.Settings.BackSpeed
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*self.Settings.BackSpeed/5
		if Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.Roundhouse
		if Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.Forward
		if Tags["Controller"]["Short"]:
			self.Pangeki()
			self.State=self.Short
		if Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.Fierce
		if Tags["Controller"]["Strong"]:
			self.Nogeki()
			self.State=self.Strong
		if Tags["Controller"]["Jab"]:
			self.Nogeki()
			self.State=self.Jab
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		if Tags["Controller"]["Jump"]:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == Tags["Side"]*2-1:
				self.State=self.Idle
		return {}
	def Jump(self,Tags):
		self.SSN="Jump"
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["jump"]
		if Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.RoundhouseAerial
		if Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.ForwardAerial
		if Tags["Controller"]["Short"]:
			self.Pangeki()
			self.State=self.ShortAerial
		if Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.FierceAerial
		if Tags["Controller"]["Strong"]:
			self.Pangeki()
			self.State=self.StrongAerial
		if Tags["Controller"]["Jab"]:
			self.Nogeki()
			self.State=self.JabAerial
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
	def Kiss(self,Tags):
		self.YV=0
		if self.StateFrame>20:
			self.Sprite=self.Sprites["kiss1"]
		else:
			self.Sprite=self.Sprites["kiss2"]
		if self.StateFrame==21:
			self.Hearts.append([
				self.X,
				self.Y-80,
				-Tags["Side"]*6+3,
				0,
				])
		if self.StateFrame==50:
			self.Panchira=25
			self.State=self.Idle
		return {}
	def Jab(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.JabData["Animation"][self.StateFrame]]
		self.Triggers=self.JabData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>0 and Tags["Controller"]["Strong"]:
			self.Nogeki()
			self.State=self.Strong
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["jab swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["jab swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.JabData["Frames"]:
			self.State=self.Idle
		return {}
	def Strong(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.StrongData["Animation"][self.StateFrame]]
		self.Triggers=self.StrongData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>1 and Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.Fierce
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["strong swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["strong swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.StrongData["Frames"]:
			self.State=self.Idle
		return {}
	def Fierce(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.FierceData["Animation"][self.StateFrame]]
		self.Triggers=self.FierceData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.StateFrame>3:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.FierceData["Frames"]:
			self.State=self.Idle
		return {}
	def Short(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.ShortData["Animation"][self.StateFrame]]
		self.Triggers=self.ShortData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["short swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["short swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if 4>self.StateFrame>0 and Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.Forward
		if self.StateFrame == self.ShortData["Frames"]:
			self.State=self.Idle
		return {}
	def Forward(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.ForwardData["Animation"][self.StateFrame]]
		self.Triggers=self.ForwardData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["forward swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["forward swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if 5>self.StateFrame>1 and Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.Roundhouse
		if self.StateFrame == self.ForwardData["Frames"]:
			self.State=self.Idle
		return {}
	def Roundhouse(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.RoundhouseData["Animation"][self.StateFrame]]
		self.Triggers=self.RoundhouseData["Triggers"][self.StateFrame]
		"""if Tags["Controller"]["Jump"] and self.Panchira>=10 and self.StateFrame==4 and abs((Tags["Other Player"].X-self.X))+abs((Tags["Other Player"].Y-self.Y))<500:
			self.YV=Tags["Other Player"].YV-2
			self.XV=Tags["Other Player"].XV+(Tags["Side"]*-2+1)
			self.Panchira-=10
			self.AirDashable=1
			self.State=self.Jump"""
		if Tags["Controller"]["Jump"] and self.StateFrame>3 and self.Panchira>=5:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.Panchira-=5
			self.State=self.Jump
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["roundhouse swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["roundhouse swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.RoundhouseData["Frames"]:
			self.State=self.Idle
		return {}
	def JabAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.JabAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.JabAerialData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>1 and Tags["Controller"]["Strong"]:
			self.Pangeki()
			self.State=self.StrongAerial
		if self.Y>=0:
			self.State=self.Idle
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.JabAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def StrongAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.StrongAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.StrongAerialData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>1 and Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.FierceAerial
		if self.Y>=0:
			self.State=self.Idle
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.StrongAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def FierceAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.FierceAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.FierceAerialData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.StateFrame>3 and self.AirDashable==1:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=0
			self.State=self.Jump
		if self.Y>=0:
			self.State=self.Idle
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.FierceAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def ShortAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.ShortAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.ShortAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if 4>self.StateFrame>1 and Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.ForwardAerial
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.ShortAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def ForwardAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.ForwardAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.ForwardAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if 5>self.StateFrame>1 and Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.RoundhouseAerial
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.ForwardAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def RoundhouseAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.Sprite=self.Sprites[self.RoundhouseAerialData["Animation"][self.StateFrame]]
		self.Triggers=self.RoundhouseAerialData["Triggers"][self.StateFrame]
		"""if Tags["Controller"]["Jump"] and self.Panchira>=10 and self.StateFrame==4 and abs((Tags["Other Player"].X-self.X))+abs((Tags["Other Player"].Y-self.Y))<500:
			self.YV=Tags["Other Player"].YV-2
			self.XV=Tags["Other Player"].XV+(Tags["Side"]*-2+1)
			self.Panchira-=10
			self.AirDashable=1
			self.State=self.Jump"""
		if Tags["Controller"]["Jump"] and self.StateFrame>3 and self.Panchira>=5:
			self.YV=-25
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.Panchira-=5
			self.State=self.Jump
		if self.Y>=0:
			self.State=self.Idle
		#if self.StateFrame == 0 or self.StateFrame == 1:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		#if self.StateFrame == 2:
			#self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.RoundhouseAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def HitStun(self, Tags):
		self.SSN="HitStun"
		self.AirDashable=1
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["hitstun1"]
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
		return {}
	def State2(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.Sprite=self.Sprites[self.States[self.State].FrameData["Animation"][self.StateFrame]]
		self.Triggers=self.States[self.State].FrameData["Triggers"][self.StateFrame]
		for i in self.State.Buttons:
			if i.End>self.StateFrame>i.Start and Tags["Controller"][i.Key]:
				self.State=i.State
		if self.StateFrame == self.States[self.State].FrameData["Frames"]:
			self.State=self.Idle
		return {}