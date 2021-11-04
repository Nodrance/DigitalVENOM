from Renderers import Loli
import pygame,json,copy
SelectedTrigger=0
Frame=0
HitBoxResizeSpeed=5
SpriteOffset=(0,0)
SpriteWidth=128
SpriteHeight=128
Sprites={}
TriggerSprite1=pygame.image.load("Sprites/Trigger.png").convert()
TriggerSprite2=pygame.image.load("Sprites/Trigger2.png").convert()
AttackData=[]

Camera=Loli.LoliCamera(0,0,-1,1)

class TriggerSelecter:
	def __init__(self,i):
		self.i=i
	def Function(self):
		global SelectedTrigger
		SelectedTrigger=self.i

def ExitHitBoxer():
	return "Exit"

def AddStartupFrame():
	AttackData["Triggers"].insert(0,AttackData["Triggers"][0])
	AttackData["Animation"].insert(0,AttackData["Animation"][0])
	AttackData["Cancels"].insert(0,AttackData["Cancels"][0])
	pass

def SelectTrigger():
	global AttackData,Frame
	X=[]
	for i in range(len(AttackData["Triggers"][Frame])):
		X.append(Loli.MenuLabel("Trigger "+str(i),Function=TriggerSelecter(i).Function))
	return Loli.SlideMenu(X).Open()
	pass

def DeleteSelectedTrigger():
	global AttackData,Frame,SelectedTrigger
	if len(AttackData["Triggers"][Frame])>1:
		AttackData["Triggers"][Frame].pop(SelectedTrigger)
		SelectedTrigger=0

def DuplicateTrigger():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame].append(copy.deepcopy(AttackData["Triggers"][Frame][SelectedTrigger]))
	pass

def ExportJSONFile():
	global AttackData
	json.dump(AttackData,open("HitBoxerAttackData.json","w"),indent="\t")
	pass

def Implement():
	global AttackData
	json.dump(AttackData,open(AttackData["Filename"],"w"),indent="\t")
	pass

def ConvertToHurtBox():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Type"]="Hurt"

def DoubleFrames():
	global AttackData,Frame,SelectedTrigger
	at=AttackData.copy()
	TR=[]
	for F in range(len(AttackData["Triggers"])):
		TR.append(AttackData["Triggers"][F])
		TR.append(AttackData["Triggers"][F])
	AN=[]
	for F in range(len(AttackData["Animation"])):
		AN.append(AttackData["Animation"][F])
		AN.append(AttackData["Animation"][F])
	CA=[]
	for F in range(len(AttackData["Cancels"])):
		CA.append(AttackData["Cancels"][F])
		CA.append(AttackData["Cancels"][F])
	AttackData["Triggers"]=TR
	AttackData["Animation"]=AN
	AttackData["Cancels"]=CA
	AttackData["Frames"]*=2

def AddBlankAttributes():
	global AttackData,Frame,SelectedTrigger
	for F in range(len(AttackData["Triggers"])):
		for J in range(len(AttackData["Triggers"][F])):
			AttackData["Triggers"][F][J]["Attributes"]=[]

def ConvertToHitBox():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Type"]="Hit"

def SetHitBoxDamage():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Damage"]=int(Loli.TextInputBox())

def SetHitBoxChipDamage():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["ChipDamage"]=int(Loli.TextInputBox())

def SetHitBoxStun():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Stun"]=int(Loli.TextInputBox())

def SetHitBoxBlockStun():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Block Stun"]=int(Loli.TextInputBox())

def SetHitBoxKnockback():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Knockback"]=int(Loli.TextInputBox())

def SetHitBoxVerticalKnockback():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Knockback2"]=int(Loli.TextInputBox())

def SetHitBoxHitLag():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Hit Lag"]=int(Loli.TextInputBox())

