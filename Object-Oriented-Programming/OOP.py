print("========== God ========= \n\n\n")

class Employee:
	
	def __init__(self, first, last, pay):  #Constuction. #  Init method - Initialize. #Self is an instance.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'


emp_0 = Employee('Mahdi','Kashani','130000')
emp_1 = Employee('Ben','Taylor','150000')
emp_2 = Employee('Maria Clare','Nunley','90000')


print(emp_1.email)
print(emp_2.email)

print("Help\n")

print(emp_0.first,emp_1.first,emp_2.first)

print('{} {}'.format(emp_0.first,emp_0.last))
