import math

class circle:
	def __init__(self,r):
		self.r = r

	def square(self):
		result = math.pi * (self.r**2)
		return int(result)
	def perimetr(self):
		result = 2 * math.pi * self.r
		return int(result)