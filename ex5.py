class parent:
	a=100
	def __init__(self):
		print("inside parent class constructor")
		self.b=20
	def i_m(self):
		print("inside parent class IM")
	@staticmethod
	def s_m():
		print("inside parent class SM")
	@classmethod
	def c_m(cls):
		print("inside parent class CM")
class child(parent):
	pass
c=child()
c.__init__()
c.i_m()
c.s_m()
c.c_m()
print(c.a)
print(c.b)