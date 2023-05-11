class parent:
	def __init__(self):
		print("parent class constructor")
	def m1(self):
		print("inside parent class IM")
class child(parent):
	def __init__(self):
		super().__init__()
		print("child class constructor")
		super().__init__()

	def m2(self):
		print("child class IM")
		super().m1()
c=child()
c.m2()
c.m1()