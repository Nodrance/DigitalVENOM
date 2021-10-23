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
		if self.SSN=="Aerial":
			#self.Character.YV+=5
			#if self.Character.StateFrame==0:
				#self.Character.YV=-20
			#self.Character.YV+=3
			self.Character.XV/=1.3
			self.Character.YV/=1.3
			#self.HitNudge()
			if self.Character.Y>=0:
				self.Character.State=self.Character.Idle
				if self.PostMove!=None:
					self.PostMove()
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
		global TagsGlobal
		#self.Panchira=0
		if abs(self.Character.X-self.Character.Tags["Other Player"].X)+abs(self.Character.Y-self.Character.Tags["Other Player"].Y) < 200:
			self.Character.XV+=(self.Character.Tags["Other Player"].X-self.Character.X)/20
			self.Character.YV+=(self.Character.Tags["Other Player"].Y-self.Character.Y)/20
		pass
		pass
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