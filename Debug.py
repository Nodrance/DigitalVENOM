from Controllers import Owen,Eden,EdenJoystick,Replayer
from Characters import InjectionCube,QuW
from Renderers import Loli
from Rulesets import Competitive,Warmup,Training
from Engines import Alchemy
from Stages import VenomCompetitive,VenomWarmup,City
from Tools import HitBoxer
import sys,copy,json,pygame,dis,inspect

"""for Function in inspect.getmembers(Loli, inspect.isfunction):
	#print(Function)
	print("PYTHON       :")
	print(Function[0])
	print("BYTECODE     :")
	print(inspect.getsource(Function[1]))
	dis.dis(Function[1])"""

def BlankFunction():
	pass

class BytecodeFunctionLabel:
	def __init__(self,Function):
		self.Function=Function
	def __call__(self):
		Loli.SlideMenu([
			Loli.MenuLabel(i,Function=BlankFunction) for i in dis.Bytecode(self.Function).dis().split("\n")
			]).Open()

class ModuleBytecodeFunctionLabel:
	def __init__(self,Module):
		self.Module=Module
	def __call__(self):
		Loli.SlideMenu([
			Loli.MenuLabel(i[0],Function=BytecodeFunctionLabel(i[1])) for i in inspect.getmembers(self.Module, inspect.isfunction)
			]).Open()

def BytecodeMenu():
	X=sys.modules.copy()
	Y={}
	for i in X:
		try:
			Y[i]=inspect.getmembers(X[i], inspect.isfunction)
		except:
			pass
	Loli.SlideMenu([
		Loli.MenuLabel(i,Function=ModuleBytecodeFunctionLabel(X[i])) for i in Y if len(Y[i])>0
		]).Open()
	pass

class SourceFunctionLabel:
	def __init__(self,Function):
		self.Function=Function
	def __call__(self):
		Loli.SlideMenu([
			Loli.MenuLabel(i,Function=BlankFunction) for i in inspect.getsource(self.Function).split("\n")
			]).Open()

class ModuleSourceFunctionLabel:
	def __init__(self,Module):
		self.Module=Module
	def __call__(self):
		Loli.SlideMenu([
			Loli.MenuLabel(i[0],Function=SourceFunctionLabel(i[1])) for i in inspect.getmembers(self.Module, inspect.isfunction)
			]).Open()

def SourceMenu():
	X=sys.modules.copy()
	Y={}
	for i in X:
		try:
			Y[i]=inspect.getmembers(X[i], inspect.isfunction)
		except:
			pass
	Loli.SlideMenu([
		Loli.MenuLabel(i,Function=ModuleSourceFunctionLabel(X[i])) for i in Y if len(Y[i])>0
		]).Open()
	pass

def DebugMenu():
	Loli.SlideMenu([
		Loli.MenuTitle("Debug Menu"),
		Loli.MenuLabel("View Bytecode",Function=BytecodeMenu),
		Loli.MenuLabel("View Source Code",Function=SourceMenu),
		]).Open()
	pass