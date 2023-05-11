class student:
	def __init__(self,name,age):
		self.nam=name
		self.ag=age

	def sai(self):
		print("sai method")
	def tarun(self):
		self.sai()
if __name__ == '__main__':
	e1=student(name="sai",age=29)
	e1.tarun()