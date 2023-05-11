import sys
class Customer:
	bankname="icici"
	def __init__(self,name,balance):
		self.name=name
		self.balance=balance
	def deposit(self):
		amount=int(input("enter the amount how much you want to deposit :  "))
		self.balance=self.balance+amount
		print("afer the deposit the current balance is: ",self.balance)
	def withdraw(self):
		amount=int(input("enter the amount you want to withdraw : "))
		if self.balance>amount:
			self.balance=self.balance-amount
			print("after withdraw the current balance is : ",self.balance)
		else:
			print("insufficient balance ....... please add balance")
	def checkbalance(self):
		print("your current balance is : " ,self.balance)

if __name__=="__main__":
	print(f"welcome to { Customer.bankname} bank ")
	name=input("enter the name : ")
	ss=Customer(name=name,balance=00.00)
	while True:
		
		print("Select option you want :  d/D for deposit \n w/W  for withdraw  \n c/C for check balance \n e/E for exit")
		option = input("enter the option you want : ")
		if option=="d" or option=="D":
			ss.deposit()
		elif option=="w" or option=="W":
			ss.withdraw()
		elif option=="c" or option=="C":
			ss.checkbalance()
		elif option=="e" or option=="E":
			sys.exit(0)
			break
		else:
			print("invalid option please select correct option ")
	print("thanks for using our bank")
