class parent:
	def __init__(self):
		print("address of the parent class")
		print(id(self))
class child(parent):
	def __init__(self):
		super().__init__()
		print("address of the child class")
		print(id(self))
c=child()
print("address of c")
print(id(c))
