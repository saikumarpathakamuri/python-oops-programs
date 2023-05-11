class parent:
	def m1(self):
		print("parent class IM")
class child(parent):
	def m2(self):
		print("child class IM")
if __name__ == '__main__':
	c=child()
	c.m2()
	c.m1()