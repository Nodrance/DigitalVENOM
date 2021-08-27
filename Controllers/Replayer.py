class Controller:
	def __init__(self,pygame,Player=0,ReplayData=[]):
		self.ReplayData=ReplayData
		self.Player=Player
		self.Frame=0
		pass
	def Character(self,pygame):
		try:
			self.Frame+=1
			return self.ReplayData[self.Frame][self.Player]
		except:
			return self.ReplayData[self.Frame-1][self.Player]
		pass
	pass