def SetHitBoxDefaultAttributes():
	global AttackData,Frame,SelectedTrigger
	AttackData["Triggers"][Frame][SelectedTrigger]["Damage"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["ChipDamage"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["Stun"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["Block Stun"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["Knockback"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["Knockback2"]=1
	AttackData["Triggers"][Frame][SelectedTrigger]["Hit Lag"]=1

def HitBoxAttributes():
	Loli.SlideMenu([
		Loli.MenuLabel("Damage",Function=SetHitBoxDamage),
		Loli.MenuLabel("Chip Damage",Function=SetHitBoxChipDamage),
		Loli.MenuLabel("Stun",Function=SetHitBoxStun),
		Loli.MenuLabel("Block Stun",Function=SetHitBoxBlockStun),
		Loli.MenuLabel("Knockback",Function=SetHitBoxKnockback),
		Loli.MenuLabel("Vertical Knockback",Function=SetHitBoxVerticalKnockback),
		Loli.MenuLabel("Hit Lag",Function=SetHitBoxHitLag),
		]).Open()

def ChangeTriggerType():
	global AttackData,Frame,SelectedTrigger
	return Loli.SlideMenu([
		Loli.MenuTitle("Trigger Type"),
		Loli.MenuLabel("Current Type:"+AttackData["Triggers"][Frame][SelectedTrigger]["Type"]),
		Loli.MenuLabel("Hurt Box",Function=ConvertToHurtBox),
		Loli.MenuLabel("Hit Box",Function=ConvertToHitBox),
		]).Open()
	pass

def Menu():
	global Frame
	return Loli.SlideMenu([
		Loli.MenuTitle("HitBoxer"),
		Loli.MenuLabel("Frame:"+str(Frame)),
		Loli.MenuLabel("Select Trigger",Function=SelectTrigger),
		Loli.MenuLabel("Delete Selected Trigger",Function=DeleteSelectedTrigger),
		Loli.MenuLabel("Duplicate Selected Trigger",Function=DuplicateTrigger),
		Loli.MenuLabel("Change Trigger Type",Function=ChangeTriggerType),
		Loli.MenuLabel("Hit Box Attributes",Function=HitBoxAttributes),
		Loli.MenuLabel("Export JSON",Function=ExportJSONFile),
		Loli.MenuLabel("Double Frames",Function=DoubleFrames),
		Loli.MenuLabel("Implement (Requires match restart)",Function=Implement),
		Loli.MenuLabel("Exit",Function=ExitHitBoxer),
		]).Open()

def Render():
	global AttackData,SelectedTrigger,Camera,TriggerSprite1,SpriteOffset,SpriteWidth,SpriteHeight
	Loli.win.fill(0)
	Loli.RenderSprite(Sprites[AttackData["Animation"][Frame]],(SpriteOffset[0],SpriteOffset[1],0),SpriteWidth,SpriteHeight,Camera)
	for l in range(len(AttackData["Triggers"][Frame])):
		i=AttackData["Triggers"][Frame][l]
		if l==SelectedTrigger:
			Loli.RenderSprite(TriggerSprite2,((i["Box"][0][1]+i["Box"][0][0])/2,(i["Box"][1][1]+i["Box"][1][0])/2,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD)
		else:
			Loli.RenderSprite(TriggerSprite1,((i["Box"][0][1]+i["Box"][0][0])/2,(i["Box"][1][1]+i["Box"][1][0])/2,0),i["Box"][0][1]-i["Box"][0][0],i["Box"][1][1]-i["Box"][1][0],Camera,pygame.BLEND_ADD)
		pass
	Loli.ScaleWin()
	pass

def Start():
	global HitBoxResizeSpeed,Frame,SelectedTrigger
	SelectedTrigger=0
	Frame=0
	try:
		AttackData["Cancels"]
	except:
		AttackData["Cancels"]=[]
		for i in range(AttackData["Frames"]+1):
			AttackData["Cancels"].append([])
	while 1:
		for Event in pygame.event.get():
			if Event.type==pygame.KEYDOWN:
				if Event.key==pygame.K_ESCAPE:
					X=Menu()
					if X=="Exit":
						return
					pass
				if Event.key==pygame.K_w:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][1][0]-=5
				if Event.key==pygame.K_a:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][0][0]-=5
				if Event.key==pygame.K_s:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][1][0]+=5
				if Event.key==pygame.K_d:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][0][0]+=5
				if Event.key==pygame.K_UP:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][1][1]-=5
				if Event.key==pygame.K_LEFT:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][0][1]-=5
				if Event.key==pygame.K_DOWN:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][1][1]+=5
				if Event.key==pygame.K_RIGHT:
					AttackData["Triggers"][Frame][SelectedTrigger]["Box"][0][1]+=5
				if Event.key==pygame.K_z:
					Frame-=1
					Frame%=len(AttackData["Triggers"])
				if Event.key==pygame.K_x:
					Frame+=1
					Frame%=len(AttackData["Triggers"])
		Render()