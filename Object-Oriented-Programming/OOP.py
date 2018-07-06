print("========== God ========= \n\n")

class Employee:
	
	def __init__(self, first, last, pay):  #Constuction. #  Init method - Initialize. #Self is an instance.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	def apply_raise(self):
		self.pay = int(self.pay * 1.04)



emp_1 = Employee('Mahdi','Kashani','130000')
emp_2 = Employee('Maria Clare','Nunley','90000')

print(emp_1.email)
print(emp_2.email)

print("Help\n")

print(emp_0.first,emp_1.first,emp_2.first)

Employee.fullname(emp_1)

print(emp_1.fullname())




print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)
