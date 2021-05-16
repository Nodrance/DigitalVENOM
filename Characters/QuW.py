import copy
class Character:
	def __init__(self,P,pygame):
		self.X=500*P-250
		self.Y=0
		self.Offset=(0,-55)
		self.XV=0
		self.YV=0
		self.KV=0
		self.W=128
		self.H=128
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Health=500
		self.MaxHealth=500
		self.Costume="64Cyan"
		self.Hearts=[]
		self.pygame=pygame
		self.TS=[]
		self.Sprites={
		"idle1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle1.png"),
		"idle2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle2.png"),
		"idle3":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Idle3.png"),
		"hitstun1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/HitStun1.png"),
		"jab1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jab1.png"),
		"jab2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jab2.png"),
		"strong1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Strong1.png"),
		"strong2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Strong2.png"),
		"fierce1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Fierce1.png"),
		"short1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Short1.png"),
		"short2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Short2.png"),
		"forward1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Forward1.png"),
		"forward2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Forward2.png"),
		"roundhouse1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse1.png"),
		"roundhouse2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse2.png"),
		"kiss1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Kiss1.png"),
		"kiss2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Kiss2.png"),
		"jab aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/JabAerial1.png"),
		"strong aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/StrongAerial1.png"),
		"fierce aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/FierceAerial1.png"),
		"short aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/ShortAerial1.png"),
		"forward aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/ForwardAerial1.png"),
		"roundhouse aerial 1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/RoundhouseAerial1.png"),
		"walk1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk1.png"),
		"walk2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk2.png"),
		"walk3":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk3.png"),
		"walk4":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Walk4.png"),
		"jump":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Jump.png"),
		"jab swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/JabSwoosh1.png"),
		"jab swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/JabSwoosh2.png"),
		"strong swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/StrongSwoosh1.png"),
		"strong swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/StrongSwoosh2.png"),
		"fierce swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/FierceSwoosh1.png"),
		"fierce swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/FierceSwoosh2.png"),
		"short swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ShortSwoosh1.png"),
		"short swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ShortSwoosh2.png"),
		"forward swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardSwoosh1.png"),
		"forward swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/ForwardSwoosh2.png"),
		"roundhouse swoosh 1":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseSwoosh1.png"),
		"roundhouse swoosh 2":pygame.image.load("Characters/QuW/Sprites/Effects/RoundhouseSwoosh2.png"),
		"heart":pygame.image.load("Characters/QuW/Sprites/Effects/Heart.png"),
		}
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
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
		self.JabAerialData=self.ViperZero("JabAerial")
		self.StrongAerialData=self.ViperZero("StrongAerial")
		self.FierceAerialData=self.ViperZero("FierceAerial")
		self.ShortAerialData=self.ViperZero("ShortAerial")
		self.ForwardAerialData=self.ViperZero("ForwardAerial")
		self.RoundhouseAerialData=self.ViperZero("RoundhouseAerial")
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
		self.LTags={}
		self.PanchiraGuage=[
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/0.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/1.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/2.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/3.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/4.png"),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/5.png"),
		]
		self.HitLag=0
	def RNG(self):
		self.RNGV+=1+self.StateFrame+self.pygame.time.get_ticks()
		return self.RNGV
		pass
	def Reset(self,P,pygame):
		self.X=500*P-250
		self.Y=0
		self.Offset=(0,-55)
		self.XV=0
		self.YV=0
		self.W=128
		self.H=128
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Health=500
		self.MaxHealth=500
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
		self.Hearts=[]
		self.Stun=0
		self.TS=[]
		self.State=self.Idle
		self.StateFrame=0
		self.BackState=self.Idle
		self.AirDashTime=0
		self.AirDashable=1
		self.DF=0
		self.Sounds=[]
		self.HitSound=0
		self.HitLag=0
		self.Panchira=0
		self.LTags={}
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
		if self.LTags=={}:
			self.LTags=Tags
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
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt":
				self.HitLag+=i[0]["Hit Lag"]
		if self.SN!=self.TSN:
			self.Sprite=self.Sprites[self.SN]
			self.TSN=self.SN
		self.X+=self.XV
		self.Y+=self.YV
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
			#self.Nogeki()
			self.State=self.Kiss
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
	def Walk(self,Tags):
		self.SN=["walk1","walk2","walk3","walk4"][int(self.StateFrame/5)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		if self.StateFrame>5:
			self.XV=Tags["Controller"]["X"]*15
		else:
			self.XV=Tags["Controller"]["X"]*self.StateFrame*3
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
			self.YV=-35
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == Tags["Side"]*-2+1:
				self.State=self.Idle
		return {}
	def BackWalk(self,Tags):
		self.SN=["walk2","walk1","walk4","walk3"][int(self.StateFrame/8)%4]
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
			self.YV=-35
			self.AirDashable=1
			self.State=self.Jump
		else:
			if not Tags["Controller"]["X"] == Tags["Side"]*2-1:
				self.State=self.Idle
		return {}
	def Jump(self,Tags):
		if self.StateFrame < 1:
			self.XV=Tags["Controller"]["X"]*10
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
		self.YV=0
		self.SN=self.JabData["Animation"][self.StateFrame]
		self.Triggers=self.JabData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["jab swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["jab swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.JabData["Frames"]:
			self.State=self.Idle
		return {}
	def Strong(self,Tags):
		self.YV=0
		self.SN=self.StrongData["Animation"][self.StateFrame]
		self.Triggers=self.StrongData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["strong swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["strong swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.StrongData["Frames"]:
			self.State=self.Idle
		return {}
	def Fierce(self,Tags):
		self.YV=0
		self.SN=self.FierceData["Animation"][self.StateFrame]
		self.Triggers=self.FierceData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.FierceData["Frames"]:
			self.State=self.Idle
		return {}
	def Short(self,Tags):
		self.YV=0
		self.SN=self.ShortData["Animation"][self.StateFrame]
		self.Triggers=self.ShortData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["short swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["short swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame==1 and Tags["Controller"]["Forward"]:
			self.Pangeki()
			self.State=self.Forward
		if self.StateFrame == self.ShortData["Frames"]:
			self.State=self.Idle
		return {}
	def Forward(self,Tags):
		self.YV=0
		self.SN=self.ForwardData["Animation"][self.StateFrame]
		self.Triggers=self.ForwardData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["forward swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["forward swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame==2 and Tags["Controller"]["Roundhouse"]:
			self.Pangeki()
			self.State=self.Roundhouse
		if self.StateFrame == self.ForwardData["Frames"]:
			self.State=self.Idle
		return {}
	def Roundhouse(self,Tags):
		self.YV=0
		self.SN=self.RoundhouseData["Animation"][self.StateFrame]
		self.Triggers=self.RoundhouseData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.Panchira>=5 and self.StateFrame==4 and abs((Tags["Other Player"].X-self.X))+abs((Tags["Other Player"].Y-self.Y))<500:
			self.YV=Tags["Other Player"].YV
			self.XV=Tags["Other Player"].XV
			self.Y=Tags["Other Player"].Y
			self.X=Tags["Other Player"].X+(Tags["Side"]*50-25)
			self.Panchira-=5
			self.AirDashable=0
			self.State=self.Jump
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["roundhouse swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["roundhouse swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.RoundhouseData["Frames"]:
			self.State=self.Idle
		return {}
	def JabAerial(self,Tags):
		self.YV+=3
		self.SN=self.JabAerialData["Animation"][self.StateFrame]
		self.Triggers=self.JabAerialData["Triggers"][self.StateFrame]
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
		self.YV+=3
		self.SN=self.StrongAerialData["Animation"][self.StateFrame]
		self.Triggers=self.StrongAerialData["Triggers"][self.StateFrame]
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
		self.YV+=3
		self.SN=self.FierceAerialData["Animation"][self.StateFrame]
		self.Triggers=self.FierceAerialData["Triggers"][self.StateFrame]
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
		self.YV+=3
		self.SN=self.ShortAerialData["Animation"][self.StateFrame]
		self.Triggers=self.ShortAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame==1 and Tags["Controller"]["Forward"]:
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
		self.YV+=3
		self.SN=self.ForwardAerialData["Animation"][self.StateFrame]
		self.Triggers=self.ForwardAerialData["Triggers"][self.StateFrame]
		if self.Y>=0:
			self.State=self.Idle
		if self.StateFrame==2 and Tags["Controller"]["Roundhouse"]:
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
		self.YV+=3
		self.SN=self.RoundhouseAerialData["Animation"][self.StateFrame]
		self.Triggers=self.RoundhouseAerialData["Triggers"][self.StateFrame]
		if Tags["Controller"]["Jump"] and self.Panchira>=10 and self.StateFrame==4 and abs((Tags["Other Player"].X-self.X))+abs((Tags["Other Player"].Y-self.Y))<500:
			self.YV=Tags["Other Player"].YV
			self.XV=Tags["Other Player"].XV
			self.Y=Tags["Other Player"].Y
			self.X=Tags["Other Player"].X+(Tags["Side"]*50-25)
			self.Panchira-=10
			self.AirDashable=0
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
		self.AirDashable=1
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="hitstun1"
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