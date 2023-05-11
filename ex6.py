class Human:
	corona_madicine="stay home"
	def __init__(self,name,age):
		self.name=name
		self.age=age
class employee(Human):
	def __init__(self,name,age,company):
		super().__init__(name,age)
		self.company=company
		print(self.company)
		print(self.name)
		print(employee.corona_madicine)
class cricketer(Human):
	def __init__(self,name,age,country):
		super().__init__(name,age)
		self.country=country
		print(self.country)
		print(self.name)
class footballpalyer(Human):
	def __init__(self,name,age,club):
		super().__init__(name,age)
		self.club=club
		print(self.club,self.name)

c=employee("sai",22,"cts")
k=cricketer("raina",35,"ind")
j=footballpalyer("mbappe",23,"manchester")