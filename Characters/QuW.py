import copy,random,math
from Characters import ViperOne
class Character:
	def __init__(self,P,pygame):
		self.ViperOne=ViperOne.Default(
			Player=P,
			DIR="Characters/QuW",
			Offset=(0,-55),
			MaxHealth=250,
			Height=128,
			Width=128,
			)
		self.ViperOne.Reset(self)
		#self.X=200*P-100
		#self.Y=0
		#self.Offset=(0,-55)
		#self.XV=0
		#self.YV=0
		#self.KV=0
		#self.W=128
		#self.H=128
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		#self.Health=500
		#self.Combo=0
		self.MaxHealth=500
		self.Costume=["64Cyan","64Alt"][P]
		self.SSN="Idle"
		self.Hearts=[]
		self.pygame=pygame
		self.TS=[]
		self.Sprites={
		"idle1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle1.png").convert_alpha(),
		"idle2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle2.png").convert_alpha(),
		"idle3":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle3.png").convert_alpha(),
		"hitstun1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/HitStun1.png").convert_alpha(),
		"jab1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jab1.png").convert_alpha(),
		"jab2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jab2.png").convert_alpha(),
		"strong1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Strong1.png").convert_alpha(),
		"strong2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Strong2.png").convert_alpha(),
		"fierce1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Fierce1.png").convert_alpha(),
		"short1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Short1.png").convert_alpha(),
		"short2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Short2.png").convert_alpha(),
		"forward1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Forward1.png").convert_alpha(),
		"forward2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Forward2.png").convert_alpha(),
		"roundhouse1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse1.png").convert_alpha(),
		"roundhouse2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse2.png").convert_alpha(),
		"kiss1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Kiss1.png").convert_alpha(),
		"kiss2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Kiss2.png").convert_alpha(),
		"jab aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/JabAerial1.png").convert_alpha(),
		"strong aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/StrongAerial1.png").convert_alpha(),
		"fierce aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/FierceAerial1.png").convert_alpha(),
		"short aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/ShortAerial1.png").convert_alpha(),
		"forward aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/ForwardAerial1.png").convert_alpha(),
		"roundhouse aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/RoundhouseAerial1.png").convert_alpha(),
		"walk1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk1.png").convert_alpha(),
		"walk2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk2.png").convert_alpha(),
		"walk3":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk3.png").convert_alpha(),
		"walk4":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk4.png").convert_alpha(),
		"jump":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jump.png").convert_alpha(),
		"dash1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Dash1.png").convert_alpha(),
		"dash2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Dash2.png").convert_alpha(),
		"jab swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/JabSwoosh1.png").convert_alpha(),
		"jab swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/JabSwoosh2.png").convert_alpha(),
		"strong swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/StrongSwoosh1.png").convert_alpha(),
		"strong swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/StrongSwoosh2.png").convert_alpha(),
		"fierce swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/FierceSwoosh1.png").convert_alpha(),
		"fierce swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/FierceSwoosh2.png").convert_alpha(),
		"short swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ShortSwoosh1.png").convert_alpha(),
		"short swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ShortSwoosh2.png").convert_alpha(),
		"forward swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardSwoosh1.png").convert_alpha(),
		"forward swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardSwoosh2.png").convert_alpha(),
		"roundhouse swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseSwoosh1.png").convert_alpha(),
		"roundhouse swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseSwoosh2.png").convert_alpha(),
		"jab aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/JabAerialSwoosh1.png").convert_alpha(),
		"jab aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/JabAerialSwoosh2.png").convert_alpha(),
		"strong aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/StrongAerialSwoosh1.png").convert_alpha(),
		"strong aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/StrongAerialSwoosh2.png").convert_alpha(),
		"fierce aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/FierceAerialSwoosh1.png").convert_alpha(),
		"fierce aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/FierceAerialSwoosh2.png").convert_alpha(),
		"short aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ShortAerialSwoosh1.png").convert_alpha(),
		"short aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ShortAerialSwoosh2.png").convert_alpha(),
		"forward aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardAerialSwoosh1.png").convert_alpha(),
		"forward aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardAerialSwoosh2.png").convert_alpha(),
		"roundhouse aerial swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseAerialSwoosh1.png").convert_alpha(),
		"roundhouse aerial swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseAerialSwoosh2.png").convert_alpha(),
		"heart":pygame.image.load("Characters/QuW/Sprites/Effects/Heart.png"),
		}
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
		#self.Stun=0
		#self.State=self.Idle
		#self.StateFrame=0
		self.BackState=self.Idle
		self.The48Frame=False
		self.JabData=self.ViperZero("Jab")
		self.StrongData=self.ViperZero("Strong")
		self.FierceData=self.ViperZero("Fierce")
		self.ShortData=self.ViperZero("Short")
		self.ForwardData=self.ViperZero("Forward")
		self.RoundhouseData=self.ViperZero("Roundhouse")
		self.JabAerialData=self.ViperZero("JabAerial")
		self.StrongAerialData=self.ViperZero("StrongAerial")
		self.FierceAerialData=self.ViperZero("FierceAerial")
		self.ShortAerialData=self.ViperZero("ShortAerial")
		self.ForwardAerialData=self.ViperZero("ForwardAerial")
		self.RoundhouseAerialData=self.ViperZero("RoundhouseAerial")
		self.DashTimer=0
		#self.AirDashTime=0
		#self.AirDashable=1
		self.DF=0
		#self.Sounds=[]
		self.RNGV=0
		self.HitSound=0
		self.HitSounds={
		"Pangeki": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/Pangeki3.wav"),
			],
		"Light": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L3.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L4.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L5.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L6.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L7.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/L8.wav"),
			],
		"Medium": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M3.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M4.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M5.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M6.wav"),
			],
		"Heavy": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H3.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H4.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H5.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H6.wav"),
			],
		"The48Frame":pygame.mixer.Sound("Characters/QuW/Hitsounds/The48Frame.wav"),
		}
		self.MiscSounds={
		"Panchira Increase": pygame.mixer.Sound("Characters/QuW/Sounds/Panchira Increase.wav"),
		"Gopan": pygame.mixer.Sound("Characters/QuW/Sounds/Gopan.wav"),
		"Jump Cancel": pygame.mixer.Sound("Characters/QuW/Sounds/Jump Cancel.wav"),}
		self.Panchira=0
		#self.LTags={}
		self.PanchiraGuage=[
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/0.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/1.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/2.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/3.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/4.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/5.png").convert_alpha(),
		]
		#self.HitLag=0
	def RNG(self):
		self.RNGV+=1+self.StateFrame+self.pygame.time.get_ticks()
		return self.RNGV
		pass
	def Reset(self,P,pygame):
		self.ViperOne.Reset(self)
		#self.X=200*P-100
		#self.Y=0
		#self.Offset=(0,-55)
		#self.XV=0
		#self.YV=0
		#self.W=128
		#self.H=128
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		#self.Health=1500
		#self.MaxHealth=500
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
		self.Hearts=[]
		#self.Stun=0
		self.TS=[]
		#self.State=self.Idle
		#self.StateFrame=0
		#self.BackState=self.Idle
		#self.AirDashTime=0
		#self.AirDashable=1
		self.DF=0
		#self.Sounds=[]
		self.HitSound=0
		#self.HitLag=0
		self.Panchira=0
		#self.LTags={}
	def ViperZero(self,AN):
		A=open("Characters/QuW/Attacks/"+AN+".vp0").read()
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
						"Hit Lag":int(F[9]),
						"Knockback2":int(F[10]),
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
		#self.Sounds.append(self.HitSounds["Nogeki"][self.RNG()%len(self.HitSounds["Nogeki"])])
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
		if self.LTags=={}:
			self.LTags=Tags
		self.Tags=Tags
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
				Knockback2=i[1]["Knockback2"]
			if i[0]["Type"]=="Hurt" and i[1]["Type"]=="Grab":
				self.Grabbed=1
				Damage+=i[1]["Damage"]
				ChipDamage+=i[1]["Chip Damage"]
				Stun=i[1]["Stun"]
				BlockStun+=i[1]["Block Stun"]
				GrabX+=i[1]["Knockback"]
				GrabY=i[1]["Knockback2"]
			#if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt" and self.Y==0:
				#self.XV=Tags["Side"]*10-5
		if Damage>0:
			if self.SSN=="Block":
				if not self.DF:
					self.Health-=Damage
					self.StateFrame=-1
					#if Knockback>0:
						#self.YV=-Knockback2*0.75
						#self.XV=Knockback*0.4*(Tags["Side"]-0.5)
						#self.KV=0#Knockback*0.2
					self.State=self.BlockStun
					self.Stun=BlockStun
				pass
			else:
				if not self.DF:
					self.Health-=Damage
					self.StateFrame=-1
					if Knockback>0:
						self.YV=-Knockback2*0.75
						self.XV=Knockback*0.4*(Tags["Side"]-0.5)
						self.KV=0#Knockback*0.2
					self.State=self.HitStun
					self.Stun=Stun
			self.DF=1
		else:
			self.DF=0
		if self.Grabbed:
			self.State=self.Idle
			self.X=GrabX
			self.Y=GrabY
		if self.State==self.BackState:
			self.StateFrame+=1
		else:
			self.StateFrame=0
			self.BackState=self.State
		R=self.State(Tags)
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt":
				self.HitLag+=i[0]["Hit Lag"]
				if self.State in [self.Jab,self.Short,self.JabAerial,self.ShortAerial]:
					self.Sounds.append(random.choice(self.HitSounds["Light"]))
				if self.State in [self.Strong,self.Forward,self.StrongAerial,self.ForwardAerial]:
					self.Sounds.append(random.choice(self.HitSounds["Medium"]))
				#if self.State==self.Fierce and not self.The48Frame:
					#self.Sounds.append(self.HitSounds["The48Frame"])
					#self.pygame.mixer.music.pause()
					#self.The48Frame=True
				if self.State in [self.Fierce,self.Roundhouse,self.FierceAerial,self.RoundhouseAerial]:# and not self.The48Frame:
					self.Sounds.append(random.choice(self.HitSounds["Heavy"]))
				if Tags["Other Player"].SSN=="HitStun":
					self.Combo+=1
				else:
					self.Combo=1
		if self.SN!=self.TSN:
			self.Sprite=self.Sprites[self.SN]
			self.TSN=self.SN
		self.X+=self.XV
		self.Y+=self.YV
		if R==None:
			R={}
		R["Hit Lag"]=self.HitLag
		R["Sounds"]=self.Sounds
		R["Sprites"]=self.TS
		R["GUI"]=[
		{"Sprite":self.PanchiraGuage[int(self.Panchira/5)],"X":5,"Y":37,"W":128,"H":32}
		]
		if self.Panchira>25:
			self.Panchira=25
		self.Triggers=copy.deepcopy(self.Triggers)
		for i in self.Triggers:
			if i["Type"]=="Hit":
				i["Damage"]+=int(self.Panchira)+Tags["Fault"]
				i["Chip Damage"]+=int(self.Panchira/2)+Tags["Fault"]
				i["Stun"]+=Tags["Fault"]*2+2
				i["Block Stun"]+=Tags["Fault"]*2+2
		self.Hearts=[[j[0]+j[2],j[1]+j[3],j[2],j[3]] for j in self.Hearts]
		Tags["Side"]=self.X>Tags["Other Player"].X
		if Tags["Side"]:
			for i in [{"X":-(j[0]-self.X),"Y":j[1]-self.Y,"W":8,"H":8,"Sprite":self.Sprites["heart"]} for j in self.Hearts]:
				R["Sprites"].append(i)
		else:
			for i in [{"X":j[0]-self.X,"Y":j[1]-self.Y,"W":8,"H":8,"Sprite":self.Sprites["heart"]} for j in self.Hearts]:
				R["Sprites"].append(i)
		for i in range(len(self.Hearts)):
			if self.Hearts[i][0]<Tags["Stage"].Bounds[0]:self.Hearts.pop(i);break
			if self.Hearts[i][0]>Tags["Stage"].Bounds[1]:self.Hearts.pop(i);break
			if self.Hearts[i][1]<Tags["Stage"].Bounds[2]:self.Hearts.pop(i);break
			if self.Hearts[i][1]>0:self.Hearts.pop(i);break
		if self.Y>0:
			self.Y=0
		if Tags["Side"]==1:
			#self.Sprite=self.Sprites["blank"]
			self.HitFlip()
		self.LTags=Tags
		return R
	def Idle(self,Tags):
		self.XV=0
		self.The48Frame=False
		self.SSN="Idle"
		self.SN=["idle1","idle2","idle3","idle2"][int(self.StateFrame/12)%4]
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
			self.State=self.Kiss
		if Tags["Controller"]["Jump"]:
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == 0:
				if self.DashTimer<3:
					if Tags["Controller"]["X"] == Tags["Side"]*2-1:
						self.State=self.BackDash
						self.Pangeki()
					else:
						self.State=self.Dash
						self.Pangeki()
				else:
					if Tags["Controller"]["X"] == Tags["Side"]*2-1:
						self.State=self.BackWalk
					else:
						self.State=self.Walk
				self.DashTimer=0
		self.DashTimer+=1
		return {}
	def Walk(self,Tags):
		self.SSN="Walk"
		self.SN=["walk1","walk2","walk3","walk4"][int(self.StateFrame/5)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*10
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*2
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
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == Tags["Side"]*-2+1:
				self.State=self.Idle
		return {}
	def BackWalk(self,Tags):
		self.SSN="Block"
		self.SN=["walk2","walk1","walk4","walk3"][int(self.StateFrame/8)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if self.StateFrame>3:
			self.XV=Tags["Controller"]["X"]*6
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*2
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
			self.YV=-30
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
		self.SN="jump"
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
		if Tags["Controller"]["X"]!=0:
			if Tags["Side"]==1 and Tags["Controller"]["X"]>0:
				self.SSN="Block"
				pass
			elif Tags["Side"]==0 and Tags["Controller"]["X"]<0:
				self.SSN="Block"
				pass
		if Tags["Controller"]["X2"]!=0:
			if self.DashTimer<3 and self.AirDashable:
				if Tags["Controller"]["X"] == Tags["Side"]*2-1:
					self.State=self.BackDash
					self.Pangeki()
				else:
					self.State=self.Dash
					self.Pangeki()
			self.DashTimer=0
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
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		if self.StateFrame>4:
			self.SN="kiss1"
		else:
			self.SN="kiss2"
		if self.StateFrame==5:
			self.Hearts.append([
				self.X,
				self.Y-80,
				-Tags["Side"]*6+3,
				0,
				])
		if self.StateFrame==15:
			self.State=self.Idle
		return {}
	def Jab(self,Tags):
		self.SSN="Attack"
		self.YV=0
		self.SN=self.JabData["Animation"][self.StateFrame]
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
		self.SN=self.StrongData["Animation"][self.StateFrame]
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
		self.SN=self.FierceData["Animation"][self.StateFrame]
		self.Triggers=self.FierceData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.StateFrame==4:
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=1
			self.State=self.Jump
		elif Tags["Controller"]["X"]!=0 and self.StateFrame==4:
			if (-Tags["Side"]+0.5>0)==(Tags["Controller"]["X"]>0):
				#self.Sounds.append(self.MiscSounds["Jump Cancel"])
				self.AirDashable=1
				self.State=self.Dash
			else:
				#self.Sounds.append(self.MiscSounds["Jump Cancel"])
				self.AirDashable=1
				self.State=self.BackDash
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
		self.SN=self.ShortData["Animation"][self.StateFrame]
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
		self.SN=self.ForwardData["Animation"][self.StateFrame]
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
		self.SN=self.RoundhouseData["Animation"][self.StateFrame]
		self.Triggers=self.RoundhouseData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.Panchira>=5 and self.StateFrame==4:
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.Panchira-=5
			self.AirDashable=1
			self.State=self.Jump
		elif Tags["Controller"]["X"]!=0 and self.Panchira>=5 and self.StateFrame==4:
			if (-Tags["Side"]+0.5>0)==(Tags["Controller"]["X"]>0):
				#self.Sounds.append(self.MiscSounds["Jump Cancel"])
				self.Panchira-=5
				self.AirDashable=1
				self.State=self.Dash
			else:
				#self.Sounds.append(self.MiscSounds["Jump Cancel"])
				self.Panchira-=5
				self.AirDashable=1
				self.State=self.BackDash
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
		self.SN=self.JabAerialData["Animation"][self.StateFrame]
		self.Triggers=self.JabAerialData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>1 and Tags["Controller"]["Strong"]:
			self.Pangeki()
			self.State=self.StrongAerial
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["jab aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["jab aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.JabAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def StrongAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.SN=self.StrongAerialData["Animation"][self.StateFrame]
		self.Triggers=self.StrongAerialData["Triggers"][self.StateFrame]
		if 4>self.StateFrame>1 and Tags["Controller"]["Fierce"]:
			self.Nogeki()
			self.State=self.FierceAerial
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["strong aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["strong aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.StrongAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def FierceAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.SN=self.FierceAerialData["Animation"][self.StateFrame]
		self.Triggers=self.FierceAerialData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.StateFrame==4 and self.AirDashable:
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.AirDashable=0
			self.State=self.Jump
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["fierce aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["fierce aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.FierceAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def ShortAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.SN=self.ShortAerialData["Animation"][self.StateFrame]
		self.Triggers=self.ShortAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if 4>self.StateFrame>1 and Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.ForwardAerial
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["short aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["short aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.ShortAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def ForwardAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.SN=self.ForwardAerialData["Animation"][self.StateFrame]
		self.Triggers=self.ForwardAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if 5>self.StateFrame>1 and Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.RoundhouseAerial
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["forward aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["forward aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.ForwardAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def RoundhouseAerial(self,Tags):
		self.SSN="Aerial"
		self.YV+=3
		self.SN=self.RoundhouseAerialData["Animation"][self.StateFrame]
		self.Triggers=self.RoundhouseAerialData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.Panchira>=5 and self.StateFrame==4:
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			self.YV=-30
			self.XV=Tags["Controller"]["X"]*10
			self.Panchira-=5
			self.AirDashable=1
			self.State=self.Jump
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["roundhouse aerial swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["roundhouse aerial swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.RoundhouseAerialData["Frames"]:
			self.State=self.Jump
		return {}
	def HitStun(self, Tags):
		self.SSN="HitStun"
		self.AirDashable=1
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="hitstun1"
		if Tags["Controller"]["Fierce"] and self.Panchira==25:
			self.Nogeki()
			self.Triggers=[{"Box":[[-64,64],[-128,0]],"Type":"Hit",
						"Damage":20,
						"Chip Damage":20,
						"Stun":10,
						"Block Stun":10,
						"Knockback":10,
						"Hit Lag":10,
						"Knockback2":10,}]
			self.State=self.Jump
		if self.Y<0 or self.YV<0:
			self.YV+=3
		elif self.StateFrame==0:
			self.XV=Tags["Side"]*10-5
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
	def BlockStun(self,Tags):
		self.SSN="Block"
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="jump"
		if self.Y<0 or self.YV<0:
			self.YV+=3
			if self.StateFrame>self.Stun:
				self.State=self.Jump
		else:
			self.Y=0
			self.YV=0
			if self.StateFrame>self.Stun:
				self.State=self.BackWalk
		return {}
	def Dash(self,Tags):
		self.SSN="Dash"
		self.SN="dash1"
		self.AirDashable=0
		self.DashTimer=5
		self.YV=0
		if self.StateFrame==0:
			self.XV=50*(-Tags["Side"]+0.5)
		elif self.XV != 50*(-Tags["Side"]+0.5):
			self.State=self.BackDash
		if self.StateFrame == 6:
			if self.Y==0:
				self.State=self.Idle
			else:
				self.State=self.Jump
		return {}
		pass
	def BackDash(self,Tags):
		self.SSN="Dash"
		self.SN="dash2"
		self.AirDashable=0
		self.DashTimer=5
		self.YV=0
		if self.StateFrame==0:
			self.XV=30*(Tags["Side"]-0.5)
		elif self.XV != 30*(Tags["Side"]-0.5):
			self.State=self.Dash
		if self.StateFrame == 6:
			if self.Y==0:
				self.State=self.Idle
			else:
				self.State=self.Jump
		return {}
		pass