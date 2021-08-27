import copy,types
from Characters import ViperOne
Costume="64Cyan"
Character=ViperOne.Character()
Character.Settings=ViperOne.Settings()
Character.Settings.DIR="Characters/QuW"
Character.Settings.Sprites={
		"idle1":"Characters/QuW/Sprites/"+Costume+"/Idle1.png",
		"idle2":"Characters/QuW/Sprites/"+Costume+"/Idle2.png",
		"idle3":"Characters/QuW/Sprites/"+Costume+"/Idle3.png",
		"hitstun1":"Characters/QuW/Sprites/"+Costume+"/HitStun1.png",
		"jab1":"Characters/QuW/Sprites/"+Costume+"/Jab1.png",
		"jab2":"Characters/QuW/Sprites/"+Costume+"/Jab2.png",
		"strong1":"Characters/QuW/Sprites/"+Costume+"/Strong1.png",
		"strong2":"Characters/QuW/Sprites/"+Costume+"/Strong2.png",
		"fierce1":"Characters/QuW/Sprites/"+Costume+"/Fierce1.png",
		"short1":"Characters/QuW/Sprites/"+Costume+"/Short1.png",
		"short2":"Characters/QuW/Sprites/"+Costume+"/Short2.png",
		"forward1":"Characters/QuW/Sprites/"+Costume+"/Forward1.png",
		"forward2":"Characters/QuW/Sprites/"+Costume+"/Forward2.png",
		"roundhouse1":"Characters/QuW/Sprites/"+Costume+"/Roundhouse1.png",
		"roundhouse2":"Characters/QuW/Sprites/"+Costume+"/Roundhouse2.png",
		"kiss1":"Characters/QuW/Sprites/"+Costume+"/Kiss1.png",
		"kiss2":"Characters/QuW/Sprites/"+Costume+"/Kiss2.png",
		"jab aerial 1":"Characters/QuW/Sprites/"+Costume+"/JabAerial1.png",
		"strong aerial 1":"Characters/QuW/Sprites/"+Costume+"/StrongAerial1.png",
		"fierce aerial 1":"Characters/QuW/Sprites/"+Costume+"/FierceAerial1.png",
		"short aerial 1":"Characters/QuW/Sprites/"+Costume+"/ShortAerial1.png",
		"forward aerial 1":"Characters/QuW/Sprites/"+Costume+"/ForwardAerial1.png",
		"roundhouse aerial 1":"Characters/QuW/Sprites/"+Costume+"/RoundhouseAerial1.png",
		"walk1":"Characters/QuW/Sprites/"+Costume+"/Walk1.png",
		"walk2":"Characters/QuW/Sprites/"+Costume+"/Walk2.png",
		"walk3":"Characters/QuW/Sprites/"+Costume+"/Walk3.png",
		"walk4":"Characters/QuW/Sprites/"+Costume+"/Walk4.png",
		"jump":"Characters/QuW/Sprites/"+Costume+"/Jump.png",
		"jab swoosh 1":"Characters/QuW/Sprites/Effects/JabSwoosh1.png",
		"jab swoosh 2":"Characters/QuW/Sprites/Effects/JabSwoosh2.png",
		"strong swoosh 1":"Characters/QuW/Sprites/Effects/StrongSwoosh1.png",
		"strong swoosh 2":"Characters/QuW/Sprites/Effects/StrongSwoosh2.png",
		"fierce swoosh 1":"Characters/QuW/Sprites/Effects/FierceSwoosh1.png",
		"fierce swoosh 2":"Characters/QuW/Sprites/Effects/FierceSwoosh2.png",
		"short swoosh 1":"Characters/QuW/Sprites/Effects/ShortSwoosh1.png",
		"short swoosh 2":"Characters/QuW/Sprites/Effects/ShortSwoosh2.png",
		"forward swoosh 1":"Characters/QuW/Sprites/Effects/ForwardSwoosh1.png",
		"forward swoosh 2":"Characters/QuW/Sprites/Effects/ForwardSwoosh2.png",
		"roundhouse swoosh 1":"Characters/QuW/Sprites/Effects/RoundhouseSwoosh1.png",
		"roundhouse swoosh 2":"Characters/QuW/Sprites/Effects/RoundhouseSwoosh2.png",
		"heart":"Characters/QuW/Sprites/Effects/Heart.png",
		}
class Extra:
	def Reset(self,P,pygame):
		self.JabAerialData=self.ViperZero("JabAerial")
		self.StrongAerialData=self.ViperZero("StrongAerial")
		self.FierceAerialData=self.ViperZero("FierceAerial")
		self.ShortAerialData=self.ViperZero("ShortAerial")
		self.ForwardAerialData=self.ViperZero("ForwardAerial")
		self.RoundhouseAerialData=self.ViperZero("RoundhouseAerial")
		self.Sprite=self.Sprites["idle1"]
		pass
	def PreFrame(self,Tags):
		pass
	def PostFrame(self,Tags):
		self.R["GUI"]=[
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
				try:
					self.R["Sprites"].append(i)
				except:
					self.R["Sprites"]=i
		else:
			for i in [{"X":j[0]-self.X,"Y":j[1]-self.Y,"W":8,"H":8,"Sprite":self.Sprites["heart"]} for j in self.Hearts]:
				try:
					self.R["Sprites"].append(i)
				except:
					self.R["Sprites"]=i
		for i in range(len(self.Hearts)):
			if self.Hearts[i][0]<Tags["Stage"].Bounds[0]:self.Hearts.pop(i);break
			if self.Hearts[i][0]>Tags["Stage"].Bounds[1]:self.Hearts.pop(i);break
			if self.Hearts[i][1]<Tags["Stage"].Bounds[2]:self.Hearts.pop(i);break
			if self.Hearts[i][1]>0:self.Hearts.pop(i);break
		pass
Character.ExtraFunctions=Extra