import copy,random,math,json,pygame,numpy
from Renderers import Loli
class Cancel:
	def __init__(self,CHA,State):
		self.CHA=CHA
		self.State=State
	def __call__(self):
		self.CHA.State=self.State
class Move:
	def __init__(self,Character,FrameData,SSN,PreFrame=None,PreMove=None,PostFrame=None,PostMove=None):
		self.Character=Character
		self.FrameData=FrameData
		self.SSN=SSN
		self.CancelState=None
		self.PreFrame=PreFrame
		self.PostFrame=PostFrame
		self.PreMove=PreMove
		self.PostMove=PostMove
		pass
	def __call__(self,Tags):
		if self.Character.StateFrame==0 and self.PreMove!=None:
			self.PreMove()
		elif self.PreFrame!=None:
			self.PreFrame()
		self.Character.HitBoxerFrameData=self.FrameData
		self.Character.SSN=self.SSN
		self.Character.SN=self.FrameData["Animation"][self.Character.StateFrame]
		self.Character.Triggers=self.FrameData["Triggers"][self.Character.StateFrame]
		if self.Character.Y<0:
			self.Character.YV+=1
		if self.SSN.lower().startswith("a"):
			#self.Character.YV+=5
			#if self.Character.StateFrame==0:
				#self.Character.YV=-20
			#self.Character.YV+=3
			#self.Character.XV/=1.3
			#self.Character.YV/=1.3
			#self.HitNudge()
			if self.Character.Y>=0:
				self.Character.State=self.Character.Idle
				if self.PostMove!=None:
					self.PostMove()
		else:
			self.Character.XV=0
		if self.Character.StateFrame == self.FrameData["Frames"]:
			self.Character.State=self.Character.Jump
		for Cancel in self.FrameData["Cancels"][self.Character.StateFrame]:
			if min([Tags["Controller"][Condition] in Cancel["Conditions"][Condition] for Condition in Cancel["Conditions"]]):
				self.CancelState=Cancel["State"]
			if Cancel["Effect"] and self.CancelState!=None:
				#self.Character.State=self.Character.States[self.CancelState]
				self.Character.CancelStates[self.CancelState]()
				X=self.CancelState
				self.CancelState=None
				if self.PostMove!=None:
					self.PostMove()
				return {"CancelState":X}
		if self.PostFrame!=None:
			self.PostFrame()
		pass
	def HitNudge(self):
		"""if abs(self.Character.X-self.Character.Tags["Other Player"].X)+abs(self.Character.Y-self.Character.Tags["Other Player"].Y) < 200:
			self.Character.XV+=(self.Character.Tags["Other Player"].X-self.Character.X)/20
			self.Character.YV+=(self.Character.Tags["Other Player"].Y-self.Character.Y)/20"""
		pass
		pass
class Default:
	def __init__(self,Player,DIR,Character,MaxHealth=500,Offset=(0,-64),Height=128,Width=128):
		self.StartDistance=100
		self.MaxHealth=MaxHealth
		self.Player=Player
		self.Offset=Offset
		self.Height=Height
		self.Width=Width
		self.DIR=DIR
		self.Character=Character
		pass
	def Reset(self,CHA):
		CHA.Health=self.MaxHealth
		CHA.MaxHealth=self.MaxHealth
		CHA.X=2*self.StartDistance*self.Player-self.StartDistance
		CHA.Y=0
		CHA.XV=0
		CHA.YV=0
		CHA.KV=0
		CHA.HalfTime=0
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
	def Frame(self,Tags):
		self.Character.Tags=Tags
		if self.Character.LTags=={}:
			self.Character.LTags=Tags
		self.Character.Tags=Tags
		self.Character.HitLag=0
		self.Character.TS=[]
		self.Character.Sounds=[]
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
				if self.Character.SSN=="Block":
					self.Character.Health-=Damage
					self.Character.StateFrame=-1
					self.Character.State=self.Character.BlockStun
					self.Character.Stun=BlockStun
					pass
				else:
					self.Character.Health-=Damage
					self.Character.StateFrame=-1
					self.Character.YV=-Knockback2
					self.Character.XV=Knockback*(Tags["Side"]-0.5)
					self.Character.KV=0
					if "Knockdown" in i[1]["Attributes"]:
						self.Character.CancelStates["Knockdown"]()
						self.Character.Stun=Stun
					else:
						self.Character.State=self.Character.HitStun
						self.Character.Stun=Stun
			if i[0]["Type"]=="Hurt" and i[1]["Type"]=="Grab":
				self.Character.Grabbed=1
				Damage+=i[1]["Damage"]
				ChipDamage+=i[1]["Chip Damage"]
				Stun=i[1]["Stun"]
				BlockStun+=i[1]["Block Stun"]
				GrabX+=i[1]["Knockback"]
				GrabY=i[1]["Knockback2"]
		if self.Character.Grabbed:
			self.Character.State=self.Character.Idle
			self.Character.X=GrabX
			self.Character.Y=GrabY
		if self.Character.State==self.Character.BackState:
			self.Character.StateFrame+=1
		else:
			self.Character.StateFrame=0
			self.Character.BackState=self.Character.State
		self.Character.State(Tags)
		R={}
		for i in Tags["Triggers"]:
			if i[0]["Type"]=="Hit" and i[1]["Type"]=="Hurt":
				self.Character.HitLag+=i[0]["Hit Lag"]
				"""if self.Character.State in [self.Character.States["gh"],self.Character.States["gb"],self.Character.States["ah"],self.Character.States["ab"]]:
					self.Character.Sounds.append(random.choice(self.Character.HitSounds["Light"]))
				if self.Character.State in [self.Character.States["gj"],self.Character.States["gn"],self.Character.States["aj"],self.Character.States["an"]]:
					self.Character.Sounds.append(random.choice(self.Character.HitSounds["Medium"]))
				if self.Character.State in [self.Character.States["gk"],self.Character.States["gm"],self.Character.States["ak"],self.Character.States["am"]]:# and not self.Character.The48Frame:
					self.Character.Sounds.append(random.choice(self.Character.HitSounds["Heavy"]))"""
				if Tags["Other Player"].SSN=="HitStun":
					self.Character.Combo+=1
					self.Character.IPSProne=self.Character.SSN in self.Character.IPSBuffer
					self.Character.IPSBuffer.append(self.Character.SSN)
				else:
					self.Character.Combo=1
					self.Character.IPSProne=0
					self.Character.IPSBuffer=[self.Character.SSN]
		if Tags["Other Player"].SSN!="HitStun":
			self.Character.IPSProne=0
		self.Character.IPSProne=self.Player
		if self.Character.SN!=self.Character.TSN:
			self.Character.Sprite=self.Character.Sprites[self.Character.SN]
			self.Character.TSN=self.Character.SN
		self.Character.X+=self.Character.XV
		self.Character.Y+=self.Character.YV
		if R==None:
			R={}
		Tags["Side"]=self.Character.X>Tags["Other Player"].X
		if self.Character.Y>0:
			self.Character.Y=0
		if Tags["Side"]==1:
			self.Character.HitFlip()
		if Tags["Fault"]>self.Character.LTags["Fault"]:
			Loli.LocalAlerts.append(Loli.AlertCutIn(Side=self.Character.ViperOne.Player,Sprite=self.Character.CutIns[1],BackgroundColor=[(0,255,255),(255,0,255)][self.Character.ViperOne.Player],Y=30))
		self.Character.LTags=Tags
		return R