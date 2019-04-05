class Circle:
	def __init__(self, raduis=10, x=0, y=0):
		self.raduis=raduis
		self.x=x
		self.y=y
	
	def values(self):
		print("Raduis=",self.raduis, " x=", self.x, " y=", self.y)

	def changevalues(self,raduis,x,y):
		self.x=x
		self.y=y
		self.raduis=raduis
