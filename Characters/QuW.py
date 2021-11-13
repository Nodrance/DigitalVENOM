import copy,random,math,json,pygame,numpy
from Renderers import Loli
from Characters import ViperOne
from Tools import HitBoxer,ColorChanger
class Character:
	#TODO:
	#This whole block of code here probably isn't best practice
	#Figure out a way to do it better
	CharacterSelectSprites=[]
	color_grid=pygame.image.load("Characters/QuW/Sprites/color_grid.png")
	for i in range(color_grid.get_height()):
		CharacterSelectSprites.append(ColorChanger.FasterSwapImageColors(pygame.image.load("Characters/QuW/Sprites/64Cyan/Idle1.png").convert_alpha(),color_grid,i))
	def __init__(self,P,pygame,color):
		self.ViperOne=ViperOne.Default(
			Player=P,
			DIR="Characters/QuW",
			Offset=(0,-55),
			MaxHealth=500,
			Height=128,
			Width=128,
			Character=self,
			)
		self.ViperOne.Reset(self)
		self.RCFont=pygame.font.Font("Fonts/Messapia-Bold.otf",256)
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.MaxHealth=500
		self.Costume=["64Cyan","64Cyan"][P]
		self.color_grid=pygame.image.load("Characters/QuW/Sprites/color_grid.png")
		self.HitBoxerFrameData=[{"Triggers":[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]}]
		self.SSN="Idle"
		self.TS=[]
		self.IPSBuffer=[]
		self.IPSProne=0
		self.MaxMeter=1000
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
		"gl2-0001":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl2-0001.png").convert_alpha(),
		"gl2-0002":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl2-0002.png").convert_alpha(),
		"gl2-0003":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl2-0003.png").convert_alpha(),
		"roundhouse1":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse1.png").convert_alpha(),
		"roundhouse2":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Roundhouse2.png").convert_alpha(),
		"gl3-0001":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0001.png").convert_alpha(),
		"gl3-0002":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0002.png").convert_alpha(),
		"gl3-0003":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0003.png").convert_alpha(),
		"gl3-0004":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0004.png").convert_alpha(),
		"gl3-0005":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0005.png").convert_alpha(),
		"gl3-0006":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0006.png").convert_alpha(),
		"gl3-0007":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/gl3-0007.png").convert_alpha(),
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
		"knockdown":pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Knockdown.png").convert_alpha(),
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
		ColorChanger.FasterSwapColors(self.Sprites,self.color_grid,color)
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
		self.BackState=self.Idle
		self.The48Frame=False
		self.The24FrameData=self.ViperZero("The24Frame")
		self.States={
		"gv":ViperOne.Move(self,self.ViperZero("gv"),"gv",PreMove=self.Nogeki),
		"gl":ViperOne.Move(self,self.ViperZero("gl"),"gl",PreMove=self.Pangeki),
		"gl2":ViperOne.Move(self,self.ViperZero("gl2"),"gl2",PreMove=self.Pangeki),
		"gl3":ViperOne.Move(self,self.ViperZero("gl3"),"gl3",PreMove=self.Pangeki),
		"gm":ViperOne.Move(self,self.ViperZero("gm"),"gm",PreMove=self.Nogeki),
		"gm2":ViperOne.Move(self,self.ViperZero("gm2"),"gm2",PreMove=self.Nogeki),
		"gh":ViperOne.Move(self,self.ViperZero("gh"),"gh",PreMove=self.Nogeki),
		"al":ViperOne.Move(self,self.ViperZero("al"),"al",PreMove=self.Pangeki),
		"al2":ViperOne.Move(self,self.ViperZero("al2"),"al2",PreMove=self.Pangeki),
		"al3":ViperOne.Move(self,self.ViperZero("al3"),"al3",PreMove=self.Pangeki),
		"am":ViperOne.Move(self,self.ViperZero("am"),"am",PreMove=self.Nogeki),
		"am2":ViperOne.Move(self,self.ViperZero("am2"),"am2",PreMove=self.Pangeki),
		"ah":ViperOne.Move(self,self.ViperZero("ah"),"ah",PreMove=self.Nogeki),
		"Knockdown":self.Knockdown,
		"HitStun":self.HitStun,
		"Idle":self.Idle,
		"The24Frame":ViperOne.Move(self,self.ViperZero("The24Frame"),"gThe24Frame"),
		}
		"""if P==0:
			for i in self.States:
				HitBoxer.AttackData=self.States[i].FrameData
				HitBoxer.AddBlankAttributes()
				HitBoxer.Implement()
				pass"""
		self.CancelStates={
		"gv":ViperOne.Cancel(self,self.States["gv"]),
		"gl":ViperOne.Cancel(self,self.States["gl"]),
		"gl2":ViperOne.Cancel(self,self.States["gl2"]),
		"gl3":ViperOne.Cancel(self,self.States["gl3"]),
		"gm":ViperOne.Cancel(self,self.States["gm"]),
		"gm2":ViperOne.Cancel(self,self.States["gm2"]),
		"gh":ViperOne.Cancel(self,self.States["gh"]),
		"al":ViperOne.Cancel(self,self.States["al"]),
		"al2":ViperOne.Cancel(self,self.States["al2"]),
		"al3":ViperOne.Cancel(self,self.States["al3"]),
		"am":ViperOne.Cancel(self,self.States["am"]),
		"am2":ViperOne.Cancel(self,self.States["am2"]),
		"ah":ViperOne.Cancel(self,self.States["ah"]),
		"Knockdown":ViperOne.Cancel(self,self.States["Knockdown"]),
		"HitStun":ViperOne.Cancel(self,self.States["HitStun"]),
		"FaultReversal":self.FaultReversal,
		"Roman":self.RomanCancel,
		"PanchiraJumpCancel":self.PanchiraJumpCancel,
		"AutoPanchiraJumpCancel":self.AutoPanchiraJumpCancel,
		"NogekiJumpCancel":self.NogekiJumpCancel,
		"Jump":self.JumpCancel,
		}
		self.DashTimer=0
		self.CancelBuffer=0
		self.MaxAirDash=5
		self.DF=0
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
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M7.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/M8.wav"),
			],
		"Heavy": [
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H1.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H2.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H3.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H4.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H5.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H6.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H7.wav"),
			pygame.mixer.Sound("Characters/QuW/Hitsounds/H8.wav"),
			],
		"h1":pygame.mixer.Sound("Characters/QuW/Hitsounds/H1.wav"),
		"The24Frame":pygame.mixer.Sound("Characters/QuW/Hitsounds/The24Frame.wav"),
		}
		self.MiscSounds={
		"Panchira Increase": pygame.mixer.Sound("Characters/QuW/Sounds/Panchira Increase.wav"),
		"Gopan": pygame.mixer.Sound("Characters/QuW/Sounds/Gopan.wav"),
		"Jump Cancel": pygame.mixer.Sound("Characters/QuW/Sounds/Jump Cancel.wav"),}
		self.Meter=0
		self.PanchiraGuage=[
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/0.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/1.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/2.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/3.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/4.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/Panchira Guage/5.png").convert_alpha(),
		]
		self.CutIns=[
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/1.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/2.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/3.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/4.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/5.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/6.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/7.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/8.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/9.png").convert_alpha(),
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/10.png").convert_alpha(),
		]
		self.MegaCutIns=[
		pygame.image.load("Characters/QuW/Sprites/"+self.Costume+"/Cut Ins/Mega1.png").convert_alpha(),
		]
	def RNG(self):
		self.RNGV+=1+self.StateFrame+pygame.time.get_ticks()
		return self.RNGV
		pass
	def Reset(self,P,pygame):
		self.ViperOne.Reset(self)
		self.Triggers=[{"Box":[[-32,32],[-64,0]],"Type":"Hurt"}]
		self.Sprite=self.Sprites["idle1"]
		self.SN="idle1"
		self.TSN="idle1"
		self.TS=[]
		self.MaxAirDash=5
		self.IPSProne=0
		self.DF=0
		self.HitSound=0
		self.Meter=0
	def MakeScreenSpaceText(self,X):
		RCT=self.RCFont.render(X,1,(255,255,255))
		W=512*256/(RCT.get_width()+RCT.get_height())
		Loli.Particles.append(Loli.ScreenSpaceParticle(W*RCT.get_width()/RCT.get_height(),W,[RCT],0.5))
		Loli.Particles.append(Loli.PulseParticle((self.X+self.Offset[0],self.Y+self.Offset[1]),0.5,200,(255,255,0)))
	def ViperZero(self,AN):
		X=json.load(open("Characters/QuW/Attacks/"+AN+".json","r"))
		X["Filename"]="Characters/QuW/Attacks/"+AN+".json"
		return X
	def HitFlip(self):
		T=[]
		for H in copy.deepcopy(self.Triggers):
			X=H
			H["Box"]=[[-H["Box"][0][1],-H["Box"][0][0]],[H["Box"][1][0],H["Box"][1][1]]]
			T.append(H)
		self.Triggers=T
	def HitNudge(self):
		if abs(self.X-self.Tags["Other Player"].X)+abs(self.Y-self.Tags["Other Player"].Y) < 200:
			self.XV+=(self.Tags["Other Player"].X-self.X)/10
			self.YV+=(self.Tags["Other Player"].Y-self.Y)/10
		pass
		pass
	def FaultReversal(self):
		if self.Meter>int(self.MaxMeter/2) and abs(self.X-self.Tags["Other Player"].X)<200:
			self.FaultReversalTag=1
			self.X+=(self.Tags["Side"]-0.5)*-512
			self.Meter-=int(self.MaxMeter/2)
			if self.Y<0 or self.YV<0:
				self.State=self.Jump
			else:
				#self.X+=(self.Tags["Side"]-0.5)*-128
				self.State=self.Idle
	def RomanCancel(self):
		"""if self.SSN in ["Idle","Jump"]:
			if self.Meter>int(self.MaxMeter/2) and abs(self.X-self.Tags["Other Player"].X)<200:
				self.FaultReversalTag=1
				self.MakeScreenSpaceText("FAULT")
				self.HitLag+=30
				self.X+=(self.Tags["Side"]-0.5)*-512
				self.Meter-=int(self.MaxMeter/2)
				self.Y=-10
				self.YV=-10
				self.State=self.Jump
			elif self.Meter==self.MaxMeter:
				self.FaultReversalTag=1
				self.MakeScreenSpaceText("FAULT")
				self.HitLag+=30
				self.X=self.Tags["Other Player"].X+(self.Tags["Side"]-0.5)*-512
				self.Meter-=self.MaxMeter
				self.Y=-10
				self.YV=-10
				self.State=self.Jump"""
		if self.Meter>int(self.MaxMeter/4):
			#self.FaultReversalTag=1
			self.MakeScreenSpaceText("CANCEL")
			self.IPSBuffer=[]
			self.HitLag+=30
			if self.Y<0 or self.YV<0:
				self.State=self.Jump
			else:
				#self.X+=(self.Tags["Side"]-0.5)*-128
				self.State=self.Idle
			self.Meter-=int(self.MaxMeter/4)
	def BurstCancel(self):
		if self.Meter>=self.MaxMeter or self.Tags["Other Player"].IPSProne:
			self.MakeScreenSpaceText("BURST")
			self.Triggers=[{"Box":[[-64,64],[-128,0]],"Type":"Hit",
				"Damage":50,
				"Chip Damage":0,
				"Stun":30,
				"Block Stun":5,
				"Knockback":30,
				"Hit Lag":30,
				"Knockback2":30,
				"Attributes":[],
				}]
			if self.Y<0 or self.YV<0:
				self.State=self.Jump
			else:
				#self.X+=(self.Tags["Side"]-0.5)*-128
				self.State=self.Idle
			if not self.Tags["Other Player"].IPSProne:
				self.Meter=0
	def Nogeki(self):
		#self.Meter-=100
		pass
	def Pangeki(self):
		self.Sounds.append(self.HitSounds["Pangeki"][self.RNG()%len(self.HitSounds["Pangeki"])])
		"""if self.Meter==24:
			self.Sounds.append(self.MiscSounds["Gopan"])
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.CutIns[random.choice([2,5,6])],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
		elif self.Meter%5==4:
			self.Sounds.append(self.MiscSounds["Panchira Increase"])
			#Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.CutIns[[6,2,9,8][int(self.Meter/5)]],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))"""
		self.Meter+=20
		pass
	def __call__(self,Tags):
		self.FaultReversalTag=0
		R=self.ViperOne.Frame(Tags)
		if Tags["Controller"]["m"] and Tags["Controller"]["h"]:
			self.BurstCancel()
		elif Tags["Controller"]["l"] and Tags["Controller"]["m"]:
			self.RomanCancel()
		#if Tags["Controller"]["l"] and Tags["Controller"]["h"]:
			#self.FaultReversal()
		R["Hit Lag"]=self.HitLag
		R["Sounds"]=self.Sounds
		R["Sprites"]=self.TS
		R["Fault Reversal"]=self.FaultReversalTag
		R["GUI"]=[
		#{"Sprite":self.PanchiraGuage[int(self.Meter/5)],"X":5,"Y":37,"W":128,"H":32}
		]
		self.Meter=min(max(self.Meter,0),self.MaxMeter)
		self.Triggers=copy.deepcopy(self.Triggers)
		"""for i in self.Triggers:
			if i["Type"]=="Hit":
				i["Damage"]/=1+max(self.Meter/self.MaxMeter/10,0)
				i["Chip Damage"]/=1+max(self.Meter/self.MaxMeter/10,0)
				i["Stun"]+=Tags["Fault"]*2+2
				i["Block Stun"]+=Tags["Fault"]*2+2"""
		return R
	def Idle(self,Tags):
		self.XV=0
		self.AirDashable=self.MaxAirDash
		self.The48Frame=False
		self.SSN="Idle"
		self.SN=["idle1","idle2","idle3","idle2"][int(self.StateFrame/12)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		"""elif Tags["Controller"]["l"] and Tags["Controller"]["m"] and self.Meter>=int(self.MaxMeter/2):# and Tags["Controller"]["Y2"]==-1:
			Tags["Other Player"].HalfTime+=50
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.MegaCutIns[0],BackgroundColor=(0,0,0),Y=30,LifeTime=12))
			self.Meter-=int(self.MaxMeter/2)"""
		if Tags["Controller"]["l"] and Tags["Controller"]["m"] and Tags["Controller"]["h"] and self.Meter>=self.MaxMeter:# and Tags["Controller"]["Y2"]==-1:
			#Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.MegaCutIns[0],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.MegaCutIns[0],BackgroundColor=(0,0,0),Y=30,LifeTime=12))
			##self.Nogeki()
			pygame.mixer.music.set_volume(0)
			self.Sounds.append(self.HitSounds["The24Frame"])
			self.State=self.The24Frame
		elif Tags["Controller"]["v"]:
			self.MakeScreenSpaceText("VENOM")
			self.X=self.Tags["Other Player"].X-32
			self.HitLag=30
			self.CancelStates["gv"]()
		elif Tags["Controller"]["l"]:
			self.CancelStates["gl"]()
		elif Tags["Controller"]["h"]:
			self.CancelStates["gh"]()
		elif Tags["Controller"]["m"]:
			self.CancelStates["gm"]()
		elif Tags["Controller"]["Jump2"]:
			self.CancelStates["Jump"]()
		elif not Tags["Controller"]["X"] == 0:
			"""if self.DashTimer<2:
				self.State=[self.Dash,self.BackDash][Tags["Controller"]["X"] == Tags["Side"]*2-1]
			else:"""
			self.State=[self.Walk,self.BackWalk][Tags["Controller"]["X"] == Tags["Side"]*2-1]
			#self.DashTimer=0
		self.DashTimer+=1
		return {}
	def Walk(self,Tags):
		if self.StateFrame>15:
			self.Meter+=int((self.StateFrame-15)/5)
		self.SSN="Walk"
		self.AirDashable=self.MaxAirDash
		self.SN=["walk1","walk2","walk3","walk4"][int(self.StateFrame/25)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.YV=0
		self.XV=Tags["Controller"]["X"]*4
		"""if Tags["Controller"]["Fierce"] and Tags["Controller"]["Strong"] and Tags["Controller"]["Jab"] and self.Meter==self.MaxMeter and Tags["Controller"]["Y2"]==-1:
			#Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.MegaCutIns[0],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.MegaCutIns[0],BackgroundColor=(0,0,0),Y=30,LifeTime=12))
			##self.Nogeki()
			pygame.mixer.music.set_volume(0)
			self.Sounds.append(self.HitSounds["The24Frame"])
			self.State=self.The24Frame"""
		if Tags["Controller"]["v"]:
			self.MakeScreenSpaceText("VENOM")
			self.X=self.Tags["Other Player"].X-32
			self.HitLag=30
			self.CancelStates["gv"]()
		elif Tags["Controller"]["l"]:
			self.CancelStates["gl"]()
		elif Tags["Controller"]["h"]:
			self.CancelStates["gh"]()
		elif Tags["Controller"]["m"]:
			self.CancelStates["gm"]()
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		elif Tags["Controller"]["Jump2"]:
			self.JumpCancel()
		elif not Tags["Controller"]["X"] == Tags["Side"]*-2+1:
			self.State=self.Idle
		return {}
	def BackWalk(self,Tags):
		self.SSN="Block"
		self.SN=["walk2","walk1","walk4","walk3"][int(self.StateFrame/40)%4]
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.Y=0
		self.AirDashable=self.MaxAirDash
		self.YV=0
		self.XV=Tags["Controller"]["X"]*2
		if Tags["Controller"]["l"]:
			self.CancelStates["gl2"]()
		elif Tags["Controller"]["h"]:
			self.CancelStates["gh"]()
		elif Tags["Controller"]["m"]:
			self.CancelStates["gm"]()
		#if Tags["Controller"]["X"] == 0:
			#self.State=self.Idle
		elif Tags["Controller"]["Jump"]:
			self.JumpCancel()
		elif not Tags["Controller"]["X"] == Tags["Side"]*2-1:
			self.State=self.Idle
		return {}
	def Jump(self,Tags):
		self.SSN="Jump"
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="jump"
		if Tags["Controller"]["l"]:
			self.CancelStates["al"]()
		elif Tags["Controller"]["m"]:
			self.CancelStates["am"]()
		elif Tags["Controller"]["h"]:
			self.CancelStates["ah"]()
		"""elif Tags["Controller"]["Jump2"] and self.AirDashable:
			self.NogekiJumpCancel()"""
		if Tags["Controller"]["X"]!=0:
			if Tags["Side"]==1 and Tags["Controller"]["X"]>0:
				self.SSN="Block"
				pass
			elif Tags["Side"]==0 and Tags["Controller"]["X"]<0:
				self.SSN="Block"
				pass
		if Tags["Controller"]["X2"]!=0:
			if self.AirDashable and self.DashTimer<20:
				if Tags["Controller"]["X2"] == Tags["Side"]*2-1:
					self.State=self.BackDash
					#self.Pangeki()
				else:
					self.State=self.Dash
					#self.Pangeki()
			self.DashTimer=0
		if self.Y<0 or self.YV<0:
			self.YV+=1
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
	def NogekiJumpCancel(self):
		if self.AirDashable:
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			#self.HitLag+=10
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.CutIns[4],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
			self.YV=-self.AirDashable*4
			self.XV=self.Tags["Controller"]["X"]*8
			self.AirDashable-=1
			self.State=self.Jump
	def JumpCancel(self):
		self.YV=-self.AirDashable*4
		self.XV=self.Tags["Controller"]["X"]*8
		#self.AirDashable=1
		self.State=self.Jump
	def PanchiraJumpCancel(self):
		if self.Meter>=100 and self.AirDashable:
			#self.HitLag+=10
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.CutIns[4],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
			self.YV=-self.AirDashable*4
			self.XV=self.Tags["Controller"]["X"]*8
			self.Meter-=100
			self.AirDashable-=1
			self.State=self.Jump
	def AutoPanchiraJumpCancel(self):
		if self.Meter>=500 and self.AirDashable:
			self.HitLag+=10
			self.Sounds.append(self.MiscSounds["Jump Cancel"])
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.ViperOne.Player,Sprite=self.CutIns[4],BackgroundColor=[(0,255,255),(255,0,255)][self.ViperOne.Player],Y=30))
			self.YV=-self.AirDashable*4
			self.XV=-(self.Tags["Side"]-0.5)*16#self.Tags["Controller"]["X"]*8
			self.Meter-=500
			self.AirDashable-=1
			self.State=self.Jump
	def The24Frame(self,Tags):
		self.HitBoxerFrameData=self.The24FrameData
		self.SSN="Attack"
		self.YV=0
		self.SN=self.The24FrameData["Animation"][self.StateFrame]
		self.Triggers=self.The24FrameData["Triggers"][self.StateFrame]
		if self.StateFrame == 0 or self.StateFrame == 1:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 1"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == 2:
			self.TS.append({"Sprite":self.Sprites["fierce swoosh 2"],"X":0,"Y":-55,"W":128,"H":128})
		if self.StateFrame == self.The24FrameData["Frames"]:
			pygame.mixer.music.set_volume(1)
			self.State=self.Idle
		return {}
	def HitStun(self, Tags):
		#self.XV/=1.3
		self.Meter+=5
		if self.Y<0:
			#self.YV/=1.3
			self.YV+=1
		#self.YV+=5
		self.SSN="HitStun"
		self.AirDashable=self.MaxAirDash
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="hitstun1"
		if self.StateFrame>self.Stun:
			self.Stun=0
			#self.XV=0
			if self.Y<0:
				#self.XV=Tags["Side"]*60-30
				self.State=self.Jump
			else:
				self.State=self.Idle
		return {}
	def Knockdown(self, Tags):
		self.XV/=1.1
		self.SSN="Knockdown"
		self.AirDashable=self.MaxAirDash
		if self.Y<-16:
			[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		else:
			self.Triggers=[]
		self.SN="knockdown"
		self.YV+=1
		if self.Y>-1:
			self.YV/=-5
			self.Y=-1
		if Tags["Controller"]["Jump2"]:
			self.State=self.Jump
			self.YV=-30
		if self.StateFrame>48:
			self.YV=0
			self.Y=0
			self.Stun=0
			self.State=self.Idle
		return {}
	def BlockStun(self,Tags):
		self.SSN="Block"
		self.Triggers=[{"Box":[[-25,30],[-105,0]],"Type":"Hurt"}]
		self.SN="jump"
		self.Meter-=3
		self.XV=(self.Tags["Side"]-0.5)*4
		if self.Y<0 or self.YV<0:
			self.YV+=1
			if self.StateFrame>self.Stun:
				self.State=self.Jump
		else:
			self.Y=0
			self.YV=0
			if self.StateFrame>self.Stun:
				self.State=self.BackWalk
		return {}
	def Dash(self,Tags):
		self.Meter+=2
		self.SSN="Dash"
		self.SN="dash1"
		self.DashTimer=5
		self.YV=0
		if self.Y<0:
			if Tags["Controller"]["l"]:
				self.CancelStates["al"]()
			elif Tags["Controller"]["h"]:
				self.CancelStates["ah"]()
			elif Tags["Controller"]["m"]:
				self.CancelStates["am"]()
			elif Tags["Controller"]["Jump2"]:
				self.CancelStates["NogekiJumpCancel"]()
		else:
			if Tags["Controller"]["l"]:
				self.CancelStates["gl"]()
			elif Tags["Controller"]["h"]:
				self.CancelStates["gh"]()
			elif Tags["Controller"]["m"]:
				self.CancelStates["gm"]()
			elif Tags["Controller"]["Jump2"]:
				self.CancelStates["Jump"]()
		if self.StateFrame==0:
			self.AirDashable-=1
			self.XV=20*(-Tags["Side"]+0.5)
		elif numpy.sign(self.XV) != numpy.sign(50*(-Tags["Side"]+0.5)):
			self.State=self.BackDash
		if self.StateFrame > 5 and (-Tags["Side"]+0.5)*Tags["Controller"]["X"]<0.1:
			self.XV=25*(-Tags["Side"]+0.5)
			if self.Y==0:
				self.State=self.Idle
			else:
				self.State=self.Jump
		return {}
		pass
	def BackDash(self,Tags):
		self.SSN="Dash"
		self.SN="dash2"
		self.DashTimer=5
		self.YV=0
		if self.StateFrame==0:
			self.AirDashable-=1
			self.XV=6*(Tags["Side"]-0.5)
		elif numpy.sign(self.XV) != numpy.sign(30*(Tags["Side"]-0.5)):
			self.State=self.Dash
		if self.StateFrame > 20:# and (Tags["Side"]-0.5)*Tags["Controller"]["X"]<0.1:
			self.XV=15*(Tags["Side"]-0.5)
			if self.Y==0:
				self.State=self.Idle
			else:
				self.State=self.Jump
		return {}
		pass
