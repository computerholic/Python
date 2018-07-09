print("========== God ========= \n\n")

class Employee:
	
	num_of_emp = 0
	raise_amount = 1.04


	def __init__(self, first, last, pay):  #Constuction. #  Init method - Initialize. #Self is an instance.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
		Employee.num_of_emp += 1  # It's nice to know how many employees we have.

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay) * Employee.raise_amount  # 4 percent increasing rate.



# %% Tutorial 3 : Staticmethods and classmethods.
# Differences between class methods and regular methods.
# A lot of people get confused about it. 

# Regular method automaticaly takes the instance as the argument(self)
# How to convert regular method to class method.


	@classmethod  # Decorator makes the regularmethod to classmethod.
	def set_raise_amt(cls, amount):  # Passing a class as an argument. # we are working with the class instead of the instance.
		class.raise_amount = amount

emp_1 = Employee('Mahdi','Kashani','80000')
emp_2 = Employee('Maria Clare','Nunley','90000')

print(emp_1.email)
print(emp_2.email)

Employee.set_raise_amt(1.05)  # Automatically take the class so we just need to give it the amount.

print('\nEmployee.raise_amount: ',Employee.raise_amount,'\n')
print('emp_1.raise_amount:',emp_1.raise_amount)
print('emp_2.raise_amount:',emp_2.raise_amount)



# %% working with classes

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

# %%

# %%

# %%
